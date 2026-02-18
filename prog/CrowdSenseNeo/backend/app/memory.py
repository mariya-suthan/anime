# app/memory.py

session_state = {}

def _get_session(session_id: str):
    if session_id not in session_state:
        session_state[session_id] = {
            "mode": "idle",
            "last_intent": "general",
            "history": []
        }
    return session_state[session_id]


def get_chat_mode(session_id: str):
    return _get_session(session_id)["mode"]


def set_chat_mode(session_id: str, mode: str):
    _get_session(session_id)["mode"] = mode


def get_last_intent(session_id: str):
    return _get_session(session_id)["last_intent"]


def set_last_intent(session_id: str, intent: str):
    _get_session(session_id)["last_intent"] = intent


def add_message(session_id: str, role: str, content: str):
    _get_session(session_id)["history"].append({
        "role": role,
        "content": content
    })

    # limit memory (prevents RAM explosion)
    if len(_get_session(session_id)["history"]) > 50:
        _get_session(session_id)["history"] = _get_session(session_id)["history"][-50:]


def get_history(session_id: str):
    return _get_session(session_id)["history"]