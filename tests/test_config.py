import pytest
import os
import tempfile
from unified.config import Config

def test_config_loads_from_env():
    """Config should load POOKIE_KEY from environment"""
    os.environ["POOKIE_KEY"] = "pk-test-123"
    config = Config.from_env()
    assert config.pookie_key == "pk-test-123"

def test_config_requires_pookie_key():
    """Config should raise error if POOKIE_KEY is missing"""
    if "POOKIE_KEY" in os.environ:
        del os.environ["POOKIE_KEY"]
    with pytest.raises(ValueError, match="POOKIE_KEY not set"):
        Config.from_env()

def test_config_defaults():
    """Config should have sensible defaults"""
    os.environ["POOKIE_KEY"] = "pk-test-123"
    config = Config.from_env()
    assert config.mcp_server_host == "127.0.0.1"
    assert config.mcp_server_port == 8000
    assert config.bash_timeout_seconds == 30

def test_mcp_url():
    """Should construct MCP URL correctly"""
    os.environ["POOKIE_KEY"] = "pk-test-123"
    config = Config.from_env()
    assert config.mcp_url() == "http://127.0.0.1:8000"
