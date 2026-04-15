import pytest
import tempfile
import os
from unified.memory import UnifiedMemory

@pytest.fixture
def temp_db():
    """Create temporary database for testing"""
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    yield path
    os.unlink(path)

def test_memory_save_and_search(temp_db):
    """Should save and retrieve memories"""
    mem = UnifiedMemory(db_path=temp_db)
    mem.save("preference", "I prefer Python over JavaScript", "user_preference")

    results = mem.search("Python")
    assert len(results) > 0
    assert "Python" in results[0]["content"]

def test_memory_isolation_by_type(temp_db):
    """Should isolate memories by type"""
    mem = UnifiedMemory(db_path=temp_db)
    mem.save("feedback", "Always use TDD", "development_rule")
    mem.save("project", "Deadline is Friday", "project_info")

    feedback = mem.search_by_type("development_rule")
    assert any("TDD" in r["content"] for r in feedback)

def test_memory_delete(temp_db):
    """Should be able to delete memories"""
    mem = UnifiedMemory(db_path=temp_db)
    mem.save("temp", "Remove me", "temp_memory")
    mem.delete_by_name("temp")

    results = mem.search("Remove me")
    assert len(results) == 0

def test_memory_list_all(temp_db):
    """Should list all memories"""
    mem = UnifiedMemory(db_path=temp_db)
    mem.save("first", "Content 1", "type1")
    mem.save("second", "Content 2", "type2")

    all_mem = mem.list_all()
    assert len(all_mem) == 2
