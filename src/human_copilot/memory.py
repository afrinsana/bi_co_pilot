import sqlite3
from datetime import datetime

class UserMemory:
    def __init__(self, db_path="user_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        """Initialize the database table."""
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS memory
               (id INTEGER PRIMARY KEY, key TEXT, value TEXT, timestamp TEXT)"""
        )
    
    def store(self, key: str, value: str):
        """Store a key-value pair."""
        timestamp = datetime.now().isoformat()
        self.conn.execute(
            "INSERT INTO memory (key, value, timestamp) VALUES (?, ?, ?)",
            (key, value, timestamp)
        )
        self.conn.commit()
    
    def recall(self, key: str) -> str:
        """Retrieve a value by key."""
        cursor = self.conn.execute(
            "SELECT value FROM memory WHERE key=? ORDER BY timestamp DESC LIMIT 1",
            (key,)
        )
        return cursor.fetchone()[0] if cursor.fetchone() else None

# Example usage:
# memory = UserMemory()
# memory.store("favorite_coffee", "latte")
# print(memory.recall("favorite_coffee"))  # Output: "latte"