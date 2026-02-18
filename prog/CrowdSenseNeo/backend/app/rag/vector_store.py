from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document
import os

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load knowledge files
def load_knowledge():
    docs = []
    base_path = os.path.join(os.path.dirname(__file__), "..", "knowledge")

    for file in os.listdir(base_path):
        if file.endswith(".txt"):
            with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
                docs.append(Document(page_content=f.read()))
    return docs


# Build vector store (once)
documents = load_knowledge()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(chunks, embeddings)


def retrieve_context(query: str, k: int = 3) -> str:
    results = vectorstore.similarity_search(query, k=k)
    return "\n".join(doc.page_content for doc in results)