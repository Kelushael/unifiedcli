import sys
from typing import Tuple, List
from unified.config import Config
from unified.integrations.pookie_client import PookieClient
from unified.integrations.toollama_client import TOOLLAMAClient
from unified.memory import UnifiedMemory
from unified.commands.model_commands import ModelCommands

class UnifiedShell:
    """Interactive shell for unified platform"""

    def __init__(self, config: Config):
        self.config = config
        self.pookie_client = PookieClient(config.pookie_registry)
        self.toollama_client = TOOLLAMAClient(config.mcp_url())
        self.memory = UnifiedMemory(config.memory_db_path)
        self.model_commands = ModelCommands(self.pookie_client)
        self.current_model = None

    def _parse_command(self, input_line: str) -> Tuple[str, List[str]]:
        """Parse slash command into (command, args)"""
        parts = input_line.strip().split()
        if not parts or not parts[0].startswith("/"):
            return None, []

        command = parts[0][1:]  # Remove leading /
        args = parts[1:]
        return command, args

    def _execute_command(self, command: str, args: List[str]) -> str:
        """Execute a single command"""
        # Model commands
        if command == "pull" and args:
            return self.model_commands.pull(args[0])
        elif command == "run" and args:
            return self.model_commands.run(args[0])
        elif command == "swap" and args:
            return self.model_commands.swap(args[0])
        elif command == "ps":
            return self.model_commands.ps()
        elif command == "status":
            return self.model_commands.status()

        # Memory commands
        elif command == "memory":
            all_memories = self.memory.list_all()
            if not all_memories:
                return "No memories saved"
            return f"Memories: {len(all_memories)}\n" + "\n".join([
                f"  - {m['name']}: {m['content'][:50]}"
                for m in all_memories
            ])

        elif command == "search" and args:
            query = " ".join(args)
            results = self.memory.search(query)
            if not results:
                return f"No memories matching '{query}'"
            return "\n".join([
                f"  [{r['type']}] {r['name']}: {r['content']}"
                for r in results
            ])

        # Help
        elif command == "help":
            return self._show_help()

        elif command == "exit":
            print("Goodbye!")
            sys.exit(0)

        else:
            return f"Unknown command: /{command}. Type /help for available commands."

    def _show_help(self) -> str:
        """Show help message"""
        return """
🔷 Unified Platform Commands:

📦 Model Management:
  /pull <model>           - Download model (qwen:7b, deepseek-r1:7b, etc.)
  /run <model>            - Start model
  /swap <model>           - Hot-swap to different model
  /ps                     - List running models
  /status                 - Show pookie status

💾 Memory:
  /memory                 - List all memories
  /search <query>         - Search memories

⚙️  System:
  /help                   - Show this message
  /exit                   - Exit shell
"""

    def run(self):
        """Start interactive shell"""
        print("=" * 60)
        print("🚀 Unified Platform Shell")
        print(f"📌 Key: {self.config.pookie_key[:20]}...")
        print(f"🔗 Registry: {self.config.pookie_registry}")
        print("Type '/help' for commands")
        print("=" * 60)

        while True:
            try:
                user_input = input("\n🔷 > ").strip()

                if not user_input:
                    continue

                if user_input.startswith("/"):
                    command, args = self._parse_command(user_input)
                    if command:
                        result = self._execute_command(command, args)
                        print(result)
                else:
                    # Regular chat (will be passed to model)
                    print("Chat mode (pass-through to model - coming soon)")

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
