from fastapi import FastAPI
import posts
import models
from database import engine

app=FastAPI()
app.include_router(posts.router)

models.Base.metadata.create_all(bind=engine)
