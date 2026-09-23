
from repositories.message_repository import MessageRepo
from managers.user_manager import UserManager


class MessageManager:

    def __init__(self, message_repo: MessageRepo):
        self.mr = message_repo
        self.db = self.mr.db


  
    def get_messages(self):
        with self.db.connect_database() as conn:
            cur = conn.cursor()
            messages = self.mr.get_messages(cur)
            return [
                {
                    'id': msg[0],
                    'user_id': msg[1],
                    'name': msg[2],
                    'message': msg[3]
                }
                for msg in messages
            ]