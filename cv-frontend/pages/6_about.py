# About Project Page
import streamlit as st
from components.css_injector import inject_global_css
from components.footer import render_footer
from utils.session_utils import init_session_state

# Page configuration
st.set_page_config(
    page_title="About - CV Disaster Dashboard",
    page_icon="ℹ️",
    layout="wide"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Page header
st.title("ℹ️ About Project")
st.markdown("---")

# Project Overview
st.markdown("## CV-Based Post-Disaster Damage Assessment & Urban Density Mapping using Satellite Imagery")

st.markdown("""
### 🎯 Project Objectives

This project leverages cutting-edge computer vision and deep learning techniques to analyze satellite imagery 
for two critical applications:

1. **Post-Disaster Damage Assessment**: Automatically identify and classify damage severity in disaster-affected 
   areas to support rapid response and recovery efforts.

2. **Urban Density Mapping**: Analyze urban development patterns and population density proxies to aid in 
   urban planning and resource allocation.

### 🔬 Methodology

Our approach combines state-of-the-art deep learning models with traditional computer vision techniques:

- **Image Preprocessing**: Satellite images are normalized and preprocessed to enhance feature extraction
- **Semantic Segmentation**: Deep neural networks segment images into meaningful regions
- **Classification**: Multi-class classifiers determine damage severity and density levels
- **Heatmap Generation**: Spatial analysis produces intuitive visualizations of results

### 🎓 Use Cases

- **Disaster Response**: Rapid assessment of damage extent for emergency response coordination
- **Urban Planning**: Data-driven insights for sustainable city development
- **Resource Allocation**: Optimize distribution of aid and infrastructure investments
- **Research**: Academic studies on urbanization patterns and disaster impact
""")

st.markdown("---")

# Technology Stack
st.markdown("### 🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Frontend**
    - Streamlit
    - Plotly
    - Python
    """)

with col2:
    st.markdown("""
    **Computer Vision**
    - OpenCV
    - PIL/Pillow
    - NumPy
    """)

with col3:
    st.markdown("""
    **Deep Learning**
    - PyTorch / TensorFlow
    - Pre-trained Models
    - Custom Architectures
    """)

st.markdown("---")

# Project Team
st.markdown("### 👥 Project Team")

st.markdown("""
This project was developed as part of the **OST Project 2026** initiative.

**Team Members:**
- Project Lead & ML Engineer
- Computer Vision Specialist
- Full-Stack Developer
- UI/UX Designer
- Data Scientist

**Acknowledgments:**
We thank our advisors, mentors, and the open-source community for their invaluable support.
""")

st.markdown("---")

# OST Project Badge
st.markdown("""
<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; color: white;">
    <h2 style="margin: 0; color: white;">🎓 OST Project 2026</h2>
    <p style="margin-top: 10px; color: white;">Building the Future with AI and Computer Vision</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Contact & Links
st.markdown("### 📬 Contact & Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📧 Email**")
    st.markdown("project@cvdisaster.ai")

with col2:
    st.markdown("**🔗 GitHub**")
    st.markdown("github.com/cv-disaster")

with col3:
    st.markdown("**📄 Documentation**")
    st.markdown("docs.cvdisaster.ai")

# Footer
render_footer()
