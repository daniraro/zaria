"""Assessments routes."""
from fastapi import APIRouter
from backend.app.schemas.assessment import AssessmentCreate, AssessmentResponse

router = APIRouter(prefix="/assessments", tags=["assessments"])


@router.get("/", response_model=list[AssessmentResponse])
async def list_assessments():
    return []


@router.post("/", response_model=AssessmentResponse)
async def create_assessment(assessment: AssessmentCreate):
    return assessment
