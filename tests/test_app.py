from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_signup_and_unregister_participant():
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    assert email in activities_response.json()[activity_name]["participants"]

    delete_response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )
    assert delete_response.status_code == 200

    updated_response = client.get("/activities")
    assert updated_response.status_code == 200
    assert email not in updated_response.json()[activity_name]["participants"]
