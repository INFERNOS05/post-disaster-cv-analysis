import numpy as np

def generate_heatmap(grid, grid_size=16):
    heat = np.zeros((grid_size, grid_size))

    for g in grid:
        i, j = g["cell"]
        heat[i, j] = g["priority_score"]

    return heat