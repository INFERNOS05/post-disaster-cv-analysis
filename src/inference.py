from ultralytics import YOLO

class DamageInference:
    def __init__(self, model_path, conf=0.4):
        self.model = YOLO(model_path)
        self.conf = conf

    def run_on_image(self, image_path):
        results = self.model(image_path, conf=self.conf)[0]

        output = {
            "image": image_path,
            "detections": []
        }

        if results.masks is None:
            return output

        masks = results.masks.data.cpu().numpy()
        boxes = results.boxes.xyxy.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()

        for i in range(len(masks)):
            output["detections"].append({
                "mask": masks[i],
                "bbox": boxes[i],
                "class": int(classes[i]),
                "confidence": float(scores[i])
            })

        return output