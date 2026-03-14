import subprocess
import sys
import os

def install_ollama():
    """Install Ollama if not present."""
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, check=True)
        print("✅ Ollama already installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("🔧 Installing Ollama...")
        if sys.platform == "win32":
            cmd = "winget install Ollama.Ollama"
        elif sys.platform == "darwin":
            cmd = "brew install ollama"
        else:
            cmd = "curl -fsSL https://ollama.com/install.sh | sh"
        
        subprocess.run(cmd, shell=True, check=True)
        print("✅ Ollama installed!")

def pull_mistral():
    """Pull Mistral 7B for resume tasks."""
    print("📥 Pulling Mistral 7B (~4GB, ~2min)...")
    subprocess.run(["ollama", "pull", "mistral:7b"], check=True)
    print("✅ Mistral 7B ready!")

def verify_setup():
    """Test Ollama + Mistral."""
    print("🔍 Testing setup...")
    result = subprocess.run(
        ["ollama", "run", "mistral:7b", "Say 'Resume agent ready!'"], 
        capture_output=True, text=True, timeout=30
    )
    if "Resume agent ready" in result.stdout:
        print("✅ FULL SETUP COMPLETE!")
        return True
    return False

if __name__ == "__main__":
    print("💼 Resume Tailoring Agent - Setup")
    print("=" * 50)
    
    install_ollama()
    pull_mistral()
    
    if verify_setup():
        print("\n🚀 Ready to run: python run.py")
        print("📂 Your resume.db will persist workflow state")
    else:
        print("❌ Setup failed. Check Ollama service.")
        sys.exit(1)
