from sqlalchemy.orm import Session
from ..models.assessment import Assessment
from ..schemas.assessment import AssessmentCreate


class AssessmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, assessment: AssessmentCreate) -> Assessment:
        db_assessment = Assessment(**assessment.model_dump())
        self.db.add(db_assessment)
        self.db.commit()
        self.db.refresh(db_assessment)
        return db_assessment

    def get_by_id(self, assessment_id: int) -> Assessment | None:
        return self.db.query(Assessment).filter(Assessment.id == assessment_id).first()

    def list_all(self) -> list:
        return self.db.query(Assessment).all()
