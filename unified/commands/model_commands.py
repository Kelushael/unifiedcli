from typing import List, Dict
from unified.integrations.pookie_client import PookieClient

class ModelCommands:
    """Model management commands"""

    def __init__(self, pookie_client: PookieClient):
        self.pookie = pookie_client

    def pull(self, model_name: str) -> str:
        """Pull a model: /pull qwen:7b"""
        print(f"📦 Pulling {model_name}...")
        success = self.pookie.pull_model(model_name)
        if success:
            return f"✓ Successfully pulled {model_name}"
        else:
            return f"✗ Failed to pull {model_name}"

    def run(self, model_name: str) -> str:
        """Run a model: /run qwen:7b"""
        print(f"🚀 Starting {model_name}...")
        result = self.pookie.run_model(model_name)
        if result["success"]:
            return f"✓ {model_name} is running"
        else:
            return f"✗ Failed to run {model_name}: {result.get('error', 'unknown error')}"

    def swap(self, model_name: str) -> str:
        """Hot-swap model: /swap deepseek-r1:7b"""
        print(f"🔄 Swapping to {model_name}...")
        success = self.pookie.swap_model(model_name)
        if success:
            return f"✓ Swapped to {model_name}"
        else:
            return f"✗ Failed to swap to {model_name}"

    def ps(self) -> str:
        """List models: /ps"""
        models = self.pookie.list_models()
        if not models:
            return "No models available"

        lines = ["NAME              STATUS     VRAM"]
        for model in models:
            lines.append(
                f"{model['name']:<17} {model['status']:<10} {model.get('vram', 'N/A')}"
            )
        return "\n".join(lines)

    def status(self) -> str:
        """Show pookie status: /status"""
        result = self.pookie.get_status()
        if result["success"]:
            return result["output"]
        else:
            return f"Error: {result.get('error', 'unknown')}"
