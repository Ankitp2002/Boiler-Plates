import gradio as gr
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from peft import PeftModel
import torch

# Load fine-tuned model + LoRA weights
base_model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=6
)
model = PeftModel.from_pretrained(base_model, "models/fake_news_detector")
tokenizer = DistilBertTokenizerFast.from_pretrained("models/fake_news_detector")

label_names = ["Pants-Fire", "False", "Barely-True", "Half-True", "Mostly-True", "True"]

def predict_fake_news(text):
    """Classify statement truthfulness."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, 
                      truncation=True, max_length=128)
    
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        pred_id = torch.argmax(probs, dim=-1).item()
        confidence = torch.max(probs).item()
    
    label = label_names[pred_id]
    verdict = "🚨 FAKE NEWS" if pred_id <= 1 else "✅ LIKELY TRUE"
    
    return {
        "prediction": f"{verdict} ({label})",
        "confidence": f"{confidence:.1%}",
        "all_probs": {label_names[i]: f"{p:.1%}" for i, p in enumerate(probs[0])}
    }

# Gradio interface
iface = gr.Interface(
    fn=predict_fake_news,
    inputs=gr.Textbox(label="News Statement", placeholder="Enter news headline or statement...", lines=3),
    outputs=[
        gr.Textbox(label="Verdict", lines=1),
        gr.Textbox(label="Confidence"),
        gr.JSON(label="All Probabilities")
    ],
    title="📰 Fake News Detector (DistilBERT + LoRA)",
    description="Fine-tuned on LIAR dataset (12K political statements). Detects 6 truthfulness levels.",
    examples=[
        ["ObamaCare will save lives!"],
        ["U.S. unemployment rate at 5.6% in November."],
        ["Hillary Clinton emails prove criminality."]
    ]
)

if __name__ == "__main__":
    iface.launch()
