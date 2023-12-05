from pydantic import BaseModel,EmailStr,constr
from typing import List
from datetime import date
import re

    
class Course(BaseModel):
    id:int
    course_name:str
    description:str
    owner_id:int
    
class Student(BaseModel):
    
    name:str
    date_of_birth: date | None = None
    age:int
    mobile_number:int
    address:str
    class_name:int
    email:EmailStr
    # course: list[str] | None = []
    course:str
    
    class Config:
        orm_mode = True

    
class ShowStudent(BaseModel):

    name:str
    date_of_birth: date | None = None
    age:int
    mobile_number:int
    address:str
    class_name:int
    email:str
    # course:list[str] | None = []
    course:str
    class config:
        orm_mode=True
    


    


    



