from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# -----------------------------
# Initialize once (GLOBAL)
# -----------------------------

docs = [
    "Crowd density above 5 people per square meter is dangerous",
    "Emergency exits must always remain accessible",
    "In panic situations, avoid pushing and move sideways",
    "Women safety systems must support SOS alerts"
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_texts(docs, embeddings)

llm = Ollama(model="llama3")

# -----------------------------
# Function used by /chat route
# -----------------------------

def get_rag_response(query: str):
    results = db.similarity_search(query, k=2)
    context = "\n".join([r.page_content for r in results])

    prompt = f"""
Answer clearly using ONLY the context below.

Context:
{context}

Question:
{query}
"""

    answer = str(llm(prompt))

    return answer
    