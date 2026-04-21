#!/usr/bin/env python3
"""
Test script to verify backend integration works correctly
"""

import sys
import os

print("=" * 60)
print("CV Disaster Dashboard - Integration Test")
print("=" * 60)
print()

# Test 1: Check Python version
print("1. Checking Python version...")
python_version = sys.version_info
if python_version.major >= 3 and python_version.minor >= 9:
    print(f"   ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
else:
    print(f"   ⚠️  Python {python_version.major}.{python_version.minor}.{python_version.micro} (3.9+ recommended)")
print()

# Test 2: Check required packages
print("2. Checking required packages...")
required_packages = [
    'streamlit',
    'cv2',
    'PIL',
    'pandas',
    'numpy',
    'plotly',
    'ultralytics',
    'sklearn'
]

missing_packages = []
for package in required_packages:
    try:
        if package == 'cv2':
            import cv2
        elif package == 'PIL':
            from PIL import Image
        elif package == 'sklearn':
            import sklearn
        else:
            __import__(package)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - NOT INSTALLED")
        missing_packages.append(package)

if missing_packages:
    print()
    print(f"   ⚠️  Missing packages: {', '.join(missing_packages)}")
    print(f"   Run: pip3 install -r requirements.txt")
else:
    print()
    print("   ✅ All required packages installed")
print()

# Test 3: Check model file
print("3. Checking YOLO model file...")
model_path = "Backend/best.pt"
if os.path.exists(model_path):
    size_mb = os.path.getsize(model_path) / (1024 * 1024)
    print(f"   ✅ Model found: {model_path} ({size_mb:.1f} MB)")
else:
    print(f"   ❌ Model NOT found: {model_path}")
    print(f"   Please ensure the model file is in the correct location")
print()

# Test 4: Check backend files
print("4. Checking backend files...")
backend_files = [
    'Backend/pipeline.py',
    'Backend/inference.py',
    'Backend/change_map.py',
    'Backend/compute_impact.py',
    'Backend/heatmap.py',
    'Backend/visualise.py',
    'Backend/clustering.py',
    'Backend/grid.py',
    'Backend/filter.py',
    'Backend/draw_boxes.py',
    'Backend/overlay_change_map.py',
    'Backend/post_process.py'
]

all_backend_files_exist = True
for file in backend_files:
    if os.path.exists(file):
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} - MISSING")
        all_backend_files_exist = False

if all_backend_files_exist:
    print()
    print("   ✅ All backend files present")
print()

# Test 5: Check frontend files
print("5. Checking frontend files...")
frontend_files = [
    'app.py',
    'utils/backend_integration.py',
    'utils/session_utils.py',
    'components/css_injector.py',
    'components/footer.py',
    'config/theme.py'
]

all_frontend_files_exist = True
for file in frontend_files:
    if os.path.exists(file):
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} - MISSING")
        all_frontend_files_exist = False

if all_frontend_files_exist:
    print()
    print("   ✅ All frontend files present")
print()

# Test 6: Test backend imports
print("6. Testing backend imports...")
try:
    sys.path.insert(0, 'Backend')
    from pipeline import FullPipeline
    from inference import DamageInference
    from compute_impact import compute_impact
    print("   ✅ Backend imports successful")
except Exception as e:
    print(f"   ❌ Backend import error: {str(e)}")
print()

# Test 7: Test frontend imports
print("7. Testing frontend imports...")
try:
    from utils.backend_integration import StreamlitPipelineWrapper, calculate_severity_metrics
    print("   ✅ Frontend integration imports successful")
except Exception as e:
    print(f"   ❌ Frontend import error: {str(e)}")
print()

# Summary
print("=" * 60)
print("SUMMARY")
print("=" * 60)

if not missing_packages and os.path.exists(model_path) and all_backend_files_exist and all_frontend_files_exist:
    print("✅ All checks passed! Ready to run the application.")
    print()
    print("To start the app, run:")
    print("   streamlit run app.py --server.port 8502")
else:
    print("⚠️  Some checks failed. Please fix the issues above.")
    print()
    if missing_packages:
        print("Install missing packages:")
        print("   pip3 install -r requirements.txt")
    if not os.path.exists(model_path):
        print()
        print("Add YOLO model file:")
        print(f"   Place your model at: {model_path}")

print()
print("=" * 60)
