"""Tests for questions endpoints."""
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_list_questions():
    response = client.get("/questions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_question():
    payload = {"text": "What is 2+2?", "subject": "Math", "grade_level": 5}
    response = client.post("/questions/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "What is 2+2?"
