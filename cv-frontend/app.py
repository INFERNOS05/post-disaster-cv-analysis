# CV-Based Post-Disaster Damage Assessment & Urban Density Mapping Dashboard
import streamlit as st
from utils.session_utils import init_session_state
from components.css_injector import inject_global_css

# Page configuration
st.set_page_config(
    page_title="CV Disaster Dashboard",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
init_session_state()

# Inject global CSS
inject_global_css()

# Sidebar navigation
with st.sidebar:
    st.image("assets/logo.png", width=50)
    st.title("CV Disaster Dashboard")
    st.markdown("---")
    
    st.page_link("app.py", label="🏠 Dashboard Home")
    st.page_link("pages/1_upload.py", label="📤 Upload Satellite Image")
    st.page_link("pages/2_damage.py", label="⚠️ Damage Assessment")
    st.page_link("pages/3_density.py", label="🏙️ Urban Density Mapping")
    st.page_link("pages/4_analytics.py", label="📊 Analytics Reports")
    st.page_link("pages/5_settings.py", label="⚙️ Settings")
    st.page_link("pages/6_about.py", label="ℹ️ About Project")

# Main content - Dashboard Home
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">CV-Based Post-Disaster Damage Assessment & Urban Density Mapping using Satellite Imagery</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-description">AI-powered satellite imagery analysis for disaster recovery and urban planning.</p>', unsafe_allow_html=True)

if st.button("🚀 Start Analysis", use_container_width=False):
    st.switch_page("pages/1_upload.py")

st.markdown('</div>', unsafe_allow_html=True)

# KPI Cards
st.markdown("### 📊 Key Performance Indicators")
from data.dummy_data import KPI_CARDS
from components.kpi_card import render_kpi_card

col1, col2, col3, col4 = st.columns(4)

with col1:
    kpi = KPI_CARDS[0]
    render_kpi_card(kpi["label"], kpi["value"], kpi["icon"], kpi["delta"])

with col2:
    kpi = KPI_CARDS[1]
    render_kpi_card(kpi["label"], kpi["value"], kpi["icon"], kpi["delta"])

with col3:
    kpi = KPI_CARDS[2]
    render_kpi_card(kpi["label"], kpi["value"], kpi["icon"], kpi["delta"])

with col4:
    kpi = KPI_CARDS[3]
    render_kpi_card(kpi["label"], kpi["value"], kpi["icon"], kpi["delta"])

# How It Works section
st.markdown("---")
st.markdown("### 🔄 How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 3rem;">📤</div>
        <h3>Upload</h3>
        <p>Upload satellite imagery in JPG, PNG, or TIFF format</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 3rem;">🤖</div>
        <h3>Analyze</h3>
        <p>AI models process the image for damage and density analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 3rem;">📊</div>
        <h3>View Results</h3>
        <p>Visualize damage assessment and urban density mapping results</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
from components.footer import render_footer
render_footer()
