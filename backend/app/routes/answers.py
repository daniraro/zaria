"""Answers routes."""
from fastapi import APIRouter
from backend.app.schemas.answer import AnswerCreate, AnswerResponse

router = APIRouter(prefix="/answers", tags=["answers"])


@router.get("/", response_model=list[AnswerResponse])
async def list_answers():
    return []


@router.post("/", response_model=AnswerResponse)
async def create_answer(answer: AnswerCreate):
    return answer
