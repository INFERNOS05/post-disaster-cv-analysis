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
        # =========================
        # PRE IMAGE
        # =========================
        pre_raw = self.infer.run_on_image(pre_path)
        pre_clean = self.post.clean_masks(pre_raw["detections"])

        # =========================
        # POST IMAGE
        # =========================
        post_raw = self.infer.run_on_image(post_path)
        post_clean = self.post.clean_masks(post_raw["detections"])

        # 🔥 FILTER using PRE buildings
        post_clean = filter_post_with_pre(pre_clean, post_clean)

        if len(post_clean) == 0:
            print("No detections in POST image")

        # =========================
        # CHANGE DETECTION
        # =========================
        change_map = compute_change_map(pre_path, post_path)

        # =========================
        # EXISTING PIPELINE (POST ONLY)
        # =========================
        img = cv2.imread(post_path)
        h, w = img.shape[:2]

        grid = self.grid.analyze((h, w), post_clean)
        clusters = self.cluster.cluster(grid)
        heatmap = generate_heatmap(grid)

        # =========================
        # 🔥 FINAL VISUAL BUILD
        # =========================

        # 1. bounding boxes
        boxed = draw_damage_boxes(post_path, post_clean)

        # 2. heatmap overlay
        heat_overlay = overlay_heatmap_on_image(post_path, heatmap)

        # 3. combine both
        final = cv2.addWeighted(boxed, 0.7, heat_overlay, 0.3, 0)

        # 4. draw clusters
        final = draw_clusters(final, clusters)

        # =========================
        # IMPACT
        # =========================
        impact = compute_impact(pre_clean, post_clean)

        return {
            "grid": grid,
            "clusters": clusters,
            "heatmap": heatmap,
            "overlay": final,   # ✅ IMPORTANT FIX
            "impact": impact,
            "change_map": change_map
        }