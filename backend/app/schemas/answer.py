"""Answer schemas."""
from pydantic import BaseModel


class AnswerBase(BaseModel):
    question_id: int
    assessment_id: int
    selected_option: str
    is_correct: bool = False


class AnswerCreate(AnswerBase):
    pass


class AnswerResponse(AnswerBase):
    id: int

    class Config:
        from_attributes = True
