from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from peft import LoraConfig, get_peft_model
import torch
from PIL import Image
import os
from torchvision import transforms

# Your custom captions for each image
CAPTIONS = {
    "image1.jpg": "a masterpiece portrait in my artistic style",
    "image2.jpg": "landscape painting in my unique style",
    # Add your 20 images + captions here
}

def train_lora_style():
    # Load base model
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16,
        use_safetensors=True
    )
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    
    # LoRA config (low-rank adaptation)
    lora_config = LoraConfig(
        r=16,  # Rank
        lora_alpha=32,
        target_modules=["to_k", "to_q", "to_v", "to_out.0.proj"],
        lora_dropout=0.1,
        bias="none",
        modules_to_save=None
    )
    
    # Apply LoRA
    pipe.unet = get_peft_model(pipe.unet, lora_config)
    pipe.unet.print_trainable_parameters()
    
    # Training dataset (your 20 images)
    images = []
    prompts = []
    for img_file, caption in CAPTIONS.items():
        if os.path.exists(f"data/{img_file}"):
            img = Image.open(f"data/{img_file}").resize((512, 512))
            images.append(img)
            prompts.append(f"a photo of my style, {caption}")
    
    print(f"🖼️ Training on {len(images)} custom images...")
    
    # Training loop (simplified)
    pipe.unet.train()
    optimizer = torch.optim.AdamW(pipe.unet.parameters(), lr=1e-4)
    
    for epoch in range(500):  # ~10min training
        for img, prompt in zip(images, prompts):
            # Tokenize prompt
            text_inputs = pipe.tokenizer(
                prompt, padding="max_length", max_length=pipe.tokenizer.model_max_length,
                truncation=True, return_tensors="pt"
            )
            
            # Encode image to latent
            encoder_hidden_states = text_inputs.input_ids
            latents = pipe.vae.encode(torch.tensor(np.array(img)).float().unsqueeze(0) / 255.0).latent_dist.sample()
            
            # Forward pass (simplified diffusion training)
            noise_pred = pipe.unet(latents, encoder_hidden_states).sample
            loss = torch.nn.functional.mse_loss(noise_pred, torch.randn_like(noise_pred))
            
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
    
    # Save LoRA weights
    pipe.unet.save_pretrained("models/my_art_style_lora")
    print("✅ LoRA training complete!")
    
    torch.save({
        'model_state_dict': pipe.unet.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }, "models/lora_checkpoint.pth")

if __name__ == "__main__":
    train_lora_style()
