from pathlib import Path

def load_documents():
    knowledge_path = Path("app/knowledge")
    docs = []

    for file in knowledge_path.glob("*.txt"):
        content = file.read_text(encoding="utf-8")
        docs.append(content)

    return docs