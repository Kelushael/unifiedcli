import subprocess
from typing import List, Dict, Optional

class PookieClient:
    """Interface to pookie CLI for model distribution"""

    def __init__(self, registry_url: str = "http://108.181.162.206:7070"):
        self.registry_url = registry_url

    def pull_model(self, model_name: str) -> bool:
        """Pull a model from bartowski via pookie"""
        try:
            result = subprocess.run(
                ["pookie", "pull", model_name],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Error pulling model: {e}")
            return False

    def run_model(self, model_name: str) -> Dict:
        """Start a model with pookie run"""
        try:
            result = subprocess.run(
                ["pookie", "run", model_name],
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def swap_model(self, new_model: str) -> bool:
        """Hot-swap to a different model"""
        try:
            result = subprocess.run(
                ["pookie", "swap", new_model],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Error swapping model: {e}")
            return False

    def list_models(self) -> List[Dict]:
        """Get list of running/available models via pookie ps"""
        try:
            result = subprocess.run(
                ["pookie", "ps"],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode != 0:
                return []

            models = []
            for line in result.stdout.split("\n")[1:]:  # Skip header
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 3:
                        models.append({
                            "name": parts[0],
                            "status": parts[1],
                            "vram": parts[2] if len(parts) > 2 else "unknown"
                        })

            return models
        except Exception as e:
            print(f"Error listing models: {e}")
            return []

    def get_status(self) -> Dict:
        """Get pookie status (key + resolved node)"""
        try:
            result = subprocess.run(
                ["pookie", "status"],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                return {"success": True, "output": result.stdout}
            else:
                return {"success": False, "error": result.stderr}
        except Exception as e:
            return {"success": False, "error": str(e)}
