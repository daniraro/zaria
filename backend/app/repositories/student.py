from sqlalchemy.orm import Session
from ..models.student import Student
from ..schemas.student import StudentCreate


class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, student: StudentCreate) -> Student:
        db_student = Student(**student.model_dump())
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def get_by_id(self, student_id: int) -> Student | None:
        return self.db.query(Student).filter(Student.id == student_id).first()

    def list_all(self) -> list:
        return self.db.query(Student).all()

    def update(self, student_id: int, data: dict) -> Student | None:
        student = self.get_by_id(student_id)
        if not student:
            return None
        for key, value in data.items():
            setattr(student, key, value)
        self.db.commit()
        self.db.refresh(student)
        return student

    def delete(self, student_id: int) -> bool:
        student = self.get_by_id(student_id)
        if not student:
            return False
        self.db.delete(student)
        self.db.commit()
        return True
