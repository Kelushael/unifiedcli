#!/bin/bash
# Termux installation script for unifiedcli
# Run in Termux on Android

set -e

echo "🚀 Installing Unified CLI on Termux..."

# Check if running in Termux
if [ ! -d "$HOME/.termux" ]; then
    echo "⚠️  This script is designed for Termux"
    echo "ℹ️  Get Termux from F-Droid or GitHub Releases"
fi

# Update packages
echo "📦 Updating Termux packages..."
apt update && apt upgrade -y

# Install Python
echo "🐍 Installing Python..."
apt install -y python3 python3-pip

# Install Git
echo "📚 Installing Git..."
apt install -y git

# Check versions
PYTHON_VERSION=$(python3 --version)
echo "✓ $PYTHON_VERSION found"

GIT_VERSION=$(git --version)
echo "✓ $GIT_VERSION found"

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

# Create alias
echo ""
echo "🔗 Creating Termux command alias..."
mkdir -p $HOME/.local/bin
cat > $HOME/.local/bin/unifiedcli << 'EOF'
#!/bin/bash
source ~/unifiedcli/venv/bin/activate
python -m unified.cli "$@"
EOF
chmod +x $HOME/.local/bin/unifiedcli

echo ""
echo "🔑 Sovereign key setup:"
echo "  1. Run: unifiedcli keygen"
echo "  2. Set: export POOKIE_KEY='pk-...'"
echo "  3. Run: unifiedcli shell"
echo ""
echo "✅ Installation complete!"
echo ""
echo "Next: Open a new Termux session and run: unifiedcli shell"
