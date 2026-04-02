# GeoDamageMapper

## Overview

A Computer Vision-based system that uses satellite imagery to assess post-disaster damage and map urban density for efficient disaster response and planning.

---

## Motivation

Natural disasters such as earthquakes, floods, and wildfires cause large-scale destruction of infrastructure.

Manual damage assessment is:

* Slow
* Risky
* Not scalable

This project aims to automate damage detection using satellite imagery and computer vision techniques.

---

## Problem Statement

To develop a Computer Vision pipeline that:

* Processes pre- and post-disaster satellite images
* Detects damaged infrastructure
* Estimates urban building density
* Generates geospatial insights for disaster recovery

---

## Input

* Multi-temporal satellite images (Pre + Post disaster)
* RGB / Multispectral imagery

---

## Output

* Damage maps
* Urban density heatmaps
* Infrastructure impact statistics

---

## Applications

* Emergency response systems
* Urban planning & reconstruction
* Disaster recovery prioritization

---

## 🧠 Methodology

The project follows a multi-stage Computer Vision pipeline:

### 1️⃣ Data Collection & Preprocessing
- Dataset: xBD, SpaceNet
- Resize images to standard dimensions
- Normalize pixel values
- Noise removal using Gaussian & Median filters
- Image registration (SIFT/SURF)

### 2️⃣ Feature Extraction & Segmentation
- Edge detection (Sobel, Canny)
- Morphological operations (Erosion, Dilation)
- Texture features (GLCM)
- Watershed segmentation
- K-means clustering

### 3️⃣ Damage Detection (Deep Learning)
- Models: YOLOv8 / Faster R-CNN
- Detect buildings from satellite images
- Classify damage:
  - No Damage
  - Minor Damage
  - Major Damage
  - Destroyed

### 4️⃣ Hybrid Feature Approach
- Combines:
  - Classical CV (SIFT, HoG)
  - Deep Learning (CNN)
- Improves robustness and accuracy

### 5️⃣ Post-Processing
- Morphological refinement
- Noise removal
- Spatial filtering (RANSAC)

### 6️⃣ Structural Analysis
- Hough Transform for road detection
- Analyze infrastructure damage beyond buildings

### 7️⃣ Spatial Analysis
- Connected Component Analysis
- Clustering (DBSCAN / K-Means)
- Identify heavily damaged regions

### 8️⃣ Density Estimation
- Building density calculation
- Damage-weighted density
- Pre vs Post disaster comparison

### 9️⃣ Visualization
- Damage heatmaps
- Density maps
- Region-wise statistics

---

## 📊 Datasets Used

### xBD Dataset
- Large-scale disaster dataset
- Provides building damage labels
- Used for training detection models

### SpaceNet Dataset
- High-resolution satellite imagery
- Used for urban structure and density estimation

---

## 🛠️ Tech Stack (Planned)
- Python
- OpenCV
- PyTorch / TensorFlow
- YOLO / Faster R-CNN
- Scikit-learn
- GIS tools (QGIS, Folium)

---

## 📌 Future Work
- Model optimization
- Real-time disaster analysis
- Deployment as web dashboard

---

## Team

* Sehajdeep Singh Sikka
* Sudhanshu Kulkarni
* Manan Khanna

---
