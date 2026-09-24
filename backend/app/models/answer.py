"""Answer model."""
from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.database.base import Base


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    assessment_id = Column(Integer, ForeignKey("assessments.id"), nullable=False)
    selected_option = Column(String, nullable=False)
    is_correct = Column(Integer, default=0)
