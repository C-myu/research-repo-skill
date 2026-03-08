# Research Focus

This document explains the research priorities and collection strategy for LLM for Education.

---

## Priority System

### Priority 1: Educational Applications & Impact

**Why this is top priority:**
The core value of LLM research in education lies in practical applications that improve learning outcomes. These papers demonstrate how LLMs can be effectively deployed in real educational settings to benefit students and teachers.

**What we're looking for:**
- Papers that demonstrate measurable improvements in learning outcomes
- Intelligent tutoring systems and personalized learning platforms
- Automated feedback and assessment systems
- LLM-based educational tools deployed in real classrooms
- Studies with rigorous evaluation on actual learners

**Search Strategy:**
- Time filter: oneYear (for regular updates)
- Sources: NeurIPS, ICML, ACL, AAAI, CHI, CSCL, EDM, LAK, AERA
- Key terms: LLM education, intelligent tutoring, personalized learning, automated feedback, educational assessment, learning outcomes, student performance

**Example queries:```
large language model education learning outcomes
LLM intelligent tutoring system evaluation
personalized learning language model student
automated feedback generation education assessment
chatgpt education classroom deployment study
```

---

### Priority 2: LLM Techniques for Education

**Why this matters:**
Technical innovations in LLM design and adaptation that specifically address educational challenges. These methods may not always have classroom deployments yet, but show promise for educational applications.

**What we're looking for:**
- Instruction tuning and prompt engineering for educational tasks
- Few-shot learning adaptations for educational content
- Knowledge distillation for student model training
- Domain adaptation techniques for educational corpora
- Safety and bias mitigation in educational LLMs
- Multi-modal LLMs for educational content understanding

**Search Strategy:**
- Time filter: oneMonth (more frequent updates)
- Sources: ACL, EMNLP, NAACL, ICLR, NeurIPS, arXiv
- Key terms: instruction tuning education, prompt engineering learning, knowledge distillation student models, educational LLM, domain adaptation education

**Example queries:```
instruction tuning educational tasks
prompt engineering learning effectiveness
knowledge distillation student models
LLM fine-tuning educational content
educational chatbot safety bias mitigation
```

---

### Priority 3: Foundational Work & Theory

**Why we include this:**
Seminal papers and theoretical foundations that establish the core concepts, methodologies, and evaluation frameworks for using language models in educational contexts.

**What we're looking for:**
- Early work on dialogue-based tutoring systems
- Natural language processing for educational applications
- Automated essay scoring and feedback systems
- Student modeling and knowledge tracing
- Theoretical frameworks for AI in education
- Evaluation methodologies for educational AI systems

**Critical rule**: Papers that don't include empirical validation with educational tasks or learners MUST explicitly state their theoretical contribution in the summary.

**Search Strategy:**
- Time filter: noLimit (historical papers OK)
- Sources: AIED, ITS, EDM, CHI, ACL, AAAI
- Key terms: intelligent tutoring systems, automated essay scoring, student modeling, knowledge tracing, dialogue tutoring, NLP education

**Example queries:```
intelligent tutoring systems foundations
automated essay scoring NLP
student modeling knowledge tracing
dialogue tutoring system natural language
educational data mining theoretical framework
```

---

## Priority Decision Tree

Use this logic to classify papers:

```
Does the paper include empirical evaluation with learners or educational tasks?
├─ Yes (measurable learning impact) → Priority 1
└─ No (technical innovation without deployment)
    ├─ Is it a novel LLM technique for educational applications? → Priority 2
    └─ Is it theoretical, foundational, or a survey without new techniques? → Priority 3
```

**Examples:**
- "ChatGPT in the Classroom: A Study of AI Tutoring Effectiveness" → Priority 1 (direct educational impact)
- "Instruction Tuning for Mathematical Reasoning" → Priority 2 (educational application, no deployment)
- "A Survey of Intelligent Tutoring Systems: 1980-2020" → Priority 3 (foundational survey)

---

## Quality Criteria

**Inclusion criteria for all priorities:**
- Published in peer-reviewed venue (conference, journal, workshop)
- Provides novel technical contribution or comprehensive review
- Includes experimental validation (for Priority 1 and 2)
- Clearly articulates educational relevance

**Exclusion criteria:**
- Non-technical blog posts or opinion pieces without peer review
- Papers without clear connection to education or learning
- Work that uses LLMs for education without addressing pedagogical concerns
- Purely theoretical work without practical relevance

---

## Search Query Collection

### Priority 1 Queries (Educational Applications & Impact)

**Time filter**: oneYear

```
large language model education learning outcomes study
LLM intelligent tutoring system student performance
personalized learning chatGPT classroom effectiveness
automated feedback generation education assessment LLM
educational chatbot learning impact empirical study
language model writing feedback student improvement
tutoring system large language model evaluation
LLM personalized learning platform deployment
AI tutor education effectiveness randomized trial
ChatGPT education classroom case study
LLM automated grading education assessment
intelligent tutoring system language learning outcomes
large language model STEM education effectiveness
educational LLM student engagement learning
LLM teacher support classroom assistant
```

### Priority 2 Queries (LLM Techniques for Education)

**Time filter**: oneMonth

```
instruction tuning educational tasks LLM
prompt engineering learning effectiveness education
knowledge distillation student model training
LLM fine-tuning educational domain adaptation
educational chatbot safety bias mitigation
multi-modal LLM educational content understanding
few-shot learning educational applications
LLM reasoning tasks education tuning
language model mathematical reasoning education
educational prompt optimization learning
LLM adaptation educational corpora training
```

### Priority 3 Queries (Foundational Work & Theory)

**Time filter**: noLimit

```
intelligent tutoring systems foundational survey
automated essay scoring natural language processing
student modeling knowledge tracing overview
dialogue tutoring system architecture
educational data mining theoretical framework
natural language processing education review
AI education evaluation methodology
adaptive learning systems theoretical foundation
```
