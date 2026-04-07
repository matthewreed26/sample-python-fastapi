from fastapi import Depends
from src.infrastructure.repositories import InMemoryUserRepository
from src.application.services import UserRegistrationService

# The global instance for "real" runtime
_user_repo = InMemoryUserRepository()

def get_user_repository() -> InMemoryUserRepository:
    return _user_repo

def get_registration_service(
    repo: InMemoryUserRepository = Depends(get_user_repository)
) -> UserRegistrationService:
    return UserRegistrationService(user_repo=repo)