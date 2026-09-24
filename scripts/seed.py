#!/usr/bin/env python3
"""Script para popular o banco com dados iniciais."""

import sys
from pathlib import Path

# Adiciona o backend ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from app.database.connection import engine
from app.database.base import Base
from app.models.student import Student
from app.models.question import Question
from app.models.assessment import Assessment
from app.models.answer import Answer
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


def run_seeds():
    # Cria as tabelas
    Base.metadata.create_all(engine)

    db = Session()

    # Seeds de alunos
    students = [
        Student(name="Ana Silva", email="ana@example.com"),
        Student(name="Bruno Santos", email="bruno@example.com"),
        Student(name="Carla Oliveira", email="carla@example.com"),
    ]
    db.add_all(students)

    # Seeds de questões
    questions = [
        Question(text="Qual a capital do Brasil?", subject="Geografia", difficulty="fácil"),
        Question(text="Quanto é 2 + 2?", subject="Matemática", difficulty="fácil"),
        Question(text="Quem descobriu o Brasil?", subject="História", difficulty="médio"),
        Question(text="Qual a fórmula da água?", subject="Química", difficulty="fácil"),
        Question(text="Qual o planeta mais próximo do Sol?", subject="Astronomia", difficulty="médio"),
    ]
    db.add_all(questions)

    db.commit()
    print("Seeds aplicadas com sucesso!")
    db.close()


if __name__ == "__main__":
    run_seeds()
