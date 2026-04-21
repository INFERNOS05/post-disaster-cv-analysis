#!/bin/bash

# CV Disaster Dashboard - Startup Script

echo "🛰️ CV Disaster Assessment Dashboard"
echo "===================================="
echo ""

# Check if Streamlit is installed
if ! command -v streamlit &> /dev/null
then
    echo "❌ Streamlit is not installed."
    echo "📦 Installing Streamlit and dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Start the application
echo "🚀 Starting the dashboard..."
echo "📍 The app will open at: http://localhost:8502"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py --server.port 8502
