diffusers transformers gradio accelerate torch torchvision peft pillow xformers safetensors

1. mkdir ai_art_generator && cd ai_art_generator
2. pip install -r requirements.txt
3. python setup.py # Downloads Stable Diffusion (~4GB)
4. # Add 20 of YOUR images to data/ folder
5. # Edit CAPTIONS dict in train_lora.py
6. python train_lora.py # Fine-tune LoRA (~10min 8GB VRAM)
7. python app.py # http://localhost:7860
