from sqlalchemy.orm import Session


class DiagnosisService:
    def __init__(self, db: Session):
        self.db = db

    def diagnose_student(self, student_id: int) -> dict:
        # TODO: implementar diagnóstico do aluno
        return {"student_id": student_id, "weaknesses": [], "strengths": []}

    def recommend_questions(self, student_id: int, limit: int = 10) -> list:
        # TODO: implementar recomendação de questões
        return []
