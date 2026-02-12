from fastapi import FastAPI

app = FastAPI(title="GenAI RAG Backend")

@app.get("/")
def hello():
    return {"message": "Hello! My backend is running🚀"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/ask")
def ask_question(question: str):
    return {
        "question": question,
        "answer": f"You asked: {question}. AI 🤖 logic will be added soon."
    }