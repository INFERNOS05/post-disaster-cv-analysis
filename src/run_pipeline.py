import os
import cv2
import matplotlib.pyplot as plt
from pipeline import FullPipeline
from pre_post_analysis import show_pre_post
from overlay_change_map import overlay_change_map

model_path = "seg_overfit_bundle/best.pt"
image_dir = "demo_images"

pipeline = FullPipeline(model_path)

# -------------------------------
# GROUP PRE & POST IMAGES
# -------------------------------
pairs = {}

for img_name in os.listdir(image_dir):
    if not img_name.endswith(".png"):
        continue

    # remove suffix
    if "_pre_disaster" in img_name:
        key = img_name.replace("_pre_disaster.png", "")
        pairs.setdefault(key, {})["pre"] = img_name

    elif "_post_disaster" in img_name:
        key = img_name.replace("_post_disaster.png", "")
        pairs.setdefault(key, {})["post"] = img_name


import matplotlib.pyplot as plt
import cv2

for key, files in pairs.items():
    if "pre" not in files or "post" not in files:
        continue

    pre_path = os.path.join(image_dir, files["pre"])
    post_path = os.path.join(image_dir, files["post"])

    print(f"\nProcessing pair: {key}")

    result = pipeline.run(pre_path, post_path)

    print("Impact:", result["impact"])
    print("Clusters:", result["clusters"])

    # =========================
    # PRE vs POST
    # =========================
    show_pre_post(pre_path, post_path)

    # =========================
    # FINAL OUTPUT
    # =========================
    final = result["overlay"]

    plt.figure(figsize=(6,6))
    plt.imshow(cv2.cvtColor(final, cv2.COLOR_BGR2RGB))
    plt.title("Final Damage Assessment")
    plt.axis("off")
    plt.show()   # 🔥 IMPORTANT

    # =========================
    # CHANGE MAP
    # =========================
    change_overlay = overlay_change_map(post_path, result["change_map"])

    plt.figure(figsize=(6,6))
    plt.imshow(cv2.cvtColor(change_overlay, cv2.COLOR_BGR2RGB))
    plt.title("Change Detection Overlay")
    plt.axis("off")
    plt.show()   # 🔥 IMPORTANT