# CV-Based Post-Disaster Damage Assessment & Urban Density Mapping Dashboard

A modern, professional Streamlit dashboard for AI-powered satellite imagery analysis.

## Features

- **Dashboard Home**: Overview with KPI cards and quick navigation
- **Upload Module**: Drag-and-drop satellite image upload with metadata display
- **Damage Assessment**: Detailed damage severity analysis with heatmaps
- **Urban Density Mapping**: Built-up area analysis and density classification
- **Analytics Reports**: Interactive charts and trend visualizations
- **Settings**: Configurable analysis parameters
- **About**: Project information and team details

## Requirements

- Python 3.8+
- Streamlit 1.35+
- See `requirements.txt` for full dependencies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd CV_Frontend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Project Structure

```
CV_Frontend/
├── app.py                  # Main entry point
├── pages/                  # Multi-page app pages
│   ├── 1_upload.py
│   ├── 2_damage.py
│   ├── 3_density.py
│   ├── 4_analytics.py
│   ├── 5_settings.py
│   └── 6_about.py
├── components/             # Reusable UI components
│   ├── css_injector.py
│   ├── footer.py
│   └── kpi_card.py
├── utils/                  # Utility functions
│   └── session_utils.py
├── config/                 # Configuration
│   └── theme.py
├── data/                   # Dummy data
│   └── dummy_data.py
├── assets/                 # Static assets
│   └── logo.png
└── requirements.txt
```

## Design Features

- Clean, professional enterprise dashboard design
- Modern card-based layout with soft shadows
- Responsive layout (mobile-friendly)
- Consistent color palette (Blue/Green accents)
- Elegant typography with clear hierarchy
- Smooth transitions and interactions

## Configuration

Edit `config/theme.py` to customize:
- Color palette
- Typography
- Spacing
- Card styles

## Data

Currently uses dummy data for demonstration. To integrate real AI models:
1. Replace `data/dummy_data.py` with actual model outputs
2. Update `utils/analysis_stub.py` with real analysis pipeline
3. Implement image processing in `utils/image_utils.py`


---

**Powered by Streamlit + OpenCV + Deep Learning**
