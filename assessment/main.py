

from fastapi import FastAPI, Depends, Response, HTTPException,status
from fastapi.exceptions import ResponseValidationError
from sqlalchemy import and_
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from . import operations

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.post('/student/', status_code=200)
def create(req: schemas.Student, db: Session = Depends(get_db)):
    try:

        return operations.create_student(db=db,student_data=req)
    except Exception as e:
        raise HTTPException(status_code=404,detail=f"{str}")
        

@app.get('/student/{id}', status_code=200, response_model=schemas.ShowStudent)
def show(id, response: Response, db: Session = Depends(get_db)):
    try:
        student = db.query(models.Student).filter(models.Student.id == id).first()
        if not student:
            raise HTTPException(status_code=404, detail=f"No students found with id {id}")
        return student
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No students found with id {id}")
        

# @app.get("/students/", response_model=List[schemas.Student] ,status_code=status.HTTP_200_OK)
# def read_all_students(db: Session = Depends(get_db)):
#     try:
#         datas = db.query(models.Student).all()
#         return datas
#         # operations.get_all_students(db)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=f"{str(e)}")
    
@app.get('/student/')
def all(db: Session = Depends(get_db)):
    try:
        students = db.query(models.Student).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Internal Server Error: {str(e)}")
        


@app.put('/student/{id}', status_code=202)
def update(id, request: schemas.Student, db: Session = Depends(get_db)):
    try:
        student = db.query(models.Student).filter(models.Student.id == id)
        if not student.first():
            raise HTTPException(status_code=404, detail=f"No students found with id {id}")

        student.update(request.dict())
        db.commit()
        return request
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No students found with id {id}")


@app.delete('/student/{id}')
def delete(id, db: Session = Depends(get_db)):
    try:
        db_student = db.query(models.Student).filter(models.Student.id == id).first()
        if not db_student:
            raise HTTPException(status_code=404, detail=f"No students found with id {id}")
        db.delete(db_student)
        db.commit()
        return {"successfully deleted student": db_student}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No students found with id {id}")


@app.get('/students/mobileOrEmail', status_code=200,response_model=schemas.Student)
def mob_and_email(mobile_number:int|None=None, email:str|None=None, db: Session = Depends(get_db)):

        if email is None:
            student = db.query(models.Student).filter((models.Student.mobile_number == mobile_number)).first()
        elif mobile_number is None:
            student = db.query(models.Student).filter((models.Student.email == email)).first()  
        else:
            student = db.query(models.Student).filter(and_(models.Student.mobile_number == mobile_number , models.Student.email == email)).first()
        if student is None:
            raise HTTPException(status_code=406 , detail=f"no students found with {mobile_number} and {email} ")
        else :
            return student


@app.get('/studentage/{age}', status_code=200, response_model=List[schemas.ShowStudent])
def student_age(age: int, db: Session = Depends(get_db)):
    try:
        students = db.query(models.Student).filter(models.Student.age == age).all()
        if not students:
            raise HTTPException(status_code=404, detail=f"No students found with age {age}")
        return students
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No students found with age {age}")


@app.get('/studentcourse/{course}', status_code=200, response_model=List[schemas.ShowStudent])
def student_course(course, db: Session = Depends(get_db)):
    try:
        student = db.query(models.Student).filter(models.Student.course == course).all()
        if not student:
            raise HTTPException(status_code=404, detail=f"No students found for course {course}")
        return student
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No students found for course {course}")


@app.post('/course/', status_code=200)
def add_course(request: schemas.Course, db: Session = Depends(get_db)):
    try:
        course = models.Course(course_name=request.course_name, description=request.description,
                               owner_id=request.owner_id)
        db.add(course)
        db.commit()
        db.refresh(course)
        return course
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{str(e)}")





