

import bcrypt

class HashManager:

    @staticmethod
    def create_hash(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt(12)).decode()

    @staticmethod
    def verify_hash(plain_password: str, hashed_password: str) -> str:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

