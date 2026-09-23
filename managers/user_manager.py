

from repositories.user_repository import UserRepo
from validators.user_validator import UserValidator
from validators.general_validator import GeneralValidator
from utils.hash_manager import HashManager
from exceptions import AuthenticationError, DatabaseDataCreationError, DatabaseFetchingError


class UserManager:

    def __init__(
                self, 
                user_repo: UserRepo, 
                user_validator: UserValidator, 
                hash_manager: HashManager,
                general_validator: GeneralValidator) -> None:
        
        self.ur = user_repo
        self.uv = user_validator
        self.hm = hash_manager
        self.db = user_repo.db
        self.gv = general_validator

    def create_user(self, name: str, plain_password: str) -> None:
        self.uv.validate_name(name)
        self.uv.validate_password(plain_password)
        password_hash = self.hm.create_hash(plain_password)

        with self.db.connect_database() as conn:
            cur = conn.cursor()
            try:
                self.ur.create_user(cur=cur, name=name, password_hash=password_hash)
            except Exception as e:
                if 'users.name' in str(e):
                    raise AuthenticationError("name already taken")
                raise DatabaseDataCreationError(f"Error occured while creating user: {str(e)}")
            conn.commit()

    def login_user(self, name: str, password: str) -> None:
        self.gv.validate_blank_input(name=name, password=password)

        with self.db.connect_database() as conn:
            cur = conn.cursor()
            try:
                user = self.ur.get_user_by_name(cur, name)
            except Exception as e:
                raise DatabaseFetchingError(f"Error occured while fetching user: {str(e)}")

            if not user or not self.hm.verify_hash(password, user[2]):
                raise AuthenticationError("Please check your username and password")
            
            return {
                'id': user[0],
                'name': user[1]
            }

    def get_user_by_name(self, name: str) -> dict:
        with self.db.connect_database() as conn:
            cur = conn.cursor()
            try:
                user = self.ur.get_user_by_name(cur, name)
                return {
                    'user_id': user[0],
                    'name': user[1]
                }
            except Exception as e:
                raise ValueError(f'Error while fetching user: {str(e)}')
        

            
            
