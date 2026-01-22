#!/bin/bash
# ignite_bare_metal.sh
# PHASE 303: MANUAL OVERRIDE (Bypass Docker)

echo "=================================================="
echo "🏰 TENT CITADEL v5.1: BARE METAL IGNITION SEQUENCE"
echo "=================================================="
echo "   ⚠️  WARNING: DOCKER FAILURE DETECTED."
echo "   🔄  SWITCHING TO LOCAL EXECUTION PROTOCOL."
echo "=================================================="

# 1. CHECK PYTHON
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: python3 not found. Please install Python 3.10+"
    exit 1
fi

# 2. CREATE VIRTUAL ENVIRONMENT (The Suit)
if [ ! -d "venv" ]; then
    echo "   🧥  Tailoring the Suit (Creating Virtual Environment)..."
    python3 -m venv venv
else
    echo "   🧥  Suit detected (venv exists)."
fi

# 3. ACTIVATE
source venv/bin/activate

# 4. INSTALL DEPENDENCIES (The Mass)
echo "   📦  Loading Mass (Installing Requirements)..."
pip install --upgrade pip
pip install -r requirements.txt

# 5. INSTALL PLAYWRIGHT BROWSERS (The Eyes)
echo "   👀  Opening Eyes (Installing Playwright Browsers)..."
playwright install chromium

# 6. LAUNCH
echo "=================================================="
echo "   🚀  ALL SYSTEMS GREEN."
echo "   🔑  TURNING THE KEY..."
echo "=================================================="

# Determine mode
if [ "$1" == "--ui" ]; then
    echo "   🖥️  LAUNCHING EXECUTIVE DASHBOARD (UI)..."
    streamlit run tent_app.py
else
    echo "   🔮  ENTERING THE MATRIX (CLI)..."
    python citadel_core.py
fi
