from sqlalchemy.orm import Session
from ..models.question import Question
from ..schemas.question import QuestionCreate


class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, question: QuestionCreate) -> Question:
        db_question = Question(**question.model_dump())
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)
        return db_question

    def get_by_id(self, question_id: int) -> Question | None:
        return self.db.query(Question).filter(Question.id == question_id).first()

    def list_all(self) -> list:
        return self.db.query(Question).all()

    def update(self, question_id: int, data: dict) -> Question | None:
        question = self.get_by_id(question_id)
        if not question:
            return None
        for key, value in data.items():
            setattr(question, key, value)
        self.db.commit()
        self.db.refresh(question)
        return question

    def delete(self, question_id: int) -> bool:
        question = self.get_by_id(question_id)
        if not question:
            return False
        self.db.delete(question)
        self.db.commit()
        return True
