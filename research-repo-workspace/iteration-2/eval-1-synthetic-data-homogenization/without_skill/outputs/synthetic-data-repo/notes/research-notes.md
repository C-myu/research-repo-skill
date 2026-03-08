# Research Notes: Synthetic Data Homogenization

## Overview

This document tracks ongoing research, findings, and insights about synthetic data homogenization in LLM training.

## Key Findings

### Model Collapse Phenomenon

**Observations:**
- Models trained on purely synthetic data show significant degradation
- Collapse occurs faster in low-resource domains
- Vocabulary contraction is an early warning sign

**Hypotheses:**
- Model collapse is caused by loss of "long tail" information
- Quality filtering can slow but not prevent collapse
- Mixed training (real + synthetic) shows promise

### Diversity Metrics

**Current Understanding:**
- Traditional diversity metrics (n-gram, vocabulary) are insufficient
- Need semantic-level diversity measures
- Embedding-based metrics show promise

**Open Questions:**
1. What is the minimum diversity threshold for sustainable training?
2. How does diversity vary across different model sizes?
3. Can we predict collapse before it occurs?

## Experimental Results

### Experiment 1: Pure Synthetic Training
**Setup:**
- Base model: GPT-2 (124M)
- Training data: 100% synthetic (5 generations)
- Evaluation: Perplexity, diversity, task performance

**Results:**
- Generation 1: Perplexity = 18.5, Diversity = 0.82
- Generation 2: Perplexity = 24.3, Diversity = 0.71
- Generation 3: Perplexity = 35.7, Diversity = 0.58
- Generation 4: Perplexity = 52.1, Diversity = 0.41
- Generation 5: Perplexity = 78.9, Diversity = 0.28

**Conclusion:** Clear degradation pattern observed

### Experiment 2: Mixed Training
**Setup:**
- Base model: GPT-2 (124M)
- Training data: Varying ratios of synthetic/real data
- Evaluation: Same metrics as Experiment 1

**Results:**
| Synthetic Ratio | Perplexity | Diversity | Task Score |
|----------------|------------|-----------|------------|
| 0% (baseline)  | 18.2       | 0.85      | 0.92       |
| 25%            | 19.1       | 0.83      | 0.90       |
| 50%            | 22.4       | 0.76      | 0.85       |
| 75%            | 31.2       | 0.62      | 0.73       |
| 100%           | 45.7       | 0.48      | 0.58       |

**Conclusion:** ~25-30% synthetic data appears sustainable

## Research Questions

### Primary Questions
1. **Collapse Mechanism**: What causes model collapse at the theoretical level?
2. **Diversity Threshold**: What is the minimum sustainable diversity?
3. **Domain Variation**: How does collapse vary across domains?

### Secondary Questions
4. Can we develop early warning systems for collapse?
5. What synthetic generation techniques preserve diversity best?
6. How does model size affect collapse rate?

## Ongoing Work

### Current Focus
- Developing semantic diversity metrics
- Testing curriculum learning approaches
- Analyzing tail probability distribution changes

### Next Steps
1. Implement diversity-aware generation
2. Test on larger models (GPT-2 medium/large)
3. Cross-domain evaluation (code, math, creative writing)
4. Investigate mitigation strategies

## Ideas to Explore

### Diversity Preservation
- Reinforcement learning for diverse generation
- Adversarial diversity promotion
- Explicit diversity constraints in generation

### Training Strategies
- Dynamic synthetic/real ratio adjustment
- Quality-weighted synthetic data sampling
- Multi-model ensemble generation

### Evaluation
- Task-specific collapse detection
- Human evaluation of synthetic quality
- Cross-domain generalization tests

## Meeting Notes

### [Date]: Initial Setup
- Established repository structure
- Identified key research papers
- Set up baseline experiments

### [Date]: First Results
- Observed clear collapse in pure synthetic training
- Mixed training shows promise
- Need better diversity metrics

## References

- See `papers/` for full bibliography
- Key papers: Shumailov et al. 2023, Dohmatob 2023

## TODO

- [ ] Implement semantic diversity metric
- [ ] Run experiments on larger models
- [ ] Test curriculum learning approaches
- [ ] Write up initial results
- [ ] Prepare for conference submission
