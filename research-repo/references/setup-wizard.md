# Research Repository Setup Wizard

This guide walks you through configuring a new research repository step-by-step. Use this when creating a repository for a new research domain.

> **Note**: This wizard references the template files in [templates/](templates/). Refer to those files for complete template content.

---

## Table of Contents

1. [Phase 1: Define Your Domain](#phase-1-define-your-domain)
   - Domain Name
   - Repository Purpose Statement
2. [Phase 2: Define Research Priorities](#phase-2-define-research-priorities)
   - Identify Priority Levels
   - Write Priority Justification
3. [Phase 3: Create Tag Taxonomy](#phase-3-create-tag-taxonomy)
   - Define Tag Categories
   - Define Tags per Category
   - Assign Color Scheme
   - Define Tag Selection Rules
4. [Phase 4: Write Search Queries](#phase-4-write-search-queries)
   - Brainstorm Query Categories
   - Construct Search Queries
   - Define Time Filters
5. [Phase 5: Customize Templates](#phase-5-customize-templates)
   - Define Item Types
   - Write Summary Templates
   - Configure Language Settings
   - Configure Git Workflow
   - Create Domain-Specific Skills
6. [Phase 6: Validate Configuration](#phase-6-validate-configuration)
   - Review Checklist
   - Test Workflow
7. [Phase 7: Launch](#phase-7-launch)
   - Initial Commit
   - Create First Entries
   - Publish
8. [Example Domains](#example-domains)
   - AI-for-Climate-Change
   - LLM-for-Education
   - Quantum-Computing-Papers

---

## Phase 1: Define Your Domain

### Step 1.1: Domain Name

Choose a clear, descriptive name for your research domain.

**Questions to answer:**
- What is the broad field? (e.g., AI for Mental Health, LLM for Education)
- What is the specific focus? (e.g., multi-turn dialogue systems, personalized learning)
- What is the target audience? (e.g., researchers, practitioners, general public)

**Examples:**
- "ml-papers-collection" - Clear, descriptive
- "nlp-research-tracker" - Specific, searchable
- "My Research" - Too vague (avoid)
- "Papers" - Not descriptive (avoid)

**Output**: Repository name (e.g., `ml-research-2024`)

---

### Step 1.2: Repository Purpose Statement

Write 1-2 sentences explaining what this repository tracks.

**Template:**
```
Curated literature collection for [DOMAIN NAME] research. Serves as:
- Centralized bibliography for [SPECIFIC FOCUS AREA]
- Resource for writing related work in academic papers
- Reference for technical roadmaps and research trends
```

**Example (Machine Learning Research):**
```
Curated literature collection for Machine Learning research. Serves as:
- Centralized bibliography for deep learning and optimization papers
- Resource for writing related work in academic papers
- Reference for technical roadmaps and research trends
```

**Output**: Purpose statement for README.md and CLAUDE.md

---

## Phase 2: Define Research Priorities

### Step 2.1: Identify Priority Levels

Most research domains work well with 3 priority levels:

**Priority 1: Core Focus**
- What is THE MOST IMPORTANT type of research in your domain?
- What would you collect first if time were limited?

**Priority 2: Supporting Research**
- What research supports the core focus?
- What evaluations, benchmarks, or related methods matter?

**Priority 3: Foundational Work**
- What background research is useful but not core?
- What provides context but isn't directly applicable?

**Example (Machine Learning Research):**
- Priority 1: Deep learning architectures (novel model designs)
- Priority 2: Training optimization & benchmarks (efficiency metrics)
- Priority 3: Foundational algorithms (gradient descent, regularization)

**Output**: 3 priority definitions with names and descriptions

---

### Step 2.2: Write Priority Justification

For each priority, explain WHY it exists.

**Template:**
```
### Priority 1: [Name]

**Why this is top priority:**
[Explain the importance]

**What we're looking for:**
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]
```

**Example:**
```
### Priority 1: Deep Learning Architectures

**Why this is top priority:**
The core challenge in ML research is developing novel architectures that
improve model performance and efficiency. This is our primary research focus.

**What we're looking for:**
- Novel neural network designs and architectures
- Improved training methodologies
- State-of-the-art performance on benchmarks
```

**Output**: Complete priority sections for research-focus.md

---

## Phase 3: Create Tag Taxonomy

### Step 3.1: Define Tag Categories

Choose 3-4 categories that cover your research domain.

**Common patterns:**

**Pattern A: Data-Method-Application**
- Data: Types of data used
- Method: Technical approaches
- Application: Use cases
- Other: Special characteristics

**Pattern B: Task-Technique-Domain**
- Task: What problem is solved
- Technique: How it's solved
- Domain: Application area
- Other: Special characteristics

**Example (Machine Learning Research):**
1. **Data**: Synthetic_Data, Real_World_Data, Benchmark_Datasets
2. **Method**: Supervised_Learning, Unsupervised_Learning, Reinforcement_Learning
3. **Application**: Computer_Vision, NLP, Recommendation_Systems
4. **Other**: Multi_Modal, Transfer_Learning

**Output**: 3-4 category names with descriptions

---

### Step 3.2: Define Tags per Category

For each category, list 2-5 specific tags.

**Guidelines:**
- Tags should be mutually exclusive (choose ONE per category max)
- Tags should be descriptive but concise
- Use Pascal_Case for multi-word tags
- Total tags: 8-15 recommended

**Template:**
```
### Category: [Category Name]

**Tags:**
- **Tag1_Name**: [Description of what this tag means]
- **Tag2_Name**: [Description]
- **Tag3_Name**: [Description]
```

**Example:**
```
### Category: Application

**Tags:**
- **Computer_Vision**: Image and video processing tasks
- **NLP**: Natural language processing systems
- **Recommendation**: Recommendation and ranking systems
- **Time_Series**: Sequential and temporal data analysis
- **Benchmark**: Evaluation datasets and metrics
```

**Output**: Complete tag definitions for classification-guide.md

---

### Step 3.3: Assign Color Scheme

Choose a base color for each category and create gradients (dark → medium → light).

**Recommended approach:**
1. Assign different base colors to categories (blue, green, purple, orange)
2. Create gradient within each category
3. Ensure WCAG AA contrast (4.5:1 ratio)

**Color templates:**

**Blue gradient:**
```
#0052cc (dark)
#0066ff (medium)
#3399ff (light)
```

**Green gradient:**
```
#008754 (dark)
#00a86b (medium)
#33d498 (light)
```

**Purple gradient:**
```
#6554c0 (dark)
#8066ff (medium)
#997dff (light)
```

**Orange gradient:**
```
#ff6b00 (dark)
#ff8c00 (medium)
#ffab33 (light)
```

**Badge URL format:**
```
https://img.shields.io/badge/Tag_Name-COLOR
```

**Example:**
```
Supervised_Learning: https://img.shields.io/badge/Supervised_Learning-0052cc
Unsupervised_Learning: https://img.shields.io/badge/Unsupervised_Learning-0066ff
Reinforcement_Learning: https://img.shields.io/badge/Reinforcement_Learning-3399ff
```

**Output**: Color assignments and badge URLs for all tags

---

### Step 3.4: Define Tag Selection Rules

Specify how tags should be selected.

**Template:**
```
**Required:**
- 1 primary tag from **[Category Name]** category

**Optional:**
- 1-2 method/technique tags from **[Category Name]** category
- 1 additional tag from any category

**Total: 2-4 tags per [item]**
```

**Example (Machine Learning Research):**
```
**Required:**
- 1 primary tag from **Application** category

**Optional:**
- 1-2 method tags from **Method** category
- 1 additional tag from any category

**Total: 2-4 tags per paper**
```

**Output**: Tag selection rules for classification-guide.md

---

## Phase 4: Write Search Queries

### Step 4.1: Brainstorm Query Categories

For each priority, brainstorm key search terms.

**Questions:**
- What are the key concepts in this priority?
- What terms do researchers use in papers?
- What synonyms or related terms exist?

**Example (Priority 1: Deep Learning):**
- Key concepts: neural network, architecture, transformer, attention
- Related terms: deep learning, model design, optimization
- Synonyms: neural architecture, network design

**Output**: Keyword lists for each priority

---

### Step 4.2: Construct Search Queries

Create 8-20 search queries per priority using the keywords.

**Query construction tips:**
- Combine 2-4 key terms
- Include domain name
- Use quotation marks for phrases
- Vary term order

**Template:**
```
[Domain] [key concept 1] [key concept 2]
[key concept 1] [domain] [specific technique]
[specific application] [domain] [method]
```

**Examples:**
```
deep learning transformer architecture optimization
neural network attention mechanism survey
convolutional neural network image classification
reinforcement learning policy gradient methods
```

**Query targets:**
- Priority 1: 15-20 queries
- Priority 2: 10-15 queries
- Priority 3: 8-10 queries

**Output**: Complete query list for search-[items] skill

---

### Step 4.3: Define Time Filters

Specify time filter for each priority.

**Common patterns:**
- Priority 1: `oneYear` (core research, regular updates)
- Priority 2: `oneMonth` (rapidly evolving, frequent updates)
- Priority 3: `noLimit` (foundational, historical OK)

**Example:**
```
Priority 1: oneYear (core architectures)
Priority 2: oneMonth (optimization methods evolving fast)
Priority 3: noLimit (foundational algorithms, any year)
```

**Output**: Time filter settings for search-[items] skill

---

## Phase 5: Customize Templates

### Step 5.1: Define Item Types

Identify the main categories/types of items in your domain.

**Example (Machine Learning Research):**
1. **Architecture Papers**: Novel neural network designs
2. **Optimization Methods**: Training efficiency improvements
3. **Foundational**: Core algorithms and theoretical work

**Output**: Item type definitions for add-[item] skill

---

### Step 5.2: Write Summary Templates

For each item type, create a 2-3 sentence summary template.

**Structure**: Purpose → Method → Results

See [readme-entry.md Summary Writing Guidelines](templates/readme-entry.md#summary-writing-guidelines) for:
- Complete structure explanation
- Templates by item type
- Writing requirements

**Output**: Summary templates for add-[item] skill

---

### Step 5.3: Configure Language Settings

Decide on language usage for:
1. User discussions with Claude
2. Reading notes
3. README files (bilingual or English-only)

**Options:**
- **English-only**: README.md only
- **Bilingual**: README.md (English) + README_zh.md (Chinese)
- **Other languages**: Adapt as needed

**Example (Bilingual Setup):**
```
User discussions: English
Technical explanations: English
Reading notes: English (in paper_notes/)
README.md: English
README_es.md: Spanish
```

**Output**: Language configuration for CLAUDE.md

---

### Step 5.4: Configure Git Workflow

Define commit message format. See SKILL.md Step 5 for the standard format.

**Customize [item] noun**:
- "paper" for academic papers
- "article" for blog posts/articles
- "resource" for general resources
- "package" for software packages

**Output**: Git commit format for CLAUDE.md and add-[item] skill

---

## Phase 5.5: Create Domain-Specific Skills

Create two skills that will automate the research workflow for this domain.

### Step 5.5.1: Create search-[items] Skill

**Purpose**: Automated discovery workflow for research items.

**Template location**: [search-items-skill.md](templates/skills/search-items-skill.md)

**Creation steps**:

See [search-items-skill.md Creation Steps](templates/skills/search-items-skill.md#creation-steps) for complete instructions.

**For this domain, prepare these values**:
- [items]: [fill in, e.g., "papers", "articles"]
- [item]: [fill in, e.g., "paper", "article"]
- [DOMAIN NAME]: [fill in your research domain]
- [Domain]: [fill in short domain name]
- [Core focus]: [fill in Priority 1 name]
- [Secondary]: [fill in Priority 2 name]
- [Foundational]: [fill in Priority 3 name]

**Output**: Fully functional `search-[items]` skill

### Step 5.5.2: Create add-[item] Skill

**Purpose**: Standardized workflow for adding items to repository.

**Template location**: [add-item-skill.md](templates/skills/add-item-skill.md)

**Creation steps**:

See [add-item-skill.md Creation Steps](templates/skills/add-item-skill.md#creation-steps) for complete instructions.

**For this domain, prepare these values**:
- [item]: [fill in, e.g., "paper", "article"]
- [items]: [fill in, e.g., "papers", "articles"]
- [lang]: [fill in secondary language code, e.g., "zh", "es"]

**Output**: Fully functional `add-[item]` skill

---



## Phase 6: Validate Configuration

### Step 6.1: Review Checklist

Run through this checklist before finalizing:

**Domain & Priorities:**
- [ ] Repository name chosen and is descriptive
- [ ] Purpose statement written (1-2 sentences)
- [ ] 3 priority levels defined with justifications
- [ ] Decision tree for classification created

**Tag System:**
- [ ] 3-4 tag categories defined
- [ ] 8-15 total tags created
- [ ] Color scheme assigned (gradients per category)
- [ ] Tag selection rules specified (2-4 tags per item)
- [ ] Badge URLs generated

**Search Queries:**
- [ ] 30-50 total queries created (15-20 P1, 10-15 P2, 8-10 P3)
- [ ] Time filters assigned per priority
- [ ] Queries tested for relevance

**Templates:**
- [ ] Item types identified
- [ ] Summary templates written (per type)
- [ ] Language settings configured
- [ ] Git commit format defined

**Files:**
- [ ] CLAUDE.md customized
- [ ] research-focus.md completed
- [ ] classification-guide.md completed
- [ ] .gitignore configured
- [ ] LICENSE added

**Skills:**
- [ ] search-[items] skill created (SKILL.md + references/queries.md)
- [ ] add-[item] skill created (SKILL.md + references/notes-template.md)
- [ ] Skills validated with /skill-creator (if available)

**README:**
- [ ] README.md initialized
- [ ] README_zh.md initialized (if bilingual)

---

### Step 6.2: Test Workflow

Run a complete test cycle:

1. **Test search:**
   ```
   /search-[items]  # e.g., /search-papers
   ```
   Verify: Queries execute, TODO.md updates correctly

2. **Test add:**
   ```
   /add-[item]  # e.g., /add-paper
   ```
   Verify: Classification works, tags selected, README updates, git commits

3. **Verify git:**
   ```bash
   git status  # Should only show README files
   git log     # Check commit message format
   ```

**Output**: Confirmation that workflow is functional

---

## Phase 7: Launch

### Step 7.1: Initial Commit

```bash
git init
git add README.md README_zh.md TODO.md LICENSE
git commit -m "Initial commit: [Domain] research repository"
```

---

### Step 7.2: Create First Entries

Add 3-5 initial [items] to establish the pattern.

---

### Step 7.3: Publish

Push to GitHub/GitLab and add description:
```
Curated literature collection for [DOMAIN] with AI-assisted workflow.
Focuses on [Core Focus]. Built with Claude Code Skills.
```

---

## Example Domains

### AI-for-Climate-Change

**Priorities:**
1. Climate modeling (prediction, simulation)
2. Policy analysis (impact assessment)
3. Carbon tracking (monitoring, measurement)

**Tags:**
- Data: Emissions, Temperature, Satellite
- Method: Modeling, Forecasting, Optimization
- Application: Policy, Adaptation, Mitigation
- Other: Multi-Modal, Real-time

**Sample queries:**
```
climate change machine learning prediction
carbon emissions AI modeling
climate policy impact assessment
```

---

### LLM-for-Education

**Priorities:**
1. Personalized learning (adaptive tutoring)
2. Assessment (automated grading, feedback)
3. Content generation (educational materials)

**Tags:**
- Data: Student_Data, Assessment_Data, Content_Corpus
- Method: Personalization, Reinforcement_Learning, Generation
- Application: Tutoring, Assessment, Content_Creation
- Other: Multi-Modal, K-12, Higher_Ed

**Sample queries:**
```
educational dialogue system LLM
AI tutoring personalization
automated essay grading large language model
```

---

### Quantum-Computing-Papers

**Priorities:**
1. Algorithms (new quantum algorithms)
2. Hardware (quantum computer construction)
3. Applications (practical quantum use cases)

**Tags:**
- Data: Benchmark, Simulation, Real_World
- Method: VQA, QAOA, Optimization, Cryptography
- Application: Chemistry, Finance, Machine_Learning
- Other: Error_Correction, Fault_Tolerant

**Sample queries:**
```
quantum machine learning algorithm
quantum error correction code
variational quantum eigensolver
```

---
