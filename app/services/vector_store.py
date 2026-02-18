from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

def create_vector_store(chunks_with_sources):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    docs = [
        Document(page_content=chunk, metadata={"source": source})
        for chunk, source in chunks_with_sources
    ]

    vector_store = FAISS.from_documents(docs, embeddings)

    return vector_store


def search_similar(vector_store, query: str, k: int = 2):
    results = vector_store.similarity_search(query, k=k)
    return results
