# Detection Method Implementations

## Overview

This directory contains implementations of various hallucination detection methods.

## Detection Methods

### 1. Self-Consistency Methods

#### Self-Check
```python
# code/detection/self_check.py

class SelfCheckDetector:
    """Self-consistency based hallucination detector"""

    def __init__(self, model_name="gpt-3.5-turbo"):
        self.generator = load_model(model_name)
        self.num_samples = 5

    def detect(self, prompt, response):
        """
        Detect hallucination through self-consistency checking

        Returns:
            - consistency_score: float (0-1)
            - is_hallucination: bool
            - details: dict with breakdown
        """
        # Generate multiple samples
        samples = self.generate_samples(prompt, self.num_samples)

        # Check consistency
        consistency_score = self.measure_consistency(response, samples)

        # Check against knowledge
        knowledge_score = self.verify_against_knowledge(prompt, response)

        # Combine scores
        final_score = self.combine_scores(consistency_score, knowledge_score)

        return {
            "consistency_score": consistency_score,
            "knowledge_score": knowledge_score,
            "final_score": final_score,
            "is_hallucination": final_score < 0.5
        }

    def generate_samples(self, prompt, n):
        """Generate n samples for the same prompt"""
        samples = []
        for _ in range(n):
            response = self.generator.generate(prompt, temperature=0.7)
            samples.append(response)
        return samples

    def measure_consistency(self, target, samples):
        """Measure semantic similarity between target and samples"""
        similarities = []
        for sample in samples:
            sim = self.semantic_similarity(target, sample)
            similarities.append(sim)
        return np.mean(similarities)
```

### 2. Uncertainty Quantification

#### Log-probability Detection
```python
# code/detection/uncertainty.py

class UncertaintyDetector:
    """Detect hallucinations using uncertainty quantification"""

    def __init__(self, model_name):
        self.model = load_model(model_name)
        self.threshold = -2.0  # Log-prob threshold

    def detect(self, text):
        """
        Detect hallucination based on token log-probabilities

        Low log-probabilities indicate high uncertainty (potential hallucination)
        """
        # Get log-probabilities for each token
        log_probs = self.model.get_token_log_probs(text)

        # Calculate statistics
        mean_log_prob = np.mean(log_probs)
        min_log_prob = np.min(log_probs)
        entropy = self.calculate_entropy(log_probs)

        # Determine if hallucination
        is_hallucination = mean_log_prob < self.threshold

        return {
            "mean_log_prob": mean_log_prob,
            "min_log_prob": min_log_prob,
            "entropy": entropy,
            "is_hallucination": is_hallucination
        }

    def calculate_entropy(self, log_probs):
        """Calculate entropy of the token distribution"""
        probs = np.exp(log_probs)
        return -np.sum(probs * log_probs)
```

### 3. DoLa (Contrastive Layer Decoding)

```python
# code/detection/dola.py

class DoLaDecoder:
    """
    Decoding by Contrasting Layers for factuality improvement

    Paper: DoLa: Decoding by Contrasting Layers (Sun et al., 2023)
    """

    def __init__(self, model_name, early_exit_layer=20, late_exit_layer=32):
        self.model = load_model(model_name)
        self.early_layer = early_exit_layer
        self.late_layer = late_exit_layer

    def generate_with_dola(self, prompt, max_length=100):
        """
        Generate text using DoLa decoding

        Contrasts early layer (factual) vs late layer (linguistic) predictions
        """
        tokens = self.model.tokenize(prompt)

        for _ in range(max_length):
            # Get logits from early layer
            early_logits = self.model.get_layer_logits(tokens, self.early_layer)

            # Get logits from late layer
            late_logits = self.model.get_layer_logits(tokens, self.late_layer)

            # Contrast and select
            contrasted_logits = late_logits - early_logits

            # Sample next token
            next_token = self.sample_token(contrasted_logits)
            tokens.append(next_token)

            if next_token == self.model.eos_token:
                break

        return self.model.decode(tokens)
```

### 4. Fact-Checking Integration

```python
# code/detection/fact_checker.py

class FactCheckingDetector:
    """Detect hallucinations through automated fact-checking"""

    def __init__(self, knowledge_base="wikipedia"):
        self.kb = load_knowledge_base(knowledge_base)
        self.retriever = initialize_retriever()

    def detect(self, text):
        """
        Detect hallucination by verifying claims against knowledge base
        """
        # Extract claims from text
        claims = self.extract_claims(text)

        verified_claims = []
        hallucination_score = 0

        for claim in claims:
            # Retrieve relevant evidence
            evidence = self.retriever.retrieve(claim, top_k=5)

            # Verify claim
            is_supported = self.verify_claim(claim, evidence)

            verified_claims.append({
                "claim": claim,
                "is_supported": is_supported,
                "evidence": evidence
            })

            if not is_supported:
                hallucination_score += 1

        # Calculate overall score
        hallucination_rate = hallucination_score / len(claims) if claims else 0

        return {
            "claims": verified_claims,
            "hallucination_rate": hallucination_rate,
            "is_hallucinated": hallucination_rate > 0.3
        }

    def extract_claims(self, text):
        """Extract individual claims from text"""
        # Simple rule-based extraction
        # In practice, use a trained claim extraction model
        sentences = split_sentences(text)
        return [s for s in sentences if self.is_claim(s)]

    def verify_claim(self, claim, evidence):
        """Verify if claim is supported by evidence"""
        # Use NLI model or similarity-based verification
        similarities = [semantic_similarity(claim, ev) for ev in evidence]
        return max(similarities) > 0.7
```

## Usage Examples

### Running Detection on a Dataset
```python
# examples/run_detection.py

from detection.self_check import SelfCheckDetector
from detection.uncertainty import UncertaintyDetector

# Initialize detectors
self_check = SelfCheckDetector()
uncertainty = UncertaintyDetector("llama-2-7b")

# Load test data
test_data = load_dataset("HaluEval", split="test")

results = []
for example in test_data:
    # Run detection
    sc_result = self_check.detect(example["prompt"], example["response"])
    unc_result = uncertainty.detect(example["response"])

    results.append({
        "id": example["id"],
        "self_check": sc_result,
        "uncertainty": unc_result,
        "ground_truth": example["is_hallucinated"]
    })

# Evaluate
evaluate_detection(results)
```

### Batch Processing
```python
# examples/batch_detect.py

def batch_detect(detector, data, batch_size=32):
    """Run detection on a dataset in batches"""
    results = []

    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]

        # Process batch
        batch_results = [detector.detect(item["text"]) for item in batch]
        results.extend(batch_results)

    return results
```

## Evaluation

### Evaluating Detection Accuracy
```python
# code/evaluation/detection_metrics.py

def evaluate_detection(predictions, ground_truth):
    """Evaluate detection performance"""
    from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score

    # Calculate metrics
    accuracy = accuracy_score(ground_truth, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(
        ground_truth, predictions, average='binary'
    )

    # Calculate AUC if we have probabilities
    if has_probabilities:
        auc = roc_auc_score(ground_truth, probabilities)
    else:
        auc = None

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "auc": auc
    }
```

## Configuration

### Example Config File
```yaml
# configs/detection/self_check.yaml

model:
  name: "gpt-3.5-turbo"
  temperature: 0.7
  num_samples: 5

detection:
  consistency_threshold: 0.5
  knowledge_threshold: 0.6
  combine_method: "average"  # or "weighted", "max"

output:
  save_scores: true
  save_details: true
```

## Testing

### Unit Tests
```bash
# Run tests
pytest tests/test_detection.py -v
```

### Test Example
```python
# tests/test_detection.py

def test_self_check_detector():
    detector = SelfCheckDetector()

    # Test case with known hallucination
    prompt = "What is the capital of Mars?"
    response = "The capital of Mars is Olympus City."

    result = detector.detect(prompt, response)
    assert result["is_hallucination"] == True
    assert result["final_score"] < 0.5
```

## Performance Optimization

### Caching
```python
# code/detection/cache.py

class CachedDetector:
    """Detector with response caching"""

    def __init__(self, detector, cache_file="cache.pkl"):
        self.detector = detector
        self.cache = load_cache(cache_file)

    def detect(self, text):
        # Check cache
        if text in self.cache:
            return self.cache[text]

        # Run detection
        result = self.detector.detect(text)

        # Save to cache
        self.cache[text] = result
        return result
```

### Parallel Processing
```python
# code/detection/parallel.py

from concurrent.futures import ProcessPoolExecutor

def parallel_detect(detector, texts, n_workers=4):
    """Run detection in parallel"""
    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        results = executor.map(detector.detect, texts)
    return list(results)
```

## Related Files
- `/papers/detection/` - Papers describing these methods
- `/data/baselines/` - Reference implementations
- `/experiments/` - Evaluation results
