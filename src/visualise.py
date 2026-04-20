import cv2
import numpy as np

def overlay_heatmap_on_image(image_path, heatmap, alpha=0.5):
    img = cv2.imread(image_path)

    heatmap_resized = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap_norm = cv2.normalize(heatmap_resized, None, 0, 255, cv2.NORM_MINMAX)
    heatmap_uint8 = heatmap_norm.astype(np.uint8)

    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)

    overlay = cv2.addWeighted(img, 1 - alpha, heatmap_color, alpha, 0)

    return overlay


def draw_clusters(image, clusters, grid_size=16):
    h, w = image.shape[:2]
    cell_h = h // grid_size
    cell_w = w // grid_size

    for c in clusters:
        i, j = c["cell"]

        x1 = j * cell_w
        y1 = i * cell_h
        x2 = x1 + cell_w
        y2 = y1 + cell_h

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return image