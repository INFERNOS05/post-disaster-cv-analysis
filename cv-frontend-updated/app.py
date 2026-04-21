# CV-Based Post-Disaster Damage Assessment Dashboard - Premium Dark Theme
import streamlit as st
from utils.session_utils import init_session_state
from components.css_injector import inject_global_css
from components.footer import render_footer
from PIL import Image
import time
import pandas as pd
import plotly.graph_objects as go
from config import theme
import numpy as np
import io

# Import backend integration
from utils.backend_integration import StreamlitPipelineWrapper, calculate_severity_metrics

# Page configuration
st.set_page_config(
    page_title="CV Disaster Assessment Dashboard",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state and CSS
init_session_state()
inject_global_css()

# Initialize backend pipeline wrapper
@st.cache_resource
def get_pipeline():
    return StreamlitPipelineWrapper()

pipeline_wrapper = get_pipeline()

# Header
st.markdown(f"""
<div class="hero-section">
    <h1 class="hero-title">🛰️ CV-Based Post-Disaster Damage Assessment</h1>
    <p class="hero-subtitle">Advanced Computer Vision Pipeline for Satellite Imagery Analysis</p>
</div>
""", unsafe_allow_html=True)

# Create horizontal tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📤 Upload & Process",
    "🔬 CV Processing Pipeline", 
    "⚠️ Damage Assessment",
    "🗺️ Heatmap Analysis",
    "📊 Reports & Export"
])

# ==================== TAB 1: Upload & Process ====================
with tab1:
    st.markdown("### 📤 Upload Satellite Images")
    st.markdown("Upload **PRE-disaster** and **POST-disaster** satellite images for comprehensive damage assessment.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📸 PRE-Disaster Image")
        pre_file = st.file_uploader(
            "Upload PRE-disaster image",
            type=["jpg", "jpeg", "png", "tiff"],
            help="Upload the satellite image taken before the disaster",
            key="pre_upload"
        )
        
        if pre_file is not None:
            try:
                pre_file.seek(0)
                pre_image = Image.open(pre_file)
                st.image(pre_image, caption="PRE-Disaster Image", use_container_width=True)
                st.session_state.pre_uploaded = True
            except Exception as e:
                st.error(f"❌ Error loading PRE image: {str(e)}")
    
    with col2:
        st.markdown("#### 📸 POST-Disaster Image")
        post_file = st.file_uploader(
            "Upload POST-disaster image",
            type=["jpg", "jpeg", "png", "tiff"],
            help="Upload the satellite image taken after the disaster",
            key="post_upload"
        )
        
        if post_file is not None:
            try:
                post_file.seek(0)
                post_image = Image.open(post_file)
                st.image(post_image, caption="POST-Disaster Image", use_container_width=True)
                st.session_state.post_uploaded = True
            except Exception as e:
                st.error(f"❌ Error loading POST image: {str(e)}")
    
    st.markdown("---")
    
    # Metadata and Analysis Button
    if pre_file is not None and post_file is not None:
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.markdown("#### 📋 PRE Metadata")
            pre_size_kb = pre_file.size / 1024
            pre_file.seek(0)
            pre_image = Image.open(pre_file)
            pre_width, pre_height = pre_image.size
            st.metric("File Size", f"{pre_size_kb:.2f} KB")
            st.metric("Dimensions", f"{pre_width}×{pre_height}")
        
        with col2:
            st.markdown("#### 🚀 Run Analysis")
            st.markdown("")
            st.markdown("")
            
            if st.button("🔥 Run Full Damage Assessment Pipeline", type="primary", use_container_width=True):
                with st.spinner("🔄 Processing through backend CV pipeline..."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    stages = [
                        "Loading YOLO detection model...",
                        "Running inference on PRE image...",
                        "Running inference on POST image...",
                        "Filtering detections...",
                        "Computing change detection map...",
                        "Analyzing grid severity...",
                        "Clustering damage regions...",
                        "Generating heatmap...",
                        "Creating overlays...",
                        "Calculating impact metrics...",
                        "Finalizing results..."
                    ]
                    
                    for i, stage in enumerate(stages):
                        status_text.text(stage)
                        progress_bar.progress((i + 1) / len(stages))
                        time.sleep(0.3)
                    
                    try:
                        # KEY FIX: reset file pointers before passing to pipeline
                        pre_file.seek(0)
                        post_file.seek(0)

                        results = pipeline_wrapper.run_uploaded_pipeline(pre_file, post_file)
                        
                        if not results.get('has_detections', False):
                            st.warning("⚠️ No buildings detected in POST image. Try different images or lower confidence threshold.")
                        
                        enhanced_metrics = calculate_severity_metrics(
                            results['impact'],
                            results['heatmap'],
                            results['avg_confidence']
                        )
                        
                        results['metrics'] = enhanced_metrics
                        st.session_state.cv_results = results
                        st.session_state.analysis_complete = True
                        
                        status_text.empty()
                        progress_bar.empty()
                        
                        st.success("✅ Analysis complete! Navigate to other tabs to view results.")
                        
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.metric("PRE Buildings", enhanced_metrics['pre_buildings'])
                        with col_b:
                            st.metric("POST Buildings", enhanced_metrics['post_buildings'])
                        with col_c:
                            st.metric("Density Drop", enhanced_metrics['density_drop'])
                        
                    except Exception as e:
                        status_text.empty()
                        progress_bar.empty()
                        st.error(f"❌ Error during analysis: {str(e)}")
                        st.exception(e)
        
        with col3:
            st.markdown("#### 📋 POST Metadata")
            post_size_kb = post_file.size / 1024
            post_file.seek(0)
            post_image = Image.open(post_file)
            post_width, post_height = post_image.size
            st.metric("File Size", f"{post_size_kb:.2f} KB")
            st.metric("Dimensions", f"{post_width}×{post_height}")
    
    else:
        st.info("👆 Please upload both PRE and POST disaster images to begin analysis.")

# ==================== TAB 2: CV Processing Pipeline ====================
with tab2:
    st.markdown("### 🔬 Computer Vision Processing Pipeline")
    st.markdown("**Exact replication of run_pipeline.py outputs**")

    if st.session_state.get('analysis_complete', False):
        results = st.session_state.cv_results

        st.markdown("#### 📸 Original Input Images")
        st.markdown("*PRE-disaster vs POST-disaster comparison*")
        col1, col2 = st.columns(2)
        with col1:
            st.image(results['pre_image'], caption="PRE-Disaster", use_container_width=True)
        with col2:
            st.image(results['post_image'], caption="POST-Disaster", use_container_width=True)

        st.markdown("---")

        st.markdown("#### 🎯 Final Damage Assessment")
        st.markdown("*Output: `result['overlay']` - Combined detection boxes + heatmap + clusters*")
        st.image(results['damage_overlay'], caption="Final Damage Assessment Overlay", use_container_width=True)
        st.caption("🟩 Green=intact  🟡 Yellow=minor  🟠 Orange=major  🔴 Red=destroyed")

        st.markdown("---")

        st.markdown("#### 🔄 Change Detection Overlay")
        st.markdown("*Output: `overlay_change_map(post_path, result['change_map'])`*")
        col1, col2 = st.columns(2)
        with col1:
            st.image(results['post_image'], caption="POST — original", use_container_width=True)
        with col2:
            st.image(results['change_overlay'], caption="Change detection overlay", use_container_width=True)
            st.caption("🔥 Hot colormap shows pixel-level changes")

        st.markdown("---")

        st.markdown("#### 📊 Impact Metrics")
        st.markdown("*Output: `result['impact']` from compute_impact.py*")
        
        metrics = results['metrics']
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("PRE Buildings",  metrics['pre_buildings'])
        c2.metric("POST Buildings", metrics['post_buildings'])
        c3.metric("Density Drop",   metrics['density_drop'])
        c4.metric("Damage Score",   f"{metrics['damage_score']:.1f}")
        c5.metric("Damage %",       f"{metrics['damage_percent']:.1f}%")

        st.markdown("---")

        st.markdown("#### 🎯 Cluster Analysis")
        st.markdown(f"*Output: `result['clusters']` - {len(results['clusters'])} cluster points detected*")
        
        if results['clusters']:
            cluster_groups = {}
            for c in results['clusters']:
                cid = c['cluster_id']
                if cid not in cluster_groups:
                    cluster_groups[cid] = []
                cluster_groups[cid].append(c)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Clusters", len(cluster_groups))
            with col2:
                total_cells = sum(len(cells) for cells in cluster_groups.values())
                st.metric("Total Grid Cells", total_cells)
            with col3:
                avg_priority = np.mean([c['priority'] for c in results['clusters']])
                st.metric("Avg Priority", f"{avg_priority:.2f}")
        else:
            st.info("No clusters detected in this analysis.")

    else:
        st.info("📤 Please upload and process images in the 'Upload & Process' tab first.")

# ==================== TAB 3: Damage Assessment ====================
with tab3:
    st.markdown("### ⚠️ Damage Assessment Results")
    
    if st.session_state.get('analysis_complete', False):
        results = st.session_state.cv_results
        metrics = results['metrics']
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Overall Classification</p>
                <p class="metric-value">{metrics['classification']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Severity Score</p>
                <p class="metric-value">{metrics['severity_score']}/10</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Total Affected</p>
                <p class="metric-value">{metrics['total_affected_pct']}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Confidence</p>
                <p class="metric-value">{metrics['confidence']*100:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("#### 🏢 Building Detection Analysis")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("PRE Buildings Detected", metrics['pre_buildings'])
        with col2:
            st.metric("POST Buildings Detected", metrics['post_buildings'])
        with col3:
            st.metric("Building Density Drop", metrics['density_drop'], 
                     delta=f"-{metrics['density_drop']}" if metrics['density_drop'] > 0 else "0",
                     delta_color="inverse")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📸 POST-Disaster Input")
            st.image(results['post_image'], use_container_width=True)
        with col2:
            st.markdown("#### 🎯 Damage Assessment Overlay")
            st.markdown("*Bounding boxes show detected buildings with damage classification*")
            st.image(results['damage_overlay'], use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("#### 📊 Damage Severity Distribution")
        
        fig = go.Figure(data=[
            go.Bar(
                x=['Low Damage', 'Medium Damage', 'Severe Damage'],
                y=[metrics['low_damage_pct'], metrics['medium_damage_pct'], metrics['severe_damage_pct']],
                marker_color=[theme.SUCCESS, theme.WARNING, theme.DANGER],
                text=[f"{metrics['low_damage_pct']:.1f}%", 
                      f"{metrics['medium_damage_pct']:.1f}%", 
                      f"{metrics['severe_damage_pct']:.1f}%"],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title="Damage Severity Distribution by Area",
            xaxis_title="Severity Level",
            yaxis_title="Percentage of Area",
            plot_bgcolor=theme.SURFACE,
            paper_bgcolor=theme.SURFACE,
            font=dict(color=theme.TEXT),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📈 Damage Statistics")
            damage_stats = pd.DataFrame({
                'Metric': ['Damage Score', 'Damage Percentage', 'Affected Buildings'],
                'Value': [
                    f"{metrics['damage_score']:.2f}",
                    f"{metrics['damage_percent']:.1f}%",
                    f"{metrics['post_buildings']}"
                ]
            })
            st.dataframe(damage_stats, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("#### 🎯 Detection Summary")
            detection_summary = pd.DataFrame({
                'Category': ['Total Clusters', 'High Priority Zones', 'Grid Cells Analyzed'],
                'Count': [
                    len(set([c['cluster_id'] for c in results['clusters']])) if results['clusters'] else 0,
                    len([g for g in results['grid'] if g['priority_score'] > 0]),
                    len(results['grid'])
                ]
            })
            st.dataframe(detection_summary, use_container_width=True, hide_index=True)
        
    else:
        st.info("📤 Please upload and process images in the 'Upload & Process' tab first.")

# ==================== TAB 4: Heatmap Analysis ====================
with tab4:
    st.markdown("### 🗺️ Heatmap Analysis")
    st.markdown("*Output: `result['heatmap']` from heatmap.py*")
    
    if st.session_state.get('analysis_complete', False):
        results = st.session_state.cv_results
        
        st.markdown("#### 🔥 Heatmap Overlay")
        st.markdown("*Output: `result['heatmap_overlay']` - Heatmap overlaid on POST image*")
        st.image(results['heatmap_overlay'], use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        
        with col2:
            st.markdown("#### 🎨 Severity Legend")
            st.markdown(f"""
            <div style="background: {theme.SURFACE}; padding: 20px; border-radius: 12px; border: {theme.CARD_BORDER};">
                <div style="margin-bottom: 16px;">
                    <div style="background: {theme.SUCCESS}; height: 30px; border-radius: 6px; margin-bottom: 8px;"></div>
                    <p style="color: {theme.TEXT}; margin: 0;">🟢 Low Risk (0-30%)</p>
                </div>
                <div style="margin-bottom: 16px;">
                    <div style="background: {theme.WARNING}; height: 30px; border-radius: 6px; margin-bottom: 8px;"></div>
                    <p style="color: {theme.TEXT}; margin: 0;">🟡 Medium Risk (30-60%)</p>
                </div>
                <div style="margin-bottom: 16px;">
                    <div style="background: {theme.DANGER}; height: 30px; border-radius: 6px; margin-bottom: 8px;"></div>
                    <p style="color: {theme.TEXT}; margin: 0;">🔴 High Risk (60-100%)</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            metrics = results['metrics']
            st.markdown("#### 📈 Risk Zone Statistics")
            risk_data = pd.DataFrame({
                'Zone': ['Low Risk', 'Medium Risk', 'High Risk'],
                'Coverage (%)': [
                    metrics['low_damage_pct'],
                    metrics['medium_damage_pct'],
                    metrics['severe_damage_pct']
                ]
            })
            st.dataframe(risk_data, use_container_width=True, hide_index=True)
        
        with col1:
            st.markdown("#### 📊 Grid-Based Damage Distribution")
            st.markdown(f"*16×16 grid analysis from grid.py*")
            
            heatmap_data = results['heatmap']
            
            fig = go.Figure(data=go.Heatmap(
                z=heatmap_data,
                colorscale='Hot',
                showscale=True,
                colorbar=dict(title="Priority Score")
            ))
            
            fig.update_layout(
                title="Grid Priority Heatmap",
                xaxis_title="Grid Column",
                yaxis_title="Grid Row",
                plot_bgcolor=theme.SURFACE,
                paper_bgcolor=theme.SURFACE,
                font=dict(color=theme.TEXT),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("#### 🎯 Damage Cluster Analysis")
        st.markdown(f"*Output: `result['clusters']` - Clustered high-priority zones*")
        
        if results['clusters']:
            cluster_groups = {}
            for c in results['clusters']:
                cid = c['cluster_id']
                if cid not in cluster_groups:
                    cluster_groups[cid] = []
                cluster_groups[cid].append(c)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Clusters Detected", len(cluster_groups))
            with col2:
                total_cells = sum(len(cells) for cells in cluster_groups.values())
                st.metric("Total Affected Grid Cells", total_cells)
            with col3:
                avg_priority = np.mean([c['priority'] for c in results['clusters']])
                st.metric("Average Priority Score", f"{avg_priority:.2f}")
            
            st.markdown("##### 📋 Cluster Details")
            cluster_data = []
            for cid, cells in cluster_groups.items():
                avg_priority = np.mean([c['priority'] for c in cells])
                cluster_data.append({
                    'Cluster ID': cid,
                    'Grid Cells': len(cells),
                    'Avg Priority': f"{avg_priority:.2f}",
                    'Status': '🔴 High' if avg_priority > 5 else '🟡 Medium' if avg_priority > 2 else '🟢 Low'
                })
            
            cluster_df = pd.DataFrame(cluster_data)
            st.dataframe(cluster_df, use_container_width=True, hide_index=True)
        else:
            st.info("No significant damage clusters detected in this analysis.")
    
    else:
        st.info("📤 Please upload and process images in the 'Upload & Process' tab first.")

# ==================== TAB 5: Reports & Export ====================
with tab5:
    st.markdown("### 📊 Reports & Export")

    if st.session_state.get('analysis_complete', False):
        results = st.session_state.cv_results
        metrics = results['metrics']

        num_clusters   = len(set([c['cluster_id'] for c in results['clusters']])) if results['clusters'] else 0
        priority_zones = len([g for g in results['grid'] if g['priority_score'] > 0])
        affected_buildings = round(metrics['post_buildings'] * metrics['damage_percent'] / 100)

        st.markdown("#### 📥 Download Analysis Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("##### 🖼️ PNG Images")

            heatmap_bytes = io.BytesIO()
            results['heatmap_overlay'].save(heatmap_bytes, format='PNG')
            heatmap_bytes.seek(0)
            st.download_button(
                label="📥 Download Heatmap Overlay",
                data=heatmap_bytes,
                file_name="damage_heatmap_overlay.png",
                mime="image/png",
                use_container_width=True
            )

            damage_bytes = io.BytesIO()
            results['damage_overlay'].save(damage_bytes, format='PNG')
            damage_bytes.seek(0)
            st.download_button(
                label="📥 Download Damage Overlay",
                data=damage_bytes,
                file_name="damage_assessment_overlay.png",
                mime="image/png",
                use_container_width=True
            )

            change_bytes = io.BytesIO()
            results['change_overlay'].save(change_bytes, format='PNG')
            change_bytes.seek(0)
            st.download_button(
                label="📥 Download Change Detection",
                data=change_bytes,
                file_name="change_detection_overlay.png",
                mime="image/png",
                use_container_width=True
            )

        with col2:
            st.markdown("##### 📊 CSV Export")

            primary_csv = pd.DataFrame([{
                'image_name':         'analysis',
                'pre_buildings':      metrics['pre_buildings'],
                'post_buildings':     metrics['post_buildings'],
                'affected_buildings': affected_buildings,
                'damage_percentage':  round(metrics['damage_percent'], 2),
                'severity_score':     metrics['severity_score'],
                'confidence':         round(metrics['confidence'], 4),
                'clusters':           num_clusters,
                'priority_zones':     priority_zones,
            }]).to_csv(index=False)

            st.download_button(
                label="📥 Download Results CSV",
                data=primary_csv,
                file_name="damage_assessment_results.csv",
                mime="text/csv",
                use_container_width=True
            )

            full_csv = pd.DataFrame({
                'Metric': [
                    'Overall Classification', 'Severity Score',
                    'Total Affected Area (%)', 'Low Damage (%)',
                    'Medium Damage (%)', 'Severe Damage (%)',
                    'Confidence', 'PRE Buildings', 'POST Buildings',
                    'Density Drop', 'Damage Score', 'Damage %',
                    'Clusters', 'Priority Zones'
                ],
                'Value': [
                    metrics['classification'], metrics['severity_score'],
                    metrics['total_affected_pct'], metrics['low_damage_pct'],
                    metrics['medium_damage_pct'], metrics['severe_damage_pct'],
                    f"{metrics['confidence']*100:.1f}%",
                    metrics['pre_buildings'], metrics['post_buildings'],
                    metrics['density_drop'], metrics['damage_score'],
                    f"{metrics['damage_percent']:.1f}%",
                    num_clusters, priority_zones
                ]
            }).to_csv(index=False)

            st.download_button(
                label="📥 Download Full Metrics CSV",
                data=full_csv,
                file_name="damage_full_metrics.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col3:
            st.markdown("##### 📄 Text Summary")

            summary_text = f"""CV-BASED POST-DISASTER DAMAGE ASSESSMENT REPORT
================================================
Overall Classification : {metrics['classification']}
Severity Score         : {metrics['severity_score']}/10
Confidence             : {metrics['confidence']*100:.1f}%

BUILDING DETECTION
PRE Buildings          : {metrics['pre_buildings']}
POST Buildings         : {metrics['post_buildings']}
Affected Buildings     : {affected_buildings}
Density Drop           : {metrics['density_drop']}

DAMAGE DISTRIBUTION
Low Damage             : {metrics['low_damage_pct']:.2f}%
Medium Damage          : {metrics['medium_damage_pct']:.2f}%
Severe Damage          : {metrics['severe_damage_pct']:.2f}%
Total Affected         : {metrics['total_affected_pct']:.2f}%

SPATIAL ANALYSIS
Damage Score           : {metrics['damage_score']:.2f}
Damage Percentage      : {metrics['damage_percent']:.1f}%
Clusters Detected      : {num_clusters}
Priority Zones         : {priority_zones}
Grid Cells Analyzed    : {len(results['grid'])}
================================================
Generated by CV Disaster Assessment Dashboard
"""
            st.download_button(
                label="📥 Download Text Summary",
                data=summary_text,
                file_name="damage_assessment_summary.txt",
                mime="text/plain",
                use_container_width=True
            )
            st.info("📄 PDF generation coming soon!")

        st.markdown("---")
        st.markdown("#### 📋 Analysis Summary")

        summary_df = pd.DataFrame({
            'Category': [
                'Overall Classification', 'Severity Score',
                'Total Affected Area', 'Building Density Drop', 'Confidence Level'
            ],
            'Result': [
                metrics['classification'],
                f"{metrics['severity_score']}/10",
                f"{metrics['total_affected_pct']:.2f}%",
                f"{metrics['density_drop']} buildings",
                f"{metrics['confidence']*100:.1f}%"
            ],
            'Status': ['⚠️', '📊', '🗺️', '🏢', '✅']
        })
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Building Detection")
            st.dataframe(pd.DataFrame({
                'Metric': ['PRE Buildings', 'POST Buildings', 'Affected', 'Density Drop'],
                'Value':  [metrics['pre_buildings'], metrics['post_buildings'],
                           affected_buildings, metrics['density_drop']]
            }), use_container_width=True, hide_index=True)
        with col2:
            st.markdown("##### Damage Analysis")
            st.dataframe(pd.DataFrame({
                'Metric': ['Damage Score', 'Damage %', 'Clusters', 'Priority Zones'],
                'Value':  [f"{metrics['damage_score']:.2f}",
                           f"{metrics['damage_percent']:.1f}%",
                           num_clusters, priority_zones]
            }), use_container_width=True, hide_index=True)

    else:
        st.info("📤 Please upload and process images in the 'Upload & Process' tab first.")

# Footer
render_footer()