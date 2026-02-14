from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "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"

KNOWLEDGE_FILE = "knowledge.txt"

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
        f.write(text)

    return {"message": "uploaded"}

@app.post("/chat")
async def chat(data: dict):
    question = data["message"]

    try:
        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
            context = f.read()
    except:
        context = "No knowledge uploaded."

    prompt = f"Context: {context}\nQuestion: {question}"

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    answer = response.json()["choices"][0]["message"]["content"]

    return {"response": answer}
