from typing import Protocol
from src.domain.models import User

class UserRepository(Protocol):
    def save(self, user: User) -> User:
        ...

    def get_by_email(self, email: str) -> User | None:
        ...
    
    def get_by_username(self, username: str) -> User | None:
        ...