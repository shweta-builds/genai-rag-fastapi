from pathlib import Path
from pypdf import PdfReader

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
PDF_PATH = DATA_DIR / "sample.pdf"

print("PDF EXISTS:", PDF_PATH.exists())

if not PDF_PATH.exists():
    raise FileNotFoundError("PDF not found")

reader = PdfReader(PDF_PATH)

text = ""
for page in reader.pages:
    text += page.extract_text()

print("\n--- PDF CONTENT START ---\n")
print(text[:500])
print("\n--- PDF CONTENT END ---\n")
