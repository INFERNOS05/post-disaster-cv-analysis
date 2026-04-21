#!/bin/bash

# CV Disaster Dashboard - Quick Start Script

echo "🚀 Starting CV Disaster Dashboard..."
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null && ! python3 -m streamlit version &> /dev/null
then
    echo "❌ Streamlit is not installed. Installing dependencies..."
    pip3 install -r requirements.txt
fi

echo "✅ Dependencies verified"
echo ""
echo "📊 Launching dashboard at http://localhost:8501"
echo "   Press Ctrl+C to stop the server"
echo ""

# Run streamlit
python3 -m streamlit run app.py
