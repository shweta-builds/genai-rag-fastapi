from services.document_loader import load_and_split_pdf

chunks = load_and_split_pdf("data/sample.pdf")
print(len(chunks))
print(chunks[0].page_content)
