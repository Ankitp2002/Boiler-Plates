# Offline Knowledge Assistant

## Quick Start

1. python setup.py # Install Ollama + Llama3.2
2. python ingest.py notes.pdf # Add your PDF
3. python chat.py # Chat at http://127.0.0.1:7860

## Features

- ✅ 100% offline after setup
- ✅ Llama 3.2 (3B) for fast CPU inference
- ✅ Sentence-transformers embeddings
- ✅ ChromaDB vector store
- ✅ PDF chunking + RAG

Data stored in `./chroma_db/`
