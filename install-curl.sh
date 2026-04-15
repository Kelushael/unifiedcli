#!/bin/bash
# Universal curl-based installer for unifiedcli
# Usage: curl https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install-curl.sh | bash

set -e

REPO="https://github.com/Kelushael/unifiedcli.git"
INSTALL_DIR="${INSTALL_DIR:-.}"

echo "🚀 Installing Unified CLI..."
echo ""

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    DISTRO=$(lsb_release -si 2>/dev/null || echo "unknown")
    echo "📍 Detected: Linux ($DISTRO)"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="mac"
    echo "📍 Detected: macOS"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
    echo "📍 Detected: Windows (Git Bash)"
else
    echo "❌ Unsupported OS: $OSTYPE"
    echo "Supported: Linux, macOS, Windows (via Git Bash), Termux"
    exit 1
fi

# Check dependencies
echo ""
echo "Checking dependencies..."

if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python 3.10+ not found"
    if [ "$OS" = "linux" ]; then
        echo "   apt-get install python3 python3-pip python3-venv"
    elif [ "$OS" = "mac" ]; then
        echo "   brew install python3"
    fi
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "❌ Git not found"
    if [ "$OS" = "linux" ]; then
        echo "   apt-get install git"
    elif [ "$OS" = "mac" ]; then
        echo "   brew install git"
    fi
    exit 1
fi

PYTHON=$(command -v python3 || command -v python)
PYTHON_VERSION=$($PYTHON --version 2>&1 | awk '{print $2}')
echo "✓ Python $PYTHON_VERSION found"

GIT_VERSION=$(git --version | awk '{print $3}')
echo "✓ Git $GIT_VERSION found"

# Clone repository
echo ""
echo "Cloning repository..."
if [ ! -d "$INSTALL_DIR/unifiedcli" ]; then
    git clone $REPO "$INSTALL_DIR/unifiedcli"
else
    echo "✓ Repository already exists at $INSTALL_DIR/unifiedcli"
fi

cd "$INSTALL_DIR/unifiedcli"

# Create virtual environment
echo ""
echo "Setting up virtual environment..."
if [ ! -d "venv" ]; then
    $PYTHON -m venv venv
fi

# Activate and install
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Create command alias (Unix-like systems)
if [ "$OS" != "windows" ]; then
    echo ""
    echo "Creating command alias..."
    SHELL_RC=""
    if [ -f ~/.bashrc ]; then
        SHELL_RC=~/.bashrc
    elif [ -f ~/.zshrc ]; then
        SHELL_RC=~/.zshrc
    fi

    if [ -n "$SHELL_RC" ]; then
        ALIAS_CMD="alias unifiedcli='source $INSTALL_DIR/unifiedcli/venv/bin/activate && unifiedcli'"
        if ! grep -q "unifiedcli" "$SHELL_RC"; then
            echo "$ALIAS_CMD" >> "$SHELL_RC"
            echo "✓ Added alias to $SHELL_RC"
        fi
    fi
fi

# Summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Installation complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔑 Next steps:"
echo "  1. Run: unifiedcli keygen"
echo "  2. Set: export POOKIE_KEY='pk-...'"
echo "  3. Run: unifiedcli shell"
echo ""
echo "📍 Installation directory: $INSTALL_DIR/unifiedcli"
echo ""
