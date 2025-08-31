from fastapi import FastAPI, Query, Path, Body
import asyncio
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def foo():
    return "hello first page"

class User(BaseModel):
    id : int
    name : str
    age : int

@app.post("/user/")
def getname(user : User):
    return "received"
