# Literature Review: Synthetic Data Homogenization

## Overview

This document reviews key literature on synthetic data homogenization, model collapse, and related phenomena in language model training.

## Core Papers

### 1. The Curse of Recursion: Training on Generated Data Makes Models Forget

**Authors:** Shumailov et al. (2023)

**Key Findings:**
- Demonstrated model collapse in both vision and language models
- Two types of collapse identified:
  - **Early collapse**: Loss of minority modes
  - **Late collapse**: Convergence to degenerate distribution
- Theoretical analysis shows collapse is inevitable without fresh data
- Collapse occurs faster in higher-dimensional data

**Methodology:**
- Multi-generation training experiments
- Theoretical modeling of variance degradation
- Empirical validation across multiple domains

**Implications:**
- Pure synthetic training is unsustainable
- Mixed training required for long-term viability
- Quality filtering can delay but not prevent collapse

### 2. Self-Consumption of Generative Models Leads to Model Collapse

**Author:** Dohmatob (2023)

**Key Findings:**
- Mathematical modeling of collapse dynamics
- Identified bounds on sustainable training
- Showed exponential decay in model quality
- Tail probability distribution changes as early indicator

**Theoretical Contributions:**
- Formal definition of model collapse
- Bounds on number of sustainable generations
- Analysis of variance propagation

### 3. Data Curation for Language Models

**Authors:** Various (2024)

**Key Findings:**
- Quality filtering improves but doesn't prevent collapse
- Diversity metrics correlate with model performance
- Need for semantic-level diversity measures
- Importance of domain diversity

## Related Work

### Synthetic Data Quality

#### Assessing Quality of Synthetic Text Data
- Focus on automatic quality metrics
- Perplexity as proxy for quality
- Limitations of automatic evaluation

#### Diversity in Language Models
- N-gram diversity measures
- Semantic diversity using embeddings
- Topic diversity through LDA

### Mitigation Strategies

#### Mixed Training Approaches
- Optimal synthetic/real ratios
- Dynamic mixing strategies
- Curriculum learning benefits

#### Quality-Aware Training
- Filtering low-quality generations
- Reweighting by quality scores
- Adaptive sampling strategies

## Research Gaps

### Theoretical Gaps
1. **Precise Collapse Mechanism**: Exact conditions for collapse onset
2. **Domain Variation**: Why collapse varies across domains
3. **Scale Effects**: How model size affects collapse rate

### Practical Gaps
1. **Early Detection**: Reliable early warning systems
2. **Optimal Strategies**: Best practices for sustainable training
3. **Evaluation Metrics**: Better metrics for diversity and quality

### Methodological Gaps
1. **Standardized Benchmarks**: Lack of standard evaluation protocols
2. **Reproducibility**: Limited replication studies
3. **Real-World Validation**: Most studies on synthetic tasks

## Key Concepts

### Model Collapse
Progressive degradation of model performance when trained on synthetic data, characterized by:
- Decreasing diversity
- Increasing perplexity
- Loss of tail probability
- Vocabulary contraction

### Diversity Metrics
1. **N-gram Diversity**: Ratio of unique n-grams
2. **Vocabulary Richness**: Type-token ratio
3. **Semantic Diversity**: Embedding-based diversity
4. **Topic Diversity**: Entropy of topic distribution

### Mitigation Strategies
1. **Mixed Training**: Combining real and synthetic data
2. **Quality Filtering**: Selecting high-quality samples
3. **Diverse Generation**: Promoting output diversity
4. **Curriculum Learning**: Gradual synthetic integration

## Open Questions

1. What is the theoretical limit on sustainable synthetic training?
2. Can we develop provably effective mitigation strategies?
3. How does domain characteristics affect collapse rate?
4. What metrics best predict collapse before it occurs?
5. How do these findings scale to larger models?

## Future Directions

### Theoretical Work
- Develop formal theory of collapse dynamics
- Analyze effects of model architecture
- Study interaction with pre-training data

### Empirical Work
- Replicate studies across domains
- Test mitigation strategies systematically
- Develop better evaluation metrics

### Practical Applications
- Guidelines for sustainable synthetic training
- Early warning systems for collapse
- Optimal data mixing strategies

## References

- Shumailov, I., et al. (2023). "The Curse of Recursion: Training on Generated Data Makes Models Forget"
- Dohmatob, E. (2023). "Self-Consumption of Generative Models Leads to Model Collapse"
- [Additional papers to be added as reviewed]

## Last Updated

2024-03-08
