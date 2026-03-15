import subprocess
import sys
import os
import shutil

def command_exists(cmd):
    return shutil.which(cmd) is not None

def install_ollama():
    """Install Ollama (Linux/Mac/Windows)."""
    if command_exists("ollama"):
        print("✅ Ollama is already installed!")
        return 
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
    """Pull Llama 3.2 (3B, CPU-friendly)."""
    try:
        # Check existing models
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True
        )
        if "llama3.2:3b" in result.stdout:
            print("✅ Llama 3.2 (3B) is already downloaded!")
            return
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Could not check existing models: {e}")

    # Pull the model if not present
    print("📥 Pulling Llama 3.2:1b (3B)... ~1.5GB")
    try:
        subprocess.run(
            ["ollama", "pull", "llama3.2:1b"],
            check=True
        )
        print("✅ Model ready!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to pull model: {e}")

if __name__ == "__main__":
    install_ollama()
    pull_model()
    print("\n🚀 Setup complete! Run: python ingest.py your_notes.pdf")
