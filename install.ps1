# PowerShell install script for unifiedcli on Windows
# Run as Administrator

Write-Host "🚀 Installing Unified CLI..." -ForegroundColor Green

# Check Python
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "❌ Python not found. Please install Python 3.10+ from https://python.org" -ForegroundColor Red
    exit 1
}

$pythonVersion = python --version 2>&1
Write-Host "✓ $pythonVersion found" -ForegroundColor Green

# Check Git
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCmd) {
    Write-Host "❌ Git not found. Please install from https://git-scm.com" -ForegroundColor Red
    exit 1
}

# Clone repo
if (-not (Test-Path "unifiedcli")) {
    Write-Host "📥 Cloning repository..." -ForegroundColor Blue
    git clone https://github.com/Kelushael/unifiedcli.git
}

Set-Location unifiedcli

# Create virtual environment
if (-not (Test-Path "venv")) {
    Write-Host "🔧 Creating virtual environment..." -ForegroundColor Blue
    python -m venv venv
}

# Activate venv
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Blue
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Setup
Write-Host ""
Write-Host "🔑 Sovereign key setup:" -ForegroundColor Green
Write-Host "  1. Run: unifiedcli keygen"
Write-Host "  2. Set: `$env:POOKIE_KEY='pk-...'"
Write-Host "  3. Run: unifiedcli shell"
Write-Host ""
Write-Host "✅ Installation complete!" -ForegroundColor Green
