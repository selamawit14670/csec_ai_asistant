from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from models import users_db

router = APIRouter()

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    email: str
    password: str

def create_token(data: dict):
    data["exp"] = datetime.utcnow() + timedelta(hours=2)
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/signup")
def signup(user: User):

    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = pwd_context.hash(user.password)
    users_db[user.email] = hashed_password

    return {"message": "Signup successful"}

@router.post("/login")
def login(user: User):

    if user.email not in users_db:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(user.password, users_db[user.email]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user": user.email})

    return {"token": token}
