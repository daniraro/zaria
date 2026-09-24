#!/usr/bin/env python3
"""Script para importar questões de um arquivo CSV."""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from app.database.connection import engine
from app.database.base import Base
from app.models.question import Question
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


def import_questions(csv_path: str):
    Base.metadata.create_all(engine)
    db = Session()

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            question = Question(
                text=row["text"],
                subject=row["subject"],
                difficulty=row["difficulty"]
            )
            db.add(question)

    db.commit()
    print(f"Questões importadas de {csv_path}!")
    db.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python import_questions.py <arquivo.csv>")
        sys.exit(1)
    import_questions(sys.argv[1])
