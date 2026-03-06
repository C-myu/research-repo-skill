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

- **CARE: Therapeutic Alliance Assessment**

    ![Specific_Therapy](https://img.shields.io/badge/Specific_Therapy-0052cc)
    ![Data_Collection](https://img.shields.io/badge/Data_Collection-0066ff)
    ![CBT](https://img.shields.io/badge/CBT-3399ff)

    > **Source:** JMIR 2026 [[Link]](https://arxiv.org/abs/xxxx.xxxxx)

    Proposes CARE, a CBT-based system for assessing therapeutic alliance. Uses expert-annotated rationales with 9,516 samples. Achieves 78.5% F1 score on WAI scale prediction.
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

### Templates by Item Type

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
Data_Synthesis: https://img.shields.io/badge/Data_Synthesis-0052cc
Data_Collection: https://img.shields.io/badge/Data_Collection-0066ff
Data_Analysis: https://img.shields.io/badge/Data_Analysis-3399ff
```

---

## Placement in README

Entries should be organized by:
1. **Year** (descending: 2026, 2025, 2024...)
2. **Month** (chronological within year)
3. **Order** (newest items at top of month section)
