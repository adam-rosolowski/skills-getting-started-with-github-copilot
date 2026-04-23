def test_get_activities(client):
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity(client):
    response = client.post("/activities/Chess%20Club/signup?email=test@example.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@example.com for Chess Club"

def test_unregister_activity(client):
    response = client.delete("/activities/Chess%20Club/unregister?email=test@example.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered test@example.com from Chess Club"