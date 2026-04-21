import cv2

def draw_damage_boxes(image_path, detections):
    img = cv2.imread(image_path)

    color_map = {
        0: (0, 255, 0),     # no damage → green
        1: (0, 255, 255),   # minor → yellow
        2: (0, 165, 255),   # major → orange
        3: (0, 0, 255)      # destroyed → red
    }

    for det in detections:
        x1, y1, x2, y2 = map(int, det["bbox"])
        cls = det["class"]

        color = color_map.get(cls, (255,255,255))

        cv2.rectangle(img, (x1,y1), (x2,y2), color, 2)

    return img