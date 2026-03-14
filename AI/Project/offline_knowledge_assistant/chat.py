import gradio as gr
import chromadb
from chromadb.utils import embedding_functions
import ollama
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedder & Chroma
embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_collection(name="notes")

def rag_query(query, top_k=3):
    """Retrieval Augmented Generation."""
    # Embed query
    query_emb = embedder.encode([query])
    
    # Retrieve relevant chunks
    results = collection.query(
        query_embeddings=query_emb.tolist(),
        n_results=top_k
    )
    
    context = "\n".join(results['documents'][0])
    
    # Prompt for Llama
    prompt = f"""You are a helpful assistant using my notes. Answer based ONLY on this context:

CONTEXT:
{context}

QUESTION: {query}

ANSWER:"""
    
    # Ollama response
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    return response['message']['content']

# Gradio chat interface
iface = gr.ChatInterface(
    fn=rag_query,
    title="📚 Offline Knowledge Assistant",
    description="Upload PDF notes → chat with your documents (Llama3.2 + ChromaDB)",
    examples=[
        ["What are the key points about Python OOP?"],
        ["Summarize chapter 3"],
        ["Explain decorators with examples"]
    ],
    cache_examples=False
)

if __name__ == "__main__":
    iface.launch()
