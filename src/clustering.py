import numpy as np
from sklearn.cluster import DBSCAN

class DamageCluster:
    def __init__(self, eps=2, min_samples=3):
        self.model = DBSCAN(eps=eps, min_samples=min_samples)

    def cluster(self, grid):
        scores = [g["priority_score"] for g in grid]

        if max(scores) == 0:
            return []

        threshold = np.percentile(scores, 80)

        points = []
        indices = []

        for g in grid:
            if g["priority_score"] > threshold:
                points.append(g["cell"])
                indices.append(g)

        if not points:
            return []

        points = np.array(points)
        labels = self.model.fit_predict(points)

        clusters = []
        for i, label in enumerate(labels):
            if label == -1:
                continue

            clusters.append({
                "cluster_id": int(label),
                "cell": indices[i]["cell"],
                "priority": indices[i]["priority_score"]
            })

        return clusters