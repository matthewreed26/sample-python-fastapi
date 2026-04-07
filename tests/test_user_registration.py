import pytest
from src.application.services import UserRegistrationService, UserAlreadyExistsError
from src.domain.models import User

# --- BDD Unit Tests (Application Layer) ---

def test_successful_user_registration_creates_new_user(mock_repo):
    # GIVEN a repository that does not have the user
    mock_repo.get_by_email.return_value = None
    mock_repo.save.side_effect = lambda user: user
    
    service = UserRegistrationService(user_repo=mock_repo)
    email = "test@example.com"
    username = "testuser"

    # WHEN the user attempts to register
    result = service.register_user(email=email, username=username)

    # THEN the user is created and saved
    assert result.email == email
    assert result.username == username
    mock_repo.save.assert_called_once()

def test_registration_fails_if_email_already_exists(mock_repo):
    # GIVEN a repository that already contains a user
    existing_user = User(email="conflict@example.com", username="existing")
    mock_repo.get_by_email.return_value = existing_user
    
    service = UserRegistrationService(user_repo=mock_repo)

    # WHEN/THEN
    with pytest.raises(UserAlreadyExistsError):
        service.register_user(email="conflict@example.com", username="newuser")

# --- BDD Integration Tests (API Boundary) ---

def test_api_can_register_valid_user(client, clean_repo):
    # GIVEN valid user payload
    payload = {"email": "api@example.com", "username": "apiuser"}

    # WHEN a POST request is sent to the FastAPI endpoint
    response = client.post("/users/", json=payload)

    # THEN the response indicates creation
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == payload["email"]
    
    # AND the data is actually in our 'clean_repo'
    assert clean_repo.get_by_email("api@example.com") is not None

def test_api_returns_409_on_duplicate_email(client, clean_repo):
    # GIVEN a user already exists in the repo
    payload = {"email": "dup@example.com", "username": "first"}
    client.post("/users/", json=payload)
    
    # WHEN we try to register the same email again
    response = client.post("/users/", json=payload)
    
    # THEN we get a 409 Conflict
    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]