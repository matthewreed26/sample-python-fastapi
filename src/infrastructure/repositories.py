from src.domain.models import User
from src.domain.ports import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def save(self, user: User) -> User:
        self._users[user.email] = user
        return user

    def get_by_email(self, email: str) -> User | None:
        return self._users.get(email)