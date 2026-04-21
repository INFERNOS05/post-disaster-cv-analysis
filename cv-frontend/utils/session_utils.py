# Session state management utilities
import streamlit as st

DEFAULT_SETTINGS = {
    "confidence_threshold": 0.5,
    "damage_sensitivity": "Medium",
    "show_heatmap": True,
    "chart_color_scheme": "Default",
    "show_dummy_banner": True,
}

def init_session_state():
    """Initialize all session state keys to defaults if not present."""
    if "uploaded_image" not in st.session_state:
        st.session_state.uploaded_image = None
    if "image_metadata" not in st.session_state:
        st.session_state.image_metadata = None
    if "damage_result" not in st.session_state:
        st.session_state.damage_result = None
    if "density_result" not in st.session_state:
        st.session_state.density_result = None
    if "settings" not in st.session_state:
        st.session_state.settings = DEFAULT_SETTINGS.copy()
    if "analysis_complete" not in st.session_state:
        st.session_state.analysis_complete = False

def update_setting(key: str, value):
    """Update a single setting in session_state['settings']."""
    if key in DEFAULT_SETTINGS:
        st.session_state.settings[key] = value

def reset_settings():
    """Reset session_state['settings'] to DEFAULT_SETTINGS."""
    st.session_state.settings = DEFAULT_SETTINGS.copy()
