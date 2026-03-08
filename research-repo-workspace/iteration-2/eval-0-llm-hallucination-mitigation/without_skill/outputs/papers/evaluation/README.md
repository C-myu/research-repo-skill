# Evaluation Benchmarks for Factuality

## Overview

This directory contains research papers on benchmarks, datasets, and evaluation methodologies for measuring hallucination and factuality in Large Language Models.

## Key Benchmarks

### 1. TruthfulQA
- **Paper**: "TruthfulQA: Measuring How Models Mimic Human Falsehoods" (Lin et al., 2022)
- **Focus**: Truthfulness vs. mimicking human misconceptions
- **Size**: ~800 questions across 38 categories
- **Website**: https://truthfulqa.ai/

### 2. HALU-EVAL
- **Paper**: "HaluEval: A Large-Scale Hallucination Evaluation Benchmark" (Li et al., 2023)
- **Focus**: Comprehensive hallucination detection
- **Scope**: QA, dialogue, and summarization tasks
- **Approach**: Uses GPT-4 to generate both faithful and hallucinated samples

### 3. FACTSCORE
- **Paper**: "Fine-Grained Hallucination Detection" (Min et al., 2023)
- **Focus**: Fact-level granularity in biography generation
- **Metric**: Precision of atomic facts
- **Application**: Long-form generation evaluation

### 4. FAITHSCORE
- **Paper**: "FAITHSCORE: Faithfulness Metric for Abstractive Summarization" (Fabbri et al., 2021)
- **Focus**: Faithfulness in summarization
- **Method**: Fact extraction and verification
- **Dataset**: CNN/DM, XSum, etc.

### 5. QAMPARI
- **Paper**: "QAMPARI: A Question Answering Benchmark on Open-Domain Multi-Document Summarization" (Amplayo et al., 2022)
- **Focus**: Multi-answer, multi-document questions
- **Challenge**: Requires comprehensive understanding

### 6. FELM (Factuality Evaluation in Language Models)
- **Paper**: "FELM: Factuality Evaluation in Language Models" (Lee et al., 2022)
- **Focus**: Factuality in dialogue systems
- **Dataset**: Wizard of Wikipedia and other dialogue datasets

## Evaluation Metrics

### Classification Metrics
- **Precision, Recall, F1**: For binary hallucination detection
- **ROC-AUC**: For confidence-based detection systems

### Generation Metrics
- **BLEU, ROUGE**: Traditional similarity metrics (limited utility)
- **BERTScore**: Semantic similarity
- **Fact-specific metrics**: FACTSCORE, FAITHSCORE

### Custom Metrics
- **Hallucination Rate**: Percentage of generated content that is hallucinated
- **Faithfulness Score**: Degree to which output adheres to source
- **Truthfulness Score**: Alignment with verifiable facts

## Dataset Categories

### Question Answering
Datasets focused on factual accuracy in QA systems:
- TruthfulQA
- HotpotQA (multi-hop reasoning)
- StrategyQA (require reasoning)

### Summarization
Datasets for evaluating faithfulness in summarization:
- CNN/DailyMail
- XSum
- PubMed (scientific summarization)

### Dialogue
Factuality in conversational systems:
- Wizard of Wikipedia
- FELM benchmark
- Self-Chat (conversational consistency)

### Long-form Generation
Biography and article generation:
- BIO dataset (FACTSCORE)
- WikiBio
- LongBench

### Domain-Specific
- **Medical**: MedQA, PubMedQA
- **Legal**: CaseHOLD
- **Finance**: FinQA

## Evaluation Challenges

### Subjectivity
- What constitutes "hallucination" vs. "creative generation"
- Edge cases in factual claims
- Ambiguity in truthfulness

### Cost
- Human evaluation is expensive and time-consuming
- Automated evaluators (like GPT-4) can be biased
- Fact-checking requires external knowledge bases

### Coverage
- No single benchmark covers all hallucination types
- Need for domain-specific evaluation
- Cross-lingual evaluation gaps

### Temporal Dynamics
- Facts change over time (cutoff date issues)
- Benchmark age and staleness
- Updating evaluation datasets

## Best Practices

### For Evaluating Detection Methods
1. Use multiple benchmarks (TruthfulQA + HaluEval)
2. Report both detection accuracy and calibration
3. Evaluate across different model sizes
4. Test domain generalization

### For Evaluating Training Methods
1. Pre-training evaluation vs. post-training evaluation
2. In-domain vs. out-of-domain performance
3. Trade-offs with fluency and diversity
4. Ablation studies for method components

### For Benchmark Selection
1. Start with TruthfulQA for general truthfulness
2. Use domain-specific benchmarks for specialized models
3. Combine automatic metrics with human evaluation
4. Consider computational constraints

## Related Directories
- `/data/datasets/` - Downloaded benchmark datasets
- `/code/evaluation/` - Evaluation scripts and metrics
- `/experiments/` - Evaluation results and comparisons
