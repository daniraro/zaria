from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_students_flow():
    # Cria aluno
    create_response = client.post(
        "/students/",
        json={"name": "Test Student", "email": "test@example.com"}
    )
    assert create_response.status_code == 200
    student_id = create_response.json()["id"]

    # Lista alunos
    list_response = client.get("/students/")
    assert list_response.status_code == 200
    assert any(s["id"] == student_id for s in list_response.json())

    # Busca aluno
    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == student_id


def test_questions_flow():
    # Cria questão
    create_response = client.post(
        "/questions/",
        json={"text": "Test question", "subject": "Test", "difficulty": "fácil"}
    )
    assert create_response.status_code == 200
    question_id = create_response.json()["id"]

    # Lista questões
    list_response = client.get("/questions/")
    assert list_response.status_code == 200
    assert any(q["id"] == question_id for q in list_response.json())
