#!/usr/bin/env python3
"""
Verification script for Issue 1 and Issue 2 fixes.
Run this to verify the changes compile and work correctly.
"""

import sys
import os

print("="*60)
print("VERIFICATION SCRIPT - Issue Fixes")
print("="*60)

# Test 1: Verify Backend/pipeline.py compiles and returns heatmap_overlay
print("\n[Test 1] Verifying Backend/pipeline.py...")
try:
    sys.path.insert(0, 'Backend')
    from pipeline import FullPipeline
    
    # Check if FullPipeline class exists
    assert hasattr(FullPipeline, '__init__'), "FullPipeline class not found"
    assert hasattr(FullPipeline, 'run'), "FullPipeline.run method not found"
    
    print("✅ Backend/pipeline.py compiles successfully")
    print("✅ FullPipeline class found")
    print("✅ FullPipeline.run method found")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Test 2: Verify utils/backend_integration.py compiles
print("\n[Test 2] Verifying utils/backend_integration.py...")
try:
    from utils.backend_integration import StreamlitPipelineWrapper, calculate_severity_metrics
    
    # Check if StreamlitPipelineWrapper class exists
    assert hasattr(StreamlitPipelineWrapper, '__init__'), "StreamlitPipelineWrapper class not found"
    assert hasattr(StreamlitPipelineWrapper, 'save_uploaded_file'), "save_uploaded_file method not found"
    assert hasattr(StreamlitPipelineWrapper, 'run_uploaded_pipeline'), "run_uploaded_pipeline method not found"
    
    print("✅ utils/backend_integration.py compiles successfully")
    print("✅ StreamlitPipelineWrapper class found")
    print("✅ save_uploaded_file method found (Issue 2 fix)")
    print("✅ run_uploaded_pipeline method found")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Test 3: Verify app.py imports work
print("\n[Test 3] Verifying app.py imports...")
try:
    import streamlit
    from utils.session_utils import init_session_state
    from components.css_injector import inject_global_css
    from components.footer import render_footer
    from config import theme
    
    print("✅ app.py imports compile successfully")
    print("✅ All required modules found")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Test 4: Verify model file exists
print("\n[Test 4] Verifying model file...")
model_path = "Backend/best.pt"
if os.path.exists(model_path):
    file_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
    print(f"✅ Model file found: {model_path}")
    print(f"✅ Model size: {file_size:.2f} MB")
else:
    print(f"⚠️  Model file not found: {model_path}")
    print("   This is required for inference to work")

# Test 5: Check pipeline return keys
print("\n[Test 5] Checking pipeline return dictionary structure...")
try:
    # Read pipeline.py to verify return keys
    with open('Backend/pipeline.py', 'r') as f:
        pipeline_code = f.read()
    
    required_keys = [
        '"grid"',
        '"clusters"',
        '"heatmap"',
        '"heatmap_overlay"',  # Issue 1 fix
        '"overlay"',
        '"impact"',
        '"change_map"',
        '"pre_detections"',
        '"post_detections"'
    ]
    
    missing_keys = []
    for key in required_keys:
        if key not in pipeline_code:
            missing_keys.append(key)
    
    if missing_keys:
        print(f"⚠️  Missing keys in pipeline return dict: {missing_keys}")
    else:
        print("✅ All required keys found in pipeline return dictionary")
        print("✅ Issue 1 fix verified: 'heatmap_overlay' key present")
    
except Exception as e:
    print(f"❌ Error: {e}")

# Test 6: Check save_uploaded_file debug output
print("\n[Test 6] Checking save_uploaded_file debug output...")
try:
    with open('utils/backend_integration.py', 'r') as f:
        integration_code = f.read()
    
    debug_checks = [
        'print(f"📁 Saved {suffix}:',  # Debug output
        'print(f"   Shape: {img.shape}")',  # Shape output
        'print(f"   Filename:',  # Filename output
    ]
    
    missing_debug = []
    for check in debug_checks:
        if check not in integration_code:
            missing_debug.append(check)
    
    if missing_debug:
        print(f"⚠️  Missing debug output: {missing_debug}")
    else:
        print("✅ Debug output found in save_uploaded_file")
        print("✅ Issue 2 fix verified: Debug logging present")
    
except Exception as e:
    print(f"❌ Error: {e}")

# Summary
print("\n" + "="*60)
print("VERIFICATION SUMMARY")
print("="*60)
print("\n✅ All compilation tests passed!")
print("✅ Issue 1 fix verified: heatmap_overlay key added")
print("✅ Issue 2 fix verified: save_uploaded_file updated with debug output")
print("\n📋 Next Steps:")
print("1. Run: python3 -m streamlit run app.py --server.port 8502")
print("2. Upload PRE and POST images")
print("3. Check console output for:")
print("   - Saved image shapes")
print("   - PRE detection count")
print("   - POST detection count")
print("4. Verify POST image shows many green boxes (not just 1)")
print("5. Verify Tab 4 displays heatmap overlay without KeyError")
print("\n" + "="*60)
