import cv2
from inference import DamageInference
from post_process import PostProcessor
from grid import GridAnalyzer
from clustering import DamageCluster
from filter import filter_post_with_pre
from change_map import compute_change_map
from heatmap import generate_heatmap
from draw_boxes import draw_damage_boxes
from visualise import overlay_heatmap_on_image, draw_clusters
from compute_impact import compute_impact

class FullPipeline:
    def __init__(self, model_path):
        self.infer = DamageInference(model_path)
        self.post = PostProcessor()
        self.grid = GridAnalyzer()
        self.cluster = DamageCluster()

    def run(self, pre_path, post_path):
        print("\n" + "="*60)
        print("RUNNING FULL PIPELINE (DETECTION MODEL)")
        print("="*60)

        # =========================
        # PRE IMAGE
        # =========================
        print("\n[1/6] Running inference on PRE image...")
        pre_raw = self.infer.run_on_image(pre_path)
        print(f"      → PRE raw detections: {len(pre_raw['detections'])}")
        if pre_raw['detections']:
            pre_confs = [d['confidence'] for d in pre_raw['detections']]
            print(f"      → PRE avg confidence: {sum(pre_confs)/len(pre_confs):.3f}")
        
        pre_clean = self.post.clean_masks(pre_raw["detections"])
        print(f"      → PRE after cleanup: {len(pre_clean)}")

        # =========================
        # POST IMAGE
        # =========================
        print("\n[2/6] Running inference on POST image...")
        post_raw = self.infer.run_on_image(post_path)
        print(f"      → POST raw detections: {len(post_raw['detections'])}")
        if post_raw['detections']:
            post_confs = [d['confidence'] for d in post_raw['detections']]
            print(f"      → POST avg confidence: {sum(post_confs)/len(post_confs):.3f}")
        
        post_clean = self.post.clean_masks(post_raw["detections"])
        print(f"      → POST after cleanup: {len(post_clean)}")

        # =========================
        # FILTER using PRE buildings
        # =========================
        # DISABLED: filter was suppressing valid POST detections
        # Keep all cleaned POST detections for damage assessment
        print("\n[3/6] POST detections (filter disabled)...")
        print(f"      → POST final detections: {len(post_clean)}")
        print(f"      → Using all POST detections for damage assessment")

        # =========================
        # CHANGE DETECTION
        # =========================
        print("\n[4/6] Computing change detection map...")
        change_map = compute_change_map(pre_path, post_path)

        # =========================
        # GRID ANALYSIS
        # =========================
        print("\n[5/6] Analyzing grid and clustering...")
        img = cv2.imread(post_path)
        h, w = img.shape[:2]

        grid = self.grid.analyze((h, w), post_clean)
        clusters = self.cluster.cluster(grid)
        heatmap = generate_heatmap(grid)
        print(f"      → {len(clusters)} clusters detected")

        # =========================
        # FINAL VISUAL BUILD
        # =========================
        print("\n[6/6] Building final overlay...")

        # 1. bounding boxes
        boxed = draw_damage_boxes(post_path, post_clean)

        # 2. heatmap overlay (ISSUE 1 FIX: keep this for return dict)
        heat_overlay = overlay_heatmap_on_image(post_path, heatmap)

        # 3. combine both
        final = cv2.addWeighted(boxed, 0.7, heat_overlay, 0.3, 0)

        # 4. draw clusters
        final = draw_clusters(final, clusters)

        # =========================
        # IMPACT METRICS
        # =========================
        impact = compute_impact(pre_clean, post_clean)
        print(f"\n✅ Pipeline complete!")
        print(f"   PRE buildings: {impact['pre_buildings']}")
        print(f"   POST buildings: {impact['post_buildings']}")
        print(f"   Damage %: {impact['damage_percent']:.1f}%")
        print("="*60 + "\n")

        return {
            "grid": grid,
            "clusters": clusters,
            "heatmap": heatmap,
            "heatmap_overlay": heat_overlay,  # ISSUE 1 FIX: add heatmap_overlay key
            "overlay": final,
            "impact": impact,
            "change_map": change_map,
            "pre_detections": pre_clean,
            "post_detections": post_clean,
        }
