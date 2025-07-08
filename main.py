from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 

app = FastAPI()

class Test(BaseModel):
    id: int
    name: str
    origin: str 

res: List[Test] = [] # changed List Name to 'res'

@app.get("/")
def read_root():
    return {"message" : "Welcome to Test Check!"}

# CRUD 

@app.get("/get_results")
def get_results():
    return res

@app.post("/results")
def add_tests(test: Test):
    res.append(test)
    return test 

@app.put("/tests/{test_id}")
def update_test(test_id: int, updated_test: Test): 
    for index, test in enumerate(res):
        if test.id == test_id:
            res[index] = update_test
            return update_test
    return {"error" : "Test not Found!"}


@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    for index, test in enumerate(res):
        if test.id == test_id:
            test_deleted = res.pop(index)
            return test_deleted
    return {"Error" : "Test not found!"}