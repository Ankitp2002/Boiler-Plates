import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import os

# Embedder (all-MiniLM-L6-v2, fast/local)
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_pdf(pdf_path, chunk_size=500, overlap=50):
    """Extract text, chunk into sentences."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    # Simple chunking
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def ingest_pdf(pdf_path):
    """Create Chroma collection."""
    chunks = chunk_pdf(pdf_path)
    embeddings = embedder.encode(chunks)
    
    client = chromadb.PersistentClient(path="./chroma_db")
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    collection = client.get_or_create_collection(
        name="notes",
        embedding_function=ef
    )
    
    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    print(f"✅ Ingested {len(chunks)} chunks from {pdf_path}")

if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "notes.pdf"
    ingest_pdf(pdf_path)
