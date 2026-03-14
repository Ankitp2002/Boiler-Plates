import os
import requests
import zipfile
from pathlib import Path

def download_chest_xray():
    """Download Kaggle Chest X-Ray Pneumonia dataset."""
    os.makedirs("data", exist_ok=True)
    
    # Direct download from Kaggle (Chest X-Ray Images Pneumonia)
    base_url = "https://github.com/ieee8023/covid-chestxray-dataset/archive/master.zip"
    
    print("📥 Downloading Chest X-Ray dataset...")
    # Note: Real project would use Kaggle API or direct GitHub release
    # For demo: create dummy structure
    os.makedirs("data/chest_xray/train/NORMAL", exist_ok=True)
    os.makedirs("data/chest_xray/train/PNEUMONIA", exist_ok=True)
    os.makedirs("data/chest_xray/test/NORMAL", exist_ok=True)
    os.makedirs("data/chest_xray/test/PNEUMONIA", exist_ok=True)
    
    print("✅ Dataset structure ready! (Add real images from Kaggle)")
    print("Download: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia")

if __name__ == "__main__":
    download_chest_xray()
    print("🚀 Run: python train.py then python app.py")
