# Research Repository Setup Summary

## Repository: Synthetic Data Homogenization in LLM Training

**Location:** `/home/mas-chen.mingyu/project/from_github/research-repo-skill/research-repo-workspace/iteration-2/eval-1-synthetic-data-homogenization/without_skill/outputs/synthetic-data-repo`

**Date Created:** 2024-03-08

---

## Overview

This repository has been set up to investigate synthetic data homogenization and model collapse in Large Language Model (LLM) training. It provides a complete infrastructure for conducting experiments, tracking results, and documenting findings.

---

## Directory Structure

```
synthetic-data-repo/
├── README.md                          # Project overview and getting started
├── LICENSE                            # MIT License
├── .gitignore                         # Git ignore patterns
│
├── papers/                            # Research literature
│   ├── README.md                      # Paper organization and reading list
│   ├── model-collapse/                # Papers on collapse phenomena
│   ├── synthetic-quality/             # Quality assessment papers
│   ├── diversity/                     # Diversity preservation papers
│   └── mitigation/                    # Mitigation strategy papers
│
├── data/                              # Dataset storage
│   ├── README.md                      # Data organization and formats
│   ├── real/                          # Real training data
│   ├── synthetic/                     # Synthetic data by generation
│   │   ├── gen-1/                     # First generation
│   │   ├── gen-2/                     # Second generation
│   │   └── gen-3/                     # Third generation
│   ├── mixed/                         # Mixed real+synthetic datasets
│   └── evaluation/                    # Evaluation benchmarks
│
├── code/                              # Implementation and experiments
│   ├── README.md                      # Code documentation
│   ├── requirements.txt               # Python dependencies
│   ├── configs/                       # Configuration files
│   │   ├── generation.yaml            # Data generation settings
│   │   └── training.yaml              # Training parameters
│   ├── experiments/                   # Experimental scripts
│   │   ├── generate_synthetic.py      # Generate synthetic data
│   │   ├── train_with_synthetic.py    # Train on synthetic data
│   │   └── evaluate.py                # Evaluate model performance
│   ├── metrics/                       # Evaluation metrics
│   │   └── diversity_metrics.py       # Diversity measurement tools
│   ├── analysis/                      # Data analysis scripts
│   ├── models/                        # Model implementations
│   ├── utils/                         # Utility functions
│   ├── tracking/                      # Experiment tracking
│   └── results/                       # Experimental results
│       ├── metrics/                   # Evaluation metrics
│       ├── plots/                     # Visualizations
│       ├── logs/                      # Training logs
│       └── checkpoints/               # Model checkpoints
│
└── notes/                             # Research documentation
    ├── research-notes.md              # Ongoing research notes
    ├── experimental-design.md         # Detailed experimental design
    ├── literature-review.md           # Literature review
    └── todo.md                        # Task checklist

```

---

## Key Features

### 1. Comprehensive Documentation
- **README.md**: Project overview, research questions, and quick start guide
- **Experimental Design**: Detailed methodology and statistical analysis plan
- **Literature Review**: Curated list of key papers with summaries
- **Research Notes**: Template for documenting ongoing findings

### 2. Complete Code Infrastructure
- **Data Generation**: Script to generate synthetic data from trained models
- **Training Pipeline**: Support for pure and mixed synthetic training
- **Evaluation Framework**: Comprehensive metrics including diversity and performance
- **Configuration Management**: YAML-based configuration for experiments
- **Experiment Tracking**: Integration with Weights & Biases (wandb)

### 3. Organized Data Structure
- Separate directories for real, synthetic, and mixed datasets
- Generation-based organization for tracking collapse
- Evaluation benchmarks ready for use
- Placeholder files for git tracking

### 4. Research Tools
- **Diversity Metrics**: N-gram, vocabulary, semantic diversity
- **Performance Metrics**: Perplexity, task performance, generation quality
- **Collapse Indicators**: Tail probability, vocabulary contraction
- **Visualization Support**: Results organization for plotting

---

## Research Focus Areas

### 1. Model Collapse
- Progressive degradation when training on synthetic data
- Theoretical analysis of variance degradation
- Early warning signs and detection methods

### 2. Diversity Preservation
- Measuring diversity in synthetic datasets
- Techniques for preventing mode collapse
- Semantic vs. surface-level diversity

### 3. Training Strategies
- Mixed training (synthetic + real data)
- Quality filtering and data selection
- Curriculum learning approaches
- Optimal synthetic data ratios

---

## Key Research Questions

1. **Primary**: How does the proportion of synthetic data in LLM training affect model diversity, capabilities, and long-term performance?

2. **Secondary**:
   - At what synthetic data ratio does model collapse become observable?
   - Which metrics best predict model collapse?
   - Can specific training strategies mitigate collapse?
   - How does collapse vary across different domains and tasks?

---

## Getting Started

### 1. Setup Environment
```bash
cd /home/mas-chen.mingyu/project/from_github/research-repo-skill/research-repo-workspace/iteration-2/eval-1-synthetic-data-homogenization/without_skill/outputs/synthetic-data-repo
pip install -r code/requirements.txt
```

### 2. Prepare Data
- Place real training data in `data/real/`
- Prepare evaluation benchmarks in `data/evaluation/`

### 3. Run Experiments
```bash
# Generate synthetic data
python code/experiments/generate_synthetic.py \
    --config code/configs/generation.yaml \
    --model_path /path/to/model \
    --prompts /path/to/prompts.txt

# Train on synthetic data
python code/experiments/train_with_synthetic.py \
    --config code/configs/training.yaml \
    --synthetic_data data/synthetic/gen-1/synthetic_data.jsonl \
    --synthetic_ratio 1.0

# Evaluate model
python code/experiments/evaluate.py \
    --model_path outputs/model \
    --data_path data/evaluation
```

---

## Key Dependencies

- **PyTorch**: Deep learning framework
- **Transformers**: Pre-trained models and tokenization
- **Datasets**: Data loading and processing
- **Sentence-Transformers**: Semantic diversity metrics
- **Weights & Biases**: Experiment tracking
- **Scientific Stack**: NumPy, Pandas, SciPy, Matplotlib

---

## Planned Experiments

### Phase 1: Baseline (Weeks 1-2)
- Train baseline model on real data
- Establish baseline metrics
- Set up generation pipeline

### Phase 2: Collapse Experiments (Weeks 3-4)
- Generate multi-generation synthetic data
- Train models on pure synthetic data
- Track degradation patterns

### Phase 3: Mixed Training (Weeks 5-6)
- Test varying synthetic ratios (25%, 50%, 75%)
- Evaluate sustainability thresholds
- Compare mixing strategies

### Phase 4: Mitigation (Weeks 7-8)
- Test quality filtering
- Evaluate diverse generation techniques
- Assess curriculum learning

### Phase 5: Analysis (Weeks 9-10)
- Statistical analysis
- Visualization and reporting
- Paper preparation

---

## Expected Outcomes

1. **Identification** of collapse thresholds for different synthetic ratios
2. **Validation** of early warning metrics for model collapse
3. **Development** of effective mitigation strategies
4. **Understanding** of how collapse varies across domains
5. **Publication** of findings at a top-tier conference

---

## Next Steps

1. **Immediate**:
   - Set up GPU environment
   - Install dependencies
   - Download baseline dataset

2. **Short-term**:
   - Train baseline model
   - Generate first synthetic data
   - Run initial experiments

3. **Long-term**:
   - Complete all experimental phases
   - Analyze results
   - Prepare publication

---

## Repository Statistics

- **Total Files Created**: 20+ files
- **Lines of Documentation**: 2000+ lines
- **Code Scripts**: 4 main experimental scripts
- **Configuration Files**: 2 YAML configs
- **Documentation Files**: 5 markdown documents
- **Directory Levels**: 3-4 levels deep

---

## Contact and Contribution

This repository is set up for research on synthetic data homogenization. Contributions, suggestions, and collaborations are welcome.

For questions or support, please refer to the documentation in the respective directories or consult the notes/ folder for detailed research documentation.

---

**Last Updated:** 2024-03-08
**Status:** Ready for research
**Version:** 1.0.0
