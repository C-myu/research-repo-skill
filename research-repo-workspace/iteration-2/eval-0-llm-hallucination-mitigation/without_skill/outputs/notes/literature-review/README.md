# Literature Review

## Overview

This directory contains literature reviews, summaries, and analyses of papers on LLM hallucination mitigation.

## Review Categories

### 1. Detection Methods Survey

**File**: `detection_survey.md`

**Key Papers Reviewed**:
- Self-Check (Manakul et al., 2023)
- DoLa (Sun et al., 2023)
- Language Models Know What They Know (Kadavath et al., 2022)

**Main Findings**:
- Self-consistency methods show strong performance but require multiple generations
- Uncertainty-based methods are fast but less accurate
- Hybrid approaches (consistency + uncertainty) perform best
- Detection accuracy varies significantly across domains

**Research Gaps**:
- Limited evaluation on multilingual models
- Scalability challenges for real-time detection
- Lack of standardized evaluation protocols

### 2. Alignment and Training Methods

**File**: `alignment_methods_review.md`

**Key Papers Reviewed**:
- Constitutional AI (Bai et al., 2022)
- RAG for Hallucination Reduction (Lewis et al., 2020)
- RLHF for Truthfulness (Ouyang et al., 2022)

**Main Findings**:
- RAG consistently reduces factual hallucinations by 20-40%
- RLHF improves truthfulness but can reduce creativity
- Constitutional AI shows promise for scalable alignment
- Training data quality is more important than quantity

**Research Gaps**:
- Limited understanding of long-term effectiveness
- Trade-offs between truthfulness and other capabilities
- Computational cost of advanced training methods

### 3. Evaluation Benchmarks

**File**: `evaluation_benchmarks_review.md`

**Key Papers Reviewed**:
- TruthfulQA (Lin et al., 2022)
- FACTSCORE (Min et al., 2023)
- HaluEval (Li et al., 2023)

**Main Findings**:
- No single benchmark captures all aspects of hallucination
- TruthfulQA focuses on common misconceptions
- FACTSCORE provides fine-grained analysis
- HaluEval offers comprehensive task coverage

**Benchmark Limitations**:
- Contamination in training data
- English-centric evaluation
- Limited domain coverage
- Temporal staleness of facts

## Detailed Paper Summaries

### Self-Check: Boosting Generative Reliability

**Authors**: Manakul et al. (2023)

**Method**:
1. Generate multiple responses to the same prompt
2. Generate questions for each response
3. Generate answers to those questions
4. Check consistency across generations

**Strengths**:
- Model-agnostic (works with any LLM)
- No additional training required
- Strong detection performance (72% on HaluEval)

**Weaknesses**:
- Computationally expensive (5-10x inference cost)
- Requires multiple API calls for closed-source models
- Slower latency makes it impractical for real-time use

**Key Results**:
- 72% accuracy on HaluEval QA task
- 68% accuracy on dialogue task
- Detects both factual and logical hallucinations

### DoLa: Decoding by Contrasting Layers

**Authors**: Sun et al. (2023)

**Method**:
1. Contrast early-layer (factual) and late-layer (linguistic) predictions
2. Use early layer logits to guide generation
3. Select tokens with high factual confidence

**Strengths**:
- No additional inference cost (single pass)
- Works at generation time
- Improves both truthfulness and fluency

**Weaknesses**:
- Requires access to model internals (not for closed APIs)
- Optimal layer selection varies by model
- Limited evaluation on diverse tasks

**Key Results**:
- 71% accuracy on HaluEval
- Reduces hallucination rate by 15-30%
- Minimal impact on generation quality

### TruthfulQA: Measuring How Models Mimic Human Falsehoods

**Authors**: Lin et al. (2022)

**Benchmark Design**:
- 817 questions across 38 categories
- Questions where humans often give incorrect answers
- Measures truthfulness vs. human mimicry

**Key Insights**:
- Models often mimic human misconceptions
- Larger models can be less truthful
- Fine-tuning on human data can increase mimicry

**Benchmark Limitations**:
- Focuses on common misconceptions (not all hallucinations)
- Some questions have ambiguous ground truth
- Limited to English language

## Research Themes

### Theme 1: Accuracy vs. Creativity Trade-off

**Observation**: Methods that reduce hallucinations often reduce creative capabilities

**Examples**:
- RAG improves factuality but limits response diversity
- RLHF improves truthfulness but reduces open-ended generation
- Conservative decoding reduces errors but makes responses bland

**Open Questions**:
- Can we develop methods that reduce hallucinations without harming creativity?
- How to measure the trade-off quantitatively?
- When is factuality more important than creativity?

### Theme 2: Detection vs. Prevention

**Two Approaches**:
1. **Detection**: Identify hallucinations after generation
2. **Prevention**: Train models to not hallucinate

**Comparison**:
- Detection: Can use any method, but requires post-processing
- Prevention: Built into model, but requires retraining
- Hybrid: Detect during generation and guide model away

**Research Direction**: Combine detection and prevention for optimal results

### Theme 3: Knowledge Cutoff and Temporal Dynamics

**Challenge**: LLMs have fixed knowledge from training cutoff date

**Solutions**:
1. **RAG**: Retrieve current information
2. **Continual Learning**: Update model with new data
3. **Hybrid**: Use both approaches

**Open Problems**:
- How to handle conflicting information over time?
- How to update models efficiently?
- How to evaluate temporal factuality?

## Future Research Directions

### High-Priority Directions

1. **Efficient Detection Methods**
   - Reduce computational cost of self-consistency methods
   - Develop single-pass detection
   - Real-time hallucination detection

2. **Multilingual Factuality**
   - Most benchmarks are English-only
   - Need cross-lingual evaluation
   - Cultural considerations in factuality

3. **Domain-Specific Methods**
   - Medical, legal, scientific domains
   - Different hallucination types per domain
   - Specialized evaluation benchmarks

4. **Causal Understanding**
   - Current methods are correlational
   - Need to understand *why* models hallucinate
   - Causal interventions to reduce hallucinations

5. **Explainable Detection**
   - Not just detecting, but explaining *why* it's a hallucination
   - Attribution to specific sources
   - User-facing explanations

### Medium-Priority Directions

6. **Adversarial Robustness**
   - Models should resist prompts designed to cause hallucinations
   - Evaluate on adversarial examples
   - Robust training methods

7. **Evaluation Standardization**
   - Standard metrics across papers
   - Shared evaluation protocols
   - Leaderboards and benchmarks

8. **Cost-Benefit Analysis**
   - Computational cost vs. accuracy improvement
   - When is simple detection "good enough"?
   - Resource-constrained deployment

### Lower-Priority (but Important)

9. **User Studies**
   - How do users perceive different levels of factuality?
   - What level of hallucination is acceptable?
   - Trust calibration in user-facing systems

10. **Legal and Ethical Considerations**
    - Liability for hallucinations
    - Disclosure requirements
    - Ethical guidelines for deployment

## Citation Graph

### Key Papers and Their Connections

```
Base Models (GPT-3, LLaMA, etc.)
    ↓
[Detection Methods]
    ├─→ Self-Check (2023) ──┐
    ├─→ DoLa (2023) ─────────┤
    └─→ Uncertainty (2022) ──┤
                             │
[Evaluation] ←───────────────┘
    ├─→ TruthfulQA (2022) ───┐
    ├─→ FACTSCORE (2023) ─────┤
    └─→ HaluEval (2023) ──────┤
                              │
[Training Methods] ←──────────┘
    ├─→ RAG (2020)
    ├─→ RLHF (2022)
    └─→ Constitutional AI (2022)
         ↓
[Applications]
    ├─→ Medical QA
    ├─→ Legal Assistant
    └─→ Education
```

## Reading Recommendations

### For Beginners
1. Start with survey papers for broad understanding
2. Read TruthfulQA paper to understand evaluation
3. Study Self-Check for practical detection
4. Review RAG papers for prevention methods

### For Researchers
1. Deep dive into detection methods (DoLa, Self-Check)
2. Study RLHF and Constitutional AI
3. Analyze evaluation benchmarks deeply
4. Identify research gaps from recent papers

### For Practitioners
1. Focus on practical methods (RAG, simple consistency checks)
2. Understand trade-offs between accuracy and cost
3. Study evaluation methods relevant to your domain
4. Review deployment case studies

## Related Files
- `/papers/` - Full papers organized by category
- `/notes/implementation-ideas/` - Practical implementation notes
- `/experiments/` - Experimental results and insights
