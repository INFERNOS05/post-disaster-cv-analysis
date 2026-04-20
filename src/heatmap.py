import numpy as np
import matplotlib.pyplot as plt

def generate_heatmap(grid, grid_size=16, save_path=None):
    heat = np.zeros((grid_size, grid_size))

    for g in grid:
        i, j = g["cell"]
        heat[i, j] = g["priority_score"]

    plt.figure(figsize=(6, 6))
    plt.imshow(heat, vmin=0, vmax=5)
    plt.colorbar()
    plt.title("Priority Heatmap")

    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

    return heat