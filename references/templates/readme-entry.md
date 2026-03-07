# README Entry Template

Standard format for adding entries to the research repository README.

---

## Entry Format

```markdown
### [Month]

- **[Item Title]**

    ![Tag1](https://img.shields.io/badge/Tag1_Name-COLOR1)
    ![Tag2](https://img.shields.io/badge/Tag2_Name-COLOR2)
    ![Tag3](https://img.shields.io/badge/Tag3_Name-COLOR3)

    > **Source:** [Venue Name] [Year] [[Link]](url)

    [Sentence 1: What the [item] proposes/presents]
    [Sentence 2: Method/approach and key capability]
    [Sentence 3: Results and impact]
```

---

## Example Entry

```markdown
### February

- **NeuralArchitecture: Efficient Transformer Design**

    ![Computer_Vision](https://img.shields.io/badge/Computer_Vision-0052cc)
    ![Optimization](https://img.shields.io/badge/Optimization-0066ff)
    ![Transformer](https://img.shields.io/badge/Transformer-3399ff)

    > **Source:** NeurIPS 2026 [[Link]](https://arxiv.org/abs/xxxx.xxxxx)

    Proposes NeuralArchitecture, a transformer-based model for efficient image classification. Uses sparse attention mechanisms for reduced computational complexity. Achieves 95.2% accuracy on ImageNet with 40% fewer FLOPs.
```

---

## Summary Writing Guidelines

### Structure
1. **Sentence 1**: Purpose/Contribution - What does the item propose or present?
2. **Sentence 2**: Method/Approach - How does it achieve its goal?
3. **Sentence 3**: Results/Impact - What were the outcomes or implications?

### Requirements
- 2-3 sentences maximum
- Active voice (e.g., "Proposes X", "Presents Y")
- Include key metrics when applicable
- Be concise but informative

### Templates by Item Type (Optional)

**Type 1: Core/System**
```
Proposes [Framework], a [technique]-based system. Uses [method] for [capability].
Achieves [results] on [dataset].
```

**Type 2: Benchmark/Dataset**
```
Presents [Name] benchmark with [N] cases. Assesses [dimensions].
Reveals [limitations].
```

**Type 3: Foundational/Analysis**
```
Focuses on [task] rather than [core capability]. Introduces [Method] for [capability].
Provides [benefit].
```

---

## Badge URL Format

```
https://img.shields.io/badge/Tag_Name-COLOR_CODE
```

**Example badges for common tags:**
```
Supervised_Learning: https://img.shields.io/badge/Supervised_Learning-0052cc
Unsupervised_Learning: https://img.shields.io/badge/Unsupervised_Learning-0066ff
Reinforcement_Learning: https://img.shields.io/badge/Reinforcement_Learning-3399ff
```

---

## Placement in README

Entries should be organized by:
1. **Year** (descending: 2026, 2025, 2024...)
2. **Month** (chronological within year)
3. **Order** (newest items at top of month section)
