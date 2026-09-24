from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.answer import AnswerCreate, AnswerResponse
from ..database.session import get_db
from ..repositories.answer import AnswerRepository

router = APIRouter(prefix="/answers", tags=["answers"])


@router.post("/", response_model=AnswerResponse)
async def create_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    repo = AnswerRepository(db)
    return repo.create(answer)


@router.get("/", response_model=list[AnswerResponse])
async def list_answers(db: Session = Depends(get_db)):
    repo = AnswerRepository(db)
    return repo.list_all()


@router.get("/{answer_id}", response_model=AnswerResponse)
async def get_answer(answer_id: int, db: Session = Depends(get_db)):
    repo = AnswerRepository(db)
    answer = repo.get_by_id(answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer
