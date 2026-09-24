from sqlalchemy.orm import Session
from ..database.session import get_db


class PerformanceService:
    def __init__(self, db: Session):
        self.db = db

    def calculate_student_performance(self, student_id: int) -> dict:
        # TODO: implementar cálculo de desempenho do aluno
        return {"student_id": student_id, "accuracy": 0.0, "total_questions": 0}

    def get_subject_breakdown(self, student_id: int) -> list:
        # TODO: implementar breakdown por matéria
        return []
