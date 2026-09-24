from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_create_question():
    response = client.post(
        "/questions/",
        json={"text": "Qual a capital do Brasil?", "subject": "Geografia", "difficulty": "fácil"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Qual a capital do Brasil?"
    assert data["subject"] == "Geografia"


def test_list_questions():
    response = client.get("/questions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_question():
    # Primeiro cria uma questão
    create_response = client.post(
        "/questions/",
        json={"text": "Quanto é 2+2?", "subject": "Matemática", "difficulty": "fácil"}
    )
    question_id = create_response.json()["id"]

    # Depois busca
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    assert response.json()["id"] == question_id
