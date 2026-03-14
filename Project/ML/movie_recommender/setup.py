import os
import requests
import zipfile
import pandas as pd
from pathlib import Path

def download_movielens():
    """Download MovieLens 100K dataset."""
    os.makedirs("data", exist_ok=True)
    
    url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
    zip_path = "data/ml-100k.zip"
    
    if not os.path.exists(zip_path):
        print("📥 Downloading MovieLens 100K...")
        resp = requests.get(url)
        with open(zip_path, "wb") as f:
            f.write(resp.content)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("data")
    
    print("✅ MovieLens 100K ready!")

if __name__ == "__main__":
    download_movielens()
    print("🚀 Run: streamlit run app.py")
