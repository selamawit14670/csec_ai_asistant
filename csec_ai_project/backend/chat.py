from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    message:str

@router.post("/chat")
async def chat(msg:Message):

    return {
        "response":
        "Hello! We provide web development and AI chatbot solutions for businesses."
    }
