from fastapi import FastAPI

app = FastAPI(title="GenAI RAG Backend")

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
def ask_question(question: str):
    return {
        "question": question,
        "answer": "This is a placeholder answer. LLM will come later."
    }
