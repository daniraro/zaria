from sqlalchemy.orm import Session
from ..models.answer import Answer
from ..schemas.answer import AnswerCreate


class AnswerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, answer: AnswerCreate) -> Answer:
        db_answer = Answer(**answer.model_dump())
        self.db.add(db_answer)
        self.db.commit()
        self.db.refresh(db_answer)
        return db_answer

    def get_by_id(self, answer_id: int) -> Answer | None:
        return self.db.query(Answer).filter(Answer.id == answer_id).first()

    def list_all(self) -> list:
        return self.db.query(Answer).all()
