"""Integration tests for API."""
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_students_crud():
    payload = {"name": "Test Student", "email": "test@example.com"}
    response = client.post("/students/", json=payload)
    assert response.status_code == 200
    student_id = response.json()["id"]
    
    response = client.get("/students/")
    assert response.status_code == 200
    assert len(response.json()) > 0
