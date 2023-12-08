from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models
import schemas


app=FastAPI()
        
db=SessionLocal()

@app.get('/items/',response_model=List[schemas.Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()
    return items

@app.get('/items/{item_id}',response_model=schemas.Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item not found")
    return item
    

@app.post('/items/',response_model=schemas.Item,status_code=status.HTTP_201_CREATED)
def create_an_item(item:schemas.Item):
    
    # db_item=db.query(models.Item).filter(item.name==item.name).all()
    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
        )
    

    db.add(new_item)
    db.commit()
    
    return new_item

@app.put('/items/{item_id}',response_model=schemas.Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:schemas.Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.description=item.description
    item_to_update.on_offer=item.on_offer
    
    db.commit()
    return item
@app.delete('/items/{item_id}')
def delete_an_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()  
    if item_to_delete is None:
        raise HTTPException(status_code=400,detail="Item not found")
    
    db.delete(item_to_delete)
    db.commit()  
    return item_to_delete
