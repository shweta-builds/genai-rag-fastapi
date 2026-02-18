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
    ├── Notes.pdf
│   ├── Report.pdf
    └── simple.pdf
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
- Embeddings integrated (MiniLM)
- FAISS vector store created
- Semantic similarity search working
- `/ask` API endpoint created
- Source tracking for answers added

### Phase 3 – LLM Integration (Next 🚧)
- Connect LLM for answer generation
- Save FAISS index to disk
- Add PDF upload API
- Deploy project

## 🛣️ Roadmap
- [x] Initialize repository and project structure
- [x] Add FastAPI skeleton
- [x] Run FastAPI server locally
- [x] Add document ingestion
- [x] Implement embeddings
- [x] Add retrieval pipeline (FAISS semantic search)
- [ ] Integrate LLM for answer generation
- [ ] Save FAISS index to disk
- [ ] Add API documentation and screenshots
- [ ] Add PDF upload API
- [ ] Deploy project on cloud

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
