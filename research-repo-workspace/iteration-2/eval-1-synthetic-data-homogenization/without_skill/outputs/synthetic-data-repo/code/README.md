# Code and Experiments

This directory contains implementations for studying synthetic data homogenization.

## Project Structure

```
code/
├── experiments/      # Experimental scripts
├── analysis/         # Data analysis tools
├── models/          # Model implementations
├── metrics/         # Evaluation metrics
└── utils/           # Utility functions
```

## Key Components

### 1. Synthetic Data Generation
- `generate_synthetic.py`: Generate synthetic data from models
- `diverse_generation.py`: Techniques for diverse generation
- `quality_filter.py`: Filter synthetic data by quality

### 2. Model Training
- `train_with_synthetic.py`: Train models on synthetic data
- `mixed_training.py`: Mixed real+synthetic training
- `recursive_training.py`: Multi-generation training experiments

### 3. Evaluation Metrics
- `diversity_metrics.py`: Measure diversity in data and outputs
- `collapse_detection.py`: Detect model collapse
- `capability_evaluation.py`: Assess model capabilities
- `perplexity_analysis.py`: Track perplexity changes

### 4. Analysis Tools
- `analyze_generations.py`: Compare across generations
- `visualize_collapse.py`: Visualize collapse dynamics
- `statistical_tests.py`: Statistical significance testing

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Running Experiments

```bash
# Generate synthetic data
python experiments/generate_synthetic.py --config configs/generation.yaml

# Train model on synthetic data
python experiments/train_with_synthetic.py --data data/synthetic/gen-1

# Evaluate model
python experiments/evaluate.py --model outputs/model checkpoints
```

### Configuration

Edit configuration files in `configs/`:
- `generation.yaml`: Synthetic data generation settings
- `training.yaml`: Model training parameters
- `evaluation.yaml`: Evaluation metrics and benchmarks

## Key Algorithms

### Diversity Metrics
1. **N-gram Diversity**: Unique n-gram ratio
2. **Embedding Diversity**: Cosine similarity distribution
3. **Vocabulary Richness**: Type-token ratio
4. **Semantic Diversity**: Topic diversity

### Collapse Detection
1. **Perplexity Tracking**: Monitor perplexity increase
2. **Performance Degradation**: Task performance over generations
3. **Tail Disappearance**: Loss of low-probability tokens
4. **Vocabulary Contraction**: Reduced vocabulary usage

### Mitigation Strategies
1. **Mixed Training**: Blend synthetic and real data
2. **Quality Filtering**: Use only high-quality synthetic data
3. **Diverse Sampling**: Encourage diverse generations
4. **Curriculum Learning**: Gradual synthetic data integration

## Experiment Tracking

Use `tracking/` to log experiments:
```python
from tracking import ExperimentTracker

tracker = ExperimentTracker("experiment_name")
tracker.log_metrics({"diversity": 0.85, "perplexity": 15.3})
```

## Results

Results are saved to `results/`:
- `metrics/`: Evaluation metrics
- `plots/`: Visualization outputs
- `logs/`: Training logs
- `checkpoints/`: Model checkpoints

## Citation

If you use this code, please cite:
```bibtex
@software{synthetic_data_homogenization,
  title = {Synthetic Data Homogenization Research Code},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/your-repo}
}
```
