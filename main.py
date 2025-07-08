from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 

app = FastAPI()

class Test(BaseModel):
    id: int
    name: str
    origin: str 

tests: List[Test] = []

@app.get("/")
def read_root():
    return {"message" : "Welcome to Test Check!"}

