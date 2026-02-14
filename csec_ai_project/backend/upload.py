from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

@router.post("/upload")
async def upload(file:UploadFile = File(...)):

    os.makedirs("data",exist_ok=True)

    path=f"data/{file.filename}"

    with open(path,"wb") as f:
        f.write(await file.read())

    return {"message":"file uploaded"}
