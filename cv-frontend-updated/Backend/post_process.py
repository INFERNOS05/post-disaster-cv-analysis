import numpy as np

class PostProcessor:
    def __init__(self, min_area=100):
        """
        min_area: minimum bounding box area (width × height) to keep
        """
        self.min_area = min_area

    def clean_masks(self, detections):
        """
        Clean detections by removing tiny bounding boxes.
        No mask logic — detection model only.
        """
        cleaned = []

        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            width = x2 - x1
            height = y2 - y1
            area = width * height

            if area < self.min_area:
                continue

            cleaned.append(det)

        return cleaned
