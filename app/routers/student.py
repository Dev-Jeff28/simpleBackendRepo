from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..crud import create_student
from ..crud import delete_student
from ..crud import get_student
from ..crud import get_students
from ..crud import update_student

from ..dependencies import get_db

from ..schemas import StudentCreate
from ..schemas import StudentResponse
from ..schemas import StudentUpdate

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.get("/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db, student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.post("/", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)


@router.put("/{student_id}", response_model=StudentResponse)
def edit_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db),
):
    updated = update_student(db, student_id, student)

    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated


@router.delete("/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    deleted = delete_student(db, student_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}