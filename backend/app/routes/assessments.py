from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.assessment import AssessmentCreate, AssessmentResponse
from ..database.session import get_db
from ..repositories.assessment import AssessmentRepository

router = APIRouter(prefix="/assessments", tags=["assessments"])


@router.post("/", response_model=AssessmentResponse)
async def create_assessment(assessment: AssessmentCreate, db: Session = Depends(get_db)):
    repo = AssessmentRepository(db)
    return repo.create(assessment)


@router.get("/", response_model=list[AssessmentResponse])
async def list_assessments(db: Session = Depends(get_db)):
    repo = AssessmentRepository(db)
    return repo.list_all()


@router.get("/{assessment_id}", response_model=AssessmentResponse)
async def get_assessment(assessment_id: int, db: Session = Depends(get_db)):
    repo = AssessmentRepository(db)
    assessment = repo.get_by_id(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessment
