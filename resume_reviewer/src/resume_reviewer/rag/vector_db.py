from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from .embedder import get_embedder

def build_vector_db(docs: list[str]) -> FAISS:
    # Convert list of strings into LangChain Documents
    documents = [Document(page_content=doc) for doc in docs]
    embedder = get_embedder()
    return FAISS.from_documents(documents, embedder)
