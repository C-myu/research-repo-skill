"""
Evaluate model performance and diversity metrics.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

import sys
sys.path.append('metrics')
from diversity_metrics import compute_all_diversity_metrics


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


def compute_perplexity(model, tokenizer, texts: List[str], max_length: int = 512) -> float:
    """Compute perplexity on texts."""
    model.eval()
    total_loss = 0.0
    total_tokens = 0

    with torch.no_grad():
        for text in tqdm(texts, desc="Computing perplexity"):
            inputs = tokenizer(
                text,
                max_length=max_length,
                truncation=True,
                return_tensors="pt"
            )

            inputs = {k: v.to(model.device) for k, v in inputs.items()}

            outputs = model(**inputs, labels=inputs["input_ids"])
            loss = outputs.loss

            total_loss += loss.item() * inputs["input_ids"].size(1)
            total_tokens += inputs["input_ids"].size(1)

    avg_loss = total_loss / total_tokens
    perplexity = torch.exp(torch.tensor(avg_loss)).item()

    return perplexity


def evaluate_model(model_path: str, data_path: str, max_samples: int = None) -> Dict[str, float]:
    """Evaluate model on data."""
    print(f"Loading model from {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    model = model.to("cuda" if torch.cuda.is_available() else "cpu")

    # Load texts
    print(f"Loading texts from {data_path}")
    texts = load_texts(data_path, max_samples)
    print(f"Loaded {len(texts)} texts")

    # Compute perplexity
    print("Computing perplexity...")
    perplexity = compute_perplexity(model, tokenizer, texts)

    # Compute diversity metrics
    print("Computing diversity metrics...")
    diversity_metrics = compute_all_diversity_metrics(texts)

    # Combine results
    results = {
        'perplexity': perplexity,
        **diversity_metrics,
        'num_samples': len(texts),
    }

    return results


def save_results(results: Dict[str, float], output_path: str):
    """Save evaluation results to JSON file."""
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Saved results to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate model")
    parser.add_argument("--model_path", type=str, required=True, help="Path to model")
    parser.add_argument("--data_path", type=str, required=True, help="Path to evaluation data")
    parser.add_argument("--output", type=str, default="results/evaluation.json", help="Output file")
    parser.add_argument("--max_samples", type=int, help="Max samples to evaluate")

    args = parser.parse_args()

    # Run evaluation
    results = evaluate_model(args.model_path, args.data_path, args.max_samples)

    # Print results
    print("\nEvaluation Results:")
    print("-" * 50)
    for metric, value in results.items():
        if isinstance(value, float):
            print(f"{metric}: {value:.4f}")
        else:
            print(f"{metric}: {value}")

    # Save results
    save_results(results, args.output)


if __name__ == "__main__":
    main()
