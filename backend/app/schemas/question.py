"""Question schemas."""
from pydantic import BaseModel


class QuestionBase(BaseModel):
    text: str
    subject: str
    grade_level: int


class QuestionCreate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: int

    class Config:
        from_attributes = True
