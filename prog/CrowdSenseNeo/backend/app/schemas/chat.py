from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    answer: str
    intent: str
    risk_level: str
    actions: dict
