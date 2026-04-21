# Damage Assessment Page
import streamlit as st
from components.css_injector import inject_global_css
from components.footer import render_footer
from utils.session_utils import init_session_state
from data.dummy_data import DAMAGE_RESULT
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Damage Assessment - CV Disaster Dashboard",
    page_icon="⚠️",
    layout="wide"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Page header
st.title("⚠️ Damage Assessment Results")
st.markdown("Detailed analysis of disaster damage severity and spatial distribution.")
st.markdown("---")

# Check if image has been uploaded
if st.session_state.uploaded_image is None:
    st.info("📤 Please upload a satellite image first to view damage assessment results.")
    if st.button("Go to Upload Page"):
        st.switch_page("pages/1_upload.py")
else:
    # Get damage result (use dummy data if not available)
    damage_result = st.session_state.damage_result if st.session_state.damage_result else DAMAGE_RESULT
    
    # Display overall damage classification
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🖼️ Original Image")
        st.image(st.session_state.uploaded_image, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Overall Assessment")
        
        # Damage class badge
        damage_class = damage_result["damage_class"]
        badge_class = f"badge-{damage_class.lower()}"
        st.markdown(f'<span class="{badge_class}">{damage_class} Damage</span>', unsafe_allow_html=True)
        
        st.markdown("")
        
        # Confidence score
        confidence = damage_result["confidence_score"]
        st.metric("Confidence Score", f"{confidence * 100:.1f}%")
        st.progress(confidence)
    
    st.markdown("---")
    
    # Region-wise damage statistics
    st.markdown("### 📋 Region-wise Damage Statistics")
    
    regions_df = pd.DataFrame(damage_result["regions"])
    regions_df.columns = ["Region Name", "Damage Class", "Affected Area (%)", "Confidence Score"]
    
    st.dataframe(
        regions_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Download report button
    st.markdown("---")
    csv = regions_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Report (CSV)",
        data=csv,
        file_name="damage_assessment_report.csv",
        mime="text/csv",
        use_container_width=True
    )

# Footer
render_footer()
