# Classification Guide

This document defines the tagging system for LLM for Education research.

---

## Tag Categories

We use **4** tag categories with **16** total tags.

### Category 1: Application Domain

**Purpose**: Describes the primary educational application or use case

**Tags:**
- **Personalized_Learning**: Adaptive systems that customize content, pace, or approach to individual learners
- **Intelligent_Tutoring**: One-on-one tutoring systems providing guided instruction and feedback
- **Assessment**: Automated evaluation, grading, or feedback on student work
- **Content_Generation**: Creation of educational materials, questions, or resources

**Color scheme**: Blue gradient (dark → medium → light → lighter)
- Personalized_Learning: `0052cc` (dark blue)
- Intelligent_Tutoring: `0066ff` (medium blue)
- Assessment: `3399ff` (light blue)
- Content_Generation: `66b3ff` (lighter blue)

**Badge URLs:**
```
https://img.shields.io/badge/Personalized_Learning-0052cc
https://img.shields.io/badge/Intelligent_Tutoring-0066ff
https://img.shields.io/badge/Assessment-3399ff
https://img.shields.io/badge/Content_Generation-66b3ff
```

**Examples:**
- "Adaptive Math Tutor Using GPT-4" uses Intelligent_Tutoring because it provides one-on-one guided instruction
- "Automated Essay Feedback System" uses Assessment because it evaluates student work
- "Personalized Reading Comprehension Coach" uses Personalized_Learning because it adapts to individual learner needs

---

### Category 2: Educational Level

**Purpose**: Specifies the target educational setting or audience

**Tags:**
- **K12**: Kindergarten through 12th grade applications
- **Higher_Ed**: College, university, and post-secondary education
- **Corporate**: Professional training, workplace learning, corporate development
- **Lifelong_Learning**: Self-directed learning, MOOCs, informal learning environments

**Color scheme**: Green gradient (dark → medium → light → lighter)
- K12: `008754` (dark green)
- Higher_Ed: `00a86b` (medium green)
- Corporate: `33d498` (light green)
- Lifelong_Learning: `66e0b8` (lighter green)

**Badge URLs:**
```
https://img.shields.io/badge/K12-008754
https://img.shields.io/badge/Higher_Ed-00a86b
https://img.shields.io/badge/Corporate-33d498
https://img.shields.io/badge/Lifelong_Learning-66e0b8
```

**Examples:**
- "AI Tutor for High School Physics" uses K12 because it targets secondary education
- "ChatGPT in University Writing Centers" uses Higher_Ed because it's deployed in college settings
- "Corporate Training Assistant with LLMs" uses Corporate because it's for workplace learning

---

### Category 3: Technical Approach

**Purpose**: Describes the primary technical method or AI technique

**Tags:**
- **Fine_Tuning**: Models trained/fine-tuned on educational data or tasks
- **RAG**: Retrieval-augmented generation using external knowledge bases
- **Prompt_Engineering**: Systems relying primarily on prompt design without fine-tuning
- **Multi_Agent**: Systems using multiple AI agents or components working together

**Color scheme**: Purple gradient (dark → medium → light → lighter)
- Fine_Tuning: `6554c0` (dark purple)
- RAG: `8066ff` (medium purple)
- Prompt_Engineering: `997dff` (light purple)
- Multi_Agent: `b3a3ff` (lighter purple)

**Badge URLs:**
```
https://img.shields.io/badge/Fine_Tuning-6554c0
https://img.shields.io/badge/RAG-8066ff
https://img.shields.io/badge/Prompt_Engineering-997dff
https://img.shields.io/badge/Multi_Agent-b3a3ff
```

**Examples:**
- "Instruction-Tuned Model for Math Problems" uses Fine_Tuning because the model is trained on educational data
- "Textbook-Grounded QA System" uses RAG because it retrieves from textbook content
- "Chain-of-Thought Tutoring with GPT-4" uses Prompt_Engineering because it relies on prompt design

---

### Category 4: Research Type

**Purpose**: Characterizes the research methodology and contribution type

**Tags:**
- **Empirical**: Papers with experimental validation, user studies, or deployment results
- **System**: Papers presenting new systems, architectures, or technical frameworks
- **Survey**: Literature reviews, meta-analyses, or comprehensive surveys
- **Case_Study**: In-depth analysis of specific implementations or deployments

**Color scheme**: Orange gradient (dark → medium → light → lighter)
- Empirical: `ff6b00` (dark orange)
- System: `ff8c00` (medium orange)
- Survey: `ffab33` (light orange)
- Case_Study: `ffc366` (lighter orange)

**Badge URLs:**
```
https://img.shields.io/badge/Empirical-ff6b00
https://img.shields.io/badge/System-ff8c00
https://img.shields.io/badge/Survey-ffab33
https://img.shields.io/badge/Case_Study-ffc366
```

**Examples:**
- "Randomized Trial of AI Tutor in 50 Classrooms" uses Empirical because it reports experimental results
- "Architecture for Multi-Modal Educational AI" uses System because it presents a new technical framework
- "State of AI in Higher Education: A Review" uses Survey because it's a comprehensive review

---

## Tag Selection Rules

**Required:**
- 1 primary tag from **Application Domain** category (describes what the system does)

**Optional:**
- 1 tag from **Educational Level** category (if applicable, otherwise omit)
- 1 tag from **Technical Approach** category (describes how it works)
- 1 tag from **Research Type** category (describes the contribution type)

**Total: 2-4 tags per paper**

**Default combinations:**
- Most papers: Application Domain + Technical Approach + Research Type (3 tags)
- Deployment studies: Application Domain + Educational Level + Empirical (3 tags)
- Framework papers: Application Domain + Technical Approach + System (3 tags)
- Survey papers: Survey + Application Domain (2 tags, technical approach not applicable)

---

## Selection Decision Tree

```
Start: What is the primary application?
├─ Personalized adaptive system → Personalized_Learning
├─ One-on-one instruction → Intelligent_Tutoring
├─ Grading/feedback on work → Assessment
└─ Creating materials → Content_Generation

Next: What educational level? (optional)
├─ K-12 school → K12
├─ College/university → Higher_Ed
├─ Workplace training → Corporate
└─ Self-directed/MOOC → Lifelong_Learning

Next: What technical approach?
├─ Custom-trained model → Fine_Tuning
├─ Uses external knowledge → RAG
├─ Prompt-based only → Prompt_Engineering
└─ Multiple AI components → Multi_Agent

Next: What research type?
├─ Experimental results → Empirical
├─ New system/architecture → System
├─ Review of existing work → Survey
└─ In-depth single example → Case_Study
```

---

## Color Best Practices

1. **Use gradients within categories**: Dark → medium → light helps visual scanning
2. **Maintain contrast**: All colors meet WCAG AA standards for readability
3. **Distinguish categories**: Different base colors (blue, green, purple, orange) for quick category identification

**Visual pattern in README:**
```
[App Domain] [Edu Level] [Tech] [Type]
Blue        Green    Purple Orange
```

---

## Common Mistakes

- **Don't**: Use multiple tags from the same category (e.g., both K12 and Higher_Ed)
- **Do**: Choose the single most representative tag per category

- **Don't**: Use all 4 categories for every paper
- **Do**: Skip Educational Level if not clearly applicable

- **Don't**: Create new tags without updating this guide
- **Do**: Propose new tags in this document first, then use consistently

- **Don't**: Guess at tag meanings
- **Do**: Refer to tag definitions and examples above

---

## Quick Reference

| Category | Tags | Color | Required? |
|----------|------|-------|-----------|
| Application Domain | Personalized_Learning, Intelligent_Tutoring, Assessment, Content_Generation | Blue | Yes (1) |
| Educational Level | K12, Higher_Ed, Corporate, Lifelong_Learning | Green | Optional |
| Technical Approach | Fine_Tuning, RAG, Prompt_Engineering, Multi_Agent | Purple | Recommended |
| Research Type | Empirical, System, Survey, Case_Study | Orange | Recommended |
