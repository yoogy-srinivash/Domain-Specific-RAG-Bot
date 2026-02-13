# app/ingestion/chunker.py

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=120,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = text_splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i

    return chunks
