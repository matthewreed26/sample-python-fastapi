import pytest
from src.application.services import UserRegistrationService, UserAlreadyExistsError
from src.domain.models import User

def test_register_user_saves_to_repository(mock_repo):
    # GIVEN
    mock_repo.get_by_email.return_value = None
    mock_repo.save.side_effect = lambda u: u 
    service = UserRegistrationService(user_repo=mock_repo)

    # WHEN
    user = service.register_user(email="test@example.com", username="tester")

    # THEN
    assert user.email == "test@example.com"
    mock_repo.save.assert_called_once()

def test_register_user_raises_error_on_duplicate(mock_repo):
    # GIVEN
    mock_repo.get_by_email.return_value = User(email="exists@test.com", username="old")
    service = UserRegistrationService(user_repo=mock_repo)

    # WHEN / THEN
    with pytest.raises(UserAlreadyExistsError):
        service.register_user(email="exists@test.com", username="new")

def test_get_user_by_email_returns_user(mock_repo):
    # GIVEN
    mock_repo.get_by_email.return_value = User(email="exists@test.com", username="tester")
    service = UserRegistrationService(user_repo=mock_repo)

    # WHEN
    user = service.get_user_by_email("exists@test.com")

    # THEN
    assert user is not None
    assert user.email == "exists@test.com"

def test_get_user_by_username_returns_user(mock_repo):
    # GIVEN
    mock_repo.get_by_username.return_value = User(email="exists@test.com", username="tester")
    service = UserRegistrationService(user_repo=mock_repo)

    # WHEN
    user = service.get_user_by_username("tester")

    # THEN
    assert user is not None
    assert user.username == "tester"