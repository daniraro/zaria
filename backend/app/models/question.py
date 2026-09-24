from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    subject = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)  # fácil, médio, difícil

    assessments = relationship("Assessment", back_populates="questions")
