"""Student repository."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.models.student import Student


class StudentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, student_id: int) -> Student | None:
        result = await self.session.execute(select(Student).where(Student.id == student_id))
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Student | None:
        result = await self.session.execute(select(Student).where(Student.email == email))
        return result.scalar_one_or_none()

    async def create(self, name: str, email: str) -> Student:
        student = Student(name=name, email=email)
        self.session.add(student)
        await self.session.commit()
        await self.session.refresh(student)
        return student
