# KPI card component
import streamlit as st

def render_kpi_card(label: str, value, icon: str, delta: str = None, color: str = None):
    """Renders a single KPI card using st.metric."""
    st.metric(
        label=f"{icon} {label}",
        value=value,
        delta=delta
    )
