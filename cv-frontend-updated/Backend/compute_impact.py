def compute_impact(pre_detections, post_detections):
    def density(dets):
        return len(dets)

    pre_density = density(pre_detections)
    post_density = density(post_detections)

    damage_score = sum([d["class"] for d in post_detections])

    damaged = sum([1 for d in post_detections if d["class"] > 0])
    total = len(post_detections)

    damage_percent = (damaged / total * 100) if total > 0 else 0

    return {
        "pre_buildings": pre_density,
        "post_buildings": post_density,
        "density_drop": pre_density - post_density,
        "damage_score": damage_score,
        "damage_percent": damage_percent
    }