#from src.pipeline import FullPipeline
import os

model_path = "/kaggle/input/datasets/sk12cs/cv-yolo/best.pt"
image_dir = "/kaggle/input/datasets/sk12cs/cv-yolo/sample_images"

pipeline = FullPipeline(model_path)

for img_name in os.listdir(image_dir):
    if not img_name.endswith(".png"):
        continue

    image_path = os.path.join(image_dir, img_name)

    print(f"\nProcessing: {img_name}")
    result = pipeline.run(image_path)

    print("Clusters:", result["clusters"])