# Unified Platform

**One CLI to rule them all.** Combines **pookie** (sovereign models) + **TOOLLAMA** (developer tools) + **YahushuaCLI** (IDE).

A single command-line agent that lets you:
- Pull and run GGUF models on your VPS
- Hot-swap models instantly
- Access persistent memory
- Execute commands and manage files
- Maintain a sovereign, local-first development environment

## Installation

```bash
# Clone and install
git clone https://github.com/kelushael/unified-platform
cd unified-platform

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Generate sovereign key
unifiedcli keygen
export POOKIE_KEY=pk-...

# Start the agent
unifiedcli shell
```

## Quick Start

```bash
# List models on your VPS
/ps

# Pull a model
/pull qwen:7b

# Run the model
/run qwen:7b

# Switch to a different model (hot-swap)
/swap deepseek-r1:7b

# Check status
/status

# Save to memory
/memory
/search python

# Get help
/help
```

## Architecture

```
┌────────────────────────────────────┐
│     unifiedcli (your agent)       │
├────────────────────────────────────┤
│   YahushuaCLI Interactive Shell    │
├──────────────┬─────────────────────┤
│  pookie      │    TOOLLAMA         │
│  ├ pull      │    ├ read/write     │
│  ├ run       │    ├ bash exec      │
│  ├ swap      │    ├ git ops        │
│  └ registry  │    └ memory         │
└──────────────┴─────────────────────┘
         Your VPS (108.181.162.206)
```

## Commands

### Model Management
- `/pull <model>` — Download model (qwen:7b, deepseek-r1:7b, llama3.1:8b, etc.)
- `/run <model>` — Start model
- `/swap <model>` — Hot-swap to different model instantly
- `/ps` — List running models and VRAM usage
- `/status` — Show pookie status (key + VPS IP)

### Memory
- `/memory` — List all saved memories
- `/search <query>` — Search memories
- `/save <key> <content>` — Save to memory

### System
- `/help` — Show available commands
- `/exit` — Exit shell

## Configuration

Create `.env` file or set environment variables:

```bash
# Required
POOKIE_KEY=pk-...  # From 'unifiedcli keygen'

# Optional (defaults shown)
POOKIE_REGISTRY=http://108.181.162.206:7070
POOKIE_VPS_HOST=108.181.162.206
MCP_SERVER_HOST=127.0.0.1
MCP_SERVER_PORT=8000
MEMORY_DB_PATH=./data/unified_memory.db
BASH_TIMEOUT_SECONDS=30
```

## Features

✅ **Sovereign:** Your models, your VPS, your data  
✅ **Model Agnostic:** Works with any GGUF model (Qwen, DeepSeek, Mistral, Llama, etc.)  
✅ **Hot-Swappable:** Switch models instantly without losing context  
✅ **Persistent Memory:** Memories survive across sessions  
✅ **Developer Tools:** File operations, bash execution, git integration  
✅ **Local-First:** No cloud dependencies  
✅ **Single Entry Point:** One `unifiedcli` command  

## Requirements

- Python 3.10+
- pookie CLI installed and running on VPS
- TOOLLAMA MCP server (optional but recommended)
- Sovereign key from `pookie keygen`

## Development

```bash
# Install dev dependencies
pip install pytest pytest-mock

# Run tests
pytest tests/

# Run linter
pylint unified/
```

## Troubleshooting

**"POOKIE_KEY not set"**
```bash
unifiedcli keygen
export POOKIE_KEY=pk-...
```

**"Connection refused"**
- Ensure pookie is running: `pookie serve` on your VPS
- Check VPS is reachable: `ping 108.181.162.206`

**"Model not found"**
- List available: `/ps`
- Pull if needed: `/pull qwen:7b`

## License

MIT

## Contributing

Contributions welcome! Areas to improve:
- Additional TOOLLAMA tool integrations
- Web UI for memory management
- Performance optimizations
- Documentation

Built with ❤️ by combining pookie + TOOLLAMA + YahushuaCLI
