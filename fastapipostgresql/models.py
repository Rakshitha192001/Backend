from database import Base
from sqlalchemy import Column,String,Boolean, Integer


class Item(Base):
    __tablename__="items"
    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)
    description=Column(String)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)
    
    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
        