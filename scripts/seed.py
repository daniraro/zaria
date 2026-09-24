"""Seed script to populate database."""
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from backend.app.config import settings
from backend.app.database.base import Base
from backend.app.models.student import Student
from backend.app.models.question import Question


async def seed():
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    
    async with AsyncSessionLocal() as session:
        students = [
            Student(name="Ana Silva", email="ana@example.com"),
            Student(name="Bruno Santos", email="bruno@example.com"),
            Student(name="Carla Oliveira", email="carla@example.com"),
        ]
        session.add_all(students)
        
        questions = [
            Question(text="Quanto é 2 + 2?", subject="Matemática", grade_level=5),
            Question(text="Qual a capital do Brasil?", subject="Geografia", grade_level=5),
            Question(text="Quem descobriu o Brasil?", subject="História", grade_level=5),
            Question(text="Qual o plural de 'cão'?", subject="Português", grade_level=5),
        ]
        session.add_all(questions)
        
        await session.commit()
        print("✅ Database seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed())
