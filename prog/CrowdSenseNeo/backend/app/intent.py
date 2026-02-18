def detect_intent(message: str):
    msg = message.lower()

    if any(word in msg for word in [
        "panic", "scared", "afraid", "crowd", "stampede", "help me", "danger"
    ]):
        return "danger"

    if any(word in msg for word in ["law", "ipc", "legal", "rights", "police"]):
        return "law"

    if any(word in msg for word in ["help", "what should i do", "guide"]):
        return "safety"

    return "general"