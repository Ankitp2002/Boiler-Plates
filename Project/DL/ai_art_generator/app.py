import gradio as gr
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from peft import PeftModel
import torch
from PIL import Image
import os

# Load base model + your LoRA
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True
)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Load your custom LoRA weights
pipe.unet = PeftModel.from_pretrained(pipe.unet, "models/my_art_style_lora")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_art(prompt, style_strength=0.8, num_inference_steps=25, guidance_scale=7.5, num_images=1):
    """Generate art in your custom style."""
    custom_prompt = f"{prompt}, masterpiece, in my artistic style"
    
    images = pipe(
        custom_prompt,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        strength=style_strength,
        num_images_per_prompt=num_images
    ).images
    
    return images

# Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 Custom AI Art Generator")
    gr.Markdown("Generate unlimited art in **YOUR artistic style** using Stable Diffusion + LoRA")
    
    with gr.Row():
        with gr.Column(scale=2):
            prompt = gr.Textbox(
                label="Art Prompt", 
                placeholder="A cyberpunk city at sunset...",
                lines=2
            )
            style_strength = gr.Slider(0.5, 1.0, value=0.8, label="Style Strength")
            steps = gr.Slider(20, 50, value=25, step=5, label="Inference Steps")
            guidance = gr.Slider(5.0, 15.0, value=7.5, step=0.5, label="Guidance Scale")
            num_images = gr.Dropdown([1, 2, 4], value=1, label="Images")
            
            generate_btn = gr.Button("🎨 Generate Art", variant="primary", size="lg")
        
        with gr.Column(scale=3):
            output_gallery = gr.Gallery(label="Generated Art", height=600)
    
    # Examples
    examples = [
        ["a majestic lion in a fantasy forest"],
        ["portrait of a wise old wizard"],
        ["futuristic robot dancing under neon lights"]
    ]
    
    gr.Examples(examples=examples, inputs=[prompt], fn=generate_art, outputs=output_gallery)
    
    gr.Markdown("""
    ### 🚀 Quick Start
    1. `pip install -r requirements.txt`
    2. `python setup.py` (downloads SD 1.5)
    3. Add 20 images to `data/` + edit captions in `train_lora.py`
    4. `python train_lora.py` (~10min)
    5. `python app.py` → **YOUR style unlocked!**
    """)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
