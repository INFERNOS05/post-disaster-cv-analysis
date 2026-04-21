# Computer Vision Processing Pipeline
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import cv2

def resize_image(image: Image.Image, target_size=(512, 512)) -> Image.Image:
    """Resize image to target size for processing."""
    return image.resize(target_size, Image.Resampling.LANCZOS)

def enhance_image(image: Image.Image) -> Image.Image:
    """Enhance image contrast and sharpness."""
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.5)
    
    # Increase sharpness
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.3)
    
    return image

def detect_edges(image: Image.Image) -> Image.Image:
    """Apply edge detection using Canny algorithm."""
    # Convert to numpy array
    img_array = np.array(image.convert('L'))
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(img_array, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Convert back to PIL Image
    return Image.fromarray(edges)

def segment_image(image: Image.Image) -> Image.Image:
    """Perform image segmentation using thresholding."""
    # Convert to numpy array
    img_array = np.array(image.convert('RGB'))
    
    # Convert to HSV for better segmentation
    hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
    
    # Create multiple masks for different regions
    # Urban areas (darker regions)
    lower_urban = np.array([0, 0, 0])
    upper_urban = np.array([180, 255, 100])
    mask_urban = cv2.inRange(hsv, lower_urban, upper_urban)
    
    # Vegetation (green regions)
    lower_veg = np.array([35, 40, 40])
    upper_veg = np.array([85, 255, 255])
    mask_veg = cv2.inRange(hsv, lower_veg, upper_veg)
    
    # Create colored segmentation
    segmented = np.zeros_like(img_array)
    segmented[mask_urban > 0] = [255, 100, 100]  # Red for urban
    segmented[mask_veg > 0] = [100, 255, 100]    # Green for vegetation
    segmented[(mask_urban == 0) & (mask_veg == 0)] = [100, 100, 255]  # Blue for other
    
    return Image.fromarray(segmented)

def extract_features(image: Image.Image) -> Image.Image:
    """Extract key features using corner detection."""
    # Convert to numpy array
    img_array = np.array(image.convert('L'))
    
    # Apply Harris corner detection
    corners = cv2.cornerHarris(img_array.astype(np.float32), 2, 3, 0.04)
    
    # Dilate corner image to enhance corner points
    corners = cv2.dilate(corners, None)
    
    # Create visualization
    img_color = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
    img_color[corners > 0.01 * corners.max()] = [255, 0, 0]
    
    return Image.fromarray(img_color)

def generate_damage_heatmap(image: Image.Image) -> tuple[Image.Image, np.ndarray]:
    """Generate damage assessment heatmap."""
    # Convert to numpy array
    img_array = np.array(image.convert('RGB'))
    
    # Simulate damage detection (in real scenario, this would be ML model output)
    # Create a heatmap based on image intensity variations
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Calculate difference (simulating damage detection)
    diff = cv2.absdiff(gray, blurred)
    
    # Normalize to 0-1 range
    heatmap_data = diff.astype(float) / 255.0
    
    # Apply colormap
    heatmap_colored = cv2.applyColorMap((heatmap_data * 255).astype(np.uint8), cv2.COLORMAP_JET)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)
    
    # Blend with original image
    alpha = 0.6
    blended = cv2.addWeighted(img_array, 1-alpha, heatmap_colored, alpha, 0)
    
    return Image.fromarray(blended), heatmap_data

def predict_damage_regions(image: Image.Image) -> Image.Image:
    """Predict and highlight damaged regions."""
    # Convert to numpy array
    img_array = np.array(image.convert('RGB'))
    
    # Simulate damage prediction (in real scenario, this would be ML model)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    
    # Apply adaptive thresholding to find potential damage areas
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on original image
    result = img_array.copy()
    cv2.drawContours(result, contours, -1, (255, 0, 0), 2)
    
    # Fill regions with semi-transparent red
    mask = np.zeros_like(img_array)
    cv2.drawContours(mask, contours, -1, (255, 0, 0), -1)
    result = cv2.addWeighted(result, 0.7, mask, 0.3, 0)
    
    return Image.fromarray(result)

def calculate_damage_metrics(heatmap_data: np.ndarray) -> dict:
    """Calculate damage assessment metrics from heatmap."""
    # Calculate various metrics
    total_pixels = heatmap_data.size
    
    # Define severity thresholds
    low_threshold = 0.3
    medium_threshold = 0.6
    high_threshold = 0.8
    
    low_damage = np.sum((heatmap_data > low_threshold) & (heatmap_data <= medium_threshold))
    medium_damage = np.sum((heatmap_data > medium_threshold) & (heatmap_data <= high_threshold))
    severe_damage = np.sum(heatmap_data > high_threshold)
    
    total_affected = low_damage + medium_damage + severe_damage
    
    # Calculate percentages
    low_pct = (low_damage / total_pixels) * 100
    medium_pct = (medium_damage / total_pixels) * 100
    severe_pct = (severe_damage / total_pixels) * 100
    total_affected_pct = (total_affected / total_pixels) * 100
    
    # Calculate overall severity score (0-10)
    severity_score = (low_pct * 0.3 + medium_pct * 0.6 + severe_pct * 1.0) / 10
    
    # Determine overall classification
    if severity_score < 3:
        classification = "Low"
    elif severity_score < 6:
        classification = "Medium"
    else:
        classification = "Severe"
    
    return {
        "classification": classification,
        "severity_score": round(severity_score, 2),
        "total_affected_pct": round(total_affected_pct, 2),
        "low_damage_pct": round(low_pct, 2),
        "medium_damage_pct": round(medium_pct, 2),
        "severe_damage_pct": round(severe_pct, 2),
        "confidence": round(np.random.uniform(0.82, 0.96), 2)  # Simulated confidence
    }

def process_full_pipeline(image: Image.Image) -> dict:
    """Process image through full CV pipeline and return all results."""
    results = {}
    
    # Stage 1: Original
    results['original'] = image
    
    # Stage 2: Resized
    results['resized'] = resize_image(image)
    
    # Stage 3: Enhanced
    results['enhanced'] = enhance_image(results['resized'])
    
    # Stage 4: Edge Detection
    results['edges'] = detect_edges(results['enhanced'])
    
    # Stage 5: Segmentation
    results['segmented'] = segment_image(results['enhanced'])
    
    # Stage 6: Feature Extraction
    results['features'] = extract_features(results['enhanced'])
    
    # Stage 7: Damage Prediction
    results['damage_regions'] = predict_damage_regions(results['enhanced'])
    
    # Stage 8: Heatmap Generation
    results['heatmap'], heatmap_data = generate_damage_heatmap(results['enhanced'])
    
    # Stage 9: Calculate Metrics
    results['metrics'] = calculate_damage_metrics(heatmap_data)
    
    return results
