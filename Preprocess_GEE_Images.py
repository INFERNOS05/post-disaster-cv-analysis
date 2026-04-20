# ==========================================================
# GeoTIFF Preprocessing Pipeline for GAN Training
# ==========================================================
# This script converts GeoTIFF (.tif) satellite images into
# normalized, resized, multi-channel NumPy arrays suitable
# for GAN model training.

import os                          # For file and directory handling
import numpy as np                # For numerical operations
import rasterio                  # For reading GeoTIFF files
import cv2                       # For resizing images

# ----------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------

INPUT_DIR = "datasets/CHIRPS_Datasets"   # Folder containing .tif files
OUTPUT_DIR = "processed_data"            # Folder to save processed files
IMAGE_SIZE = 256                         # Target size for GAN input

# Create output directory if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ----------------------------------------------------------
# FUNCTION: Process a single GeoTIFF image
# ----------------------------------------------------------

def process_tif(file_path, output_path):
    """
    Reads a GeoTIFF image, normalizes it, resizes it,
    converts to 3-channel format, and saves as .npy file.
    """

    # Open GeoTIFF file
    with rasterio.open(file_path) as src:
        img = src.read()  # shape: (channels, H, W)
        img = np.nan_to_num(img)
    # Replace NaN values with zero to avoid computation issues
    img = np.nan_to_num(img)

    # Normalize each channel independently
    for i in range(img.shape[0]):
        band = img[i]
        band_min, band_max = band.min(), band.max()
        img[i] = (band - band_min) / (band_max - band_min + 1e-8)

    # Resize each channel
    resized_channels = []
    for i in range(img.shape[0]):
        resized = cv2.resize(img[i], (IMAGE_SIZE, IMAGE_SIZE))
        resized_channels.append(resized)

    img_resized = np.stack(resized_channels, axis=-1)  # (H, W, C)

    # Ensure exactly 3 channels
    if img_resized.shape[-1] >= 3:
        img_3ch = img_resized[:, :, :3]
    else:
        img_3ch = np.repeat(img_resized, 3, axis=-1)

    img_3ch = img_3ch.astype(np.float32) # Ensure dtype consistency
    # Save processed image as NumPy array (.npy)
    np.save(output_path, img_3ch)

# ----------------------------------------------------------
# MAIN LOOP: Process all .tif files in directory
# ----------------------------------------------------------

def main():
    """
    Iterates through all .tif files and processes them.
    """

    for file_name in os.listdir(INPUT_DIR):

        # Check if file is a GeoTIFF
        if file_name.endswith(".tif"):

            # Full input file path
            input_path = os.path.join(INPUT_DIR, file_name)

            # Output file path (.npy format)
            output_file = file_name.replace(".tif", ".npy")
            output_path = os.path.join(OUTPUT_DIR, output_file)

            # Process the image
            process_tif(input_path, output_path)

            # Print progress for tracking
            print(f"Processed: {file_name} → {output_file}")

# ----------------------------------------------------------
# ENTRY POINT
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
