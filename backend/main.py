
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import chat

app = FastAPI(
    title="Local AI Assistant",
    description="My locally hosted LLM application",
    version="1.0.0"
)

MODEL_NAME = "qwen3:1.7b"


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Local LLM API is running"}


@app.post("/chat")
def chat_with_llm(request: ChatRequest):
    try:
        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        )

        return {
            "model": MODEL_NAME,
            "question": request.message,
            "response": response.message.content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
