from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_create_student():
    response = client.post(
        "/students/",
        json={"name": "Test Student", "email": "test@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Student"
    assert data["email"] == "test@example.com"


def test_list_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_student():
    # Primeiro cria um aluno
    create_response = client.post(
        "/students/",
        json={"name": "Another Student", "email": "another@example.com"}
    )
    student_id = create_response.json()["id"]

    # Depois busca
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
