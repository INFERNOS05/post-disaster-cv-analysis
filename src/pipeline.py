import cv2
from collections import Counter

'''from inference import DamageInference
from postprocess import PostProcessor
from grid import GridAnalyzer
from clustering import DamageCluster
from heatmap import generate_heatmap
from visualize import overlay_heatmap_on_image, draw_clusters'''

class FullPipeline:
    def __init__(self, model_path):
        self.infer = DamageInference(model_path)
        self.post = PostProcessor()
        self.grid = GridAnalyzer()
        self.cluster = DamageCluster()

    def run(self, image_path):
        raw = self.infer.run_on_image(image_path)

        cleaned = self.post.clean_masks(raw["detections"])

        if len(cleaned) == 0:
            print("No detections")

        cls_counts = Counter([d["class"] for d in cleaned])
        print("Class distribution:", cls_counts)

        img = cv2.imread(image_path)
        h, w = img.shape[:2]

        grid = self.grid.analyze((h, w), cleaned)
        clusters = self.cluster.cluster(grid)
        heatmap = generate_heatmap(grid)

        overlay = overlay_heatmap_on_image(image_path, heatmap)
        overlay = draw_clusters(overlay, clusters)

        return {
            "grid": grid,
            "clusters": clusters,
            "heatmap": heatmap,
            "overlay": overlay,
            "class_distribution": dict(cls_counts)
        }