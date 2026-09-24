from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.question import QuestionCreate, QuestionResponse
from ..database.session import get_db
from ..repositories.question import QuestionRepository

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/", response_model=QuestionResponse)
async def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    repo = QuestionRepository(db)
    return repo.create(question)


@router.get("/", response_model=list[QuestionResponse])
async def list_questions(db: Session = Depends(get_db)):
    repo = QuestionRepository(db)
    return repo.list_all()


@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int, db: Session = Depends(get_db)):
    repo = QuestionRepository(db)
    question = repo.get_by_id(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question
