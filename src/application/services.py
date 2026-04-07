from src.domain.models import User
from src.domain.ports import UserRepository

class UserAlreadyExistsError(Exception):
    pass

class UserRegistrationService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, email: str, username: str) -> User:
        if self.user_repo.get_by_email(email):
            raise UserAlreadyExistsError(f"User with email {email} already exists.")
        
        new_user = User(email=email, username=username)
        return self.user_repo.save(new_user)
    
    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repo.get_by_email(email)

    def get_user_by_username(self, username: str) -> User | None:
        return self.user_repo.get_by_username(username)