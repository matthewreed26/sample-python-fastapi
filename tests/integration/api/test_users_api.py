from src.domain.models import User


def test_post_user_returns_201_and_json(client, clean_repo):
    # GIVEN
    payload = {"email": "api@test.com", "username": "api_user"}

    # WHEN
    response = client.post("/users/", json=payload)

    # THEN
    assert response.status_code == 201
    assert response.json()["email"] == "api@test.com"
    # Verify it actually reached the repository
    assert clean_repo.get_by_email("api@test.com") is not None

def test_api_returns_409_on_duplicate_email(client, clean_repo):
    # GIVEN a user already exists in the repo
    payload = {"email": "dup@example.com", "username": "first"}
    client.post("/users/", json=payload)
    
    # WHEN we try to register the same email again
    response = client.post("/users/", json=payload)
    
    # THEN we get a 409 Conflict
    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]

def test_get_user_by_email_returns_200_and_json(client, clean_repo):
    # GIVEN
    user_to_save = User(email="api@test.com", username="api_user")
    clean_repo.save(user_to_save)

    # WHEN
    response = client.get(f"/users/email/{user_to_save.email}")

    # THEN
    assert response.status_code == 200
    assert response.json()["email"] == "api@test.com"

def test_api_returns_404_if_user_not_found_by_email(client, clean_repo):
    # GIVEN

    # WHEN
    response = client.get("/users/email/made_up_email")

    # THEN
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_get_user_by_username_returns_200_and_json(client, clean_repo):
    # GIVEN
    user_to_save = User(email="api@test.com", username="api_user")
    clean_repo.save(user_to_save)

    # WHEN
    response = client.get(f"/users/username/{user_to_save.username}")

    # THEN
    assert response.status_code == 200
    assert response.json()["username"] == "api_user"


def test_api_returns_404_if_user_not_found_by_username(client, clean_repo):
    # GIVEN

    # WHEN
    response = client.get("/users/username/made_up_username")

    # THEN
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]