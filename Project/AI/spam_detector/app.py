import gradio as gr
import joblib
import numpy as np
from preprocessor import preprocess_text

# Load models
nb_model = joblib.load('nb_model.pkl')
lr_model = joblib.load('lr_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_sms(text, model_choice):
    """Predict spam/ham."""
    processed = preprocess_text(text)
    vec = vectorizer.transform([processed])
    
    if model_choice == "Naive Bayes":
        model = nb_model
    else:
        model = lr_model
    
    prob = model.predict_proba(vec)[0]
    pred = model.predict(vec)[0]
    
    label = "🛑 SPAM" if pred == 1 else "✅ HAM"
    confidence = max(prob) * 100
    
    return f"{label} (Confidence: {confidence:.1f}%)"

# Gradio interface
iface = gr.Interface(
    fn=predict_sms,
    inputs=[
        gr.Textbox(label="Enter SMS text", placeholder="Type your message here...", lines=3),
        gr.Radio(["Naive Bayes", "Logistic Regression"], label="Model", value="Logistic Regression")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="🤖 SMS Spam Detector",
    description="Trained on UCI SMS Spam Collection. Test any message!",
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    iface.launch(share=False)
