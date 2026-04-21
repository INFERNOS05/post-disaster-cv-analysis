def filter_post_with_pre(pre_detections, post_detections, iou_thresh=0.3):
    def compute_iou(box1, box2):
        x1, y1, x2, y2 = box1
        x1_p, y1_p, x2_p, y2_p = box2

        xi1 = max(x1, x1_p)
        yi1 = max(y1, y1_p)
        xi2 = min(x2, x2_p)
        yi2 = min(y2, y2_p)

        inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)

        box1_area = (x2 - x1) * (y2 - y1)
        box2_area = (x2_p - x1_p) * (y2_p - y1_p)

        union = box1_area + box2_area - inter_area

        return inter_area / union if union > 0 else 0

    filtered = []

    for post_det in post_detections:
        post_box = post_det["bbox"]

        for pre_det in pre_detections:
            pre_box = pre_det["bbox"]

            if compute_iou(post_box, pre_box) > iou_thresh:
                filtered.append(post_det)
                break

    return filtered