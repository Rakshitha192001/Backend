from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str | None = None
    body: str

    
class User(BaseModel):
    id:int
    name:str
    email:str
    password:str


#response model
class ShowBlog(BaseModel):
    title:str
    class Config():
        orm_mode=True
        
