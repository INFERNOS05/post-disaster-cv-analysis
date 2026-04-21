# Run Instructions - CV Disaster Dashboard

## ✅ Changes Applied

The Streamlit dashboard now **exactly replicates** the flow from `Backend/run_pipeline.py`.

### What Changed:
1. **Simplified backend integration** - No fake stages, uses only real pipeline outputs
2. **Updated Tab 2** - Shows only real outputs: final overlay, change detection, impact, clusters
3. **Fixed key names** - Uses `result["impact"]` and `result["heatmap"]` correctly
4. **Removed fake preprocessing** - No CLAHE, Canny, HSV, Harris stages

## 🚀 How to Run

```bash
# Install dependencies (if needed)
pip install -r requirements.txt

# Run the dashboard
python3 -m streamlit run app.py --server.port 8502
```

Then open: **http://localhost:8502**

## 📋 Testing Steps

### 1. Upload Images
- Upload PRE-disaster satellite image
- Upload POST-disaster satellite image

### 2. Run Analysis
- Click "🔥 Run Full Damage Assessment Pipeline"
- Watch the progress bar

### 3. Check Console Output
You should see output matching `run_pipeline.py`:

```
==============================================================
STREAMLIT PIPELINE (replicating run_pipeline.py)
==============================================================
PRE:  /tmp/cv_dashboard_pre.jpg
POST: /tmp/cv_dashboard_post.jpg

==============================================================
RUNNING FULL PIPELINE (DETECTION MODEL)
==============================================================

[1/6] Running inference on PRE image...
      → PRE raw detections: X
      → PRE avg confidence: X.XXX

[2/6] Running inference on POST image...
      → POST raw detections: X
      → POST avg confidence: X.XXX

[3/6] POST detections (filter disabled)...
      → POST final detections: X
      → Using all POST detections for damage assessment

[4/6] Computing change detection map...

[5/6] Analyzing grid and clustering...
      → X clusters detected

[6/6] Building final overlay...

✅ Pipeline complete!
   PRE buildings: X
   POST buildings: X
   Damage %: XX.X%
==============================================================

📊 Impact: {'pre_buildings': X, 'post_buildings': X, ...}
🎯 Clusters: X

✅ Pipeline complete!
   PRE detections:  X
   POST detections: X
   Avg confidence:  X.XXX
==============================================================
```

### 4. Verify Tabs

**Tab 1 (Upload & Process):**
- ✅ Shows PRE/POST images
- ✅ Shows quick summary metrics after analysis

**Tab 2 (CV Processing Pipeline):**
- ✅ Shows original PRE/POST images
- ✅ Shows final damage assessment overlay (`result["overlay"]`)
- ✅ Shows change detection overlay (`overlay_change_map(...)`)
- ✅ Shows impact metrics (`result["impact"]`)
- ✅ Shows cluster analysis (`result["clusters"]`)

**Tab 3 (Damage Assessment):**
- ✅ Shows damage overlay
- ✅ Shows metrics and statistics
- ✅ Shows damage distribution chart

**Tab 4 (Heatmap Analysis):**
- ✅ Shows final damage overlay (contains heatmap)
- ✅ Shows grid visualization
- ✅ Shows cluster details

**Tab 5 (Reports & Export):**
- ✅ Download PNG images
- ✅ Download CSV with correct format
- ✅ Download text summary

### 5. Verify CSV Export

Download "Results CSV" and verify it contains:

```csv
image_name,pre_buildings,post_buildings,affected_buildings,damage_percentage,severity_score,confidence,clusters,priority_zones
analysis,X,X,X,XX.XX,X.XX,X.XXXX,X,X
```

## 🔍 Debugging

If you see errors:

1. **Import errors:**
   ```bash
   python3 -c "from utils.backend_integration import StreamlitPipelineWrapper"
   ```

2. **Model not found:**
   - Verify `Backend/best.pt` exists
   - Check model path in `utils/backend_integration.py` (line 23)

3. **No detections:**
   - Check console output for detection counts
   - Verify confidence threshold is 0.20 in `Backend/inference.py`
   - Try different images with visible buildings

4. **Dimension errors:**
   - Already fixed in `Backend/grid.py` and `Backend/post_process.py`
   - Should not occur with current code

## 📊 Expected Behavior

### With Valid Building Images:
- PRE detections: > 0
- POST detections: > 0
- Damage %: Based on building classes
- Clusters: 1-5 typically
- Final overlay: Shows colored bounding boxes + heatmap + cluster markers

### With No Buildings:
- PRE detections: 0
- POST detections: 0
- Warning: "⚠️ No buildings detected in POST image"
- Metrics: Safe defaults (0 values)

## 🎯 Success Criteria

✅ Console output matches `run_pipeline.py` format
✅ PRE and POST detection counts are correct
✅ Final overlay shows detection boxes + heatmap + clusters
✅ Change detection overlay shows pixel-level changes
✅ Impact metrics are accurate
✅ CSV export contains correct data
✅ No fake preprocessing stages shown
✅ All outputs come from real backend modules

## 📁 Files Modified

1. `utils/backend_integration.py` - Simplified to exact pipeline replication
2. `app.py` - Updated Tab 1, Tab 2, Tab 4

## 📁 Files NOT Modified

- `Backend/pipeline.py` - Source of truth
- `Backend/inference.py` - Confidence 0.20
- `Backend/run_pipeline.py` - Reference implementation
- All other Backend modules

## 🆘 Support

If issues persist:
1. Check `PIPELINE_REPLICATION_SUMMARY.md` for detailed changes
2. Compare console output with expected output above
3. Verify all Backend modules are present and unchanged
4. Check that `Backend/best.pt` model file exists
