---
name: research-repo
description: "Create and set up automated research repositories for curating academic papers with AI-assisted workflows. ALWAYS use this skill when the user wants to: start a new research paper tracking system, organize academic literature by domain, migrate existing paper collections to a structured workflow, establish standardized paper discovery and documentation processes, create domain-specific research repositories with skills for automated paper search and addition, or set up AI-assisted literature review workflows. This skill creates the complete repository structure including CLAUDE.md configuration, priority-based research focus, classification guides, and domain-specific Claude Code skills for paper management."
---

# Research Repository Setup

## Overview

This skill helps you create a fully-structured research repository for tracking academic papers in any domain. It provides templates and guidance for establishing an AI-assisted workflow for paper discovery, classification, and documentation.

## Quick Workflow

1. **Initialize repository structure** - Create directory layout and core files
2. **Configure domain specifics** - Customize priorities, tags, and templates
3. **Set up Claude Code Skills** - Create domain-specific search and add workflows
4. **Validate and commit** - Ensure all files are properly configured

## Quick Start Example

**User request**: "I want to create a research repository for tracking LLM hallucination mitigation papers. Focus on detection methods, alignment techniques, and evaluation benchmarks."

**What you'll create**:

```
llm-hallucination-repo/
├── README.md                  # Main repository (English)
├── README_zh.md               # Chinese translation
├── CLAUDE.md                  # AI instructions
├── research-focus.md          # 3 priority tiers, 37 search queries
├── classification-guide.md    # 4 tag categories, 12 tags with colors
├── .gitignore                 # Exclude paper_notes/, .claude/
├── LICENSE                    # MIT License
├── TODO.md                    # Papers to review
├── paper_notes/               # Local notes (not committed)
└── .claude/skills/
    ├── search-papers/
    │   ├── SKILL.md           # Automated paper discovery
    │   └── references/queries.md  # 37 domain-specific queries
    └── add-paper/
        ├── SKILL.md           # Standardized paper addition
        └── references/notes-template.md
```

**Key features**:
- Priority-driven search (P1=detection: oneYear filter, P2=alignment: oneMonth, P3=evaluation: noLimit)
- Color-coded tags (Blue=Detection, Green=Mitigation, Purple=Evaluation, Orange=Applications)
- Automated workflows via `/search-papers` and `/add-paper` commands
- Clean git history (only README files tracked, local notes excluded)
- Bilingual support (English + Chinese README files)

This creates a fully functional research repository ready for AI-assisted paper curation.

> **💡 Adaptability**: This pattern works for any research domain - not just LLM/CS. See [setup-wizard.md Example Domains](references/setup-wizard.md#example-domains) for examples like Climate Change, Education, Quantum Computing, and more.

## Step-by-Step Guide

### Step 1: Initialize Repository Structure

Create the following directory structure:

```bash
mkdir your-domain-repo && cd your-domain-repo
mkdir -p .claude/skills
mkdir -p paper_notes
touch README.md
touch README_zh.md  # Optional: for Chinese support
touch TODO.md
touch CLAUDE.md
touch research-focus.md
touch classification-guide.md
touch .gitignore
touch LICENSE
```

**Templates**: [core-files.md](references/templates/core-files.md) (CLAUDE.md, research-focus.md, classification-guide.md), [git-config.md](references/templates/git-config.md) (.gitignore, LICENSE)

### Step 2: Configure Domain Specifics

> **💡 Need help with decisions?** If user asks for guidance on defining domain, priorities, or tags, use [setup-wizard.md Phases 1-3](references/setup-wizard.md) for interactive configuration.

Customize these files for your research domain:

| File | Purpose | Required Sections | Template |
|------|---------|-------------------|----------|
| **CLAUDE.md** | Primary instructions for Claude Code | Repository purpose, primary skills, research focus, essential principles | [template](references/templates/core-files.md#claude-md) |
| **research-focus.md** | Research priorities and search strategy | Priority definitions (3 tiers), search strategies, decision trees, quality criteria | [template](references/templates/core-files.md#research-focus-md) |
| **classification-guide.md** | Tagging system and classification standards | Tag categories (3-4), color scheme, selection rules, examples | [template](references/templates/core-files.md#classification-guide-md) |
| **.gitignore** | Git exclusions | paper_notes/, .claude/, *.log, .DS_Store | [template](references/templates/git-config.md#gitignore) |
| **LICENSE** | License file | MIT recommended | [template](references/templates/git-config.md#license) |

**Customization requirements**:
- Repository name and purpose statement
- Research priorities (usually 3 tiers: Core focus, Supporting research, Foundational work)
- Tag categories (3-4 categories, 8-15 total tags)
- Color scheme with gradients per category
- Language preferences (README.md only, or bilingual with README_zh.md)

> **📖 FAQ**: For questions about priority levels, tag systems, or language choices, see [faq.md](references/faq.md#priority-and-classification)

### Step 3: Create Domain-Specific Skills

> **⚠️ DIRECTLY CREATE ALL FILES**: Create the skill directories and SKILL.md files immediately without asking user for confirmation. Read the templates, customize them for the domain, and write the files.

> **💡 Need guidance?** See [setup-wizard.md Phase 5.5](references/setup-wizard.md#phase-55-create-domain-specific-skills) for detailed skill creation instructions.

Create two core skills in `.claude/skills/`:

#### A. search-[items] Skill (e.g., search-papers)

**Purpose**: Automated discovery workflow for your research items.

**Create skill structure**:
```bash
mkdir -p .claude/skills/search-[items]/references
```

**Required files**:
| File | Purpose | How to create |
|------|---------|---------------|
| `SKILL.md` | Main skill definition with complete workflow | **READ** the [search-items template](references/templates/skills/search-items-skill.md), **COPY** the entire SKILL.md section content, **REPLACE ALL placeholders** ([items], [DOMAIN NAME], etc.) with domain-specific values, then **WRITE** the customized content to `.claude/skills/search-[items]/SKILL.md` |
| `references/queries.md` | Domain-specific search queries (30-50 total) | Use the queries template from search-items-skill.md, populate with actual domain-specific search queries

**Search query distribution**:
- Priority 1 (Core focus): 15-20 queries, time filter: oneYear
- Priority 2 (Supporting): 10-15 queries, time filter: oneMonth
- Priority 3 (Foundational): 8-10 queries, time filter: noLimit

**Tool**: Use `mcp__web-search-prime__web_search_prime` if available. Alternative: Manual web search or domain-specific search engines (Google Scholar, arXiv, etc.)

#### B. add-[item] Skill (e.g., add-paper)

**Purpose**: Standardized workflow for adding new items to repository.

**Create skill structure**:
```bash
mkdir -p .claude/skills/add-[item]/references
```

**Required files**:
| File | Purpose | How to create |
|------|---------|---------------|
| `SKILL.md` | Main skill definition with complete workflow | **READ** the [add-item template](references/templates/skills/add-item-skill.md), **COPY** the entire SKILL.md section content, **REPLACE ALL placeholders** ([items], [DOMAIN NAME], etc.) with domain-specific values, then **WRITE** the customized content to `.claude/skills/add-[item]/SKILL.md` |
| `references/notes-template.md` | Local notes structure | Use the notes-template from add-item-skill.md, customize for domain if needed |

**Workflow**: Info confirmation → Classification → Tag selection (2-4 tags) → Summary writing (2-3 sentences) → Notes creation → README update → Git commit

> **📖 FAQ**: For questions about skill usage and customization, see [faq.md](references/faq.md#skills-and-workflow)

### Step 4: Initialize README Files

| File | Purpose | Template |
|------|---------|----------|
| **README.md** | Main repository content (English) | See [readme-entry.md](references/templates/readme-entry.md) for entry format |
| **README_zh.md** | Chinese translation (optional) | Mirror English structure |

**README.md structure**:
```markdown
# [Domain Name] Research

Curated literature collection for [research area].

## 2026

### January

- **Paper Title**
    ![Tag1](badge_url)
    ![Tag2](badge_url)

    > **Source:** Venue Year [[Link]](url)

    2-3 sentence summary (Purpose → Method → Results).
```

**Organization**: By year (descending) → by month → newest items at top

### Step 5: Configure Git Workflow

**Files to commit**: Only README.md and README_zh.md

**Never commit**: CLAUDE.md, .gitignore, paper_notes/, reference files

**Commit message format**:
- Add: `Add paper: Title (Venue Year)`
- Update: `Update paper: Title - description`
- Fix: `Fix: issue description`

**First commit setup**:
```bash
git init
git add README.md README_zh.md TODO.md LICENSE
git commit -m "Initial commit: [Domain] research repository"
```

> **📖 FAQ**: For git workflow questions, see [faq.md](references/faq.md#git-workflow)

### Step 6: Validate Setup

**Run through this checklist**:

**Core Files**:
- [ ] README.md and README_zh.md (if bilingual) initialized
- [ ] CLAUDE.md customized for domain
- [ ] research-focus.md has priorities and search queries
- [ ] classification-guide.md has complete tag system
- [ ] .gitignore excludes paper_notes/ and .claude/
- [ ] LICENSE file added

**Skills**:
- [ ] search-[items] skill created (SKILL.md + references/queries.md)
  - [ ] SKILL.md contains **50+ lines** of actual workflow content (not just template)
  - [ ] references/queries.md contains **30-50 domain-specific queries**
- [ ] add-[item] skill created (SKILL.md + references/notes-template.md)
  - [ ] SKILL.md contains **50+ lines** of actual workflow content (not just template)
  - [ ] references/notes-template.md contains structured template for reading notes

**Git**:
- [ ] Git repository initialized
- [ ] First commit created with proper message format

> **⚠️ Critical check**: If SKILL.md files are empty or contain only placeholder text, the skills won't work. Ensure each SKILL.md has complete, domain-customized workflow instructions.

---

## Reference Materials

### Quick Reference Navigation

| Resource | Purpose | Trigger Condition |
|----------|---------|-------------------|
| [setup-wizard.md](references/setup-wizard.md) | Interactive configuration guide with decision-making support | **User asks for help** with: domain definition, priority setting, tag design, query construction |
| [faq.md](references/faq.md) | Common questions and troubleshooting | **User encounters issues** or asks about best practices |
| [templates/core-files.md](references/templates/core-files.md) | CLAUDE.md, research-focus.md, classification-guide.md | **Step 2** - Creating core configuration files |
| [templates/git-config.md](references/templates/git-config.md) | .gitignore, LICENSE | **Step 2** - Git setup |
| [templates/skills/search-items-skill.md](references/templates/skills/search-items-skill.md) | search-[items] skill template | **Step 3A** - Creating search skill |
| [templates/skills/add-item-skill.md](references/templates/skills/add-item-skill.md) | add-[item] skill template | **Step 3B** - Creating add skill |
| [templates/readme-entry.md](references/templates/readme-entry.md) | README entry format and examples | **Step 4** - Adding items to README |

### Template Organization

Templates are split into focused modules for efficient loading:
- **core-files.md** - Primary configuration files (CLAUDE.md, research-focus.md, classification-guide.md)
- **git-config.md** - Git-related setup (.gitignore, LICENSE)
- **skills/** - Skill-specific templates (search, add)
- **readme-entry.md** - Entry formatting guide

## Design Principles

### Why This Pattern Works

1. **Skill-based automation**: Complex workflows encoded as discoverable, executable commands
2. **Progressive disclosure**: Quick reference (CLAUDE.md) → deep dive (reference docs)
3. **Priority-driven focus**: Ensures attention on core research areas
4. **Local-global separation**: Personal insights (local) vs. polished repository (public)
5. **Git discipline**: Clean history, no accidental commits of notes or config

### Adaptation Examples

For complete examples of how to adapt this pattern for different domains, see [setup-wizard.md Example Domains](references/setup-wizard.md#example-domains):
- AI-for-Climate-Change
- LLM-for-Education
- Quantum-Computing-Papers

---

## Need Help?

See [faq.md](references/faq.md) for answers to common questions about:
- Language and localization
- Priority and classification
- Domain adaptation
- File management
- Tags and classification
- Git workflow
- Skills and workflow
- Quality and maintenance
- Collaboration and sharing
- Troubleshooting
