import gradio as gr
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from model import ChestXRayClassifier
from gradcam import GradCAM
import matplotlib.pyplot as plt

# Load model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = ChestXRayClassifier().to(device)
model.load_state_dict(torch.load("models/chest_xray_resnet18.pth"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Get target layer for Grad-CAM (layer4)
target_layer = model.resnet.layer4[-1]

def predict(image):
    """Predict + Grad-CAM visualization."""
    # Preprocess
    input_tensor = transform(image).unsqueeze(0).to(device)
    
    # Predict
    with torch.no_grad():
        output = model(input_tensor)
        probs = F.softmax(output, dim=1)
        confidence = torch.max(probs, 1).values.item()
        pred_class = torch.argmax(probs, 1).item()
    
    label = "❌ PNEUMONIA" if pred_class == 1 else "✅ NORMAL"
    
    # Grad-CAM
    gradcam = GradCAM(model, target_layer)
    cam = gradcam.generate(input_tensor)
    
    # Overlay heatmap
    img_np = np.array(image.resize((224, 224)))
    heatmap = cv2.resize(cam, (224, 224))
    heatmap = cm.jet(heatmap)[..., :3]
    heatmap = (heatmap * 255).astype(np.uint8)
    
    superimposed = (heatmap * 0.4 + img_np * 0.6).astype(np.uint8)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(img_np)
    ax1.set_title("Original")
    ax1.axis('off')
    
    ax2.imshow(superimposed)
    ax2.set_title(f"Grad-CAM: {label} ({confidence:.1%})")
    ax2.axis('off')
    
    plt.tight_layout()
    return label, confidence, fig

# Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload Chest X-Ray"),
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Slider(label="Confidence", minimum=0, maximum=1, step=0.01),
        gr.Plot(label="Grad-CAM Heatmap")
    ],
    title="🩺 Chest X-Ray Classifier (ResNet18)",
    description="Upload chest X-ray → AI classifies Normal/Pneumonia + Grad-CAM heatmap",
    examples=None
)

if __name__ == "__main__":
    iface.launch()
