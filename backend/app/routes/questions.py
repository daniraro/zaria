"""Questions routes."""
from fastapi import APIRouter
from backend.app.schemas.question import QuestionCreate, QuestionResponse

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=list[QuestionResponse])
async def list_questions():
    return []


@router.post("/", response_model=QuestionResponse)
async def create_question(question: QuestionCreate):
    return question
