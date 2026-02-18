import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are Assistant, a friendly, calm, emoji-aware chatbot.
You help users casually and also guide them during crowd risks.
Never panic the user.
Use simple language and emojis when suitable.
"""

def ai_reply(user_text, chat_history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for msg in chat_history[-10:]:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    messages.append({"role": "user", "content": user_text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.6
    )

    return response["choices"][0]["message"]["content"]