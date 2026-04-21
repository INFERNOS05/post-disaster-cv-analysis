import numpy as np

class GridAnalyzer:
    def __init__(self, grid_size=16):
        self.grid_size = grid_size

    def analyze(self, image_shape, detections):
        """
        Analyze detections using bounding box centroids.
        No mask logic — detection model only.
        """
        h, w = image_shape
        cell_h = h // self.grid_size
        cell_w = w // self.grid_size

        grid = [
            {"cell": (i, j), "count": 0, "damage_sum": 0, "priority_score": 0}
            for i in range(self.grid_size)
            for j in range(self.grid_size)
        ]

        for det in detections:
            x1, y1, x2, y2 = det["bbox"]

            # Compute bbox center
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            # Clamp to image bounds
            cx = max(0, min(cx, w - 1))
            cy = max(0, min(cy, h - 1))

            # Map to grid cell
            cell_x = min(cx // cell_w, self.grid_size - 1)
            cell_y = min(cy // cell_h, self.grid_size - 1)

            idx = cell_y * self.grid_size + cell_x

            grid[idx]["count"] += 1
            grid[idx]["damage_sum"] += det["class"]

        # Compute priority scores
        for g in grid:
            if g["count"] > 0:
                severity = g["damage_sum"] / g["count"]
                density = g["count"]
                g["priority_score"] = severity * density
            else:
                g["priority_score"] = 0

        return grid
