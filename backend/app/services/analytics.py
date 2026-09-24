from sqlalchemy.orm import Session


class AnalyticsService:
    def __init__(self, db: Session):
        self.db = db

    def get_general_stats(self) -> dict:
        # TODO: implementar estatísticas gerais
        return {"total_students": 0, "total_questions": 0, "total_assessments": 0}

    def get_difficulty_distribution(self) -> dict:
        # TODO: implementar distribuição por dificuldade
        return {"fácil": 0, "médio": 0, "difícil": 0}
