from fastapi import FastAPI

app = FastAPI(title="GenAI RAG Backend")

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
