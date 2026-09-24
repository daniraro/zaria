"""Question model."""
from sqlalchemy import Column, Integer, String, Text
from backend.app.database.base import Base


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    subject = Column(String, nullable=False)
    grade_level = Column(Integer, nullable=False)
