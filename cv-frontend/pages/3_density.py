# Urban Density Mapping Page
import streamlit as st
from components.css_injector import inject_global_css
from components.footer import render_footer
from components.kpi_card import render_kpi_card
from utils.session_utils import init_session_state
from data.dummy_data import DENSITY_RESULT

# Page configuration
st.set_page_config(
    page_title="Urban Density - CV Disaster Dashboard",
    page_icon="🏙️",
    layout="wide"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Page header
st.title("🏙️ Urban Density Mapping")
st.markdown("Analyze urban density patterns and built-up area distribution.")
st.markdown("---")

# Check if image has been uploaded
if st.session_state.uploaded_image is None:
    st.info("📤 Please upload a satellite image first to view urban density results.")
    if st.button("Go to Upload Page"):
        st.switch_page("pages/1_upload.py")
else:
    # Get density result (use dummy data if not available)
    density_result = st.session_state.density_result if st.session_state.density_result else DENSITY_RESULT
    
    # Display image
    st.markdown("### 🗺️ Satellite Image with Density Overlay")
    st.image(st.session_state.uploaded_image, use_container_width=True)
    
    st.markdown("---")
    
    # Summary metrics
    st.markdown("### 📊 Summary Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Built-Up Area", f"{density_result['built_up_area_pct']:.1f}%")
    
    with col2:
        st.metric("Population Proxy Score", f"{density_result['population_proxy_score']:.1f}")
    
    with col3:
        st.metric("Dominant Density Class", density_result['dominant_class'])
    
    st.markdown("---")
    
    # Zone breakdown
    st.markdown("### 🏘️ Density Zone Breakdown")
    
    col1, col2, col3 = st.columns(3)
    
    zone_breakdown = density_result['zone_breakdown']
    
    with col1:
        render_kpi_card("Sparse Zones", f"{zone_breakdown['Sparse']:.1f}%", "🌾")
    
    with col2:
        render_kpi_card("Moderate Zones", f"{zone_breakdown['Moderate']:.1f}%", "🏘️")
    
    with col3:
        render_kpi_card("Dense Zones", f"{zone_breakdown['Dense']:.1f}%", "🏙️")
    
    # Legend
    st.markdown("---")
    st.markdown("### 🎨 Density Class Legend")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("🟢 **Sparse** - Low building density, rural areas")
    
    with col2:
        st.markdown("🟡 **Moderate** - Medium density, suburban areas")
    
    with col3:
        st.markdown("🔴 **Dense** - High density, urban core areas")

# Footer
render_footer()
