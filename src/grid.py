import numpy as np

class GridAnalyzer:
    def __init__(self, grid_size=16):
        self.grid_size = grid_size

    def analyze(self, image_shape, detections):
        h, w = image_shape
        cell_h = h // self.grid_size
        cell_w = w // self.grid_size

        grid = [
            {"cell": (i, j), "count": 0, "damage_sum": 0, "priority_score": 0}
            for i in range(self.grid_size)
            for j in range(self.grid_size)
        ]

        for det in detections:
            mask = det["mask"]

            ys, xs = np.where(mask > 0)
            if len(xs) == 0:
                continue

            cx = int(xs.mean())
            cy = int(ys.mean())

            cell_x = min(cx // cell_w, self.grid_size - 1)
            cell_y = min(cy // cell_h, self.grid_size - 1)

            idx = cell_y * self.grid_size + cell_x

            grid[idx]["count"] += 1
            grid[idx]["damage_sum"] += det["class"]

        
        for g in grid:
            if g["count"] > 0:
                severity = g["damage_sum"] / g["count"]
                density = g["count"]
                g["priority_score"] = severity * density
            else:
                g["priority_score"] = 0

        return grid