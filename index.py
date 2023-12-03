#csv with generators
import csv

def csv_reader(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row

# Example usage
file_path = 'example.csv'
for data_row in csv_reader(file_path):
    print(data_row)
    
#xml to json
import json
import xmltodict

# Read XML from file
with open('your_xml_file.xml', 'r') as xml_file:
    xml_content = xml_file.read()

# Convert XML to JSON
json_data = json.dumps(xmltodict.parse(xml_content), indent=2)

# Save JSON to file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

# Fetch specific key-value pairs (example: CREATION_DATE)
parsed_json = json.loads(json_data)
creation_date = parsed_json.get('root_element_name', {}).get('CREATION_DATE', None)

print(f'CREATION_DATE: {creation_date}')

#creating json file
import json

# Sample JSON data
json_data = {
    "productOrder": {
        "relatedContactInformation": {
            "buyerContactInfo": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "123-456-7890"
            }
        },
        "state": "pending"
    }
}

# Update related contact information with your details
json_data["productOrder"]["relatedContactInformation"]["buyerContactInfo"] = {
    "name": "Your Name",
    "email": "your.email@example.com",
    "phone": "987-654-3210"
}

# Change the status to "updated"
json_data["productOrder"]["state"] = "updated"

# Add more information and set the state to "cancelled"
json_data["productOrder"]["moreInformation"] = "Additional details"
json_data["productOrder"]["state"] = "cancelled"

# Save the modified data to a JSON file
with open("modified_data.json", "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print("JSON data updated and saved to 'modified_data.json'.")

#CRUD operation
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime

# SQLAlchemy Setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model
class Task(Base):
    _tablename_ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_completed = Column(Boolean, default=False)

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI Setup
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations

# Create Task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task, db: Session = Depends(get_db)):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Read Task
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update Task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update only provided fields
    for field, value in updated_task.dict().items():
        setattr(task, field, value)
    
    db.commit()
    db.refresh(task)
    return task

# Delete Task
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return task
    