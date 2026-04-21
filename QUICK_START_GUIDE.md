# 🚀 Quick Start Guide

## CV Disaster Dashboard - Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip3 install -r requirements.txt
```

Or use the quick start script:
```bash
./run.sh
```

### Step 2: Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will automatically open in your browser at:
**http://localhost:8501**

### Step 3: Explore the Dashboard

#### 🏠 Dashboard Home
- View KPI cards showing system statistics
- Click "Start Analysis" to upload an image
- See "How It Works" workflow

#### 📤 Upload Satellite Image
1. Click "Browse files" or drag & drop an image
2. Supported formats: JPG, PNG, TIFF
3. View image preview and metadata
4. Click "Analyze Image" to process
5. Navigate to results pages

#### ⚠️ Damage Assessment
- View original satellite image
- See overall damage classification (Low/Medium/Severe)
- Check confidence score
- Review region-wise damage statistics
- Download CSV report

#### 🏙️ Urban Density Mapping
- View satellite image with density overlay
- See built-up area percentage
- Check population proxy score
- Review zone breakdown (Sparse/Moderate/Dense)
- View density class legend

#### 📊 Analytics Reports
- Damage trend by region (bar chart)
- Monthly processed images (bar chart)
- Model confidence history (line chart)
- Interactive charts with hover tooltips

#### ⚙️ Settings
- Adjust confidence threshold
- Set damage sensitivity level
- Toggle heatmap overlay
- Choose chart color scheme
- Reset to defaults

#### ℹ️ About Project
- Read project objectives
- Learn about methodology
- View technology stack
- Meet the team
- See OST Project 2026 information

## 🎨 UI Features

### Navigation
- **Sidebar**: Always accessible navigation menu
- **Page Links**: Click any page to navigate instantly
- **Breadcrumbs**: Know where you are at all times

### Visual Design
- **Clean Layout**: Card-based design with soft shadows
- **Color Coding**: 
  - 🟢 Green (Low damage, Sparse density)
  - 🟡 Yellow (Medium damage, Moderate density)
  - 🔴 Red (Severe damage, Dense areas)
- **Responsive**: Works on desktop, tablet, and mobile
- **Icons**: Visual indicators throughout the interface

### Interactions
- **Hover Effects**: Buttons and cards respond to mouse hover
- **Progress Indicators**: See analysis progress in real-time
- **Notifications**: Success/error messages for user actions
- **Downloads**: Export reports with one click

## 📊 Sample Workflow

### Complete Analysis Workflow

1. **Start** → Open Dashboard Home
2. **Upload** → Go to Upload page, select satellite image
3. **Analyze** → Click "Analyze Image" button
4. **View Damage** → Navigate to Damage Assessment
5. **View Density** → Navigate to Urban Density Mapping
6. **Check Analytics** → View trends and statistics
7. **Download** → Export CSV report from Damage page
8. **Configure** → Adjust settings as needed

## 🔧 Customization

### Change Theme Colors

Edit `config/theme.py`:
```python
PRIMARY = "#2563EB"    # Change to your primary color
SECONDARY = "#10B981"  # Change to your secondary color
```

### Update Dummy Data

Edit `data/dummy_data.py`:
```python
KPI_CARDS = [
    {"label": "Your Metric", "value": 100, "icon": "🎯", "delta": "+10"}
]
```

### Add Custom Pages

1. Create new file in `pages/` directory
2. Name it with number prefix: `7_newpage.py`
3. Add page link in `app.py` sidebar
4. Follow existing page structure

## 🐛 Troubleshooting

### Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found
```bash
pip3 install --upgrade -r requirements.txt
```

### Image Upload Issues
- Ensure file is JPG, PNG, or TIFF
- Check file size (< 50MB recommended)
- Verify file is not corrupted

### Blank Page
- Clear browser cache
- Restart Streamlit server
- Check console for errors

## 💡 Tips & Tricks

### Keyboard Shortcuts
- `R` - Rerun the app
- `C` - Clear cache
- `Ctrl+C` - Stop server (in terminal)

### Performance
- Use smaller images for faster processing
- Clear session state periodically
- Restart app if it becomes slow

### Development
- Enable debug mode: `streamlit run app.py --logger.level=debug`
- Watch for file changes: Auto-reload is enabled by default
- Use `st.write()` for quick debugging

## 📚 Additional Resources

### Documentation
- Streamlit Docs: https://docs.streamlit.io
- Plotly Docs: https://plotly.com/python/
- PIL/Pillow Docs: https://pillow.readthedocs.io/

### Support
- Check README.md for detailed information
- Review IMPLEMENTATION_SUMMARY.md for technical details
- Contact project team for assistance

## ✅ Checklist

Before presenting/demoing:
- [ ] All dependencies installed
- [ ] Dashboard launches without errors
- [ ] All 7 pages load correctly
- [ ] Image upload works
- [ ] Charts display properly
- [ ] Navigation works smoothly
- [ ] Responsive design tested
- [ ] Sample images prepared

## 🎓 OST Project 2026

Built with ❤️ using Streamlit, OpenCV, and Deep Learning

---

**Ready to go!** Run `./run.sh` or `streamlit run app.py` to start exploring.
