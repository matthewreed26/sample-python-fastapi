import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from src.api.main import app
from src.api.dependencies import get_user_repository
from src.infrastructure.repositories import InMemoryUserRepository

@pytest.fixture
def mock_repo():
    """Provides a mocked version of the repository for unit tests."""
    return MagicMock()

@pytest.fixture(scope="session")
def client():
    """Provides a FastAPI TestClient for integration tests."""
    with TestClient(app) as c:
        yield c

@pytest.fixture
def clean_repo():
    """
    Provides a real In-Memory repo that is cleared for every test.
    We override the app dependency to use this instance.
    """
    repo = InMemoryUserRepository()
    
    # This 'overrides' the global dependency in the FastAPI app
    app.dependency_overrides[get_user_repository] = lambda: repo
    yield repo
    app.dependency_overrides.clear()