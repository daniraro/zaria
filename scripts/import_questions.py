"""Script to import questions from external source."""
import csv
import asyncio
from backend.app.database.session import AsyncSessionLocal
from backend.app.models.question import Question


async def import_questions_from_csv(filepath: str):
    async with AsyncSessionLocal() as session:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                question = Question(
                    text=row['text'],
                    subject=row['subject'],
                    grade_level=int(row['grade_level'])
                )
                session.add(question)
            await session.commit()
        print(f"✅ Imported questions from {filepath}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        asyncio.run(import_questions_from_csv(sys.argv[1]))
    else:
        print("Usage: python import_questions.py <path_to_csv>")
