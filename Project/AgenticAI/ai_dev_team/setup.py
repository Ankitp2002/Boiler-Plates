import subprocess
import sys

print("🔧 Installing Ollama + Mistral 7B...")
subprocess.run(["ollama", "pull", "mistral:7b"], check=True)
print("✅ Dev Team ready! Run: python run.py")
