# Analytics Reports Page
import streamlit as st
from components.css_injector import inject_global_css
from components.footer import render_footer
from utils.session_utils import init_session_state
from data.dummy_data import ANALYTICS_DAMAGE_TREND, ANALYTICS_MONTHLY_VOLUME, ANALYTICS_CONFIDENCE_HISTORY
import plotly.graph_objects as go
import plotly.express as px
from config import theme

# Page configuration
st.set_page_config(
    page_title="Analytics - CV Disaster Dashboard",
    page_icon="📊",
    layout="wide"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Page header
st.title("📊 Analytics Reports")
st.markdown("Comprehensive analytics and trends for damage assessment and model performance.")
st.markdown("---")

# Chart 1: Damage Trend by Region
st.markdown("### 📈 Damage Trend by Region")
st.markdown("Distribution of damage severity classifications across analyzed regions.")

regions = [d["region"] for d in ANALYTICS_DAMAGE_TREND]
low_values = [d["Low"] for d in ANALYTICS_DAMAGE_TREND]
medium_values = [d["Medium"] for d in ANALYTICS_DAMAGE_TREND]
severe_values = [d["Severe"] for d in ANALYTICS_DAMAGE_TREND]

fig1 = go.Figure(data=[
    go.Bar(name='Low', x=regions, y=low_values, marker_color=theme.SECONDARY),
    go.Bar(name='Medium', x=regions, y=medium_values, marker_color=theme.AMBER),
    go.Bar(name='Severe', x=regions, y=severe_values, marker_color=theme.DANGER)
])

fig1.update_layout(
    barmode='group',
    xaxis_title="Region",
    yaxis_title="Percentage",
    hovermode='x unified',
    height=400
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# Chart 2 & 3 in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📅 Monthly Processed Images")
    st.markdown("Volume of satellite images processed per month.")
    
    months = [d["month"] for d in ANALYTICS_MONTHLY_VOLUME]
    counts = [d["count"] for d in ANALYTICS_MONTHLY_VOLUME]
    
    fig2 = go.Figure(data=[
        go.Bar(x=months, y=counts, marker_color=theme.PRIMARY)
    ])
    
    fig2.update_layout(
        xaxis_title="Month",
        yaxis_title="Image Count",
        height=350
    )
    
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.markdown("### 🎯 Model Confidence History")
    st.markdown("Average model confidence score per analysis session.")
    
    sessions = [d["session"] for d in ANALYTICS_CONFIDENCE_HISTORY]
    confidences = [d["avg_confidence"] for d in ANALYTICS_CONFIDENCE_HISTORY]
    
    fig3 = go.Figure(data=[
        go.Scatter(
            x=sessions,
            y=confidences,
            mode='lines+markers',
            marker=dict(color=theme.SECONDARY, size=8),
            line=dict(color=theme.SECONDARY, width=2)
        )
    ])
    
    fig3.update_layout(
        xaxis_title="Session",
        yaxis_title="Avg Confidence Score",
        yaxis_range=[0.7, 1.0],
        height=350
    )
    
    st.plotly_chart(fig3, use_container_width=True)

# Footer
render_footer()
