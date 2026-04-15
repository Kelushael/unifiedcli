# Installation Guide

**Unified Platform** works on Linux, macOS, Windows, and Android. Choose your installation method below.

---

## Quick Install (One Command)

### 🐧 Linux / macOS / WSL

```bash
curl https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install-curl.sh | bash
```

### 🪟 Windows (PowerShell)

```powershell
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install.ps1 -OutFile install.ps1; .\install.ps1"
```

---

## Operating System Specific

### 🐧 Linux / macOS

**Option 1: Bash (Recommended)**
```bash
bash <(curl -s https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install.sh)
```

**Option 2: Download and Run**
```bash
curl -O https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install.sh
chmod +x install.sh
./install.sh
```

**Option 3: Manual**
```bash
git clone https://github.com/Kelushael/unifiedcli.git
cd unifiedcli
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### 🪟 Windows (PowerShell)

**Option 1: One-Liner**
```powershell
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install.ps1 -OutFile install.ps1; .\install.ps1"
```

**Option 2: Download and Run**
```powershell
# Download
Invoke-WebRequest https://raw.githubusercontent.com/Kelushael/unifiedcli/main/install.ps1 -OutFile install.ps1

# Run as Administrator
.\install.ps1
```

**Option 3: Git Bash**
```bash
bash install.sh
```

### 🍎 macOS (Homebrew)

```bash
bash install-brew.sh
```

Or manually:
```bash
brew tap kelushael/taps
brew install kelushael/taps/unifiedcli
```

### 📦 npm (Global)

```bash
npm install -g unifiedcli
```

Or via script:
```bash
bash install-npm.sh
```

### 🤖 Termux (Android)

```bash
bash install-termux.sh
```

Or run the commands manually:
```bash
apt update && apt upgrade -y
apt install python3 python3-pip git
git clone https://github.com/Kelushael/unifiedcli.git
cd unifiedcli
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

## Post-Installation Setup

After installing, complete the setup:

```bash
# 1. Generate your sovereign key
unifiedcli keygen

# 2. Copy the output and set environment variable
export POOKIE_KEY='pk-...'

# 3. Start the agent
unifiedcli shell
```

**Optional:** Add to your shell config for persistence:
```bash
# Add to ~/.bashrc, ~/.zshrc, or ~/.profile
export POOKIE_KEY='pk-your-key-here'
```

---

## Verification

Test your installation:

```bash
# Check version
unifiedcli --version

# Generate test key
unifiedcli keygen

# Start shell
unifiedcli shell
```

---

## Troubleshooting

### Python not found
- **Linux:** `apt-get install python3 python3-pip python3-venv`
- **macOS:** `brew install python3`
- **Windows:** Install from [python.org](https://python.org)

### Git not found
- **Linux:** `apt-get install git`
- **macOS:** `brew install git`
- **Windows:** Install from [git-scm.com](https://git-scm.com)

### Permission denied (Linux/macOS)
```bash
chmod +x install.sh
./install.sh
```

### POOKIE_KEY not set
```bash
unifiedcli keygen
export POOKIE_KEY='pk-...'
```

### Virtual environment issues
```bash
# Remove and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### Connection refused
- Verify pookie is running: `pookie serve` on VPS
- Check VPS IP: `ping 108.181.162.206`
- Verify environment: `echo $POOKIE_KEY`

---

## Installation Scripts Reference

| Script | OS | Method | Run |
|--------|-----|--------|-----|
| `install.sh` | Linux/macOS | Bash | `bash install.sh` |
| `install.ps1` | Windows | PowerShell | `.\install.ps1` |
| `install-curl.sh` | All (Unix) | Curl | `curl ... \| bash` |
| `install-npm.sh` | All | npm | `npm install -g unifiedcli` |
| `install-brew.sh` | macOS | Homebrew | `bash install-brew.sh` |
| `install-termux.sh` | Android | Termux | `bash install-termux.sh` |

---

## Getting Help

- **Quick Start:** See [QUICKSTART.md](QUICKSTART.md)
- **Full Docs:** See [README.md](README.md)
- **Issues:** [GitHub Issues](https://github.com/Kelushael/unifiedcli/issues)

---

Built with ❤️ for sovereign AI agents
