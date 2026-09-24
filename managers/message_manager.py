
from repositories.message_repository import MessageRepo
from managers.user_manager import UserManager
from exceptions import MessageCreationError, MessageFetchingError


class MessageManager:

    def __init__(self, message_repo: MessageRepo):
        self.mr = message_repo
        self.db = self.mr.db

    def create_message(self, user_id: int, message: str) ->None:
        with self.db.connect_database() as conn:
            cur = conn.cursor()
            try:
                self.mr.create_message(cur, user_id, message)
                conn.commit()
            except Exception as e:
                raise MessageCreationError(f'Error occured while creating message: {str(e)}')
                
    
    def get_messages(self):
        with self.db.connect_database() as conn:
            cur = conn.cursor()
            try:
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
            except Exception as e:
                raise MessageFetchingError(f'Error occured while fetching messages: {str(e)}')