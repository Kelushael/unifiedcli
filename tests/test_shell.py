import pytest
from unittest.mock import Mock, patch
from unified.shell import UnifiedShell
from unified.config import Config

@pytest.fixture
def mock_config():
    """Mock configuration"""
    config = Mock(spec=Config)
    config.pookie_key = "pk-test-123"
    config.pookie_registry = "http://108.181.162.206:7070"
    config.mcp_url.return_value = "http://127.0.0.1:8000"
    config.memory_db_path = ":memory:"
    return config

@pytest.fixture
def shell(mock_config):
    """Create UnifiedShell instance"""
    with patch('unified.shell.PookieClient'):
        with patch('unified.shell.TOOLLAMAClient'):
            return UnifiedShell(config=mock_config)

def test_shell_parses_slash_command(shell):
    """Should parse slash commands"""
    cmd, args = shell._parse_command("/pull qwen:7b")
    assert cmd == "pull"
    assert args == ["qwen:7b"]

def test_shell_parses_multi_arg_command(shell):
    """Should parse commands with multiple arguments"""
    cmd, args = shell._parse_command("/search some query here")
    assert cmd == "search"
    assert args == ["some", "query", "here"]

def test_shell_help_command(shell):
    """Should show help"""
    result = shell._execute_command("help", [])
    assert "Model Management" in result
    assert "/pull" in result
    assert "/swap" in result

def test_shell_unknown_command(shell):
    """Should handle unknown commands"""
    result = shell._execute_command("unknown_command", [])
    assert "Unknown command" in result
