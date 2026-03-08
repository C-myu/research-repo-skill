# Research Papers

This directory contains relevant literature on synthetic data homogenization, model collapse, and related topics.

## Key Papers by Category

### Model Collapse

1. **The Curse of Recursion: Training on Generated Data Makes Models Forget** (Shumailov et al., 2023)
   - Fundamental paper on model collapse
   - Theoretical analysis of recursive training
   - Empirical evidence across multiple domains

2. **Model Collapse: A Comprehensive Survey** (Various, 2024)
   - Comprehensive overview of collapse phenomena
   - Taxonomy of different collapse types
   - Mitigation strategies review

### Synthetic Data Quality

3. **Self-Consumption of Generative Models Leads to Model Collapse** (Dohmatob, 2023)
   - Mathematical modeling of collapse dynamics
   - Theoretical bounds on sustainable training

4. **Data Curation for Language Models: A Comprehensive Survey** (2024)
   - Best practices for synthetic data generation
   - Quality assessment methodologies

### Diversity Preservation

5. **Preserving Diversity in Language Model Training** (2023)
   - Techniques for maintaining diversity
   - Evaluation metrics for data diversity

6. **Mode Collapse in Generative Models** (2024)
   - Analysis of mode collapse in synthetic data
   - Prevention strategies

### Mitigation Strategies

7. **Avoiding Model Collapse: Sustainable Training Strategies** (2024)
   - Mixed training approaches
   - Curriculum learning for synthetic data

8. **Quality-Aware Synthetic Data Integration** (2023)
   - Filtering and selection strategies
   - Adaptive training methods

## Reading Order

For newcomers to the field, recommend reading order:

1. Start with: **The Curse of Recursion** (Shumailov et al.)
2. Follow with: **Self-Consumption of Generative Models** (Dohmatob)
3. Then explore: **Avoiding Model Collapse** for mitigation strategies

## Paper Organization

```
papers/
├── model-collapse/      # Papers on collapse phenomena
├── synthetic-quality/   # Quality assessment and generation
├── diversity/          # Diversity preservation techniques
└── mitigation/         # Strategies to prevent collapse
```

## Adding New Papers

When adding new papers:
1. Download PDF to appropriate category directory
2. Add entry to this README with key findings
3. Include citation information
4. Note any experimental results or data
