from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from pypdf import PdfReader

from app.services.text_chunker import chunk_text
from app.services.vector_store import create_vector_store, search_similar

app = FastAPI()


# Request model
class QuestionRequest(BaseModel):
    question: str


# Load PDF and prepare vector store at startup
BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "data" / "sample.pdf"

reader = PdfReader(PDF_PATH)
text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

chunks = chunk_text(text, chunk_size=200, chunk_overlap=20)
vector_store = create_vector_store(chunks)

@app.get("/")
def home():
    return {"message": "RAG API is running 🚀"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    results = search_similar(vector_store, request.question)

    if results:
        return {
            "question": request.question,
            "answer": results[0].page_content
        }

    return {"answer": "No relevant information found."}