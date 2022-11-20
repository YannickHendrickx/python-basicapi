# Imports
import requests
from sqlalchemy.orm import Session
import models
import schemas

# get student by provided id
def get_student(db: Session, student_id: int):
    student_by_id = db.query(models.Student).filter(models.Student.id == student_id).first()
    return student_by_id

# get all Students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    all_students = db.query(models.Student).offset(skip).limit(limit).all()
    return all_students

# Add new student
def add_student(db: Session, student: schemas.studentAdd):
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# get all subjects
def get_subject(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Subject).offset(skip).limit(limit).all()

# Add new subject to student
def create_student_subject(db: Session, subject: schemas.studentAdd, student_id: int):
    db_subject = models.Subject(**subject.dict(), owner_id=student_id)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject