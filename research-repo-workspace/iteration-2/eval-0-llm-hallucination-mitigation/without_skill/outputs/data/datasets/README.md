# Benchmark Datasets

## Overview

This directory contains benchmark datasets for evaluating hallucination detection, mitigation, and factuality in LLMs.

## Dataset Structure

```
datasets/
├── truthfulqa/              # TruthfulQA benchmark
├── halueval/                # HaluEval benchmark
├── factscore/               # FACTSCORE biography dataset
├── faithscore/              # Summarization faithfulness datasets
└── domain_specific/         # Domain-specific factuality datasets
    ├── medical/
    ├── legal/
    └── finance/
```

## Key Datasets

### 1. TruthfulQA
- **Location**: `truthfulqa/`
- **Format**: JSON, CSV
- **Size**: ~800 questions
- **Download**: https://truthfulqa.ai/
- **Usage Instructions**:
  ```bash
  # Load from Python
  import datasets
  dataset = datasets.load_dataset('truthfulqa/truthful_qa')
  ```

### 2. HaluEval
- **Location**: `halueval/`
- **Tasks**: QA, Dialogue, Summarization
- **Splits**: Train, validation, test
- **Download**: https://github.com/RUCAIBox/HaluEval

### 3. FACTSCORE
- **Location**: `factscore/`
- **Domain**: Biography generation
- **Annotations**: Atomic fact extractions
- **Download**: https://github.com/shmswn25/FACTSCORE

### 4. Summarization Datasets
- **Location**: `faithscore/`
- **Datasets**: CNN/DM, XSum, PubMed
- **Format**: Source articles + summaries + fact annotations

### 5. Domain-Specific Datasets

#### Medical
- **MedQA**: Medical exam questions
- **PubMedQA**: Biomedical literature QA
- **MedicationQA**: Drug information QA

#### Legal
- **CaseHOLD**: Legal case holding classification
- **LegalBench: Comprehensive legal reasoning benchmark

#### Finance
- **FinQA**: Financial numerical reasoning
- **ConvFinQA: Conversational financial QA

## Download Instructions

### Automated Download Script
```bash
# From repository root
python scripts/download_datasets.py --all
# Or download specific datasets
python scripts/download_datasets.py --datasets truthfulqa halueval
```

### Manual Download
1. Visit dataset websites
2. Download to appropriate subdirectory
3. Verify checksums (see `checksums.txt`)
4. Run preprocessing scripts if needed

## Data Formats

### Common Formats
- **JSON**: Most benchmarks use JSON format
- **CSV**: For tabular data (TruthfulQA)
- **JSONL**: Line-by-line JSON for large datasets
- **Parquet**: Efficient storage for large datasets

### Preprocessing
Many datasets require preprocessing:
```python
# Example preprocessing script
python scripts/preprocess_truthfulqa.py \
  --input data/truthfulqa/raw \
  --output data/truthfulqa/processed
```

## Dataset Statistics

| Dataset | Questions | Documents | Domains | Year |
|---------|-----------|-----------|---------|------|
| TruthfulQA | 817 | - | 38 | 2022 |
| HaluEval | ~5,000 | - | QA, Dialog, Summ | 2023 |
| FACTSCORE | - | ~3,000 biographies | Biography | 2023 |
| QAMPARI | ~10,000 | ~15,000 | Open-domain | 2022 |
| FELM | ~5,000 | - | Dialogue | 2022 |

## Usage Examples

### Loading TruthfulQA
```python
import json

with open('data/truthfulqa/TruthfulQA.csv', 'r') as f:
    qa_data = load_qa_data(f)

for question in qa_data:
    print(f"Question: {question['question']}")
    print(f"Correct: {question['correct_answers']}")
    print(f"Incorrect: {question['incorrect_answers']}")
```

### Evaluating on HaluEval
```python
from datasets import load_dataset

dataset = load_dataset('csv', data_files='data/halueval/qa_pairs.csv')
for example in dataset:
    prediction = model.generate(example['question'])
    is_hallucination = detect_hallucination(prediction)
```

## Data Quality

### Verification
- Check file sizes match expected values
- Verify number of examples
- Validate JSON/CSV formatting
- Cross-check with paper statistics

### Known Issues
- **Contamination**: Some benchmarks may be in training data
- **Ambiguity**: Some questions have unclear ground truth
- **Date Sensitivity**: Facts may have changed since benchmark creation
- **Language Bias**: Mostly English benchmarks

## Licensing

Each dataset has its own license:
- **TruthfulQA**: Apache 2.0
- **HaluEval**: MIT
- **FACTSCORE**: CC-BY-4.0
- Check individual dataset directories for specific license information

## Citation

When using these datasets, please cite:

```bibtex
@misc{truthfulqa,
  title={TruthfulQA: Measuring How Models Mimic Human Falsehoods},
  author={Lin, Stephanie and Hilton, Jacob and Evans, Owain},
  year={2022}
}

@misc{halueval,
  title={HaluEval: A Large-Scale Hallucination Evaluation Benchmark},
  author={Li, Yixin and others},
  year={2023}
}
```
