// =============================================
// TerraClimate Temperature Data Extraction Script
// =============================================

// This script extracts temperature data (maximum temperature)
// from TerraClimate dataset and exports it for analysis.

// ---------------------------------------------
// STEP 1: Define Region
// ---------------------------------------------
var region = ee.Geometry.Rectangle([68, 6, 97, 37]);

Map.centerObject(region, 4);

// ---------------------------------------------
// STEP 2: Load Dataset
// ---------------------------------------------
// TerraClimate provides monthly climate variables
var terraclimate = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE');

// ---------------------------------------------
// STEP 3: Filter Data
// ---------------------------------------------

// BEFORE period (Pre-monsoon month)
var before = terraclimate
  .filterDate('2023-05-01', '2023-05-31')
  .mean()              // Average over month
  .select('tmmx')      // Select maximum temperature band
  .clip(region);

// AFTER period (Monsoon month)
var after = terraclimate
  .filterDate('2023-07-01', '2023-07-31')
  .mean()
  .select('tmmx')
  .clip(region);

// ---------------------------------------------
// STEP 4: Visualization
// ---------------------------------------------
// Temperature values are in Kelvin
var vis = {
  min: 280,
  max: 320,
  palette: ['blue', 'green', 'yellow', 'red']
};

Map.addLayer(before, vis, 'Temp Before (India)');
Map.addLayer(after, vis, 'Temp After (India)');

// ---------------------------------------------
// STEP 5: Export
// ---------------------------------------------

Export.image.toDrive({
  image: before,
  description: 'TerraClimate_before_India_2023',
  folder: 'GEE_exports',
  fileNamePrefix: 'TerraClimate_before_India_2023',
  region: region,
  scale: 4000,          // ~4km resolution
  crs: 'EPSG:4326',
  fileFormat: 'GeoTIFF',
  maxPixels: 1e13
});

Export.image.toDrive({
  image: after,
  description: 'TerraClimate_after_India_2023',
  folder: 'GEE_exports',
  fileNamePrefix: 'TerraClimate_after_India_2023',
  region: region,
  scale: 4000,
  crs: 'EPSG:4326',
  fileFormat: 'GeoTIFF',
  maxPixels: 1e13
});
