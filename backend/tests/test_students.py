"""Tests for students endpoints."""
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_list_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_student():
    payload = {"name": "Test Student", "email": "test@example.com"}
    response = client.post("/students/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Student"
