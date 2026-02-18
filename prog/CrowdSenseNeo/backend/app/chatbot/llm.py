import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_answer(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast + cheap
        messages=[
            {"role": "system", "content": "You are a kind, calm, supportive safety assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()