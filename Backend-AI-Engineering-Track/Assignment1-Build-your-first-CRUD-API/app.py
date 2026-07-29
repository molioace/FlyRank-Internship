from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    exp: int
    name: str


users = {}


@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{id}")
def get_user(id: int):
    if id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[id]


@app.post("/users/{id}")
def add_user(id: int, user: User):
    users[id] = user
    return users[id]


@app.put("/users/{id}")
def update_user(id: int, user: User):
    if id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[id] = user
    return users[id]