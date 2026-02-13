from pathlib import Path
from pypdf import PdfReader

from app.services.text_chunker import chunk_text
from app.services.vector_store import create_vector_store, search_similar


# Locate project root
BASE_DIR = Path(__file__).resolve().parents[1]
PDF_PATH = BASE_DIR / "data" / "simple.pdf"

# Read PDF
reader = PdfReader(PDF_PATH)
text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

# Chunk
chunks = chunk_text(text, chunk_size=200, chunk_overlap=20)

print(f"Total chunks: {len(chunks)}")

# Create vector store
vector_store = create_vector_store(chunks)

# Test query
query = "What is this document about?"
results = search_similar(vector_store, query)

print("\nSemantic Search Results:\n")
for r in results:
    print(r.page_content)
    print("-" * 40)
