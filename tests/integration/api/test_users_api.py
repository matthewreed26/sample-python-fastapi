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