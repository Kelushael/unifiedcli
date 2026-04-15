import requests
from typing import List, Dict, Optional, Any

class TOOLLAMAClient:
    """Interface to TOOLLAMA MCP server for developer tools"""

    def __init__(self, mcp_url: str = "http://127.0.0.1:8000"):
        self.mcp_url = mcp_url

    def list_tools(self) -> List[Dict]:
        """Get list of available tools from MCP server"""
        try:
            response = requests.get(f"{self.mcp_url}/tools", timeout=5)
            if response.status_code == 200:
                return response.json().get("tools", [])
            return []
        except Exception as e:
            print(f"Error listing tools: {e}")
            return []

    def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict:
        """Execute a tool via MCP"""
        try:
            payload = {
                "tool": tool_name,
                "arguments": arguments
            }
            response = requests.post(
                f"{self.mcp_url}/execute",
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def save_memory(self, key: str, content: str, memory_type: str) -> Dict:
        """Save to TOOLLAMA memory"""
        return self.execute_tool("memory_save", {
            "key": key,
            "content": content,
            "type": memory_type
        })

    def search_memory(self, query: str) -> Dict:
        """Search memory"""
        return self.execute_tool("memory_search", {
            "query": query
        })

    def read_file(self, path: str) -> Dict:
        """Read file via TOOLLAMA"""
        return self.execute_tool("read_file", {
            "path": path
        })

    def write_file(self, path: str, content: str) -> Dict:
        """Write file via TOOLLAMA"""
        return self.execute_tool("write_file", {
            "path": path,
            "content": content
        })

    def bash_execute(self, command: str) -> Dict:
        """Execute bash command via TOOLLAMA"""
        return self.execute_tool("bash_execute", {
            "command": command
        })

    def git_commit(self, message: str) -> Dict:
        """Create git commit via TOOLLAMA"""
        return self.execute_tool("git_commit", {
            "message": message
        })

    def is_healthy(self) -> bool:
        """Check if MCP server is responsive"""
        try:
            response = requests.get(f"{self.mcp_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
