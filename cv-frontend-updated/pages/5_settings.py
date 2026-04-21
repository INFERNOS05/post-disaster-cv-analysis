# Settings Page
import streamlit as st
from components.css_injector import inject_global_css
from components.footer import render_footer
from utils.session_utils import init_session_state, update_setting, reset_settings

# Page configuration
st.set_page_config(
    page_title="Settings - CV Disaster Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Page header
st.title("⚙️ Settings")
st.markdown("Configure analysis parameters and display preferences.")
st.markdown("---")

# Model Configuration Section
st.markdown("### 🤖 Model Configuration")

col1, col2 = st.columns(2)

with col1:
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.settings["confidence_threshold"],
        step=0.05,
        help="Minimum confidence score for predictions"
    )
    update_setting("confidence_threshold", confidence_threshold)

with col2:
    damage_sensitivity = st.selectbox(
        "Damage Sensitivity Level",
        options=["Low", "Medium", "High"],
        index=["Low", "Medium", "High"].index(st.session_state.settings["damage_sensitivity"]),
        help="Sensitivity level for damage detection"
    )
    update_setting("damage_sensitivity", damage_sensitivity)

show_heatmap = st.checkbox(
    "Enable Heatmap Overlay",
    value=st.session_state.settings["show_heatmap"],
    help="Show/hide heatmap overlay on damage assessment"
)
update_setting("show_heatmap", show_heatmap)

st.markdown("---")

# Display Preferences Section
st.markdown("### 🎨 Display Preferences")

col1, col2 = st.columns(2)

with col1:
    chart_color_scheme = st.selectbox(
        "Chart Color Scheme",
        options=["Default", "Colorblind-Friendly"],
        index=["Default", "Colorblind-Friendly"].index(st.session_state.settings["chart_color_scheme"]),
        help="Color scheme for charts and visualizations"
    )
    update_setting("chart_color_scheme", chart_color_scheme)

with col2:
    show_dummy_banner = st.checkbox(
        "Show Dummy Data Banner",
        value=st.session_state.settings["show_dummy_banner"],
        help="Display banner when using dummy data"
    )
    update_setting("show_dummy_banner", show_dummy_banner)

st.markdown("---")

# Reset to Defaults
if st.button("🔄 Reset to Defaults", type="secondary", use_container_width=True):
    reset_settings()
    st.success("✅ Settings have been reset to default values!")
    st.rerun()

# Current Settings Summary
st.markdown("---")
st.markdown("### 📋 Current Settings")

settings_data = {
    "Setting": [
        "Confidence Threshold",
        "Damage Sensitivity",
        "Show Heatmap",
        "Chart Color Scheme",
        "Show Dummy Banner"
    ],
    "Value": [
        f"{st.session_state.settings['confidence_threshold']:.2f}",
        st.session_state.settings['damage_sensitivity'],
        "Enabled" if st.session_state.settings['show_heatmap'] else "Disabled",
        st.session_state.settings['chart_color_scheme'],
        "Enabled" if st.session_state.settings['show_dummy_banner'] else "Disabled"
    ]
}

import pandas as pd
st.dataframe(pd.DataFrame(settings_data), use_container_width=True, hide_index=True)

# Footer
render_footer()
