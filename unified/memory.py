import sqlite3
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

class UnifiedMemory:
    """Local memory system (SQLite) with optional remote sync"""

    def __init__(self, db_path: str = "./data/unified_memory.db"):
        """Initialize memory database"""
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        """Create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                content TEXT NOT NULL,
                type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()

    def save(self, name: str, content: str, memory_type: str) -> None:
        """Save a memory"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO memories (name, content, type, timestamp)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            """, (name, content, memory_type))
        except sqlite3.IntegrityError:
            # Update if exists
            cursor.execute("""
                UPDATE memories
                SET content = ?, type = ?, updated_at = CURRENT_TIMESTAMP
                WHERE name = ?
            """, (content, memory_type, name))

        conn.commit()
        conn.close()

    def search(self, query: str) -> List[Dict]:
        """Search memories by content"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, content, type, timestamp
            FROM memories
            WHERE content LIKE ?
            ORDER BY timestamp DESC
        """, (f"%{query}%",))

        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row[0],
                "name": row[1],
                "content": row[2],
                "type": row[3],
                "timestamp": row[4]
            })

        conn.close()
        return results

    def search_by_type(self, memory_type: str) -> List[Dict]:
        """Search memories by type"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, content, type, timestamp
            FROM memories
            WHERE type = ?
            ORDER BY timestamp DESC
        """, (memory_type,))

        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row[0],
                "name": row[1],
                "content": row[2],
                "type": row[3],
                "timestamp": row[4]
            })

        conn.close()
        return results

    def delete_by_name(self, name: str) -> None:
        """Delete a memory by name"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM memories WHERE name = ?", (name,))
        conn.commit()
        conn.close()

    def list_all(self) -> List[Dict]:
        """List all memories"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, content, type, timestamp
            FROM memories
            ORDER BY timestamp DESC
        """)

        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row[0],
                "name": row[1],
                "content": row[2],
                "type": row[3],
                "timestamp": row[4]
            })

        conn.close()
        return results
