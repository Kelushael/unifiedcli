#!/bin/bash
# Homebrew installation script for unifiedcli
# Run: brew install kelushael/taps/unifiedcli

set -e

echo "🚀 Installing Unified CLI via Homebrew..."

# Check macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Homebrew installation only works on macOS"
    echo "ℹ️  Use install.sh for Linux or install.ps1 for Windows"
    exit 1
fi

# Check Homebrew
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Install from https://brew.sh"
    exit 1
fi

BREW_VERSION=$(brew --version | head -1)
echo "✓ $BREW_VERSION found"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Installing via Homebrew..."
    brew install python3
fi

PYTHON_VERSION=$(python3 --version)
echo "✓ $PYTHON_VERSION found"

# Add tap and install
echo "📥 Adding Homebrew tap..."
brew tap kelushael/taps

echo "📦 Installing unifiedcli..."
brew install kelushael/taps/unifiedcli

echo ""
echo "🔑 Sovereign key setup:"
echo "  1. Run: unifiedcli keygen"
echo "  2. Set: export POOKIE_KEY='pk-...'"
echo "  3. Run: unifiedcli shell"
echo ""
echo "✅ Installation complete!"
echo ""
echo "Verify with: unifiedcli --version"
