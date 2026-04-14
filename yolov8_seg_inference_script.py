"""
YOLOv8-seg Inference Script
--------------------------
Purpose:
Run inference using trained model and extract:
- segmentation masks
- class labels
- bounding boxes

This is the first step after training.
"""

import cv2
import numpy as np
import os
from ultralytics import YOLO

# =========================
# CONFIG
# =========================
MODEL_PATH = "best.pt"
IMAGE_PATH = "test.jpg"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# LOAD MODEL
# =========================
model = YOLO(MODEL_PATH)

# =========================
# RUN INFERENCE
# =========================
results = model(IMAGE_PATH, conf=0.25)

# Load image
image = cv2.imread(IMAGE_PATH)
h, w, _ = image.shape

mask_output = np.zeros((h, w), dtype=np.uint8)

# =========================
# PROCESS RESULTS
# =========================
for r in results:
    if r.masks is not None:
        masks = r.masks.data.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy()
        boxes = r.boxes.xyxy.cpu().numpy()

        for i in range(len(masks)):
            mask = masks[i]

            # Resize mask to original image
            mask = cv2.resize(mask, (w, h))
            mask = (mask > 0.5).astype(np.uint8)

            # Add mask to combined output
            mask_output = np.maximum(mask_output, mask * 255)

            # Draw bounding box
            x1, y1, x2, y2 = boxes[i].astype(int)
            cls = int(classes[i])

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f"class {cls}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# =========================
# SAVE OUTPUTS
# =========================
cv2.imwrite(os.path.join(OUTPUT_DIR, "detections.png"), image)
cv2.imwrite(os.path.join(OUTPUT_DIR, "mask.png"), mask_output)

print("✅ Inference Done")
print("Outputs saved in:", OUTPUT_DIR)