from pydantic import BaseModel
from datetime import datetime


class AssessmentBase(BaseModel):
    student_id: int
    question_id: int


class AssessmentCreate(AssessmentBase):
    pass


class AssessmentResponse(AssessmentBase):
    id: int
    answered_at: datetime

    class Config:
        from_attributes = True
