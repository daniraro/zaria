import httpx

BASE_URL = "http://localhost:8000"


def get_students():
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/students/")
        response.raise_for_status()
        return response.json()


def get_questions():
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/questions/")
        response.raise_for_status()
        return response.json()


def create_assessment(student_id: int, question_id: int):
    with httpx.Client() as client:
        response = client.post(
            f"{BASE_URL}/assessments/",
            json={"student_id": student_id, "question_id": question_id}
        )
        response.raise_for_status()
        return response.json()
