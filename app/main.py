#!/usr/bin/python3

#Imports
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import os
import crud, models, schemas
from database import SessionLocal, engine

# ----------------
#  Basic API assignment
# ----------------
# Yannick Hendrickx
# r0615765

# make database dir if it doesn't exist
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# create tables in database 'sqlitedata.db' (check datapase.py database-URL)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# make database session/connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# allowed origins for CORS
origins = ["*"]

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

# get all students
@app.get("/students/all", response_model=list[schemas.student])
async def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

# Get specific student
@app.get("/students/{student_id}", response_model=schemas.student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return db_student

# Add new student
@app.post("/students/", response_model=schemas.student)
async def add_student(student: schemas.studentAdd, db: Session = Depends(get_db)):
    add_student = crud.add_student(db=db, student=student)
    return add_student

# Add a new subject to  specific student
@app.post("/students/{student_id}/subjects/", response_model=schemas.Subject)
def create_student_subject(
    student_id: int, subject: schemas.SubjectAdd, db: Session = Depends(get_db)
):
    return crud.create_student_subject(db=db, subject=subject, student_id=student_id)

# Get all subjects
@app.get("/subjects/", response_model=list[schemas.Subject])
def read_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subjects = crud.get_subject(db, skip=skip, limit=limit)
    return subjects