from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.student import StudentCreate, StudentResponse
from ..database.session import get_db
from ..repositories.student import StudentRepository

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    repo = StudentRepository(db)
    return repo.create(student)


@router.get("/", response_model=list[StudentResponse])
async def list_students(db: Session = Depends(get_db)):
    repo = StudentRepository(db)
    return repo.list_all()


@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    repo = StudentRepository(db)
    student = repo.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
