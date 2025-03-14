# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from run_conversation import run_conversation

app = FastAPI()

# CORS to allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    model: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        reply = run_conversation(request.prompt)
        return {"reply": str(reply)}
    except Exception as e:
        return {"reply": f"❌ Error occurred: {str(e)}"}
