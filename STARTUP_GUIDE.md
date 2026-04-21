# 🚀 Complete Startup Guide - CV Disaster Assessment Dashboard

## ✅ What You Need to Run the App

Based on your system, here's what you need:

### System Information
- ✅ **Python 3.9** - Already installed
- ✅ **pip3** - Already installed
- ✅ **opencv-python** - Already installed
- ✅ **pandas** - Already installed
- ✅ **Streamlit 1.50.0** - Already installed

## 🎯 How to Run the Application

### Method 1: Quick Start (Easiest)
```bash
./start_app.sh
```

### Method 2: Direct Command
```bash
streamlit run app.py --server.port 8502
```

### Method 3: Default Port
```bash
streamlit run app.py
```

## 📱 Accessing the Dashboard

After running the command, you'll see output like:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8502
Network URL: http://192.168.x.x:8502
```

**Open your browser and go to:** `http://localhost:8502`

## 🎨 What You'll See

The dashboard has 5 main tabs:

### 1. 📤 Upload & Process
- Upload PRE-disaster satellite image
- Upload POST-disaster satellite image
- Click "Run Full Damage Assessment Pipeline"
- Watch the progress bar as it processes

### 2. 🔬 CV Processing Pipeline
- View 7 stages of image processing:
  - Original images (PRE & POST)
  - Resized images
  - Enhanced images (CLAHE)
  - Edge detection (Canny)
  - Segmentation (HSV-based)
  - Feature extraction (Harris corners)
  - Change detection map

### 3. ⚠️ Damage Assessment
- Overall classification (Low/Medium/Severe)
- Severity score (0-10)
- Total affected area percentage
- Confidence score
- Damage distribution chart
- Visual comparison of input vs predicted damage

### 4. 🗺️ Heatmap Analysis
- Damage intensity heatmap
- Severity legend (Low/Medium/High risk zones)
- Risk zone statistics table

### 5. 📊 Reports & Export
- Download heatmap as PNG
- Download damage regions as PNG
- Download metrics as CSV
- View analysis summary table

## ⚠️ Important Notes

### Backend Model File
The app expects a YOLO model file at:
```
Backend/best.pt
```

**If this file is missing:**
- The app will still run
- You'll get an error when clicking "Run Full Damage Assessment Pipeline"
- You need to either:
  1. Add the YOLO model file to that location, OR
  2. Update the model path in `utils/backend_integration.py`

### Sample Images
For testing, you can use:
- Any satellite imagery (JPG, PNG, TIFF)
- Aerial photos
- Google Earth screenshots
- The `sample_satellite.jpg` file in the project root

## 🐛 Troubleshooting

### Problem: "streamlit: command not found"
**Solution:**
```bash
pip3 install streamlit
```

### Problem: "ModuleNotFoundError: No module named 'cv2'"
**Solution:**
```bash
pip3 install opencv-python
```

### Problem: "Port 8502 is already in use"
**Solution:**
```bash
# Use a different port
streamlit run app.py --server.port 8503
```

### Problem: "Cannot find YOLO model"
**Solution:**
Either:
1. Place your YOLO model at `Backend/best.pt`
2. Or modify the model path in `utils/backend_integration.py`

### Problem: App loads but shows errors
**Solution:**
```bash
# Reinstall all dependencies
pip3 install -r requirements.txt --upgrade
```

## 🛑 How to Stop the App

Press `Ctrl + C` in the terminal where the app is running.

## 📊 Testing the App

### Quick Test (Without Backend Model)
1. Start the app
2. Navigate through all 5 tabs
3. Check that the UI loads correctly
4. Upload test images (they won't process without the model)

### Full Test (With Backend Model)
1. Ensure YOLO model is at `Backend/best.pt`
2. Start the app
3. Upload PRE-disaster image
4. Upload POST-disaster image
5. Click "Run Full Damage Assessment Pipeline"
6. Wait for processing (may take 30-60 seconds)
7. Navigate through all tabs to see results
8. Download reports from the Export tab

## 🎯 Expected Behavior

### Successful Run
```
✅ Analysis complete! Navigate to other tabs to view results.
```

### Error (Missing Model)
```
❌ Error during analysis: [Errno 2] No such file or directory: 'Backend/best.pt'
```

## 📁 Project Structure

```
CV_Frontend/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── start_app.sh                    # Startup script
├── HOW_TO_RUN.md                   # Quick reference
├── STARTUP_GUIDE.md                # This file
│
├── Backend/                        # Backend CV pipeline
│   ├── pipeline.py                 # Main pipeline class
│   ├── inference.py                # YOLO inference
│   ├── change_map.py               # Change detection
│   ├── clustering.py               # Damage clustering
│   ├── heatmap.py                  # Heatmap generation
│   └── ...
│
├── components/                     # UI components
│   ├── css_injector.py             # Dark theme CSS
│   ├── footer.py                   # Footer component
│   └── kpi_card.py                 # KPI card component
│
├── config/                         # Configuration
│   └── theme.py                    # Theme colors
│
├── utils/                          # Utilities
│   ├── backend_integration.py      # Backend wrapper
│   ├── cv_pipeline.py              # CV operations
│   └── session_utils.py            # Session management
│
└── data/                           # Data
    └── dummy_data.py               # Sample data
```

## 🎓 Next Steps

After successfully running the app:

1. **Test with sample images** - Use any satellite imagery
2. **Add YOLO model** - For full functionality
3. **Customize theme** - Edit `config/theme.py`
4. **Add features** - Extend functionality as needed
5. **Deploy** - Consider Streamlit Cloud for hosting

## 💡 Tips

- **First time users**: Start without the YOLO model to see the UI
- **Development**: Use `--server.runOnSave true` for auto-reload
- **Performance**: Smaller images process faster
- **Browser**: Works best in Chrome or Firefox
- **Mobile**: Responsive design works on tablets and phones

## 📞 Support

If you encounter issues:
1. Check the terminal output for error messages
2. Verify all dependencies are installed
3. Ensure Python 3.9+ is being used
4. Check that all files are in the correct locations
5. Try reinstalling dependencies

## ✨ Features Checklist

- ✅ Premium dark theme UI
- ✅ Dual image upload (PRE/POST)
- ✅ Real-time progress tracking
- ✅ 7-stage CV pipeline visualization
- ✅ Damage assessment with metrics
- ✅ Interactive heatmap analysis
- ✅ Export results (PNG/CSV)
- ✅ Responsive design
- ✅ Error handling
- ⚠️ YOLO model integration (requires model file)

---

**Ready to start?** Run: `./start_app.sh` or `streamlit run app.py --server.port 8502`
