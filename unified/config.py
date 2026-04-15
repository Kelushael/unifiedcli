import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ConfigDict

class Config(BaseModel):
    """Unified Platform configuration"""

    model_config = ConfigDict(env_file=".env")

    pookie_key: str = Field(default="", description="Sovereign key from pookie keygen")
    pookie_registry: str = Field(
        default="http://108.181.162.206:7070",
        description="pookie registry URL"
    )
    pookie_vps_host: Optional[str] = Field(
        default=None,
        description="VPS hostname/IP (optional; registry resolves if not set)"
    )

    mcp_server_host: str = Field(default="127.0.0.1")
    mcp_server_port: int = Field(default=8000)

    memory_db_path: str = Field(default="./data/unified_memory.db")
    bash_timeout_seconds: int = Field(default=30)
    file_read_timeout_seconds: int = Field(default=30)

    @classmethod
    def from_env(cls, env_file: Optional[str] = None) -> "Config":
        """Load config from environment and optional .env file"""
        if env_file:
            load_dotenv(env_file)
        elif Path(".env").exists():
            load_dotenv(".env")

        # Validate required fields
        pookie_key = os.getenv("POOKIE_KEY", "")
        if not pookie_key:
            raise ValueError(
                "POOKIE_KEY not set. Run 'pookie keygen' and set POOKIE_KEY environment variable."
            )

        return cls(
            pookie_key=pookie_key,
            pookie_registry=os.getenv("POOKIE_REGISTRY", "http://108.181.162.206:7070"),
            pookie_vps_host=os.getenv("POOKIE_VPS_HOST"),
            mcp_server_host=os.getenv("MCP_SERVER_HOST", "127.0.0.1"),
            mcp_server_port=int(os.getenv("MCP_SERVER_PORT", "8000")),
            memory_db_path=os.getenv("MEMORY_DB_PATH", "./data/unified_memory.db"),
            bash_timeout_seconds=int(os.getenv("BASH_TIMEOUT_SECONDS", "30")),
            file_read_timeout_seconds=int(os.getenv("FILE_READ_TIMEOUT_SECONDS", "30")),
        )

    def mcp_url(self) -> str:
        """Get MCP server URL"""
        return f"http://{self.mcp_server_host}:{self.mcp_server_port}"
