# Research Focus

This document explains the research priorities and collection strategy for LLM for Education.

---

## Priority System

### Priority 1: LLM-Powered Educational Applications

**Why this is top priority:**
Core interest in how LLMs are being deployed to solve real educational problems. These systems represent the forefront of AI in education and inform future research directions.

**What we're looking for:**
- Working systems deployed in educational settings (pilot studies or full deployment)
- Novel applications of LLMs to educational tasks (tutoring, assessment, content creation)
- Systems that demonstrate measurable learning outcomes
- Papers addressing specific educational challenges using LLM capabilities

**Search Strategy:**
- Time filter: oneYear (for regular updates)
- Sources: AERA, CHI, L@S, EDM, JEL, ACL, NeurIPS (education tracks), arXiv (cs.AI, cs.CL)
- Key terms: LLM tutoring, AI education system, GPT classroom, large language model learning, educational AI assistant, personalized learning LLM, AI tutor, intelligent tutoring systems LLM

**Example queries:```
LLM personalized learning system student outcomes
GPT tutoring effectiveness educational settings
large language model K-12 classroom deployment
AI writing assistant education learning gains
LLM automated essay scoring reliability
chatbot teaching assistant student engagement
LLM educational chatbot learning analytics
```

---

### Priority 2: Evaluation Methodologies and Learning Measurements

**Why this matters:**
Educational applications need rigorous evaluation. Priority 2 papers provide methods and metrics for assessing whether LLM-based interventions actually work, which is critical for building credible systems.

**What we're looking for:**
- Evaluation frameworks for AI in education
- Learning outcome measurement methodologies
- Comparative studies (AI vs. traditional methods)
- Assessment of LLM limitations and failure modes in educational contexts
- Bias and fairness evaluations in educational AI

**Search Strategy:**
- Time filter: oneMonth (more frequent updates)
- Sources: EDM, JLA, TOCHI, Computers & Education, IEEE TLT
- Key terms: AI education evaluation, learning outcome measurement, educational assessment AI, LLM evaluation education, bias detection educational AI, fairness AI tutoring, automated evaluation educational chatbots

**Example queries:```
LLM education evaluation framework methodology
measuring learning outcomes AI tutoring systems
bias detection large language models education
fairness assessment educational AI systems
comparative study AI tutor human tutor
automated evaluation educational chatbot quality
student engagement measurement AI learning
```

---

### Priority 3: Foundational LLM Capabilities and Educational Theory

**Why we include this:**
Provides theoretical grounding and understanding of LLM capabilities/limitations relevant to education. Includes work on prompt engineering, fine-tuning, and RAG that enable educational applications.

**What we're looking for:**
- LLM capabilities relevant to education (explanation generation, feedback provision)
- Fine-tuning methods for educational content
- Retrieval-augmented generation for educational knowledge bases
- Prompt engineering techniques for educational tasks
- Theoretical work on LLM reasoning, generation quality, hallucination rates

**Critical rule**: Papers that don't include educational applications MUST explicitly state relevance to education in the summary.

**Search Strategy:**
- Time filter: noLimit (historical papers OK)
- Sources: ACL, EMNLP, NeurIPS, ICLR, arXiv (cs.CL, cs.LG)
- Key terms: LLM fine-tuning education, prompt engineering teaching, retrieval augmented generation education, LLM explanation generation, feedback generation AI, knowledge tracing LLM, educational content generation LLM

**Example queries:```
large language model fine-tuning educational content
prompt engineering techniques for teaching
retrieval augmented generation educational applications
LLM explanation generation for students
automated feedback generation student learning
knowledge tracing large language models
hallucination detection educational chatbots
```

---

## Priority Decision Tree

Use this logic to classify papers:

```
Does the paper describe an educational application or deployment?
├─ Yes → Priority 1 (Educational Application)
└─ No → Does the paper focus on evaluation/assessment of educational AI?
    ├─ Yes → Priority 2 (Evaluation & Measurement)
    └─ No → Does the paper address foundational LLM capabilities relevant to education?
        ├─ Yes → Priority 3 (Foundational Work)
        └─ No → Exclude (out of scope)
```

**Examples:**
- "ChatGPT as a Writing Tutor: A Pilot Study in College Composition": Priority 1 (deployed educational application)
- "Evaluating Bias in AI Tutoring Systems Across Demographic Groups": Priority 2 (evaluation methodology)
- "Instruction Tuning for Improved Explanation Generation": Priority 3 (foundational LLM capability relevant to education)

---

## Quality Criteria

**Inclusion criteria for all priorities:**
- Published in peer-reviewed venue (conference, journal, or preprint with clear methodology)
- Provides novel technical contribution or empirical findings
- Includes experimental validation or rigorous analysis (for Priority 1 and 2)

**Exclusion criteria:**
- Non-technical blog posts or opinion pieces without empirical backing
- Papers without clear methodology or evaluation (except pure theoretical work in Priority 3)
- Vendor whitepapers or marketing materials
- Papers that merely apply existing LLMs without novel adaptation or evaluation

---

## Search Query Collection

### Priority 1 Queries (Core Focus)
```
LLM personalized learning system student outcomes
GPT tutoring effectiveness educational settings
large language model K-12 classroom deployment
AI writing assistant education learning gains
LLM automated essay scoring reliability
chatbot teaching assistant student engagement
LLM educational chatbot learning analytics
GPT-4 education pilot study results
AI tutor mathematics learning outcomes
large language model science education
LLM programming tutor computer science
educational AI assistant deployment study
personalized tutoring large language models
LLM homework help effectiveness
AI teaching assistant higher education
LLM language learning application
```

### Priority 2 Queries (Secondary Focus)
```
LLM education evaluation framework methodology
measuring learning outcomes AI tutoring systems
bias detection large language models education
fairness assessment educational AI systems
comparative study AI tutor human tutor
automated evaluation educational chatbot quality
student engagement measurement AI learning
AI education assessment metrics validity
LLM tutoring effectiveness randomized controlled trial
educational chatbot evaluation rubrics
learning analytics AI tutoring systems
AI tutor reliability measurement
educational AI bias mitigation strategies
fairness auditing educational LLM systems
student satisfaction AI tutor survey
```

### Priority 3 Queries (Foundational)
```
large language model fine-tuning educational content
prompt engineering techniques for teaching
retrieval augmented generation educational applications
LLM explanation generation for students
automated feedback generation student learning
knowledge tracing large language models
hallucination detection educational chatbots
instruction tuning educational tasks
LLM reasoning chain of thought education
educational knowledge base construction LLM
few-shot learning educational applications
LLM safety guardrails education
conversational AI educational dialogue systems
LLM adaptive learning systems architecture
```

---
