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

**Reference**: See [core-files.md](references/templates/core-files.md) for complete file contents.

### Step 2: Configure Domain Specifics

Customize these files for your research domain:

#### A. CLAUDE.md

**Purpose**: Primary instructions for Claude Code when working with this repository.

**Required sections**:
- Repository Purpose (what this repo tracks)
- Primary Skills (which skills to use and when)
- Research Focus (quick reference to priorities)
- Essential Principles (language usage, git workflow)
- Repository Structure
- Quick Reference

**Customization needed**:
- Repository name and purpose
- Research priorities (what matters most in your domain)
- Language preferences (keep bilingual if needed)
- Domain-specific conventions

**Template**: See [CLAUDE.md template](references/templates/core-files.md#claude-md)

#### B. research-focus.md

**Purpose**: Detailed explanation of research priorities and collection strategy.

**Required sections**:
- Priority definitions (why each priority exists)
- Search strategies per priority
- Decision trees for classification
- Quality criteria

**Customization needed**:
- Priority levels (usually 3 tiers based on relevance)
- Search queries specific to your domain
- Classification logic

**Template**: See [research-focus.md template](references/templates/core-files.md#research-focus-md)

#### C. classification-guide.md

**Purpose**: Complete tagging system and classification standards.

**Required sections**:
- Tag categories (3-4 categories recommended)
- Color scheme
- Tag selection rules
- Examples per tag

**Customization needed**:
- Tag names relevant to your domain
- Color scheme (use gradients per category)
- Selection rules (e.g., "1 primary + 1-2 secondary")

**Template**: See [classification-guide.md template](references/templates/core-files.md#classification-guide-md)

#### D. .gitignore

**Purpose**: Exclude local notes and Claude-specific files from git.

**Required exclusions**:
```
paper_notes/
.claude/
*.log
.DS_Store
```

### Step 3: Create Domain-Specific Skills

Create two core skills in `.claude/skills/`:

#### A. search-[items] Skill (e.g., search-papers)

**Purpose**: Automated discovery workflow for your research items.

**Key components**:
1. **Search strategy**: Priority-based queries
2. **Time filters**: Recent vs. historical
3. **Filtering logic**: Duplicate detection, classification
4. **TODO update**: Add newly found items

**Customization needed**:
- Search queries for your domain (30-50 recommended)
- Priority levels
- Time filter strategy
- Sources (arXiv, Google Scholar, specific venues)

**Structure**: See [search-items skill template](references/templates/skills/search-items-skill.md)

#### B. add-[item] Skill (e.g., add-paper)

**Purpose**: Standardized workflow for adding new items to repository.

**Key components**:
1. **Info confirmation**: Verify all metadata
2. **Classification**: Determine type/priority
3. **Tag selection**: Choose appropriate tags
4. **Summary writing**: Follow template
5. **Notes creation**: Detailed local notes
6. **README update**: Synchronized English + translation
7. **Git commit**: Standardized format

**Customization needed**:
- Entry format (README template)
- Summary templates (by item type)
- Notes structure
- Commit message format

**Structure**: See [add-item skill template](references/templates/skills/add-item-skill.md)

### Step 4: Initialize README Files

#### README.md Structure

```markdown
# [Domain Name] Research

Curated literature collection for [research area].

## 2026

### January

- **Paper Title**
    ![Tag1](badge_url)
    ![Tag2](badge_url)

    > **Source:** Venue Year [[Link]](url)

    2-3 sentence summary.
```

**Sections to include**:
- Introduction
- Year-based organization (2026, 2025, ...)
- TODO section (papers to document)
- License

#### README_zh.md (Optional)

Mirror the English structure with Chinese translations.

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

### Step 6: Validate Setup

Run through this checklist:

- [ ] All core files created (README, CLAUDE.md, etc.)
- [ ] CLAUDE.md customized for domain
- [ ] research-focus.md has priorities and search queries
- [ ] classification-guide.md has complete tag system
- [ ] .gitignore excludes paper_notes/ and .claude/
- [ ] search-[items] skill created with domain queries
- [ ] add-[item] skill created with templates
- [ ] README.md has proper structure
- [ ] Git repository initialized
- [ ] LICENSE file added (MIT recommended)

## Reference Materials

### Quick Reference Navigation

| Resource | Purpose | When to Read |
|----------|---------|--------------|
| [setup-wizard.md](references/setup-wizard.md) | Interactive configuration guide | Creating a new repository |
| [faq.md](references/faq.md) | Common questions and answers | Troubleshooting issues |
| [templates/core-files.md](references/templates/core-files.md) | CLAUDE.md, research-focus.md, classification-guide.md | Setting up core files |
| [templates/git-config.md](references/templates/git-config.md) | .gitignore, LICENSE | Git initialization |
| [templates/skills/search-items-skill.md](references/templates/skills/search-items-skill.md) | search-[items] skill template | Creating search skill |
| [templates/skills/add-item-skill.md](references/templates/skills/add-item-skill.md) | add-[item] skill template | Creating add skill |
| [templates/readme-entry.md](references/templates/readme-entry.md) | README entry format | Adding items to README |

### Template Organization

Templates are split into focused modules for efficient loading:
- **core-files.md** - Primary configuration files
- **git-config.md** - Git-related setup
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

**AI-for-Climate-Change**:
- Priorities: Climate modeling > Policy analysis > Carbon tracking
- Tags: Emissions, Modeling, Policy, Adaptation
- Queries: "climate change LLM", "carbon emissions prediction"

**LLM-for-Education**:
- Priorities: Personalized learning > Assessment > Content generation
- Tags: Personalization, Assessment, Tutoring, Multi-modal
- Queries: "educational dialogue system", "AI tutoring"

**Quantum-Computing-Papers**:
- Priorities: Algorithms > Hardware > Applications
- Tags: Algorithms, Hardware, Cryptography, Simulation
- Queries: "quantum machine learning", "error correction"

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
