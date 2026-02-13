# GenAI RAG Backend (FastAPI)

## 📌 Overview
This project is a backend service built using FastAPI.  
It will gradually evolve into a **GenAI RAG (Retrieval-Augmented Generation)** system that can answer questions from documents.

## 🛠 Tech Stack (Planned)
- Python
- FastAPI
- LangChain
- Vector Database (FAISS / Chroma)
- LLM (OpenAI / Llama)

## 📂 Project Structure
```bash
genai-rag-fastapi/
│
├── app/
│   ├── services/
│   │   ├── pdf_reader.py
│   │   ├── document_loader.py
│   │   ├── text_chunker.py
│   │   ├── vector_store.py
│   │
│   ├── main.py
│   └── test_semantic_search.py
│
├── data/
│   └── simple.pdf
│
├── requirements.txt
└── README.md
```

## 📅 Learning Goal
Build a production-style GenAI backend while learning step-by-step.

## 🚀Project Status

### Phase 0 – Backend Setup ✅
- Python virtual environment setup
- FastAPI backend initialized
- Health check endpoint
- Mock AI question endpoint

### Phase 1 – Document Processing ✅
- PDF ingestion completed
- Text extraction working
- Recursive text chunking implemented
- Sample PDF tested successfully
- Project structured for RAG pipeline

### Phase 2 – Vector Search ✅
- Embedding model integrated (MiniLM)
- FAISS vector store created
- Semantic similarity search working

## 🛣️ Roadmap
- [x] Initialize repository and project structure
- [x] Add FastAPI skeleton
- [x] Run FastAPI server locally
- [x] Add document ingestion
- [ ] Implement embeddings
- [ ] Add retrieval pipeline
- [ ] Integrate LLM for answer generation
- [ ] Add API documentation and screenshots

## ▶️ How to Run
1. Clone the repository

   git clone https://github.com/your-username/genai-rag-fastapi.git
   cd genai-rag-fastapi

2. Create virtual environment

   python -m venv venv

3. Activate virtual environment

   On Windows:
   venv\Scripts\activate

   On Mac/Linux:
   source venv/bin/activate

4. Install dependencies

   pip install -r requirements.txt

5. Run FastAPI server

   uvicorn app.main:app --reload

6. Open in browser

   http://127.0.0.1:8000/docs
