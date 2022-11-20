# Imports
from pydantic import BaseModel

# Subject schemas
class SubjectBase(BaseModel):
    subjectName: str


class SubjectAdd(SubjectBase):
    pass


class Subject(SubjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Student schemas
class studentBase(BaseModel):
    name: str

class studentAdd(studentBase):
    pass

class student(studentBase):
    id: int
    items: list[Subject] = []

    class Config:
        orm_mode = True