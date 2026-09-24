"""Question repository."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.models.question import Question


class QuestionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, question_id: int) -> Question | None:
        result = await self.session.execute(select(Question).where(Question.id == question_id))
        return result.scalar_one_or_none()

    async def get_by_subject(self, subject: str) -> list[Question]:
        result = await self.session.execute(select(Question).where(Question.subject == subject))
        return result.scalars().all()
