# Synthetic Data Homogenization in LLM Training

## Research Overview

This repository investigates the phenomenon of synthetic data homogenization and model collapse in Large Language Model (LLM) training. The focus is on understanding how training on AI-generated data affects model diversity, capabilities, and long-term performance.

## Key Research Areas

### 1. Model Collapse
- Investigating degradation in model performance when trained recursively on synthetic data
- Quantifying the rate of information loss across generations
- Identifying early warning signs of model collapse

### 2. Diversity Preservation
- Measuring and maintaining diversity in synthetic datasets
- Techniques for preventing mode collapse in generated data
- Evaluating the impact of data diversity on model capabilities

### 3. Training Strategies
- Mixed training approaches (synthetic + real data)
- Curriculum learning for synthetic data integration
- Quality filtering and data selection strategies

## Repository Structure

```
.
├── papers/          # Research papers and literature
├── data/            # Datasets and experimental data
├── code/            # Implementation and experiments
├── notes/           # Research notes and documentation
└── .claude/         # Claude-specific configurations
```

## Getting Started

1. Review existing literature in `papers/`
2. Explore datasets in `data/`
3. Run experiments in `code/`
4. Document findings in `notes/`

## Research Questions

1. How does the proportion of synthetic data in training sets affect model performance?
2. What metrics best capture synthetic data homogenization?
3. Can we develop robust strategies to maintain model capabilities when training on generated data?
4. How does synthetic data homogenization vary across different domains and tasks?

## Citation

If you use this repository in your research, please cite appropriately.
