#!/usr/bin/env python3
"""
Test script to validate all imports and basic functionality
"""

import sys

def test_imports():
    """Test all module imports"""
    print("Testing imports...")
    try:
        from config import theme
        from data import dummy_data
        from utils import session_utils
        from components import css_injector, footer, kpi_card
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_theme():
    """Test theme configuration"""
    print("\nTesting theme configuration...")
    try:
        from config import theme
        assert hasattr(theme, 'PRIMARY')
        assert hasattr(theme, 'SECONDARY')
        assert hasattr(theme, 'FONT_FAMILY')
        print(f"✅ Theme configured: PRIMARY={theme.PRIMARY}")
        return True
    except Exception as e:
        print(f"❌ Theme error: {e}")
        return False

def test_dummy_data():
    """Test dummy data structure"""
    print("\nTesting dummy data...")
    try:
        from data import dummy_data
        assert len(dummy_data.KPI_CARDS) == 4
        assert 'damage_class' in dummy_data.DAMAGE_RESULT
        assert 'dominant_class' in dummy_data.DENSITY_RESULT
        print(f"✅ Dummy data valid: {len(dummy_data.KPI_CARDS)} KPI cards")
        return True
    except Exception as e:
        print(f"❌ Dummy data error: {e}")
        return False

def test_components():
    """Test component functions"""
    print("\nTesting components...")
    try:
        from components import css_injector, footer
        css = css_injector.get_global_css()
        footer_html = footer.get_footer_html()
        assert len(css) > 0
        assert 'OST Project 2026' in footer_html
        print("✅ Components functional")
        return True
    except Exception as e:
        print(f"❌ Component error: {e}")
        return False

def test_file_structure():
    """Test file structure"""
    print("\nTesting file structure...")
    import os
    required_files = [
        'app.py',
        'requirements.txt',
        'config/theme.py',
        'data/dummy_data.py',
        'utils/session_utils.py',
        'components/css_injector.py',
        'components/footer.py',
        'components/kpi_card.py',
        'pages/1_upload.py',
        'pages/2_damage.py',
        'pages/3_density.py',
        'pages/4_analytics.py',
        'pages/5_settings.py',
        'pages/6_about.py',
        'assets/logo.png'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    else:
        print(f"✅ All {len(required_files)} required files present")
        return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("CV Disaster Dashboard - Validation Tests")
    print("=" * 60)
    
    tests = [
        test_file_structure,
        test_imports,
        test_theme,
        test_dummy_data,
        test_components
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ ALL TESTS PASSED - App is ready to run!")
        print("\nTo start the app, run:")
        print("  streamlit run app.py")
        print("\nOr use the quick start script:")
        print("  ./run.sh")
        return 0
    else:
        print("❌ SOME TESTS FAILED - Please fix errors above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
