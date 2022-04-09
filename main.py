from fastapi import FastAPI
from models import User
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/users")
async def users():
    return {"user_list": ["a", "b"]}


@app.get("/users/{user_id}")
async def users(user_id: int):
    return {"user_details": {user_id: 1}}


@app.post("/create_user")
async def create_user(user: User):
    return user

