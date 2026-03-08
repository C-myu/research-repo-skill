"""
Diversity metrics for measuring synthetic data and model output diversity.
"""

import numpy as np
from collections import Counter
from typing import List, Dict
import torch
from sentence_transformers import SentenceTransformer


def ngram_diversity(texts: List[str], n: int = 3) -> float:
    """
    Calculate n-gram diversity (unique n-gram ratio).

    Args:
        texts: List of text samples
        n: N-gram size

    Returns:
        Diversity score (0-1, higher is more diverse)
    """
    all_ngrams = []

    for text in texts:
        tokens = text.lower().split()
        ngrams = [' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
        all_ngrams.extend(ngrams)

    if len(all_ngrams) == 0:
        return 0.0

    unique_ngrams = len(set(all_ngrams))
    total_ngrams = len(all_ngrams)

    return unique_ngrams / total_ngrams


def vocabulary_richness(texts: List[str]) -> float:
    """
    Calculate type-token ratio (vocabulary richness).

    Args:
        texts: List of text samples

    Returns:
        TTR score (0-1, higher is more diverse)
    """
    all_tokens = []

    for text in texts:
        tokens = text.lower().split()
        all_tokens.extend(tokens)

    if len(all_tokens) == 0:
        return 0.0

    unique_tokens = len(set(all_tokens))
    total_tokens = len(all_tokens)

    return unique_tokens / total_tokens


def semantic_diversity(texts: List[str], model_name: str = 'all-MiniLM-L6-v2') -> float:
    """
    Calculate semantic diversity using sentence embeddings.

    Measures diversity as 1 - mean pairwise cosine similarity.

    Args:
        texts: List of text samples
        model_name: Sentence transformer model name

    Returns:
        Semantic diversity score (0-1, higher is more diverse)
    """
    if len(texts) < 2:
        return 0.0

    # Load model
    model = SentenceTransformer(model_name)

    # Generate embeddings
    embeddings = model.encode(texts, convert_to_tensor=True)

    # Calculate pairwise similarities
    similarities = torch.nn.functional.cosine_similarity(
        embeddings.unsqueeze(1),
        embeddings.unsqueeze(0),
        dim=-1
    )

    # Exclude diagonal (self-similarity)
    mask = ~torch.eye(similarities.shape[0], dtype=torch.bool)
    similarities = similarities[mask]

    # Diversity = 1 - mean similarity
    mean_similarity = similarities.mean().item()

    return 1.0 - mean_similarity


def compute_entropy(probabilities: np.ndarray) -> float:
    """
    Compute Shannon entropy of a probability distribution.

    Args:
        probabilities: Probability distribution

    Returns:
        Entropy value
    """
    # Filter out zero probabilities
    probs = probabilities[probabilities > 0]

    if len(probs) == 0:
        return 0.0

    entropy = -np.sum(probs * np.log2(probs))

    return entropy


def vocabulary_entropy(texts: List[str]) -> float:
    """
    Calculate vocabulary entropy (measure of vocabulary distribution).

    Args:
        texts: List of text samples

    Returns:
        Entropy of token distribution
    """
    all_tokens = []

    for text in texts:
        tokens = text.lower().split()
        all_tokens.extend(tokens)

    if len(all_tokens) == 0:
        return 0.0

    # Count token frequencies
    counter = Counter(all_tokens)
    total = len(all_tokens)

    # Calculate probabilities
    probs = np.array([count / total for count in counter.values()])

    return compute_entropy(probs)


def tail_probability(texts: List[str], tokenizer) -> float:
    """
    Calculate probability mass in the tail (low-probability tokens).

    Args:
        texts: List of text samples
        tokenizer: Tokenizer to use

    Returns:
        Fraction of probability mass in tail
    """
    # This would require a trained model to compute probabilities
    # Placeholder for now
    return 0.0


def compute_all_diversity_metrics(texts: List[str]) -> Dict[str, float]:
    """
    Compute all diversity metrics.

    Args:
        texts: List of text samples

    Returns:
        Dictionary of metric names to scores
    """
    metrics = {
        'ngram_diversity_2': ngram_diversity(texts, n=2),
        'ngram_diversity_3': ngram_diversity(texts, n=3),
        'ngram_diversity_4': ngram_diversity(texts, n=4),
        'vocabulary_richness': vocabulary_richness(texts),
        'vocabulary_entropy': vocabulary_entropy(texts),
        'semantic_diversity': semantic_diversity(texts),
    }

    return metrics


if __name__ == "__main__":
    # Test with sample texts
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "A fast brown fox leaps across a sleepy dog.",
        "The dog was sleeping when the fox jumped.",
    ]

    metrics = compute_all_diversity_metrics(sample_texts)

    print("Diversity Metrics:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.4f}")
