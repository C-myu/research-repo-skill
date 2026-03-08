"""
Train a language model on synthetic data.

This script trains a model on synthetic data with options for
mixed real/synthetic training and different mixing strategies.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List
import yaml

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)
from tqdm import tqdm


class TextDataset(Dataset):
    """Simple text dataset for language modeling."""

    def __init__(self, texts: List[str], tokenizer, max_length: int = 512):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": encoding["input_ids"].squeeze(0)
        }


def load_config(config_path: str) -> Dict:
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def load_texts(data_path: str, max_samples: int = None) -> List[str]:
    """Load texts from JSONL file."""
    texts = []

    with open(data_path, 'r') as f:
        for line in f:
            if line.strip():
                data = json.loads(line)
                texts.append(data['text'])

                if max_samples and len(texts) >= max_samples:
                    break

    return texts


def mix_datasets(
    real_texts: List[str],
    synthetic_texts: List[str],
    synthetic_ratio: float,
    strategy: str = "random"
) -> List[str]:
    """Mix real and synthetic texts according to strategy."""
    if synthetic_ratio == 0.0:
        return real_texts
    elif synthetic_ratio == 1.0:
        return synthetic_texts

    n_synthetic = int(len(real_texts) * synthetic_ratio / (1 - synthetic_ratio))

    if strategy == "random":
        # Random sampling from both
        import random
        combined = real_texts + synthetic_texts[:n_synthetic]
        random.shuffle(combined)
        return combined
    else:
        raise ValueError(f"Unknown mixing strategy: {strategy}")


def main():
    parser = argparse.ArgumentParser(description="Train on synthetic data")
    parser.add_argument("--config", type=str, required=True, help="Path to config file")
    parser.add_argument("--real_data", type=str, help="Path to real data")
    parser.add_argument("--synthetic_data", type=str, help="Path to synthetic data")
    parser.add_argument("--output_dir", type=str, default="outputs", help="Output directory")
    parser.add_argument("--synthetic_ratio", type=float, default=1.0, help="Ratio of synthetic data")
    parser.add_argument("--max_samples", type=int, help="Max samples to use")

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Load tokenizer
    print("Loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(config['model']['name'])
    tokenizer.pad_token = tokenizer.eos_token

    # Load and mix data
    print("Loading datasets")
    real_texts = load_texts(args.real_data, args.max_samples) if args.real_data else []
    synthetic_texts = load_texts(args.synthetic_data, args.max_samples) if args.synthetic_data else []

    print(f"Loaded {len(real_texts)} real samples")
    print(f"Loaded {len(synthetic_texts)} synthetic samples")

    mixed_texts = mix_datasets(
        real_texts,
        synthetic_texts,
        args.synthetic_ratio,
        config['data']['mix_strategy']
    )

    print(f"Using {len(mixed_texts)} total samples (synthetic ratio: {args.synthetic_ratio})")

    # Create dataset
    dataset = TextDataset(mixed_texts, tokenizer, max_length=512)

    # Load model
    print("Loading model")
    model = AutoModelForCausalLM.from_pretrained(config['model']['name'])

    # Training arguments
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=config['training']['num_epochs'],
        per_device_train_batch_size=config['training']['batch_size'],
        gradient_accumulation_steps=config['training']['gradient_accumulation_steps'],
        learning_rate=config['training']['learning_rate'],
        warmup_steps=config['training']['warmup_steps'],
        weight_decay=config['training']['weight_decay'],
        logging_dir=f"{args.output_dir}/logs",
        logging_steps=config['logging']['log_every'],
        save_steps=config['logging']['save_every'],
        fp16=config['optimization']['fp16'],
        report_to=["wandb"] if config['logging']['wandb_project'] else [],
        run_name=f"synthetic_{args.synthetic_ratio}",
    )

    # Create trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    # Train
    print("Starting training")
    trainer.train()

    # Save model
    print(f"Saving model to {args.output_dir}")
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)


if __name__ == "__main__":
    main()
