from database import Base
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,text

class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    content=Column(String)
    published=Column(Boolean, server_default='TRUE')
    created_at=Column(TIMESTAMP(timezone=True), server_default=text('now()'))