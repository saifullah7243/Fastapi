from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'Hello welcome to my fastapi'}

# Simple route
@app.get("/home")
def home():
    return {'message': 'Home'}

# ✅ Path Parameter
@app.get("/home/{name}")
def get_name(name: str):
    return {'message': name}

# ✅ Query Parameter
@app.get("/search")
def search(query: str, price: Optional[int] = None):
    return {'message': query, 'price': price}
# Post MEthis
class Student(BaseModel):
    name:str
    age:int
    course:str

@app.post("/student")
def create_student(student:Student):
    return {
        "name": student.name,
        "age": student.age,
        "course": student.course
    }
