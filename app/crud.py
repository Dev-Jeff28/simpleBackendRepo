from sqlalchemy.orm import Session

from .models import Student
from .schemas import StudentCreate
from .schemas import StudentUpdate


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.model_dump())

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student


def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    for key, value in student.model_dump().items():
        setattr(db_student, key, value)

    db.commit()

    db.refresh(db_student)

    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)

    db.commit()

    return db_student