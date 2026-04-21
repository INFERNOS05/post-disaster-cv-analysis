# Upload Satellite Image Page
import streamlit as st
from PIL import Image
import time
from components.css_injector import inject_global_css
from components.footer import render_footer
from utils.session_utils import init_session_state
from data.dummy_data import DAMAGE_RESULT, DENSITY_RESULT

# Page configuration
st.set_page_config(
    page_title="Upload Image - CV Disaster Dashboard",
    page_icon="📤",
    layout="wide"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Page header
st.title("📤 Upload Satellite Image")
st.markdown("Upload a satellite image to begin AI-powered damage assessment and urban density analysis.")
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a satellite image",
    type=["jpg", "jpeg", "png", "tiff"],
    help="Supported formats: JPG, PNG, TIFF"
)

if uploaded_file is not None:
    try:
        # Load and display image
        image = Image.open(uploaded_file)
        
        # Display image preview
        st.markdown("### 🖼️ Image Preview")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.image(image, caption="Uploaded Satellite Image", use_container_width=True)
        
        with col2:
            st.markdown("### 📋 Image Metadata")
            
            # Extract metadata
            file_size_kb = uploaded_file.size / 1024
            width, height = image.size
            format_name = image.format if image.format else "Unknown"
            
            metadata = {
                "Filename": uploaded_file.name,
                "File Size": f"{file_size_kb:.2f} KB",
                "Dimensions": f"{width} × {height} pixels",
                "Format": format_name
            }
            
            for key, value in metadata.items():
                st.metric(label=key, value=value)
            
            # Store metadata in session state
            st.session_state.image_metadata = {
                "filename": uploaded_file.name,
                "size_kb": file_size_kb,
                "dimensions": (width, height),
                "format": format_name
            }
        
        st.markdown("---")
        
        # Analyze button
        if st.button("🤖 Analyze Image", type="primary", use_container_width=True):
            with st.spinner("Running AI Analysis... This may take a moment."):
                # Simulate analysis
                time.sleep(2)
                
                # Store results in session state
                st.session_state.uploaded_image = image
                st.session_state.damage_result = DAMAGE_RESULT
                st.session_state.density_result = DENSITY_RESULT
                st.session_state.analysis_complete = True
                
                st.success("✅ Analysis complete! Navigate to Damage Assessment or Urban Density Mapping to view results.")
                
                # Show quick navigation buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⚠️ View Damage Assessment", use_container_width=True):
                        st.switch_page("pages/2_damage.py")
                with col2:
                    if st.button("🏙️ View Urban Density", use_container_width=True):
                        st.switch_page("pages/3_density.py")
    
    except Exception as e:
        st.error(f"❌ Error processing image: {str(e)}")
        st.error("Please ensure the file is a valid image in JPG, PNG, or TIFF format.")

else:
    # Show instructions when no file is uploaded
    st.info("👆 Please upload a satellite image to begin analysis.")
    
    st.markdown("### 📝 Instructions")
    st.markdown("""
    1. Click the **Browse files** button above
    2. Select a satellite image (JPG, PNG, or TIFF format)
    3. Review the image preview and metadata
    4. Click **Analyze Image** to run AI analysis
    5. View results in the Damage Assessment or Urban Density pages
    """)

# Footer
render_footer()
