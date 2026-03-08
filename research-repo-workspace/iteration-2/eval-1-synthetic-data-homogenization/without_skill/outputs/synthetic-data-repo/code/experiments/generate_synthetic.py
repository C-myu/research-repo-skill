"""
Generate synthetic data using a trained language model.

This script generates synthetic text samples from a trained model,
with options for diversity control and quality filtering.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List
import yaml

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm


def load_config(config_path: str) -> Dict:
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def generate_samples(
    model,
    tokenizer,
    prompts: List[str],
    config: Dict
) -> List[str]:
    """Generate synthetic samples from prompts."""
    model.eval()
    generated_texts = []

    with torch.no_grad():
        for prompt in tqdm(proms, desc="Generating"):
            inputs = tokenizer.encode(prompt, return_tensors='pt')
            inputs = inputs.to(model.device)

            outputs = model.generate(
                inputs,
                max_length=config['model']['max_length'],
                temperature=config['model']['temperature'],
                top_p=config['model']['top_p'],
                top_k=config['model']['top_k'],
                do_sample=True,
                num_return_sequences=config['generation']['num_return_sequences'],
                repetition_penalty=config['generation']['repetition_penalty']
            )

            for output in outputs:
                text = tokenizer.decode(output, skip_special_tokens=True)
                generated_texts.append(text)

    return generated_texts


def filter_by_quality(texts: List[str], config: Dict) -> List[str]:
    """Filter generated texts by quality criteria."""
    filtered = []

    for text in texts:
        length_ok = config['quality']['min_length'] <= len(text) <= config['quality']['max_length']

        if length_ok:
            filtered.append(text)

    return filtered


def save_outputs(texts: List[str], output_dir: Path, generation: int):
    """Save generated texts to file."""
    output_dir = Path(output_dir) / f"gen-{generation}"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "synthetic_data.jsonl"

    with open(output_file, 'w') as f:
        for text in texts:
            json.dump({"text": text}, f)
            f.write('\n')

    print(f"Saved {len(texts)} samples to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate synthetic data")
    parser.add_argument("--config", type=str, required=True, help="Path to config file")
    parser.add_argument("--model_path", type=str, required=True, help="Path to trained model")
    parser.add_argument("--prompts", type=str, required=True, help="Path to prompts file")
    parser.add_argument("--generation", type=int, default=1, help="Generation number")
    parser.add_argument("--output_dir", type=str, default="data/synthetic", help="Output directory")

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Load model and tokenizer
    print(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    model = AutoModelForCausalLM.from_pretrained(args.model_path)
    model = model.to("cuda" if torch.cuda.is_available() else "cpu")

    # Load prompts
    with open(args.prompts, 'r') as f:
        prompts = [line.strip() for line in f if line.strip()]

    print(f"Loaded {len(prompts)} prompts")

    # Generate samples
    generated_texts = generate_samples(model, tokenizer, prompts, config)
    print(f"Generated {len(generated_texts)} samples")

    # Filter by quality
    if config['quality']['filter_enabled']:
        filtered_texts = filter_by_quality(generated_texts, config)
        print(f"Filtered to {len(filtered_texts)} high-quality samples")
    else:
        filtered_texts = generated_texts

    # Save outputs
    save_outputs(filtered_texts, args.output_dir, args.generation)


if __name__ == "__main__":
    main()
