
from database import Database


class MessageRepo:

    def __init__(self, db: Database) -> None:
        self.db = db

    def create_message(self, cur, user_id: int, message: str) -> None:
        cur.execute("""
        INSERT INTO messages
        (user_id, message)
        VALUES
        (%s, %s)""", (user_id, message))


    def get_messages(self, cur) -> list[tuple]:
        cur.execute("""
        SELECT m.id, m.user_id, u.name, m.message
        FROM messages AS m
        LEFT JOIN users AS u
            ON m.user_id = u.id
        """)
        rows = cur.fetchall()
        if not rows: return None
        return rows