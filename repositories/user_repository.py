

from database import Database


class UserRepo:

    def __init__(self, db: Database) -> None:
        self.db = db

    def create_user(self, cur, name: str, password_hash: str) ->None:
        cur.execute("""
        INSERT INTO users
        (name, password_hash)
        VALUES
        (%s, %s)""",(name, password_hash))

    def get_user_by_name(self, cur, name: str) ->tuple:
        cur.execute("""
        SELECT id, name, password_hash
        FROM users
        WHERE name = %s""", (name,))
        row = cur.fetchone()
        if not row: return None
        return row

    def get_name_by_id(self, cur, user_id: int) ->tuple:
            cur.execute("""
            SELECT name
            FROM users
            WHERE id = %s""", (user_id,))
            row = cur.fetchone()
            if not row: return None
            return row