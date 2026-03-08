# Datasets

This directory contains datasets for studying synthetic data homogenization.

## Dataset Categories

### Real Data Benchmarks
- **CommonCrawl**: Web-scale text data for baseline training
- **The Pile**: Diverse 800GB dataset for language modeling
- **C4**: Colossal Clean Crawled Corpus

### Synthetic Data Collections
- **Model-Generated Corpora**: Data generated at various generations
- **Recursive Training Sets**: Multi-generation synthetic data
- **Quality-Filtered Synthetic**: High-quality generated samples

### Evaluation Sets
- **Diversity Benchmarks**: Measure data and output diversity
- **Capability Tests**: Assess model capabilities across tasks
- **Hallucination Datasets**: Test factual accuracy

## Data Organization

```
data/
├── real/              # Real training data
├── synthetic/         # Synthetic data by generation
│   ├── gen-1/        # First generation synthetic
│   ├── gen-2/        # Second generation
│   └── gen-n/        # Nth generation
├── mixed/            # Mixed real+synthetic ratios
└── evaluation/       # Evaluation datasets
```

## Data Formats

- **JSONL**: Line-by-line JSON format for samples
- **Parquet**: Columnar storage for large datasets
- **TXT**: Plain text for language modeling
- **Metadata.csv**: Data provenance and statistics

## Quality Metrics

Each dataset should include:
- Source information
- Generation timestamp
- Model used for generation
- Quality scores
- Diversity metrics

## Data Citation

When using datasets, cite both:
1. Original dataset source
2. This repository's specific preprocessing/processing
