---
name: research-repo
description: "Create and set up automated research repositories for curating academic papers in any domain. Use when user wants to start a new research tracking repository, migrate existing literature collection to AI-assisted workflow, or establish standardized workflows for paper discovery and documentation"
---

# Research Repository Setup

## Overview

This skill helps you create a fully-structured research repository for tracking academic papers in any domain. It provides templates and guidance for establishing an AI-assisted workflow for paper discovery, classification, and documentation.

## Quick Workflow

1. **Initialize repository structure** - Create directory layout and core files
2. **Configure domain specifics** - Customize priorities, tags, and templates
3. **Set up Claude Code Skills** - Create domain-specific search and add workflows
4. **Validate and commit** - Ensure all files are properly configured

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

> **💡 Need guidance?** See [setup-wizard.md Phase 5.5](references/setup-wizard.md#phase-55-create-domain-specific-skills) for detailed skill creation instructions.

Create two core skills in `.claude/skills/`:

#### A. search-[items] Skill (e.g., search-papers)

**Purpose**: Automated discovery workflow for your research items.

**Create skill structure**:
```bash
mkdir -p .claude/skills/search-[items]/references
```

**Required files**:
| File | Purpose | Template |
|------|---------|----------|
| `SKILL.md` | Main skill definition | [search-items template](references/templates/skills/search-items-skill.md) |
| `references/queries.md` | Domain-specific search queries (30-50 total) | See template in search-items-skill.md |

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
| File | Purpose | Template |
|------|---------|----------|
| `SKILL.md` | Main skill definition | [add-item template](references/templates/skills/add-item-skill.md) |
| `references/notes-template.md` | Local notes structure | See template in add-item-skill.md |

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
- [ ] add-[item] skill created (SKILL.md + references/notes-template.md)

**Git**:
- [ ] Git repository initialized
- [ ] First commit created with proper message format

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
