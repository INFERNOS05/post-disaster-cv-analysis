// =============================================
// CHIRPS Rainfall Data Extraction Script
// =============================================

// This script extracts rainfall data from CHIRPS dataset
// for two time periods (before and after) and exports them
// as GeoTIFF images for further analysis (e.g., ML/GAN models).

// ---------------------------------------------
// STEP 1: Define Region of Interest (ROI)
// ---------------------------------------------
// Coordinates represent bounding box of India
var region = ee.Geometry.Rectangle([68, 6, 97, 37]);

// Center the map on the selected region
Map.centerObject(region, 4);

// ---------------------------------------------
// STEP 2: Load Dataset
// ---------------------------------------------
// CHIRPS provides daily precipitation data
var chirps = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY');

// ---------------------------------------------
// STEP 3: Filter Data for Time Periods
// ---------------------------------------------

// BEFORE period (Pre-monsoon: low rainfall)
var before = chirps
  .filterDate('2023-05-01', '2023-05-15') // Filter by date
  .sum()                                  // Aggregate rainfall over period
  .clip(region);                          // Restrict to region

// AFTER period (Monsoon: high rainfall)
var after = chirps
  .filterDate('2023-07-01', '2023-07-15')
  .sum()
  .clip(region);

// ---------------------------------------------
// STEP 4: Visualization
// ---------------------------------------------
// Lower max value helps visualize low rainfall regions
var vis = {
  min: 0,
  max: 50,
  palette: ['white', 'lightblue', 'blue', 'darkblue']
};

// Display layers on map
Map.addLayer(before, vis, 'Rainfall Before (India)');
Map.addLayer(after, vis, 'Rainfall After (India)');

// ---------------------------------------------
// STEP 5: Export Data to Google Drive
// ---------------------------------------------

// Export BEFORE image
Export.image.toDrive({
  image: before,
  description: 'CHIRPS_before_India_2023',
  folder: 'GEE_exports',
  fileNamePrefix: 'CHIRPS_before_India_2023',
  region: region,
  scale: 5000,              // ~5km resolution
  crs: 'EPSG:4326',         // Standard geographic coordinate system
  fileFormat: 'GeoTIFF',
  maxPixels: 1e13           // Prevent export size errors
});

// Export AFTER image
Export.image.toDrive({
  image: after,
  description: 'CHIRPS_after_India_2023',
  folder: 'GEE_exports',
  fileNamePrefix: 'CHIRPS_after_India_2023',
  region: region,
  scale: 5000,
  crs: 'EPSG:4326',
  fileFormat: 'GeoTIFF',
  maxPixels: 1e13
});
