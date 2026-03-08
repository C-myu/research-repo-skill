# Classification Guide

This document defines the tagging system for LLM for Education research.

---

## Tag Categories

We use **4** tag categories with **12** total tags.

### Category 1: Educational Application

**Purpose**: Identifies the primary educational context or domain where the LLM is applied.

**Tags:**
- **Tutoring_System**: Intelligent tutoring and one-on-one learning assistance
- **Writing_Assistance**: Automated feedback on writing, essays, and composition
- **Assessment**: Automated grading, scoring, and evaluation of student work
- **Content_Generation**: Creation of educational materials, questions, and resources

**Color scheme**: Blue (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/Tutoring_System-0052cc
https://img.shields.io/badge/Writing_Assistance-0066ff
https://img.shields.io/badge/Assessment-3399ff
https://img.shields.io/badge/Content_Generation-5c8aff
```

**Examples:**
- "ChatGPT as a Math Tutor" uses Tutoring_System because it provides one-on-one tutoring
- "Automated Essay Feedback with GPT-4" uses Writing_Assistance because it focuses on writing improvement
- "LLM-based Automated Grading System" uses Assessment because it evaluates student work
- "Generating Practice Problems with Language Models" uses Content_Generation because it creates educational materials

---

### Category 2: LLM Technique

**Purpose**: Describes the core LLM method or technique used in the work.

**Tags:**
- **Instruction_Tuning**: Fine-tuning LLMs with instruction-following data
- **Prompt_Engineering**: Designing effective prompts without model updates
- **Fine_Tuning**: Domain-specific adaptation through continued pre-training or fine-tuning
- **RAG**: Retrieval-Augmented Generation and knowledge retrieval approaches

**Color scheme**: Green (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/Instruction_Tuning-008754
https://img.shields.io/badge/Prompt_Engineering-00a86b
https://img.shields.io/badge/Fine_Tuning-33d498
https://img.shields.io/badge/RAG-66e3b8
```

**Examples:**
- "EduChat: An Instruction-Tuned Model for Education" uses Instruction_Tuning because it fine-tunes on educational instructions
- "Zero-Shot Tutoring with ChatGPT" uses Prompt_Engineering because it relies on prompt design
- "Domain-Adapted LLM for Science Education" uses Fine_Tuning because it adapts the model
- "Retrieval-Augmented Educational Q&A" uses RAG because it retrieves external knowledge

---

### Category 3: Education Level

**Purpose**: Specifies the educational level or target audience.

**Tags:**
- **K12**: Kindergarten through 12th grade education
- **Higher_Ed**: College, university, and adult learning
- **Professional**: Workplace training and professional development
- **Lifelong**: General learning outside formal education

**Color scheme**: Purple (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/K12-6554c0
https://img.shields.io/badge/Higher_Ed-8066ff
https://img.shields.io/badge/Lifelong-997dff
https://img.shields.io/badge/Professional-b3a3ff
```

**Examples:**
- "LLM for Elementary Math Tutoring" uses K12 because it targets elementary education
- "University Writing Assistant with GPT-4" uses Higher_Ed because it serves college students
- "Corporate Training with ChatGPT" uses Professional because it's workplace training
- "General Knowledge Learning Assistant" uses Lifelong because it's for informal learning

---

### Category 4: Evaluation Method

**Purpose**: Identifies how the educational effectiveness is measured or validated.

**Tags:**
- **Classroom_Study**: Real-world deployment with actual students in classrooms
- **User_Study**: Controlled experiments with human participants
- **Benchmark**: Evaluation on standardized educational datasets
- **Simulation**: Automated evaluation or simulated environments

**Color scheme**: Orange (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/Classroom_Study-ff6b00
https://img.shields.io/badge/User_Study-ff8c00
https://img.shields.io/badge/Benchmark-ffab33
https://img.shields.io/badge/Simulation-ffc366
```

**Examples:**
- "Deploying ChatGPT in 10 Classrooms" uses Classroom_Study because it's a real deployment
- "User Study of AI Writing Feedback" uses User_Study because it's a controlled experiment
- "Evaluating Math Word Problem Solving" uses Benchmark because it uses a dataset
- "Simulated Student Evaluation Framework" uses Simulation because it's automated testing

---

## Tag Selection Rules

**Required:**
- 1 primary tag from **Educational Application** category

**Optional:**
- 1 LLM technique tag from **LLM Technique** category
- 1 education level tag from **Education Level** category (if applicable)
- 1 evaluation method tag from **Evaluation Method** category (if specified)

**Total: 2-4 tags per paper**

---

## Selection Decision Tree

```
Start: What is the primary educational use case?
├─ One-on-one teaching or tutoring → Tutoring_System
├─ Improving writing or essays → Writing_Assistance
├─ Grading or evaluating student work → Assessment
└─ Creating educational materials → Content_Generation

Then: What LLM technique is central to the work?
├─ Custom fine-tuned model → Instruction_Tuning or Fine_Tuning
├─ Clever prompt design only → Prompt_Engineering
├─ Uses external knowledge retrieval → RAG
└─ Not specified or applies multiple → (skip this tag)

Then: What education level is targeted? (if applicable)
├─ K-12 students → K12
├─ College/university → Higher_Ed
├─ Workplace training → Professional
└─ General informal learning → Lifelong

Finally: How was it evaluated? (if specified)
├─ Real classroom deployment → Classroom_Study
├─ Controlled experiment with participants → User_Study
├─ Standardized dataset → Benchmark
└─ Automated/simulated evaluation → Simulation
```

---

## Color Best Practices

1. **Use gradients within categories**: Dark → medium → light
2. **Maintain contrast**: Ensure WCAG AA compliance (4.5:1 ratio)
3. **Distinguish categories**: Use different base colors (blue, green, purple, orange)

**Recommended color values:**
- Blue: `0052cc`, `0066ff`, `3399ff`, `5c8aff`
- Green: `008754`, `00a86b`, `33d498`, `66e3b8`
- Purple: `6554c0`, `8066ff`, `997dff`, `b3a3ff`
- Orange: `ff6b00`, `ff8c00`, `ffab33`, `ffc366`

---

## Common Mistakes

- **Don't**: Use more than 4 tags (too many dilutes meaning)
- **Do**: Focus on 2-3 most relevant tags

- **Don't**: Skip the Educational Application tag (it's required)
- **Do**: Always select one primary educational use case

- **Don't**: Use tags without understanding their definition
- **Do**: Refer to this guide when unsure

- **Don't**: Add Evaluation Method tag if not specified in paper
- **Do**: Skip optional categories if information is unclear

---

## Complete Tag Reference

| Tag | Category | Color Code | Badge URL |
|-----|----------|------------|-----------|
| Tutoring_System | Educational Application | #0052cc | [![Tutoring_System](https://img.shields.io/badge/Tutoring_System-0052cc)](https://img.shields.io/badge/Tutoring_System-0052cc) |
| Writing_Assistance | Educational Application | #0066ff | [![Writing_Assistance](https://img.shields.io/badge/Writing_Assistance-0066ff)](https://img.shields.io/badge/Writing_Assistance-0066ff) |
| Assessment | Educational Application | #3399ff | [![Assessment](https://img.shields.io/badge/Assessment-3399ff)](https://img.shields.io/badge/Assessment-3399ff) |
| Content_Generation | Educational Application | #5c8aff | [![Content_Generation](https://img.shields.io/badge/Content_Generation-5c8aff)](https://img.shields.io/badge/Content_Generation-5c8aff) |
| Instruction_Tuning | LLM Technique | #008754 | [![Instruction_Tuning](https://img.shields.io/badge/Instruction_Tuning-008754)](https://img.shields.io/badge/Instruction_Tuning-008754) |
| Prompt_Engineering | LLM Technique | #00a86b | [![Prompt_Engineering](https://img.shields.io/badge/Prompt_Engineering-00a86b)](https://img.shields.io/badge/Prompt_Engineering-00a86b) |
| Fine_Tuning | LLM Technique | #33d498 | [![Fine_Tuning](https://img.shields.io/badge/Fine_Tuning-33d498)](https://img.shields.io/badge/Fine_Tuning-33d498) |
| RAG | LLM Technique | #66e3b8 | [![RAG](https://img.shields.io/badge/RAG-66e3b8)](https://img.shields.io/badge/RAG-66e3b8) |
| K12 | Education Level | #6554c0 | [![K12](https://img.shields.io/badge/K12-6554c0)](https://img.shields.io/badge/K12-6554c0) |
| Higher_Ed | Education Level | #8066ff | [![Higher_Ed](https://img.shields.io/badge/Higher_Ed-8066ff)](https://img.shields.io/badge/Higher_Ed-8066ff) |
| Lifelong | Education Level | #997dff | [![Lifelong](https://img.shields.io/badge/Lifelong-997dff)](https://img.shields.io/badge/Lifelong-997dff) |
| Professional | Education Level | #b3a3ff | [![Professional](https://img.shields.io/badge/Professional-b3a3ff)](https://img.shields.io/badge/Professional-b3a3ff) |
| Classroom_Study | Evaluation Method | #ff6b00 | [![Classroom_Study](https://img.shields.io/badge/Classroom_Study-ff6b00)](https://img.shields.io/badge/Classroom_Study-ff6b00) |
| User_Study | Evaluation Method | #ff8c00 | [![User_Study](https://img.shields.io/badge/User_Study-ff8c00)](https://img.shields.io/badge/User_Study-ff8c00) |
| Benchmark | Evaluation Method | #ffab33 | [![Benchmark](https://img.shields.io/badge/Benchmark-ffab33)](https://img.shields.io/badge/Benchmark-ffab33) |
| Simulation | Evaluation Method | #ffc366 | [![Simulation](https://img.shields.io/badge/Simulation-ffc366)](https://img.shields.io/badge/Simulation-ffc366) |
