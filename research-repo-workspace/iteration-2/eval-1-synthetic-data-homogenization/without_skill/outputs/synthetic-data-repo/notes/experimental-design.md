# Experimental Design

## Research Questions

### Primary Question
**How does the proportion of synthetic data in LLM training affect model diversity, capabilities, and long-term performance?**

### Sub-Questions
1. At what synthetic data ratio does model collapse become observable?
2. Which metrics best predict model collapse?
3. Can specific training strategies mitigate collapse?
4. How does collapse vary across different domains and tasks?

## Experimental Setup

### Models
- **Primary**: GPT-2 (124M parameters)
- **Secondary**: GPT-2 Medium (355M), GPT-2 Large (774M)
- **Rationale**: Computationally accessible, well-studied baseline

### Data
- **Base Dataset**: OpenWebText (subset)
- **Synthetic Generation**: Multiple generations (G1, G2, G3, G4, G5)
- **Mixed Ratios**: 0%, 25%, 50%, 75%, 100% synthetic

### Training Conditions

#### Condition 1: Pure Real Data
- 100% real data (baseline)
- 3 epochs, standard hyperparameters

#### Condition 2: Pure Synthetic Data
- 100% synthetic data by generation
- Track degradation across generations
- Same compute as baseline

#### Condition 3: Mixed Training
- Varying synthetic ratios (25%, 50%, 75%)
- Fixed mixing strategy (random sampling)

#### Condition 4: Curriculum Learning
- Start with 100% real
- Gradually increase synthetic ratio
- Test different schedules

## Evaluation Metrics

### Diversity Metrics

1. **N-gram Diversity**
   - Unique n-gram ratio (n=2,3,4)
   - Metric: |unique n-grams| / |total n-grams|

2. **Vocabulary Richness**
   - Type-token ratio (TTR)
   - Metric: |unique tokens| / |total tokens|

3. **Semantic Diversity**
   - Embedding diversity (sentence-transformers)
   - Metric: 1 - mean(cosine similarity)

4. **Topic Diversity**
   - LDA topic distribution entropy
   - Metric: Entropy(topic distribution)

### Performance Metrics

1. **Perplexity**
   - Standard language modeling metric
   - Compute on held-out test set

2. **Task Performance**
   - Downstream tasks (classification, generation)
   - Accuracy, F1, BLEU, ROUGE

3. **Generation Quality**
   - Human evaluation (random sample)
   - Automated metrics (diversity, coherence)

### Collapse Indicators

1. **Tail Disappearance**
   - Track low-probability token mass
   - Metric: Probability mass in bottom 10%

2. **Vocabulary Contraction**
   - Unique token count over generations
   - Metric: Vocabulary size ratio

3. **Perplexity Increase**
   - Track perplexity across generations
   - Metric: Relative perplexity change

## Experimental Procedure

### Phase 1: Baseline Establishment
1. Train model on 100% real data
2. Establish baseline metrics
3. Create evaluation benchmarks

### Phase 2: Synthetic Data Generation
1. Generate synthetic data from baseline model
2. Apply quality filters
3. Create multiple generations (G1-G5)

### Phase 3: Collapse Experiments
1. Train models on pure synthetic data (by generation)
2. Track all metrics
3. Identify collapse patterns

### Phase 4: Mixed Training Experiments
1. Train models with varying synthetic ratios
2. Test different mixing strategies
3. Identify sustainable ratios

### Phase 5: Mitigation Testing
1. Test quality filtering strategies
2. Evaluate curriculum learning
3. Assess diversity-promoting techniques

## Statistical Analysis

### Sample Size
- Minimum 3 runs per condition
- Use different random seeds
- Ensure statistical power

### Significance Testing
- Paired t-tests for metric comparisons
- Bootstrap confidence intervals
- Effect size calculations

### Visualization
- Line plots for generational changes
- Bar charts for ratio comparisons
- Heatmaps for correlation analysis

## Expected Outcomes

### Hypotheses

1. **H1**: Pure synthetic training leads to measurable collapse within 3-5 generations
2. **H2**: Mixed training with <30% synthetic data is sustainable
3. **H3**: Semantic diversity metrics correlate better with collapse than n-gram metrics
4. **H4**: Curriculum learning outperforms random mixing

### Potential Results
- Clear identification of collapse threshold
- Validated early warning metrics
- Effective mitigation strategies
- Domain-specific insights

## Limitations

### Computational Constraints
- Limited to GPT-2 scale models
- May not scale to larger models
- Finite compute budget

### Data Constraints
- Single base dataset (OpenWebText)
- May not generalize to all domains
- Limited diversity in training data

### Evaluation Constraints
- Limited human evaluation resources
- Metrics may not capture all aspects
- Task selection bias

## Timeline

### Week 1-2: Setup
- Implement data generation pipeline
- Set up training infrastructure
- Prepare evaluation metrics

### Week 3-4: Baseline Experiments
- Run baseline training
- Generate synthetic data
- Validate metrics

### Week 5-8: Main Experiments
- Run collapse experiments
- Test mixed training
- Evaluate mitigation strategies

### Week 9-10: Analysis
- Analyze results
- Create visualizations
- Write findings

## Reproducibility

### Code Organization
- Modular, well-documented code
- Configuration files for all experiments
- Automated experiment tracking

### Data Management
- Version-controlled datasets
- Provenance tracking
- Metadata documentation

### Reporting
- Detailed methods sections
- Statistical analysis
- Supplementary materials
