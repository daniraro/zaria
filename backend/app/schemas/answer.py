from pydantic import BaseModel


class AnswerBase(BaseModel):
    assessment_id: int
    text: str
    is_correct: bool = False


class AnswerCreate(AnswerBase):
    pass


class AnswerResponse(AnswerBase):
    id: int

    class Config:
        from_attributes = True
