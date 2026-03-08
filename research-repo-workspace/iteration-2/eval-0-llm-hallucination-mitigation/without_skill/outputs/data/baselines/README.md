# Baseline Models and Systems

## Overview

This directory contains baseline models, pretrained weights, and reference implementations for hallucination detection and mitigation.

## Baseline Categories

### 1. Detection Baselines
Reference implementations for hallucination detection systems.

### 2. Training Baselines
Base models and training checkpoints for comparison.

### 3. Evaluation Baselines
Reference implementations of evaluation metrics.

## Detection Baselines

### Self-Check Baseline
- **Paper**: Manakul et al., 2023
- **Location**: `detection/self_check/`
- **Components**:
  - Question generation
  - Answer generation
  - Consistency checking
- **Usage**:
  ```python
  from detection.self_check import SelfCheck
  checker = SelfCheck(model_name="gpt-3.5-turbo")
  result = checker.check_consistency(prompt, response)
  ```

### DoLa Decoding
- **Paper**: Sun et al., 2023
- **Location**: `detection/dola/`
- **Method**: Contrastive layer decoding
- **Implementation**: PyTorch model wrapper

### Uncertainty-based Detection
- **Location**: `detection/uncertainty/`
- **Methods**:
  - Semantic uncertainty
  - Log-probability thresholding
  - Ensemble disagreement

## Training Baselines

### Base Models
Reference checkpoints for common LLMs:
- **Llama-2**: `models/llama2/`
- **GPT-NeoX**: `models/neox/`
- **Falcon**: `models/falcon/`

### Fine-tuned Models
Models fine-tuned for reduced hallucination:
- **TruthfulQA-tuned models**
- **RAG-augmented models**
- **RLHF-aligned models**

### Model Comparison Table

| Model | Size | Training Data | Alignment | Notes |
|-------|------|---------------|-----------|-------|
| Llama-2-7B | 7B | 2T tokens | RLHF | Good baseline |
| GPT-3.5 | - | - | RLHF | Proprietary |
| Falcon-7B | 7B | 1.5T tokens | No | Open weights |
| Vicuna | 13B | Llama-2 | Fine-tuned | Open source |

## Evaluation Baselines

### FACTSCORE Implementation
- **Location**: `evaluation/factscore/`
- **Requirements**: OpenAI API or local embedding model
- **Usage**:
  ```bash
  python -m evaluation.factscore \
    --input bio.txt \
    --output scores.json
  ```

### TruthfulQA Evaluator
- **Location**: `evaluation/truthfulqa/`
- **Metrics**: Truthfulness, human mimicry
- **Implementation**: Reference evaluator

### FAITHSCORE
- **Location**: `evaluation/faithscore/`
- **Task**: Summarization faithfulness
- **Dependencies**: NLP library for fact extraction

## Downloading Baselines

### Automated Download
```bash
# Clone baseline implementations
git clone https://github.com/papers/CodeRepository baselines/

# Download model weights (requires HuggingFace CLI)
huggingface-cli download meta-llama/Llama-2-7b \
  --local-dir models/llama2-7b
```

### Manual Setup
1. Visit repository websites
2. Follow installation instructions
3. Download required models
4. Update configuration files

## Usage Guidelines

### For Detection Evaluation
```python
# Evaluate detection baseline on HaluEval
from evaluation import evaluate_detector

detector = SelfCheckDetector()
results = evaluate_detector(
    detector=detector,
    dataset="HaluEval",
    split="test"
)
```

### For Training Comparison
```python
# Compare trained model against baseline
from training import compare_models

baseline_model = load_model("llama-2-7b")
trained_model = load_model("my-aligned-model")

metrics = compare_models(
    baseline=baseline_model,
    trained=trained_model,
    benchmarks=["truthfulqa", "factscore"]
)
```

## Baseline Results

### Detection Performance (Reference)

| Method | TruthfulQA | HaluEval | Latency |
|--------|------------|----------|---------|
| Self-Check | 0.65 | 0.72 | High |
| DoLa | 0.71 | 0.68 | Low |
| Uncertainty | 0.58 | 0.61 | Medium |

Note: These are example values. Run your own evaluation.

### Training Improvement (Reference)

| Model | TruthfulQA | FACTSCORE |
|-------|------------|-----------|
| Llama-2-base | 0.42 | 0.65 |
| Llama-2-RLHF | 0.51 | 0.71 |
| RAG-Llama | 0.58 | 0.76 |

## Custom Baselines

### Adding Your Own Baselines
1. Create directory under appropriate category
2. Add implementation files
3. Include README with usage instructions
4. Update this main README
5. Add results to `results/` subdirectory

### Baseline Requirements
- **Reproducibility**: Include seeds and hyperparameters
- **Documentation**: Clear usage examples
- **Dependencies**: List all required packages
- **Results**: Include benchmark scores

## Reference Implementations

### Key Repositories
- **Self-Check**: https://github.com/manakul/self-check
- **DoLa**: https://github.com/voidism/DoLa
- **FACTSCORE**: https://github.com/shmswn25/FACTSCORE
- **TruthfulQA**: https://github.com/sylinrl/TruthfulQA

## Configuration

### Model Configurations
Config files in `configs/`:
```
configs/
├── detection/
│   ├── self_check.yaml
│   └── dola.yaml
└── training/
    ├── llama2.yaml
    └── rlhf.yaml
```

### Environment Setup
```bash
# Create environment
conda create -n hallu-baseline python=3.10
conda activate hallu-baseline

# Install dependencies
pip install -r requirements.txt
```

## Troubleshooting

### Common Issues
1. **Model Download Failures**: Check HuggingFace authentication
2. **Memory Errors**: Use quantized models or gradient checkpointing
3. **API Key Errors**: Set up OpenAI/Anthropic API keys
4. **Version Conflicts**: Use exact package versions from requirements.txt

## Related Directories
- `/code/` - Custom implementations
- `/experiments/` - Experimental results
- `/papers/` - Papers describing these baselines
