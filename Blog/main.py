
from fastapi import FastAPI, Depends, Response, HTTPException
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=204)
def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404,detail="Not found")
    
    blog.delete()
    db.commit()
    return Response(status_code=204)

@app.put('/blog/{id}', status_code=202)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404,detail="Not found")
    
    blog.update(request.dict())  # Update the blog using the dictionary representation of the request
    db.commit()
    return {'message': 'updated successfully'}

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,detail="Not found")
    return blog


# pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

@app.post('/user', status_code=201)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashedPassword=pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# users=[]
# @app.post("/user",tags=["user"])
# def user_signup(user:schemas.User,db: Session = Depends(get_db)):
#     # hashedPassword=pwd_cxt.hash(request.password)
#     users.append(user)
#     db.add(users)
#     db.commit()
#     db.refresh(users)
    
#     return users