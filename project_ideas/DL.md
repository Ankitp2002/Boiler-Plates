🩺 Medical Image Classifier

CONCEPTS COVERED
◆ Backpropagation & gradient descent (build from scratch)
◆ CNN layers: Conv2D, MaxPool, BatchNorm
◆ Transfer learning: ResNet18, EfficientNet (free on HuggingFace)
◆ Data augmentation with Albumentations (free)

CAPSTONE PROJECT
Chest X-Ray dataset from Kaggle (free, CC license). Fine-tune ResNet18 via PyTorch + torchvision (both free). Implement Grad-CAM heatmaps to visualize what the model sees. Deploy as Gradio app — runs on CPU if no GPU, or free Colab GPU.

📰 Fake News Detector

CONCEPTS COVERED
◆ Attention mechanism & self-attention from scratch
◆ BERT, DistilBERT, RoBERTa architecture
◆ Fine-tuning with HuggingFace Trainer API (free)
◆ PEFT / LoRA: fine-tune large models on CPU/low RAM

CAPSTONE PROJECT
Fine-tune DistilBERT (lighter, faster than BERT) on the free LIAR dataset (HuggingFace datasets). Use PEFT/LoRA to fine-tune on even a laptop. Deploy as Gradio app. Optional: use free Colab T4 GPU to fine-tune full BERT.

🎨 Custom AI Art Generator

CONCEPTS COVERED
◆ GANs: Generator + Discriminator training loop
◆ Diffusion models: DDPM forward & reverse process
◆ Stable Diffusion locally via diffusers (HuggingFace, free)
◆ LoRA fine-tuning for custom image styles

CAPSTONE PROJECT
Install diffusers + Stable Diffusion 1.5 (free weights on HuggingFace) locally. Fine-tune with LoRA on 20 of your own images to create a custom art model. Build a Gradio interface with prompt input, style controls, and image gallery. 100% local, runs on 8GB VRAM or Google Colab free.
