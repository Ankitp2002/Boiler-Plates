from datasets import load_dataset
import os
from transformers import DistilBertTokenizerFast

def download_and_prepare():
    """Load LIAR dataset + tokenize."""
    print("📥 Loading LIAR dataset...")
    
    # LIAR dataset from HuggingFace (12K statements, 6 truth labels)
    dataset = load_dataset("liar", split="train")
    
    # Save locally
    os.makedirs("data", exist_ok=True)
    dataset.to_csv("data/liar_train.csv")
    
    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
    
    print("✅ LIAR dataset ready! 12K fake news samples")
    print("Labels: pants-fire, false, barely-true, half-true, mostly-true, true")

if __name__ == "__main__":
    download_and_prepare()
    print("🚀 Run: python trainer.py then python app.py")
