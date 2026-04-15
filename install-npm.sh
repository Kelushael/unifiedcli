#!/bin/bash
# NPM installation script for unifiedcli
# Run: npm install -g unifiedcli

set -e

echo "🚀 Installing Unified CLI via npm..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install from https://nodejs.org"
    exit 1
fi

NODE_VERSION=$(node --version)
echo "✓ $NODE_VERSION found"

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install from https://nodejs.org"
    exit 1
fi

NPM_VERSION=$(npm --version)
echo "✓ npm $NPM_VERSION found"

# Install globally
echo "📦 Installing unifiedcli globally..."
npm install -g unifiedcli

echo ""
echo "🔑 Sovereign key setup:"
echo "  1. Run: unifiedcli keygen"
echo "  2. Set: export POOKIE_KEY='pk-...'"
echo "  3. Run: unifiedcli shell"
echo ""
echo "✅ Installation complete!"
echo ""
echo "Verify with: unifiedcli --version"
