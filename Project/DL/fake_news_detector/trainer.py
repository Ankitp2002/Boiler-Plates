from transformers import (
    DistilBertForSequenceClassification, DistilBertTokenizerFast,
    TrainingArguments, Trainer
)
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType
import torch
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
import os

# Load data
dataset = load_dataset("liar", split="train")
label_map = {"pants-fire": 0, "false": 1, "barely-true": 2, 
             "half-true": 3, "mostly-true": 4, "true": 5}

def tokenize_function(examples):
    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
    return tokenizer(examples["statement"], padding="max_length", 
                    truncation=True, max_length=128)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
tokenized_dataset = tokenized_dataset.rename_column("label", "labels")
tokenized_dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

# LoRA config (CPU-friendly fine-tuning)
lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    inference_mode=False,
    r=16,
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["q_lin", "v_lin"]  # DistilBERT attention layers
)

# Model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=6
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# Training args
training_args = TrainingArguments(
    output_dir="./outputs",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=2,
    warmup_steps=500,
    logging_steps=10,
    evaluation_strategy="steps",
    eval_steps=500,
    save_steps=1000,
    load_best_model_at_end=True,
    fp16=torch.cuda.is_available(),
    report_to=None  # Disable wandb
)

# Metrics
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return {
        "accuracy": accuracy_score(labels, predictions),
        "f1": f1_score(labels, predictions, average="weighted")
    }

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset.select(range(8000)),
    eval_dataset=tokenized_dataset.select(range(8000, 10000)),
    compute_metrics=compute_metrics
)

print("🎓 Training DistilBERT + LoRA...")
trainer.train()

# Save
os.makedirs("models", exist_ok=True)
model.save_pretrained("models/fake_news_detector")
tokenizer.save_pretrained("models/fake_news_detector")
print("✅ Model saved!")
