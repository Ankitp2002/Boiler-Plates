import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./agent_memory")

def add_to_memory(content, session_id="default"):
    """Store conversation/research to memory."""
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_or_create_collection(name=f"session_{session_id}", embedding_function=ef)
    collection.add(documents=[content], ids=[f"mem_{len(collection.get())}"])

def retrieve_memory(query, session_id="default", n_results=5):
    """Retrieve relevant memory."""
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_collection(name=f"session_{session_id}")
    results = collection.query(query_texts=[query], n_results=n_results)
    return results['documents'][0] if results['documents'] else []
