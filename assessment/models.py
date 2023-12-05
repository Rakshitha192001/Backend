
from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Date
from sqlalchemy.orm import relationship
import datetime
from typing import List
import re
 
class Student(Base):
    __tablename__="Student"
    id=Column(Integer,primary_key=True,index=True,unique=True)
    name=Column(String)
    date_of_birth=Column(Date)
    age=Column(Integer)
    mobile_number=Column(Integer,unique=True)
    address=Column(String)
    class_name=Column(Integer)
    email=Column(String,unique=True,nullable=False)
    course=Column(String)
    
    # student = relationship("Course", back_populates="owner")
    
    courses = relationship("Course", back_populates="student")



class Course(Base):
    __tablename__="Course"
    id=Column(Integer,primary_key=True)
    course_name=Column(String,unique=True)
    description=Column(String)
    
    # owner_id = Column(Integer, ForeignKey("Student.id"))
    # owner=relationship("Student",back_populates="student")
    owner_id = Column(Integer, ForeignKey("Student.id"))
    student = relationship("Student", back_populates="courses")


