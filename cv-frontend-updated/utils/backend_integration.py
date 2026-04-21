# Backend Integration Module for Streamlit
# EXACT REPLICATION OF run_pipeline.py FLOW
import os
import sys
import cv2
import numpy as np
from PIL import Image
import tempfile

# Add Backend folder to path
backend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Import ONLY the modules used in run_pipeline.py
from pipeline import FullPipeline
from overlay_change_map import overlay_change_map


def _to_pil(bgr_array):
    """Convert BGR numpy array to PIL RGB image."""
    return Image.fromarray(cv2.cvtColor(bgr_array, cv2.COLOR_BGR2RGB))


class StreamlitPipelineWrapper:
    """
    Exact replication of run_pipeline.py flow for Streamlit uploads.
    
    Original flow:
    1. pipeline = FullPipeline(model_path)
    2. result = pipeline.run(pre_path, post_path)
    3. Use result["overlay"], result["change_map"], result["impact"], result["clusters"]
    """

    def __init__(self, model_path="Backend/best.pt"):
        self.model_path = model_path
        self.pipeline = None

    def initialize_pipeline(self):
        """Lazy-load the pipeline - matches: pipeline = FullPipeline(model_path)"""
        if self.pipeline is None:
            print(f"🔧 Initializing pipeline with model: {self.model_path}")
            self.pipeline = FullPipeline(self.model_path)

    def save_uploaded_file(self, uploaded_file, suffix="_temp"):
        temp_dir = tempfile.gettempdir()
        file_ext = os.path.splitext(uploaded_file.name)[1] or ".png"
        temp_path = os.path.join(temp_dir, f"cv_dashboard{suffix}{file_ext}")
    
    # FIX: always seek to 0 before reading
        uploaded_file.seek(0)
        raw_bytes = uploaded_file.read()
    
        with open(temp_path, "wb") as f:
            f.write(raw_bytes)
    
        img = cv2.imread(temp_path)
        if img is not None:
            print(f"📁 Saved {suffix}: {temp_path}, Shape: {img.shape}")
        else:
            print(f"⚠️ Failed to read saved image: {temp_path}")
    
        return temp_path

    def run_uploaded_pipeline(self, pre_file, post_file):
        """
        EXACT REPLICATION of run_pipeline.py flow:
        
        result = pipeline.run(pre_path, post_path)
        print("Impact:", result["impact"])
        print("Clusters:", result["clusters"])
        final = result["overlay"]
        change_overlay = overlay_change_map(post_path, result["change_map"])
        """
        self.initialize_pipeline()

        # ISSUE 2 FIX: Save uploaded files to temp paths (preserving original format)
        pre_path  = self.save_uploaded_file(pre_file,  suffix="_pre")
        post_path = self.save_uploaded_file(post_file, suffix="_post")

        try:
            print(f"\n{'='*60}")
            print("STREAMLIT PIPELINE (replicating run_pipeline.py)")
            print(f"{'='*60}")
            print(f"PRE:  {pre_path}")
            print(f"POST: {post_path}")
            
            # ============================================================
            # EXACT MATCH: result = pipeline.run(pre_path, post_path)
            # ============================================================
            result = self.pipeline.run(pre_path, post_path)
            
            # ============================================================
            # EXACT MATCH: print("Impact:", result["impact"])
            # ============================================================
            print("\n📊 Impact:", result["impact"])
            print("🎯 Clusters:", len(result["clusters"]))
            
            # ISSUE 2 FIX: Print detection counts for comparison
            print(f"\n🔍 Detection Comparison:")
            print(f"   PRE detections:  {result['impact']['pre_buildings']}")
            print(f"   POST detections: {result['impact']['post_buildings']}")
            
            # ============================================================
            # EXACT MATCH: final = result["overlay"]
            # ============================================================
            final_overlay = result["overlay"]
            
            # ============================================================
            # EXACT MATCH: change_overlay = overlay_change_map(post_path, result["change_map"])
            # ============================================================
            change_overlay = overlay_change_map(post_path, result["change_map"])
            
            # ISSUE 1 FIX: Use heatmap_overlay from pipeline result
            heatmap_overlay = result["heatmap_overlay"]
            
            # Load original images for display
            pre_img  = cv2.imread(pre_path)
            post_img = cv2.imread(post_path)
            
            # Compute average confidence from POST detections
            post_dets = result.get("post_detections", [])
            if post_dets:
                avg_conf = float(np.mean([d["confidence"] for d in post_dets]))
            else:
                avg_conf = 0.0
            
            print(f"\n✅ Pipeline complete!")
            print(f"   Avg confidence:  {avg_conf:.3f}")
            print(f"{'='*60}\n")
            
            # Return outputs matching run_pipeline.py structure
            return {
                # Original images
                "pre_image":  _to_pil(pre_img),
                "post_image": _to_pil(post_img),
                
                # EXACT OUTPUTS from run_pipeline.py
                "damage_overlay":  _to_pil(final_overlay),      # result["overlay"]
                "change_overlay":  _to_pil(change_overlay),     # overlay_change_map(...)
                "heatmap_overlay": _to_pil(heatmap_overlay),    # ISSUE 1 FIX: result["heatmap_overlay"]
                "impact":          result["impact"],             # result["impact"]
                "clusters":        result["clusters"],           # result["clusters"]
                "heatmap":         result["heatmap"],            # result["heatmap"]
                "grid":            result["grid"],               # result["grid"]
                
                # Additional data for frontend
                "pre_detections":  result.get("pre_detections", []),
                "post_detections": result.get("post_detections", []),
                "avg_confidence":  avg_conf,
                "has_detections":  len(post_dets) > 0,
            }

        finally:
            # Cleanup temp files
            for p in (pre_path, post_path):
                if os.path.exists(p):
                    os.remove(p)


def calculate_severity_metrics(impact_dict, heatmap_data, avg_confidence=0.0):
    """
    Enrich the raw impact dict from compute_impact.py with additional metrics.
    
    Original impact dict contains:
    - pre_buildings
    - post_buildings
    - density_drop
    - damage_score
    - damage_percent
    
    We add:
    - classification (Low/Medium/Severe)
    - severity_score (0-10)
    - damage distribution percentages
    - confidence
    """
    # Check if we have any detections
    if impact_dict['post_buildings'] == 0:
        return {
            **impact_dict,
            "classification":    "No Detections",
            "severity_score":    0.0,
            "total_affected_pct": 0.0,
            "low_damage_pct":    0.0,
            "medium_damage_pct": 0.0,
            "severe_damage_pct": 0.0,
            "confidence":        0.0,
        }

    total_pixels = heatmap_data.size

    # Normalize heatmap to 0-1
    heatmap_norm = heatmap_data / (heatmap_data.max() + 1e-6)

    # Classify damage zones by heatmap intensity
    low_damage    = np.sum((heatmap_norm > 0.3) & (heatmap_norm <= 0.6))
    medium_damage = np.sum((heatmap_norm > 0.6) & (heatmap_norm <= 0.8))
    severe_damage = np.sum(heatmap_norm > 0.8)
    total_affected = low_damage + medium_damage + severe_damage

    low_pct    = (low_damage    / total_pixels) * 100
    medium_pct = (medium_damage / total_pixels) * 100
    severe_pct = (severe_damage / total_pixels) * 100
    total_pct  = (total_affected / total_pixels) * 100

    # Weighted severity score 0-10
    severity_score = (low_pct * 0.3 + medium_pct * 0.6 + severe_pct * 1.0) / 10

    if severity_score < 3:
        classification = "Low"
    elif severity_score < 6:
        classification = "Medium"
    else:
        classification = "Severe"

    # Use real model confidence
    confidence = avg_confidence if avg_confidence > 0 else 0.5

    return {
        **impact_dict,
        "classification":    classification,
        "severity_score":    round(severity_score, 2),
        "total_affected_pct": round(total_pct, 2),
        "low_damage_pct":    round(low_pct, 2),
        "medium_damage_pct": round(medium_pct, 2),
        "severe_damage_pct": round(severe_pct, 2),
        "confidence":        round(confidence, 4),
    }
