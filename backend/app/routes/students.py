"""Students routes."""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.session import get_session
from backend.app.schemas.student import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=list[StudentResponse])
async def list_students(session: AsyncSession = Depends(get_session)):
    return []


@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate, session: AsyncSession = Depends(get_session)):
    return student
