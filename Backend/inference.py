from ultralytics import YOLO

class DamageInference:
    def __init__(self, model_path, conf=0.20):
        self.model = YOLO(model_path)
        self.conf = conf

    def run_on_image(self, image_path):
        results = self.model(image_path, conf=self.conf)[0]

        output = {
            "image": image_path,
            "detections": []
        }

        # DETECTION model — use boxes only, no masks
        if results.boxes is None or len(results.boxes) == 0:
            print(f"⚠️  No detections in {image_path}")
            return output

        boxes = results.boxes.xyxy.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()

        for i in range(len(boxes)):
            output["detections"].append({
                "bbox": boxes[i].tolist(),  # [x1, y1, x2, y2]
                "class": int(classes[i]),
                "confidence": float(scores[i])
            })

        # Debug output
        print(f"✅ {len(output['detections'])} detections in {image_path}")
        print(f"   Classes: {set(int(c) for c in classes)}")
        print(f"   Avg confidence: {scores.mean():.3f}")

        return output
