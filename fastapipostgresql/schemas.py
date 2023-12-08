from pydantic import BaseModel

class Item(BaseModel):        
    # id:int
    name:str
    description:str
    price:int
    on_offer:bool