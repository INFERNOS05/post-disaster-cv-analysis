# Dummy data for CV Disaster Dashboard
import numpy as np

# KPI Cards for Dashboard Home
KPI_CARDS = [
    {"label": "Images Processed", "value": 142, "icon": "🛰️", "delta": "+12"},
    {"label": "Damage Severity Score", "value": "7.4", "icon": "⚠️", "delta": "-0.3"},
    {"label": "Dense Urban Zones", "value": 38, "icon": "🏙️", "delta": "+5"},
    {"label": "Analysis Accuracy %", "value": "94.2", "icon": "🎯", "delta": "+1.1"},
]

# Damage Assessment Result
DAMAGE_RESULT = {
    "damage_class": "Medium",
    "confidence_score": 0.87,
    "heatmap": np.random.rand(100, 100).astype(np.float32),
    "regions": [
        {"region_name": "Zone A", "damage_class": "Severe", "affected_area_pct": 45.2, "confidence_score": 0.92},
        {"region_name": "Zone B", "damage_class": "Medium", "affected_area_pct": 32.8, "confidence_score": 0.85},
        {"region_name": "Zone C", "damage_class": "Low", "affected_area_pct": 15.3, "confidence_score": 0.78},
        {"region_name": "Zone D", "damage_class": "Medium", "affected_area_pct": 28.7, "confidence_score": 0.88},
    ]
}

# Urban Density Result
DENSITY_RESULT = {
    "dominant_class": "Moderate",
    "built_up_area_pct": 62.5,
    "population_proxy_score": 7.8,
    "segmentation_mask": np.random.randint(0, 3, (100, 100), dtype=np.uint8),
    "zone_breakdown": {
        "Sparse": 25.3,
        "Moderate": 48.2,
        "Dense": 26.5,
    }
}

# Analytics Data
ANALYTICS_DAMAGE_TREND = [
    {"region": "Zone A", "Low": 20, "Medium": 45, "Severe": 35},
    {"region": "Zone B", "Low": 35, "Medium": 40, "Severe": 25},
    {"region": "Zone C", "Low": 50, "Medium": 30, "Severe": 20},
    {"region": "Zone D", "Low": 25, "Medium": 50, "Severe": 25},
    {"region": "Zone E", "Low": 40, "Medium": 35, "Severe": 25},
    {"region": "Zone F", "Low": 30, "Medium": 45, "Severe": 25},
]

ANALYTICS_MONTHLY_VOLUME = [
    {"month": "Jan 2024", "count": 8},
    {"month": "Feb 2024", "count": 12},
    {"month": "Mar 2024", "count": 15},
    {"month": "Apr 2024", "count": 18},
    {"month": "May 2024", "count": 22},
    {"month": "Jun 2024", "count": 25},
    {"month": "Jul 2024", "count": 20},
    {"month": "Aug 2024", "count": 28},
    {"month": "Sep 2024", "count": 24},
    {"month": "Oct 2024", "count": 30},
    {"month": "Nov 2024", "count": 27},
    {"month": "Dec 2024", "count": 32},
]

ANALYTICS_CONFIDENCE_HISTORY = [
    {"session": 1, "avg_confidence": 0.82},
    {"session": 2, "avg_confidence": 0.85},
    {"session": 3, "avg_confidence": 0.83},
    {"session": 4, "avg_confidence": 0.87},
    {"session": 5, "avg_confidence": 0.86},
    {"session": 6, "avg_confidence": 0.88},
    {"session": 7, "avg_confidence": 0.89},
    {"session": 8, "avg_confidence": 0.87},
    {"session": 9, "avg_confidence": 0.90},
    {"session": 10, "avg_confidence": 0.91},
    {"session": 11, "avg_confidence": 0.89},
    {"session": 12, "avg_confidence": 0.92},
    {"session": 13, "avg_confidence": 0.90},
    {"session": 14, "avg_confidence": 0.93},
    {"session": 15, "avg_confidence": 0.91},
    {"session": 16, "avg_confidence": 0.94},
    {"session": 17, "avg_confidence": 0.92},
    {"session": 18, "avg_confidence": 0.93},
    {"session": 19, "avg_confidence": 0.94},
    {"session": 20, "avg_confidence": 0.95},
]
