from fastapi import APIRouter
from pydantic import BaseModel
from app.ai_brain import ai_reply
from app.memory import (
    get_history,
    get_chat_mode,
    set_chat_mode,
    add_message,
)

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    session_id: str


@router.post("/chat")
def chat(req: ChatRequest):
    session_id = req.session_id
    raw_text = req.query.strip()

    print("🔵 USER:", raw_text)

    # 🚀 FORCE CHAT MODE
    set_chat_mode(session_id, "chatting")

    history = get_history(session_id)

    print("🧠 AI CALLED")

    # ✅ ALWAYS CREATE base_answer
    base_answer = ai_reply(raw_text, history)

    print("🤖 AI SAID:", base_answer)

    # save memory
    add_message(session_id, "user", raw_text)
    add_message(session_id, "assistant", base_answer)

    return {
        "answer": base_answer,
        "mode": "chatting"
    }