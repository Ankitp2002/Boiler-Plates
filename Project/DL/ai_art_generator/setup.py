import os
from diffusers import StableDiffusionPipeline
import torch

print("🎨 Setting up Stable Diffusion 1.5...")
os.makedirs("models", exist_ok=True)

# Test download (will cache locally)
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    use_safetensors=True
)

print("✅ Stable Diffusion ready! (cached in ~/.cache/huggingface)")
print("📁 Add 20 images to data/ folder, then: python train_lora.py")
