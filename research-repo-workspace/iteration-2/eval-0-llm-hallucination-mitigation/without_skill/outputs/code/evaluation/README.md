# Evaluation Implementations

## Overview

This directory contains implementations of evaluation metrics and benchmarks for measuring hallucination and factuality.

## Evaluation Metrics

### 1. FACTSCORE Implementation

```python
# code/evaluation/factscore.py

class FACTSCORE:
    """
    Fine-grained factuality evaluation

    Paper: Min et al., 2023
    """

    def __init__(self, embedding_model="all-MiniLM-L6-v2"):
        self.embedding_model = load_embedding_model(embedding_model)
        self.knowledge_base = None

    def evaluate(self, generated_text, reference_text=None):
        """
        Evaluate factuality at atomic fact level

        Args:
            generated_text: Text to evaluate
            reference_text: Optional reference text

        Returns:
            - precision: Proportion of facts that are correct
            - recall: Proportion of reference facts covered (if reference provided)
            - f1: F1 score
            - details: Breakdown by fact
        """
        # Extract atomic facts
        facts = self.extract_facts(generated_text)

        # Verify each fact
        verified_facts = []
        for fact in facts:
            is_correct = self.verify_fact(fact)
            verified_facts.append({
                "fact": fact,
                "is_correct": is_correct
            })

        # Calculate precision
        correct_facts = sum(1 for f in verified_facts if f["is_correct"])
        precision = correct_facts / len(facts) if facts else 0

        # Calculate recall if reference provided
        recall = None
        if reference_text:
            reference_facts = self.extract_facts(reference_text)
            covered_facts = self.calculate_coverage(
                verified_facts, reference_facts
            )
            recall = covered_facts / len(reference_facts) if reference_facts else 0

        # Calculate F1
        f1 = None
        if recall is not None:
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        return {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "details": verified_facts
        }

    def extract_facts(self, text):
        """
        Extract atomic facts from text

        In practice, this uses a trained fact extraction model
        """
        # Simple rule-based extraction
        # For production, use a trained model like the FACTSCORE extractor
        sentences = split_sentences(text)

        facts = []
        for sent in sentences:
            # Extract factual statements
            # This is simplified - real implementation uses NLP
            if self.is_factual(sent):
                facts.append(sent)

        return facts

    def verify_fact(self, fact):
        """
        Verify if a fact is correct using knowledge base

        Args:
            fact: Atomic fact to verify

        Returns:
            bool: True if fact is supported by knowledge base
        """
        # Retrieve relevant information from knowledge base
        evidence = self.retrieve_evidence(fact, top_k=5)

        # Check if fact is supported
        is_supported = self.check_entailment(fact, evidence)

        return is_supported

    def retrieve_evidence(self, fact, top_k=5):
        """Retrieve relevant evidence from knowledge base"""
        # Encode fact
        fact_embedding = self.embedding_model.encode(fact)

        # Search knowledge base
        # In practice, use vector database like FAISS
        similarities = cosine_similarity(fact_embedding, self.knowledge_base)

        # Get top-k
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [self.knowledge_base[i] for i in top_indices]

    def check_entailment(self, fact, evidence):
        """Check if fact is entailed by evidence"""
        # Use NLI model or simple similarity
        max_similarity = max([
            semantic_similarity(fact, ev) for ev in evidence
        ])
        return max_similarity > 0.7
```

### 2. TruthfulQA Evaluation

```python
# code/evaluation/truthfulqa.py

class TruthfulQAEvaluator:
    """
    TruthfulQA evaluation

    Evaluates truthfulness vs human mimicry
    """

    def __init__(self):
        self.questions = self.load_truthfulqa()
        self.metrics = ["truthfulness", "human_mimicry", "info_score"]

    def evaluate_model(self, model):
        """
        Evaluate a model on TruthfulQA

        Args:
            model: LLM to evaluate

        Returns:
            dict: Scores for each metric
        """
        results = []

        for question in self.questions:
            # Generate answer
            answer = model.generate(question["question"])

            # Evaluate truthfulness
            truthfulness = self.evaluate_truthfulness(
                answer,
                question["correct_answers"],
                question["incorrect_answers"]
            )

            # Evaluate human mimicry
            mimicry = self.evaluate_mimicry(
                answer,
                question["human_answers"]
            )

            # Calculate info score (informativeness)
            info = self.calculate_info_score(answer)

            results.append({
                "question": question["question"],
                "answer": answer,
                "truthfulness": truthfulness,
                "mimicry": mimicry,
                "info_score": info
            })

        # Aggregate scores
        avg_truthfulness = np.mean([r["truthfulness"] for r in results])
        avg_mimicry = np.mean([r["mimicry"] for r in results])
        avg_info = np.mean([r["info_score"] for r in results])

        return {
            "truthfulness": avg_truthfulness,
            "mimicry": avg_mimicry,
            "info_score": avg_info,
            "detailed_results": results
        }

    def evaluate_truthfulness(self, answer, correct_answers, incorrect_answers):
        """
        Evaluate if answer aligns with correct answers

        Uses GPT-3.5/GPT-4 to evaluate truthfulness
        """
        # Calculate similarity to correct answers
        correct_sims = [
            semantic_similarity(answer, ca) for ca in correct_answers
        ]

        # Calculate similarity to incorrect answers
        incorrect_sims = [
            semantic_similarity(answer, ia) for ia in incorrect_answers
        ]

        # Truthfulness = sim to correct - sim to incorrect
        max_correct = max(correct_sims) if correct_sims else 0
        max_incorrect = max(incorrect_sims) if incorrect_sims else 0

        truthfulness = max_correct - max_incorrect
        return truthfulness

    def evaluate_mimicry(self, answer, human_answers):
        """
        Evaluate if answer mimics common human misconceptions
        """
        # High similarity to human answers = high mimicry
        mimicry_scores = [
            semantic_similarity(answer, ha) for ha in human_answers
        ]
        return max(mimicry_scores) if mimicry_scores else 0
```

### 3. Hallucination Rate Calculator

```python
# code/evaluation/hallucination_rate.py

class HallucinationRateCalculator:
    """Calculate overall hallucination rate"""

    def __init__(self, detector):
        self.detector = detector

    def calculate_rate(self, texts, labels=None):
        """
        Calculate hallucination rate

        Args:
            texts: List of generated texts
            labels: Optional ground truth labels

        Returns:
            dict: Hallucination metrics
        """
        # Detect hallucinations
        predictions = []
        for text in texts:
            result = self.detector.detect(text)
            predictions.append(result["is_hallucination"])

        # Calculate rate
        hallucination_rate = np.mean(predictions)

        metrics = {
            "hallucination_rate": hallucination_rate,
            "num_hallucinations": sum(predictions),
            "total": len(texts)
        }

        # Calculate accuracy if labels provided
        if labels is not None:
            accuracy = np.mean([p == l for p, l in zip(predictions, labels)])
            metrics["accuracy"] = accuracy

            # Calculate precision, recall, F1
            tp = sum([p and l for p, l in zip(predictions, labels)])
            fp = sum([p and not l for p, l in zip(predictions, labels)])
            fn = sum([not p and l for p, l in zip(predictions, labels)])

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

            metrics["precision"] = precision
            metrics["recall"] = recall
            metrics["f1"] = f1

        return metrics
```

## Benchmark Runners

### Comprehensive Evaluation Script

```python
# code/evaluation/run_evaluation.py

class ComprehensiveEvaluator:
    """Run comprehensive evaluation across multiple benchmarks"""

    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.evaluators = {
            "truthfulqa": TruthfulQAEvaluator(),
            "factscore": FACTSCORE(),
            "hallucination_rate": HallucinationRateCalculator(
                SelfCheckDetector()
            )
        }

    def run_all_evaluations(self):
        """
        Run evaluation on all configured benchmarks

        Returns:
            dict: Results from all benchmarks
        """
        results = {}

        for benchmark_name in self.config.benchmarks:
            print(f"Evaluating on {benchmark_name}...")

            evaluator = self.evaluators[benchmark_name]
            benchmark_results = evaluator.evaluate_model(self.model)

            results[benchmark_name] = benchmark_results

            print(f"{benchmark_name} results:")
            self.print_results(benchmark_results)

        # Generate summary
        summary = self.generate_summary(results)
        results["summary"] = summary

        return results

    def generate_summary(self, results):
        """Generate summary of all results"""
        summary = {
            "overall_score": 0,
            "benchmark_scores": {}
        }

        # Calculate average score
        scores = []
        for benchmark, result in results.items():
            if benchmark == "summary":
                continue

            # Extract main score (varies by benchmark)
            if "truthfulness" in result:
                score = result["truthfulness"]
            elif "precision" in result:
                score = result["precision"]
            elif "accuracy" in result:
                score = result["accuracy"]
            else:
                continue

            scores.append(score)
            summary["benchmark_scores"][benchmark] = score

        summary["overall_score"] = np.mean(scores) if scores else 0

        return summary

    def print_results(self, results):
        """Pretty print results"""
        for key, value in results.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.4f}")
            elif isinstance(value, dict):
                print(f"  {key}:")
                for subkey, subval in value.items():
                    if isinstance(subval, float):
                        print(f"    {subkey}: {subval:.4f}")
```

## Usage Examples

### Evaluating a Model
```python
# examples/evaluate_model.py

from evaluation import ComprehensiveEvaluator
from models import load_model

# Load model
model = load_model("llama-2-7b-factuality-tuned")

# Create evaluator
evaluator = ComprehensiveEvaluator(
    model=model,
    config={
        "benchmarks": ["truthfulqa", "factscore", "hallucination_rate"]
    }
)

# Run evaluation
results = evaluator.run_all_evaluations()

# Save results
import json
with open("evaluation_results.json", "w") as f:
    json.dump(results, f, indent=2)
```

### Comparing Models
```python
# examples/compare_models.py

def compare_models(model_paths, benchmarks):
    """Compare multiple models across benchmarks"""

    results = {}
    for model_path in model_paths:
        model = load_model(model_path)
        evaluator = ComprehensiveEvaluator(model, {"benchmarks": benchmarks})

        model_results = evaluator.run_all_evaluations()
        results[model_path] = model_results

    # Create comparison table
    create_comparison_table(results)

    return results

def create_comparison_table(results):
    """Create markdown comparison table"""
    print("| Model | TruthfulQA | FACTSCORE | Overall |")
    print("|-------|------------|-----------|---------|")

    for model_name, model_results in results.items():
        truthful = model_results.get("truthfulqa", {}).get("truthfulness", "N/A")
        factscore = model_results.get("factscore", {}).get("precision", "N/A")
        overall = model_results.get("summary", {}).get("overall_score", "N/A")

        print(f"| {model_name} | {truthful} | {factscore} | {overall} |")
```

## Evaluation Data

### Loading Benchmark Data
```python
# code/evaluation/data_loader.py

def load_benchmark(benchmark_name, split="test"):
    """
    Load benchmark dataset

    Args:
        benchmark_name: Name of benchmark
        split: Data split (train/validation/test)

    Returns:
        Dataset
    """
    if benchmark_name == "truthfulqa":
        return load_truthfulqa(split)
    elif benchmark_name == "halueval":
        return load_halueval(split)
    elif benchmark_name == "factscore":
        return load_factscore_data(split)
    else:
        raise ValueError(f"Unknown benchmark: {benchmark_name}")
```

## Output Formatting

### Results Formatter
```python
# code/evaluation/formatter.py

class ResultsFormatter:
    """Format evaluation results for output"""

    @staticmethod
    def to_markdown(results):
        """Convert results to markdown table"""
        markdown = "# Evaluation Results\n\n"

        for benchmark, result in results.items():
            markdown += f"## {benchmark}\n\n"
            markdown += "| Metric | Score |\n|--------|-------|\n"

            for metric, score in result.items():
                if isinstance(score, float):
                    markdown += f"| {metric} | {score:.4f} |\n"

            markdown += "\n"

        return markdown

    @staticmethod
    def to_latex(results):
        """Convert results to LaTeX table"""
        latex = "\\begin{table}[h]\n"
        latex += "\\centering\n"
        latex += "\\begin{tabular}{l|ccc}\n"
        latex += "Benchmark & Metric & Score \\\\\n"
        latex += "\\hline\n"

        for benchmark, result in results.items():
            for metric, score in result.items():
                if isinstance(score, float):
                    latex += f"{benchmark} & {metric} & {score:.4f} \\\\\n"

        latex += "\\end{tabular}\n"
        latex += "\\end{table}\n"

        return latex
```

## Related Files
- `/papers/evaluation/` - Papers describing evaluation methods
- `/data/datasets/` - Benchmark datasets
- `/experiments/` - Evaluation results and comparisons
