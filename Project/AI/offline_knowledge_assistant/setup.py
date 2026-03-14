import subprocess
import sys
import os

def install_ollama():
    """Install Ollama (Linux/Mac/Windows)."""
    if sys.platform == "win32":
        cmd = "winget install Ollama.Ollama"
    elif sys.platform == "darwin":
        cmd = "brew install ollama"
    else:
        cmd = "curl -fsSL https://ollama.com/install.sh | sh"
    
    print("🔧 Installing Ollama...")
    subprocess.run(cmd, shell=True, check=True)
    print("✅ Ollama installed!")

def pull_model():
    """Pull Llama 3.2 (3B, fast on CPU)."""
    print("📥 Pulling Llama 3.2 (3B)... ~2GB")
    subprocess.run(["ollama", "pull", "llama3.2:3b"], check=True)
    print("✅ Model ready!")

if __name__ == "__main__":
    install_ollama()
    pull_model()
    print("\n🚀 Setup complete! Run: python ingest.py your_notes.pdf")
