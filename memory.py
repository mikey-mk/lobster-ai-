import sqlite3
from config import DB_PATH, MAX_MEMORY_MESSAGES

class Memory:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    role TEXT,
                    content TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def add_message(self, user_id, role, content):
        with self.conn:
            self.conn.execute(
                "INSERT INTO chat_history (user_id, role, content) VALUES (?, ?, ?)",
                (user_id, role, content)
            )

    def get_history(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT role, content FROM chat_history WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?",
            (user_id, MAX_MEMORY_MESSAGES)
        )
        rows = cursor.fetchall()
        # Return in chronological order
        return [{"role": row[0], "content": row[1]} for row in reversed(rows)]

    def clear_history(self, user_id):
        with self.conn:
            self.conn.execute("DELETE FROM chat_history WHERE user_id = ?", (user_id,))
