import os
import requests
import pandas as pd
from pathlib import Path

def download_dataset():
    """Download Give Me Some Credit dataset."""
    os.makedirs("data", exist_ok=True)
    
    # Kaggle 'Give Me Some Credit' dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank-additional.zip"
    
    print("📥 Downloading dataset...")
    resp = requests.get(url)
    with open("data/bank_data.zip", "wb") as f:
        f.write(resp.content)
    
    print("✅ Dataset ready in data/")

if __name__ == "__main__":
    download_dataset()
    print("🚀 Run: streamlit run app.py")
