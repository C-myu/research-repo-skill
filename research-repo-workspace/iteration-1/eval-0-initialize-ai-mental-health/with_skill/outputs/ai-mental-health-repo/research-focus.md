# Research Focus

This document explains the research priorities and collection strategy for AI for Mental Health.

---

## Priority System

### Priority 1: Multi-turn Dialogue Systems for Mental Health

**Why this is top priority:**
Multi-turn dialogue systems represent the core intersection of AI and mental health support. These systems engage in extended conversations with users, building context and rapport over multiple exchanges - essential for effective mental health interventions, therapy, and emotional support.

**What we're looking for:**
- Systems that maintain conversation context across multiple turns
- Mental health chatbots, virtual therapists, and counseling agents
- Empathy-driven dialogue models with emotional intelligence
- Systems with proven effectiveness through user studies or clinical trials
- Real-world deployed systems and advanced research prototypes

**Search Strategy:**
- Time filter: oneYear (for regular updates)
- Sources: ACL, EMNLP, NeurIPS, ICML, ICLR, CHI, CSCW, AAAI, JAMIA, JMIR, arXiv (cs.CL, cs.HC)
- Key terms: mental health dialogue, conversational agents, emotional support chatbot, therapy bot, counseling AI, empathetic dialogue, mental health NLP

**Example queries:**
```
mental health dialogue system multi-turn
conversational agent emotional support chatbot
AI therapy bot empathy dialogue
virtual counselor mental health support
chat-based intervention mental health
```

---

### Priority 2: Dialogue Technologies and Evaluation Methods

**Why this matters:**
Supporting technologies and evaluation methodologies are critical for advancing mental health dialogue systems. This includes dialogue management, response generation, safety mechanisms, and evaluation frameworks specific to mental health applications.

**What we're looking for:**
- Dialogue management and response generation techniques
- Safety and ethics in mental health AI systems
- Evaluation methods for mental health chatbots and dialogue systems
- User study methodologies for mental health technology
- Dataset creation for mental health conversations
- Personalization and adaptation in dialogue systems

**Search Strategy:**
- Time filter: oneMonth (more frequent updates)
- Sources: ACL, EMNLP, CHI, CSCW, LREC, Interspeech
- Key terms: dialogue evaluation, safety AI mental health, mental health dataset, empathetic response generation, conversational safety

**Example queries:**
```
mental health dialogue evaluation framework
safety mechanisms mental health chatbot
empathetic response generation dialogue
conversational dataset mental health
personalization dialogue system therapy
```

---

### Priority 3: Foundational Dialogue and NLP Technologies

**Why we include this:**
Foundational work in dialogue systems, NLP, and emotional AI provides the building blocks for mental health applications. Understanding these core technologies is essential for advancing the field.

**What we're looking for:**
- General dialogue systems and conversational AI
- Emotion recognition and sentiment analysis
- Context-aware language models for dialogue
- Psychological text analysis and linguistic markers
- Ethical frameworks for AI in healthcare

**Critical rule**: Papers must demonstrate clear relevance to mental health applications either through explicit discussion or obvious applicability to emotional/supportive conversations.

**Search Strategy:**
- Time filter: noLimit (historical papers OK)
- Sources: ACL, EMNLP, NeurIPS, ICML, ICLR, CHI, AAAI
- Key terms: dialogue system, empathetic computing, emotion recognition AI, psychological NLP, conversational AI

**Example queries:**
```
empathetic dialogue system transformer
emotion recognition conversational AI
psychological text analysis NLP
context-aware dialogue model
ethical AI healthcare chatbot
```

---

## Priority Decision Tree

Use this logic to classify papers:

```
Does the paper focus on mental health dialogue systems?
├─ Yes → Priority 1
└─ No
    ├─ Does it address dialogue technologies or evaluation for mental health?
    │   ├─ Yes → Priority 2
    │   └─ No
    │       ├─ Is it foundational dialogue/NLP work relevant to mental health?
    │       │   ├─ Yes → Priority 3
    │       └─ No → Exclude (out of scope)
```

**Examples:**
- "A Multi-turn Dialogue System for Depression Screening": Priority 1 (direct focus on mental health dialogue)
- "Evaluating Safety in Mental Health Chatbots": Priority 2 (evaluation methodology for mental health AI)
- "Empathetic Dialogue Models with Transformers": Priority 3 (foundational dialogue technology applicable to mental health)
- "Sentiment Analysis for Product Reviews": Exclude (not relevant to mental health)

---

## Quality Criteria

**Inclusion criteria for all priorities:**
- Published in peer-reviewed venue or preprint with clear technical contribution
- Includes empirical validation (user studies, experiments, or system evaluation)
- Provides novel technical contribution or comprehensive survey
- Clear relevance to mental health support or dialogue systems

**Exclusion criteria:**
- Pure opinion pieces without technical content
- Non-technical blog posts or news articles
- Work without any empirical evaluation
- General NLP papers with no clear connection to dialogue or mental health

---

## Search Query Collection

### Priority 1 Queries (Core Focus)
```
"mental health dialogue system" multi-turn
"conversational agent" "emotional support" chatbot
AI therapy bot empathy dialogue
virtual counselor mental health support
"chat-based intervention" mental health
"mental health chatbot" user study
"counseling chatbot" clinical trial
"emotional support" dialogue system
"virtual therapist" conversational AI
"mental health support" chatbot NLP
"crisis counseling" dialogue system
"psychological support" conversational agent
"depression screening" dialogue
"anxiety support" chatbot
"well-being assistant" dialogue
"mental health intervention" conversational
```

### Priority 2 Queries (Secondary Focus)
```
"mental health dialogue" evaluation framework
safety mechanisms "mental health chatbot"
"empathetic response generation" dialogue
"conversational dataset" mental health
personalization "dialogue system" therapy
"dialogue management" mental health
"response generation" emotional support
"user study" mental health chatbot
"mental health corpus" dialogue
"safety evaluation" healthcare chatbot
"conversation quality" mental health AI
"ethical guidelines" mental health chatbot
"risk assessment" dialogue system mental health
"clinical evaluation" conversational agent
```

### Priority 3 Queries (Foundational)
```
"empathetic dialogue" transformer
"emotion recognition" conversational AI
"psychological text analysis" NLP
"context-aware dialogue" model
"ethical AI" healthcare chatbot
"emotional intelligence" dialogue system
"affective computing" dialogue
"sentiment analysis" mental health
"commonsense reasoning" dialogue
"personalization" conversational AI
"dialogue act" classification
"response selection" dialogue
"neural dialogue" model
"grounding" dialogue system
```

---
