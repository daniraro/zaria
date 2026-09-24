"""Assessment schemas."""
from pydantic import BaseModel
from datetime import datetime


class AssessmentBase(BaseModel):
    title: str
    student_id: int


class AssessmentCreate(AssessmentBase):
    pass


class AssessmentResponse(AssessmentBase):
    id: int
    completed_at: datetime

    class Config:
        from_attributes = True
