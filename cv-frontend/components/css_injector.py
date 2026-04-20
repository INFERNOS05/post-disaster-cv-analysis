# CSS injection component
import streamlit as st
from config import theme

def get_global_css() -> str:
    """Returns the global CSS string."""
    return f"""
    <style>
        /* Global reset and font */
        * {{
            font-family: {theme.FONT_FAMILY};
        }}
        
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        /* Card containers */
        .kpi-card, .chart-card, .result-card {{
            background: #FFFFFF;
            border-radius: {theme.CARD_BORDER_RADIUS};
            box-shadow: {theme.CARD_BOX_SHADOW};
            padding: {theme.CARD_PADDING};
            margin-bottom: {theme.SPACING_SM};
        }}
        
        /* Damage class badges */
        .badge-low {{
            background: {theme.SECONDARY};
            color: white;
            border-radius: 6px;
            padding: 4px 10px;
            font-weight: 600;
            display: inline-block;
        }}
        
        .badge-medium {{
            background: {theme.AMBER};
            color: white;
            border-radius: 6px;
            padding: 4px 10px;
            font-weight: 600;
            display: inline-block;
        }}
        
        .badge-severe {{
            background: {theme.DANGER};
            color: white;
            border-radius: 6px;
            padding: 4px 10px;
            font-weight: 600;
            display: inline-block;
        }}
        
        /* Footer */
        .dashboard-footer {{
            border-top: 1px solid rgba(17,24,39,0.1);
            color: {theme.MUTED};
            padding-top: {theme.SPACING_SM};
            margin-top: {theme.SPACING_LG};
            font-size: {theme.FONT_SIZE_SMALL};
            text-align: center;
        }}
        
        /* Hero section */
        .hero-section {{
            text-align: center;
            padding: {theme.SPACING_LG} 0;
            margin-bottom: {theme.SPACING_MD};
        }}
        
        .hero-title {{
            font-size: {theme.FONT_SIZE_H1};
            font-weight: 700;
            color: {theme.TEXT};
            margin-bottom: {theme.SPACING_SM};
        }}
        
        .hero-description {{
            font-size: {theme.FONT_SIZE_BODY};
            color: {theme.MUTED};
            max-width: 600px;
            margin: 0 auto {theme.SPACING_MD};
        }}
        
        /* Responsive: single column below 768px */
        @media (max-width: 768px) {{
            [data-testid="column"] {{
                width: 100% !important;
            }}
        }}
        
        /* Streamlit button styling */
        .stButton > button {{
            background-color: {theme.PRIMARY};
            color: white;
            border-radius: 8px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }}
        
        .stButton > button:hover {{
            background-color: #1d4ed8;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }}
    </style>
    """

def inject_global_css():
    """Injects the global CSS into the Streamlit app."""
    st.markdown(get_global_css(), unsafe_allow_html=True)
