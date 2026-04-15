#!/bin/bash
# Universal install script for unifiedcli on Linux/Mac

set -e

echo "🚀 Installing Unified CLI..."

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="mac"
else
    echo "❌ Unsupported OS: $OSTYPE"
    exit 1
fi

echo "📍 Detected: $OS"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.10+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Python $PYTHON_VERSION found"

# Clone repo
if [ ! -d "unifiedcli" ]; then
    echo "📥 Cloning repository..."
    git clone https://github.com/Kelushael/unifiedcli.git
fi

cd unifiedcli

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Generate sovereign key
echo ""
echo "🔑 Generating sovereign key..."
echo "Run: unifiedcli keygen"
echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "  1. Run: unifiedcli keygen"
echo "  2. Set: export POOKIE_KEY=pk-..."
echo "  3. Run: unifiedcli shell"
echo ""
