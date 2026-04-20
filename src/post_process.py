import numpy as np
import cv2

class PostProcessor:
    def __init__(self, min_area=50):
        self.min_area = min_area

    def clean_masks(self, detections):
        cleaned = []

        for det in detections:
            mask = det["mask"].astype(np.uint8)

            if np.sum(mask) < self.min_area:
                continue

            kernel = np.ones((3, 3), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            det["mask"] = mask
            cleaned.append(det)

        return cleaned