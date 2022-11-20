# Imports
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subjects = relationship("Subject", back_populates="owner")

class Subject(Base):
    __tablename__ = "Subjects"

    id = Column(Integer, primary_key=True, index=True)
    subjectName = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("Students.id"))

    owner = relationship("Student", back_populates="subjects")