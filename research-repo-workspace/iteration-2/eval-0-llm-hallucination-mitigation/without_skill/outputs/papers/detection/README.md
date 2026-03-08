# Hallucination Detection Methods

## Overview

This directory contains research papers focusing on detecting hallucinations in Large Language Models. This is the **highest priority** area of research in this repository.

## Key Approaches

### 1. Self-Consistency Methods
Papers focusing on detecting hallucinations through consistency checks across multiple generations.

### 2. Uncertainty Estimation
Methods for quantifying model uncertainty to identify potential hallucinations.

### 3. Automated Fact-Checking
Systems that verify LLM outputs against external knowledge bases.

### 4. Neural Probing
Using probe networks to detect hallucination patterns.

### 5. Contrastive Detection
Methods that distinguish between factual and hallucinated outputs.

## Essential Papers

### Must-Read Foundation Papers
- **Self-Check: Boosting Generative Reliability** (Manakul et al., 2023)
- **Language Models Know What They Know** (Kadavath et al., 2022)
- **Detecting Pretraining Data** (Liu et al., 2023)

### Recent Advances (2023-2024)
- **DoLa: Decoding by Contrasting Layers** (Sun et al., 2023)
- **Self-Contrastive Decoding** (Liu et al., 2023)
- **Hallucination Detection via Attribution** (Mishra et al., 2023)

### Survey and Overview Papers
- **Survey on Hallucination in Large Language Models** (Huang et al., 2023)
- **A Taxonomy of Hallucination Causes** (Zhang et al., 2023)

## Reading Order

For new researchers, we recommend this reading sequence:

1. Start with survey papers for broad understanding
2. Read foundation papers (Self-Check, Calibrating LLMs)
3. Explore specific detection approaches
4. Review recent advances and cutting-edge methods

## Paper Format

Each paper should include:
- Original PDF
- BibTeX citation
- Short summary (1-2 paragraphs)
- Key methodology overview
- Results and performance metrics
- Code implementation link (if available)

## Related Directories
- `/code/detection/` - Implementation of detection methods
- `/notes/literature-review/` - Detailed analysis and summaries
- `/data/baselines/` - Baseline detection systems
