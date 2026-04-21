# 🛰️ CV Disaster Assessment Dashboard - Quick Start

## Prerequisites
- Python 3.9 or higher
- pip3 installed

## Installation & Running

### Option 1: Using the startup script (Recommended)
```bash
./start_app.sh
```

### Option 2: Manual commands
```bash
# Install dependencies (first time only)
pip3 install -r requirements.txt

# Run the application
streamlit run app.py --server.port 8502
```

### Option 3: Default Streamlit port
```bash
streamlit run app.py
```

## Accessing the Dashboard

Once the app starts, it will automatically open in your browser at:
- **http://localhost:8502** (if using custom port)
- **http://localhost:8501** (if using default port)

If it doesn't open automatically, copy the URL from the terminal and paste it in your browser.

## Using the Dashboard

### Step 1: Upload Images
1. Go to the **"📤 Upload & Process"** tab
2. Upload a **PRE-disaster** satellite image (JPG, PNG, or TIFF)
3. Upload a **POST-disaster** satellite image
4. Click **"🔥 Run Full Damage Assessment Pipeline"**

### Step 2: View Results
Navigate through the tabs to see:
- **🔬 CV Processing Pipeline**: View all processing stages
- **⚠️ Damage Assessment**: See damage metrics and classifications
- **🗺️ Heatmap Analysis**: View damage intensity heatmap
- **📊 Reports & Export**: Download results as PNG/CSV

## Troubleshooting

### If Streamlit is not found:
```bash
pip3 install streamlit
```

### If you get import errors:
```bash
pip3 install -r requirements.txt --upgrade
```

### If port 8502 is already in use:
```bash
# Use a different port
streamlit run app.py --server.port 8503
```

### To stop the server:
Press `Ctrl+C` in the terminal

## Features

✅ Dual image upload (PRE and POST disaster)
✅ Real backend CV pipeline integration
✅ YOLO-based segmentation
✅ Change detection mapping
✅ Damage clustering and heatmap generation
✅ Comprehensive metrics and KPIs
✅ Export results as PNG/CSV
✅ Premium dark theme UI
✅ Responsive design

## Notes

- The backend pipeline requires the YOLO model file at: `Backend/best.pt`
- If the model file is missing, you'll see an error during analysis
- Sample satellite images can be used for testing
- Processing time depends on image size and system performance

## Support

For issues or questions, check the terminal output for error messages.
