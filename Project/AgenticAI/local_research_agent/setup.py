import subprocess
import sys

def setup_ollama():
    """Install Ollama + Mistral 7B."""
    print("🔧 Setting up Ollama...")
    # Ollama install (run manually or adapt from previous)
    subprocess.run(["ollama", "pull", "mistral:7b"], check=True)
    print("✅ Mistral 7B ready!")

if __name__ == "__main__":
    setup_ollama()
