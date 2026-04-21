import cv2
import numpy as np

def overlay_change_map(post_path, change_map):
    img = cv2.imread(post_path)

    change_map = cv2.resize(change_map, (img.shape[1], img.shape[0]))

    change_colored = cv2.applyColorMap(change_map.astype(np.uint8), cv2.COLORMAP_HOT)

    # 🔥 reduce intensity
    overlay = cv2.addWeighted(img, 0.8, change_colored, 0.2, 0)

    return overlay