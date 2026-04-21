import math


def _center(box):
    x1, y1, x2, y2 = box
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def _center_dist(box1, box2):
    cx1, cy1 = _center(box1)
    cx2, cy2 = _center(box2)
    return math.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)


def _compute_iou(box1, box2):
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


def filter_post_with_pre(pre_detections, post_detections, iou_thresh=0.10):
    """
    Keep POST detections that correspond to a PRE building.

    Strategy (in order):
    1. IoU overlap >= iou_thresh (lenient, default 0.10)
    2. Nearest-center fallback: if no IoU match, keep POST detection
       if its center is within max_center_dist pixels of any PRE center.

    If PRE is empty, return all POST detections unchanged so we never
    suppress everything due to a bad PRE inference.
    """

    # Safety: if no PRE buildings detected, don't suppress POST at all
    if len(pre_detections) == 0:
        print("⚠️  filter: PRE is empty — returning all POST detections unfiltered")
        return post_detections

    # Estimate a reasonable center-distance threshold from PRE box sizes
    pre_sizes = []
    for d in pre_detections:
        x1, y1, x2, y2 = d["bbox"]
        pre_sizes.append(max(x2 - x1, y2 - y1))
    avg_size = sum(pre_sizes) / len(pre_sizes) if pre_sizes else 100
    max_center_dist = avg_size * 2.0   # generous: 2× average box size

    filtered = []

    for post_det in post_detections:
        post_box = post_det["bbox"]
        matched = False

        # Pass 1: IoU match
        for pre_det in pre_detections:
            if _compute_iou(post_box, pre_det["bbox"]) >= iou_thresh:
                matched = True
                break

        # Pass 2: nearest-center fallback
        if not matched:
            for pre_det in pre_detections:
                if _center_dist(post_box, pre_det["bbox"]) <= max_center_dist:
                    matched = True
                    break

        if matched:
            filtered.append(post_det)

    print(f"   filter: {len(post_detections)} POST → {len(filtered)} kept "
          f"(iou_thresh={iou_thresh}, center_dist≤{max_center_dist:.0f}px)")

    # Final safety: if filter wiped everything, return all POST detections
    if len(filtered) == 0 and len(post_detections) > 0:
        print("⚠️  filter: all POST detections were suppressed — bypassing filter")
        return post_detections

    return filtered
