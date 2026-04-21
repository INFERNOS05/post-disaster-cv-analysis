# CSS injection component - Premium Dark Theme
import streamlit as st
from config import theme

def get_global_css() -> str:
    """Returns the global CSS string for premium dark theme."""
    return f"""
    <style>
        /* Global reset and dark theme */
        * {{
            font-family: {theme.FONT_FAMILY};
        }}
        
        /* Main app background */
        .stApp {{
            background: {theme.BACKGROUND};
            color: {theme.TEXT};
        }}
        
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background: {theme.SURFACE};
            border-right: 1px solid {theme.SURFACE_LIGHT};
        }}
        
        [data-testid="stSidebar"] .stMarkdown {{
            color: {theme.TEXT};
        }}
        
        /* Card containers */
        .cv-card {{
            background: {theme.SURFACE};
            border-radius: {theme.CARD_BORDER_RADIUS};
            box-shadow: {theme.CARD_BOX_SHADOW};
            padding: {theme.CARD_PADDING};
            margin-bottom: {theme.SPACING_MD};
            border: {theme.CARD_BORDER};
        }}
        
        .cv-card-header {{
            font-size: {theme.FONT_SIZE_H3};
            font-weight: 700;
            color: {theme.TEXT};
            margin-bottom: {theme.SPACING_SM};
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .cv-card-body {{
            color: {theme.TEXT_MUTED};
        }}
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background: {theme.SURFACE};
            padding: 8px;
            border-radius: {theme.TAB_BORDER_RADIUS};
            border: {theme.CARD_BORDER};
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background: transparent;
            border-radius: 8px;
            color: {theme.TEXT_MUTED};
            padding: 12px 24px;
            font-weight: 600;
            border: none;
        }}
        
        .stTabs [data-baseweb="tab"]:hover {{
            background: {theme.TAB_HOVER_BG};
            color: {theme.TEXT};
        }}
        
        .stTabs [aria-selected="true"] {{
            background: {theme.TAB_ACTIVE_BG} !important;
            color: {theme.PRIMARY} !important;
            border: 1px solid {theme.PRIMARY} !important;
        }}
        
        /* Damage severity badges */
        .badge-low {{
            background: {theme.SUCCESS};
            color: white;
            border-radius: 8px;
            padding: 6px 16px;
            font-weight: 700;
            display: inline-block;
            font-size: {theme.FONT_SIZE_SMALL};
        }}
        
        .badge-medium {{
            background: {theme.WARNING};
            color: white;
            border-radius: 8px;
            padding: 6px 16px;
            font-weight: 700;
            display: inline-block;
            font-size: {theme.FONT_SIZE_SMALL};
        }}
        
        .badge-severe {{
            background: {theme.DANGER};
            color: white;
            border-radius: 8px;
            padding: 6px 16px;
            font-weight: 700;
            display: inline-block;
            font-size: {theme.FONT_SIZE_SMALL};
        }}
        
        /* CV Processing stage badges */
        .cv-stage {{
            background: {theme.SURFACE_LIGHT};
            color: {theme.TEXT};
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: 600;
            display: inline-block;
            font-size: {theme.FONT_SIZE_SMALL};
            border: 1px solid {theme.PRIMARY};
        }}
        
        /* Metric cards */
        .metric-card {{
            background: linear-gradient(135deg, {theme.SURFACE} 0%, {theme.SURFACE_LIGHT} 100%);
            border-radius: {theme.CARD_BORDER_RADIUS};
            padding: {theme.SPACING_MD};
            border: {theme.CARD_BORDER};
            text-align: center;
        }}
        
        .metric-value {{
            font-size: {theme.FONT_SIZE_H2};
            font-weight: 800;
            color: {theme.PRIMARY};
            margin: 8px 0;
        }}
        
        .metric-label {{
            font-size: {theme.FONT_SIZE_SMALL};
            color: {theme.TEXT_MUTED};
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Progress bar */
        .stProgress > div > div > div > div {{
            background: linear-gradient(90deg, {theme.PRIMARY} 0%, {theme.ACCENT} 100%);
        }}
        
        /* Buttons */
        .stButton > button {{
            background: linear-gradient(135deg, {theme.PRIMARY} 0%, {theme.ACCENT} 100%);
            color: white;
            border-radius: 12px;
            padding: 12px 32px;
            font-weight: 700;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        }}
        
        /* File uploader */
        [data-testid="stFileUploader"] {{
            background: {theme.SURFACE};
            border: 2px dashed {theme.PRIMARY};
            border-radius: {theme.CARD_BORDER_RADIUS};
            padding: {theme.SPACING_LG};
        }}
        
        [data-testid="stFileUploader"] label {{
            color: {theme.TEXT} !important;
        }}
        
        /* Dataframe styling */
        .stDataFrame {{
            background: {theme.SURFACE};
            border-radius: {theme.CARD_BORDER_RADIUS};
        }}
        
        /* Image containers */
        .cv-image-container {{
            background: {theme.SURFACE};
            border-radius: {theme.CARD_BORDER_RADIUS};
            padding: {theme.SPACING_SM};
            border: {theme.CARD_BORDER};
            margin-bottom: {theme.SPACING_SM};
        }}
        
        .cv-image-label {{
            font-size: {theme.FONT_SIZE_SMALL};
            color: {theme.TEXT_MUTED};
            text-align: center;
            margin-top: 8px;
            font-weight: 600;
        }}
        
        /* Hero section */
        .hero-section {{
            text-align: center;
            padding: {theme.SPACING_XL} 0;
            margin-bottom: {theme.SPACING_LG};
            background: linear-gradient(135deg, {theme.SURFACE} 0%, {theme.SURFACE_LIGHT} 100%);
            border-radius: {theme.CARD_BORDER_RADIUS};
            border: {theme.CARD_BORDER};
        }}
        
        .hero-title {{
            font-size: {theme.FONT_SIZE_H1};
            font-weight: 900;
            background: linear-gradient(135deg, {theme.PRIMARY} 0%, {theme.ACCENT} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: {theme.SPACING_SM};
        }}
        
        .hero-subtitle {{
            font-size: {theme.FONT_SIZE_H4};
            color: {theme.TEXT_MUTED};
            max-width: 800px;
            margin: 0 auto {theme.SPACING_MD};
        }}
        
        /* Pipeline stage cards */
        .pipeline-stage {{
            background: {theme.SURFACE};
            border-radius: {theme.CARD_BORDER_RADIUS};
            padding: {theme.SPACING_MD};
            border: {theme.CARD_BORDER};
            margin-bottom: {theme.SPACING_SM};
            transition: all 0.3s ease;
        }}
        
        .pipeline-stage:hover {{
            border-color: {theme.PRIMARY};
            box-shadow: 0 4px 20px rgba(59, 130, 246, 0.2);
        }}
        
        .pipeline-stage-title {{
            font-size: {theme.FONT_SIZE_H4};
            font-weight: 700;
            color: {theme.PRIMARY};
            margin-bottom: 8px;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            [data-testid="column"] {{
                width: 100% !important;
            }}
            
            .hero-title {{
                font-size: {theme.FONT_SIZE_H2};
            }}
        }}
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: {theme.SURFACE};
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: {theme.SURFACE_LIGHT};
            border-radius: 5px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: {theme.PRIMARY};
        }}
    </style>
    """

def inject_global_css():
    """Injects the global CSS into the Streamlit app."""
    st.markdown(get_global_css(), unsafe_allow_html=True)
