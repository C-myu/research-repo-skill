# Classification Guide

This document defines the tagging system for AI for Mental Health research.

---

## Tag Categories

We use **4** tag categories with **13** total tags.

### Category 1: Application Domain

**Purpose**: Identifies the primary mental health application area of the work

**Tags:**
- **Therapy_Support**: Systems designed for therapeutic interventions, counseling, and clinical mental health support
- **Emotional_Support**: Systems focused on emotional well-being, companionship, and non-clinical emotional support
- **Crisis_Intervention**: Systems designed for crisis response, suicide prevention, and emergency mental health support
- **Wellbeing**: Systems focused on general mental wellness, stress management, and preventive mental health

**Color scheme**: Blue (dark → medium → light → lighter)
- Therapy_Support: `0052cc`
- Emotional_Support: `0066ff`
- Crisis_Intervention: `3399ff`
- Wellbeing: `66b3ff`

**Badge URLs:**
```
https://img.shields.io/badge/Therapy_Support-0052cc
https://img.shields.io/badge/Emotional_Support-0066ff
https://img.shields.io/badge/Crisis_Intervention-3399ff
https://img.shields.io/badge/Wellbeing-66b3ff
```

**Examples:**
- "A Virtual Therapist for CBT Delivery" uses Therapy_Support because it provides clinical therapeutic interventions
- "Empathetic Chatbot for Emotional Support" uses Emotional_Support because it provides non-clinical emotional companionship
- "Crisis Text Line AI Assistant" uses Crisis_Intervention because it handles emergency mental health situations

---

### Category 2: Dialogue Technology

**Purpose**: Identifies the core dialogue system technology or approach

**Tags:**
- **Generative_Model**: Systems using generative approaches (LLMs, seq2seq, transformers) for response generation
- **Retrieval_Based**: Systems using retrieval-based methods for selecting responses
- **Hybrid**: Systems combining multiple approaches (retrieval + generation, rule-based + ML)
- **Rule_Based**: Systems using rule-based, decision tree, or script-based dialogue management

**Color scheme**: Green (dark → medium → light → lighter)
- Generative_Model: `008754`
- Retrieval_Based: `00a86b`
- Hybrid: `33d498`
- Rule_Based: `66e8b8`

**Badge URLs:**
```
https://img.shields.io/badge/Generative_Model-008754
https://img.shields.io/badge/Retrieval_Based-00a86b
https://img.shields.io/badge/Hybrid-33d498
https://img.shields.io/badge/Rule_Based-66e8b8
```

**Examples:**
- "GPT-based Mental Health Chatbot" uses Generative_Model because it uses a generative language model
- "Retrieval-based Counseling System" uses Retrieval_Based because it selects responses from a predefined set

---

### Category 3: Clinical Focus

**Purpose**: Identifies specific mental health conditions or areas of focus

**Tags:**
- **Depression**: Work specifically addressing depression, depressive disorders, or mood improvement
- **Anxiety**: Work focused on anxiety disorders, stress, and anxiety management
- **General_MH**: Work addressing general mental health or multiple conditions

**Color scheme**: Purple (dark → medium → light)
- Depression: `6554c0`
- Anxiety: `8066ff`
- General_MH: `997dff`

**Badge URLs:**
```
https://img.shields.io/badge/Depression-6554c0
https://img.shields.io/badge/Anxiety-8066ff
https://img.shields.io/badge/General_MH-997dff
```

**Examples:**
- "CBT Chatbot for Depression" uses Depression because it specifically targets depressive disorders
- "Anxiety Management Virtual Coach" uses Anxiety because it focuses on anxiety reduction

---

### Category 4: Evaluation Type

**Purpose**: Identifies the primary evaluation methodology used

**Tags:**
- **User_Study**: Work with human user studies, clinical trials, or real-world deployment
- **Automatic_Eval**: Work evaluated using automatic metrics, benchmark datasets, or offline evaluation
- **Survey**: Work that is a survey, review, or meta-analysis of existing research

**Color scheme**: Orange (dark → medium → light)
- User_Study: `ff6b00`
- Automatic_Eval: `ff8c00`
- Survey: `ffab33`

**Badge URLs:**
```
https://img.shields.io/badge/User_Study-ff6b00
https://img.shields.io/badge/Automatic_Eval-ff8c00
https://img.shields.io/badge/Survey-ffab33
```

**Examples:**
- "Randomized Controlled Trial of Therapy Bot" uses User_Study because it includes human participants
- "A Survey of Mental Health Chatbots" uses Survey because it reviews existing work

---

## Tag Selection Rules

**Required:**
- 1 primary tag from **Application Domain** category
- 1 tag from **Dialogue Technology** category

**Optional:**
- 1 tag from **Clinical Focus** category (if applicable)
- 1 tag from **Evaluation Type** category

**Total: 2-4 tags per paper**

---

## Selection Decision Tree

```
Start: What is the primary application domain?
├─ Clinical therapy/counseling → Therapy_Support
├─ Non-clinical emotional support → Emotional_Support
├─ Crisis/emergency response → Crisis_Intervention
└─ General wellness/prevention → Wellbeing

Then: What dialogue technology is used?
├─ Generative models (LLMs, seq2seq) → Generative_Model
├─ Retrieval from database → Retrieval_Based
├─ Combination of methods → Hybrid
└─ Rules/scripts → Rule_Based

Then (optional): Specific mental health focus?
├─ Depression → Depression
├─ Anxiety → Anxiety
└─ General/multiple → General_MH

Then (optional): How was it evaluated?
├─ Human participants → User_Study
├─ Automatic metrics → Automatic_Eval
└─ Review paper → Survey
```

---

## Color Best Practices

1. **Use gradients within categories**: Dark → medium → light → lighter
2. **Maintain contrast**: Ensure WCAG AA compliance (4.5:1 ratio)
3. **Distinguish categories**: Use different base colors (blue, green, purple, orange)

**Recommended color values:**
- Blue: `0052cc`, `0066ff`, `3399ff`, `66b3ff`
- Green: `008754`, `00a86b`, `33d498`, `66e8b8`
- Purple: `6554c0`, `8066ff`, `997dff`
- Orange: `ff6b00`, `ff8c00`, `ffab33`

---

## Common Mistakes

- **Don't**: Use more than 4 tags (too many dilutes meaning)
- **Do**: Focus on 2-3 most relevant tags

- **Don't**: Mix tags from same category (e.g., 2 Clinical Focus tags)
- **Do**: Choose one representative tag per category max

- **Don't**: Use tags without understanding their definition
- **Do**: Refer to this guide when unsure

- **Don't**: Skip the required Application Domain tag
- **Do**: Always include at least one tag from Category 1

---

## Example Classifications

**Example 1:**
- Paper: "A GPT-based Virtual Therapist for Depression"
- Tags: Therapy_Support, Generative_Model, Depression, User_Study
- Rationale: Clinical application (Therapy_Support), uses GPT (Generative_Model), targets depression (Depression), evaluated with users (User_Study)

**Example 2:**
- Paper: "Retrieval-based Emotional Support Chatbot"
- Tags: Emotional_Support, Retrieval_Based, Automatic_Eval
- Rationale: Non-clinical support (Emotional_Support), retrieval-based (Retrieval_Based), automatic evaluation (Automatic_Eval)

**Example 3:**
- Paper: "Survey of Mental Health Dialogue Systems"
- Tags: General_MH, Survey
- Rationale: Covers general mental health (General_MH), is a survey paper (Survey)

---
