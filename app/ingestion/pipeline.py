# app/ingestion/pipeline.py

from loader import load_pdfs
from chunker import chunk_documents
from embedder import create_vector_store

def run_ingestion():

    print("Loading PDFs...")
    docs = load_pdfs("data/raw_pdfs")

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print("Creating vector store...")
    create_vector_store(chunks)

    print("Ingestion complete!")

if __name__ == "__main__":
    run_ingestion()
