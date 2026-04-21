# Footer component
import streamlit as st

def get_footer_html() -> str:
    """Returns the footer HTML string."""
    return """
    <div class="dashboard-footer">
        <p>
            <strong>Project Team</strong> | 
            <strong>OST Project 2026</strong> | 
            Powered by Streamlit + OpenCV + Deep Learning
        </p>
    </div>
    """

def render_footer():
    """Renders the standard footer."""
    st.markdown(get_footer_html(), unsafe_allow_html=True)
