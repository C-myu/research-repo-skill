# Setup Guide

## Quick Start

This guide will help you get started with the LLM Hallucination Mitigation Research Repository.

## Installation

### 1. Clone the Repository

```bash
cd /path/to/your/workspace
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys (Optional)

If using closed-source models (GPT-3.5, Claude, etc.):

```bash
# Create .env file
cp .env.example .env

# Edit .env with your keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## Download Datasets

### Option 1: Download All Datasets

```bash
python scripts/download_datasets.py --all
```

### Option 2: Download Specific Datasets

```bash
# TruthfulQA only
python scripts/download_datasets.py --datasets truthfulqa

# Multiple datasets
python scripts/download_datasets.py --datasets truthfulqa halueval factscore
```

### Option 3: Manual Download

See `/data/datasets/README.md` for manual download instructions.

## Download Baseline Models

### HuggingFace Models

```bash
# Login to HuggingFace
huggingface-cli login

# Download model
huggingface-cli download meta-llama/Llama-2-7b \
  --local-dir data/baselines/models/llama2-7b
```

### Reference Implementations

```bash
# Clone reference implementations
git clone https://github.com/manakul/self-check data/baselines/self_check
```

## Running Experiments

### Detection Experiments

```bash
# Run self-check evaluation
python scripts/run_detection_experiment.py \
  --config configs/detection/self_check.yaml \
  --output experiments/detection/self_check/results.json
```

### Training Experiments

```bash
# Train RAG model
python scripts/run_training_experiment.py \
  --config configs/training/rag.yaml \
  --output experiments/training/rag/results.json
```

### Evaluation

```bash
# Evaluate on benchmarks
python scripts/evaluate_model.py \
  --model_path outputs/rag_model \
  --benchmarks truthfulqa factscore \
  --output results/evaluation.json
```

## Project Structure

```
├── papers/              # Research papers organized by category
│   ├── detection/      # Detection methods (highest priority)
│   ├── alignment/      # Training and alignment techniques
│   └── evaluation/     # Evaluation benchmarks
├── data/               # Datasets and baseline models
│   ├── datasets/       # Benchmark datasets
│   └── baselines/      # Baseline models and systems
├── code/               # Implementation code
│   ├── detection/      # Detection method implementations
│   ├── training/       # Training and alignment code
│   └── evaluation/     # Evaluation scripts and metrics
├── notes/              # Research notes and documentation
│   ├── literature-review/    # Paper summaries and reviews
│   └── implementation-ideas/ # Practical implementation notes
├── experiments/        # Experimental configurations and results
└── logs/              # Experiment logs
```

## Key Resources

### Must-Read Papers

Start with these foundational papers:

1. **Self-Check** (Manakul et al., 2023) - Detection
2. **DoLa** (Sun et al., 2023) - Detection
3. **TruthfulQA** (Lin et al., 2022) - Evaluation
4. **Constitutional AI** (Bai et al., 2022) - Alignment
5. **RAG** (Lewis et al., 2020) - Training

See `/papers/` directories for full lists.

### Key Benchmarks

- **TruthfulQA**: General truthfulness evaluation
- **HaluEval**: Comprehensive hallucination detection
- **FACTSCORE**: Fine-grained factuality measurement

See `/data/datasets/README.md` for details.

### Detection Methods

Quick comparison:

| Method | Accuracy | Latency | Best For |
|--------|----------|---------|----------|
| Self-Check (5) | 72% | 12.5s | Accuracy-critical |
| Self-Check (3) | 68% | 7.5s | Balanced |
| DoLa | 71% | 0.8s | Real-time (open source) |
| Hybrid | 70% | 3.8s | Production |

See `/code/detection/README.md` for implementations.

## Common Workflows

### Workflow 1: Evaluate Detection Method

```bash
# 1. Choose detection method
# 2. Run on benchmark
python scripts/run_detection_experiment.py \
  --method self_check \
  --benchmark halueval \
  --output results/

# 3. Analyze results
python scripts/analyze_results.py --input results/
```

### Workflow 2: Train and Evaluate Model

```bash
# 1. Train with RAG
python scripts/train_rag.py \
  --base_model llama-2-7b \
  --data wikipedia \
  --output models/llama-rag

# 2. Evaluate on benchmarks
python scripts/evaluate_model.py \
  --model models/llama-rag \
  --benchmarks truthfulqa factscore

# 3. Compare with baseline
python scripts/compare_models.py \
  --models llama-2-base llama-rag \
  --output results/comparison.json
```

### Workflow 3: Literature Review

```bash
# 1. Read survey papers
# Start in /papers/detection/ with survey papers

# 2. Read foundation papers
# Self-Check, DoLa, TruthfulQA

# 3. Review implementation notes
# Check /notes/implementation-ideas/

# 4. Explore code examples
# See /code/ directories
```

## Troubleshooting

### Issue: Out of Memory

**Solution**: Reduce batch size or use gradient checkpointing

```bash
# In training config
batch_size: 4  # Reduce from 8
gradient_checkpointing: true
```

### Issue: API Rate Limits

**Solution**: Add rate limiting and retries

```python
# In your code
from time import sleep
import random

def call_with_retry(api_func, max_retries=5):
    for i in range(max_retries):
        try:
            return api_func()
        except RateLimitError:
            sleep_time = 2 ** i + random.random()
            sleep(sleep_time)
    raise Exception("Max retries exceeded")
```

### Issue: Slow Inference

**Solution**: Use quantization or fewer samples

```python
# Use 8-bit quantization
model = AutoModelForCausalLM.from_pretrained(
    "llama-2-7b",
    load_in_8bit=True
)

# Or use fewer samples in self-check
self_check = SelfCheckDetector(num_samples=3)  # Instead of 5
```

## Getting Help

- **Documentation**: Check README files in each directory
- **Issues**: Search existing issues or create new one
- **Code Examples**: See `/code/` directories for examples
- **Literature**: `/notes/literature-review/` for summaries

## Next Steps

1. **Read main README** - Overview of entire project
2. **Browse papers** - Start with `/papers/detection/`
3. **Explore code** - Check `/code/detection/` for practical examples
4. **Run experiments** - Start with baseline evaluations
5. **Contribute** - See `CONTRIBUTING.md`

## Citation

If you use this repository in your research:

```bibtex
@misc{llm-hallucination-repo,
  title = {LLM Hallucination Mitigation Research Repository},
  year = {2026},
  note = {Focused on detection, alignment, and evaluation}
}
```

## License

MIT License - See `LICENSE` file for details.
