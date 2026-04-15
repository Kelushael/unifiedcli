# Quick Start Guide

## Prerequisites

- Python 3.10+
- pookie CLI installed on your machine and running on your VPS
- Sovereign key from `pookie keygen`

## Setup (5 minutes)

```bash
# 1. Clone the repo
git clone https://github.com/kelushael/unified-platform
cd unified-platform

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install
pip install -r requirements.txt
pip install -e .

# 4. Generate your sovereign key
unifiedcli keygen
# Copy the output: export POOKIE_KEY=pk-...

# 5. Set your key
export POOKIE_KEY=pk-...

# 6. Start the agent
unifiedcli shell
```

## Using the CLI

```bash
🔷 Unified Platform Shell
📌 Key: pk-test-...
🔗 Registry: http://108.181.162.206:7070
Type '/help' for commands

# List available models on your VPS
🔷 > /ps
NAME              STATUS     VRAM
qwen:7b           running    4.2GB
mistral:7b        stopped    0GB

# Pull a new model
🔷 > /pull deepseek-r1:7b
📦 Pulling deepseek-r1:7b...
✓ Successfully pulled deepseek-r1:7b

# Run it
🔷 > /run deepseek-r1:7b
🚀 Starting deepseek-r1:7b...
✓ deepseek-r1:7b is running

# Switch models (hot-swap)
🔷 > /swap qwen:7b
🔄 Swapping to qwen:7b...
✓ Swapped to qwen:7b

# Check status
🔷 > /status
Key: pk-...
Node: 108.181.162.206

# Save memory
🔷 > /memory
Memories: 0

# Get help
🔷 > /help
🔷 Unified Platform Commands:

📦 Model Management:
  /pull <model>           - Download model (qwen:7b, deepseek-r1:7b, etc.)
  /run <model>            - Start model
  /swap <model>           - Hot-swap to different model instantly
  /ps                     - List running models and VRAM usage
  /status                 - Show pookie status (key + VPS IP)

💾 Memory:
  /memory                 - List all saved memories
  /search <query>         - Search memories
  /save <key> <content>   - Save to memory

⚙️  System:
  /help                   - Show available commands
  /exit                   - Exit shell
```

## Common Models

```bash
# Qwen series
/pull qwen:7b
/pull qwen:14b
/pull qwen2.5:7b

# DeepSeek
/pull deepseek-r1:7b
/pull deepseek-r1:14b

# Mistral
/pull mistral:7b
/pull mistral:8x7b

# Llama
/pull llama3.1:8b
/pull llama3.1:70b

# Phi
/pull phi:3.5b
/pull phi:14b
```

## Docker Usage

```bash
# Build
docker-compose build

# Run
docker-compose up -d

# Exec shell
docker-compose exec unified-platform bash -c "source venv/bin/activate && unifiedcli shell"
```

## Troubleshooting

**"POOKIE_KEY not set"**
```bash
unifiedcli keygen
export POOKIE_KEY=pk-your-key
```

**"Connection refused"**
- Check pookie is running: `pookie serve` on your VPS
- Verify VPS IP: should be `108.181.162.206`

**"Model not found"**
```bash
/ps  # List available models
/pull qwen:7b  # Pull if needed
```

**Memory persists?**
```bash
/memory  # List all saved memories
/search keyword  # Search across memories
```

## Next Steps

- Read [README.md](README.md) for full documentation
- Check [CONTRIBUTING.md](CONTRIBUTING.md) if you want to add features
- Run tests: `pytest tests/ -v`

## Architecture

```
your machine              VPS (108.181.162.206)
┌─────────────┐          ┌──────────────────┐
│ unifiedcli │ ◄──────► │  pookie server   │
│  ├ pookie   │  (REST)  │  + llama.cpp     │
│  ├ toollama │          │  + registry      │
│  └ memory   │          │  + models        │
└─────────────┘          └──────────────────┘
```

Enjoy your sovereign AI agent! 🚀
