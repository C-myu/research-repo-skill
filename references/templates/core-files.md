# Core Repository Files

This file contains templates for the core configuration files in a research repository.

---

## Table of Contents

1. [CLAUDE.md](#claude-md) - Primary AI assistant instructions
2. [research-focus.md](#research-focus-md) - Detailed research priorities
3. [classification-guide.md](#classification-guide-md) - Tagging system

---

## CLAUDE.md

```markdown
# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

**IMPORTANT**: This repository uses **[LANGUAGE]** for user-Claude communication.

---

## Repository Purpose

Curated literature collection for **[DOMAIN NAME]** research. Serves as:
- Centralized bibliography for [specific focus area]
- Resource for writing related work in academic papers
- Reference for technical roadmaps and research trends

**Project context**: [Brief description of what makes this repository unique]

---

## Primary Skills

**Claude should use these skills for ALL [ITEM]-related tasks:**

1. **/search-[items]** - Search and collect latest [items]
   - When user asks to search for [items]
   - Regular [item] collection updates
   - Automatically uses proper priorities and search strategies

2. **/add-[item]** - Add [items] to README
   - When user finishes reading a [paper/item]
   - When user provides [link/info]
   - Handles classification, summaries, reading notes, git commits

**Why use skills?**
- Skills contain complete execution workflows
- Ensures consistency across operations
- Single source of truth for procedures

---

## Research Focus (Quick Reference)

**Priorities:**
- 🔥 **Priority 1**: [Core focus - most important type]
- 🎯 **Priority 2**: [Secondary focus - supporting research]
- 📚 **Priority 3**: [Foundational work - background research]

**Critical rule**: [Any critical classification rules, e.g., "Priority 3 papers MUST state they don't do X"]

---

## Essential Principles

### Language Usage
- ✅ User discussions: **[PRIMARY LANGUAGE]**
- ✅ Technical explanations: **[PRIMARY LANGUAGE]**
- ✅ Reading notes: **[PRIMARY LANGUAGE]** (stored in `item_notes/`, never committed)
- ❌ README.md: English
- ❌ README_[LANG].md: [SECONDARY LANGUAGE if bilingual]

### Git Workflow
**Files to commit**: Only README.md and README_[LANG].md
**Never commit**: CLAUDE.md, .gitignore, item_notes/, reference files (.md), chat history

**Commit message format**:
- Add: `Add [item]: Title (Venue Year)`
- Update: `Update [item]: Title - description`
- Fix: `Fix: issue description`

---

## For Deeper Understanding

**Reference documents** (read when needed for context, not required for daily tasks):
- [research-focus.md](research-focus.md) - Detailed priority rationale and search strategies
- [classification-guide.md](classification-guide.md) - Complete tagging guide with examples

**When to read these:**
- Understanding WHY we prioritize certain [items]
- Need detailed classification examples
- Onboarding to the repository structure

**Daily work**: Just use the skills - they contain all necessary procedures.

---

## Repository Structure

```
[domain-name]/
├── README.md              # English main documentation
├── README_[lang].md       # [Secondary language] translation
├── TODO.md                # [Items] to be documented
├── LICENSE                # MIT license
├── CLAUDE.md              # This file (not committed)
├── research-focus.md      # Detailed research priorities (reference)
├── classification-guide.md # Tagging standards (reference)
├── .claude/
│   └── skills/            # Skills (primary execution guides)
│       ├── search-[items]/
│       └── add-[item]/
└── item_notes/            # Local reading notes (not committed)
```

---

## Quick Reference

**Skills invoke:**
- `/search-[items]` - Automatically searches and categorizes [items]
- `/add-[item]` - Walks through adding a [item] step-by-step

**Manual tools** (rarely needed, skills handle these):
- `mcp__web-search-prime__web_search_prime` - [Item] search
- `mcp__web-reader__webReader` - Get [item] text

---

**Last updated**: [DATE]
```

---

## research-focus.md

```markdown
# Research Focus

This document explains the research priorities and collection strategy for [DOMAIN NAME].

---

## Priority System

### 🔥 Priority 1: [Core Focus Name]

**Why this is top priority:**
[Explain why this is the most important type of research for your domain]

**What we're looking for:**
- [Specific characteristic 1]
- [Specific characteristic 2]
- [Specific characteristic 3]

**Search Strategy:**
- Time filter: oneYear (for regular updates)
- Sources: [List specific venues/conferences/journals]
- Key terms: [List 5-10 key search terms]

**Example queries:**
```
[Domain] [core technique] [specific application]
[Domain] [key feature] [method]
```

---

### 🎯 Priority 2: [Secondary Focus Name]

**Why this matters:**
[Explain how this supports the core focus]

**What we're looking for:**
- [Specific characteristic 1]
- [Specific characteristic 2]

**Search Strategy:**
- Time filter: oneMonth (more frequent updates)
- Sources: [List venues]
- Key terms: [List 5-10 key search terms]

**Example queries:**
```
[Domain] [secondary technique] [context]
[Domain] [evaluation method]
```

---

### 📚 Priority 3: [Foundational Work Name]

**Why we include this:**
[Explain the foundational value]

**What we're looking for:**
- [Specific characteristic 1]
- [Specific characteristic 2]

**Critical rule**: [Important classification rule, e.g., "Papers that don't do X MUST explicitly state so in summary"]

**Search Strategy:**
- Time filter: noLimit (historical papers OK)
- Sources: [List venues]
- Key terms: [List 5-10 key search terms]

**Example queries:**
```
[Domain] [foundational topic]
[Domain] [background method]
```

---

## Classification Decision Tree

Use this logic to classify [items]:

```
[Start with key question]
├─ [Condition A] → Priority 1
└─ [Condition B]
    ├─ [Condition C] → Priority 2
    └─ [Condition D] → Priority 3
```

**Examples:**
- [Example 1]: [Why it's Priority X]
- [Example 2]: [Why it's Priority Y]

---

## Quality Criteria

**Inclusion criteria for all priorities:**
- [Criterion 1, e.g., "Published in peer-reviewed venue"]
- [Criterion 2, e.g., "Provides novel technical contribution"]
- [Criterion 3, e.g., "Includes experimental validation"]

**Exclusion criteria:**
- [What to skip, e.g., "Non-technical blog posts"]
- [What to skip, e.g., "Without empirical evaluation"]

---

## Search Query Collection

### Priority 1 Queries (Core Focus)
```
[Query 1]
[Query 2]
[Query 3]
...
```

### Priority 2 Queries (Secondary Focus)
```
[Query 1]
[Query 2]
[Query 3]
...
```

### Priority 3 Queries (Foundational)
```
[Query 1]
[Query 2]
[Query 3]
...
```

---

**Last updated**: [DATE]
```

---

## classification-guide.md

```markdown
# Classification Guide

This document defines the tagging system for [DOMAIN NAME] research.

---

## Tag Categories

We use **[N]** tag categories with **[M]** total tags.

### Category 1: [Category Name]

**Purpose**: [What this category represents]

**Tags:**
- **Tag1_Name**: [Description]
- **Tag2_Name**: [Description]
- **Tag3_Name**: [Description]

**Color scheme**: [Color gradient, e.g., Blue (dark → medium → light)]

**Badge URLs:**
```
https://img.shields.io/badge/Tag1_Name-[COLOR1]
https://img.shields.io/badge/Tag2_Name-[COLOR2]
https://img.shields.io/badge/Tag3_Name-[COLOR3]
```

**Examples:**
- [Example paper/item] uses Tag1_Name because [reason]
- [Example paper/item] uses Tag2_Name because [reason]

---

### Category 2: [Category Name]

**Purpose**: [What this category represents]

**Tags:**
- **Tag1_Name**: [Description]
- **Tag2_Name**: [Description]

**Color scheme**: [Color gradient]

**Badge URLs:**
```
https://img.shields.io/badge/Tag1_Name-[COLOR1]
https://img.shields.io/badge/Tag2_Name-[COLOR2]
```

**Examples:**
- [Example] uses Tag1_Name because [reason]

---

### Category 3: [Category Name]

[Same structure as above]

---

### Category 4: [Category Name]

[Same structure as above]

---

## Tag Selection Rules

**Required:**
- 1 primary tag from **[Category Name]** category

**Optional:**
- 1-2 method/technique tags from **[Category Name]** category
- 1 additional tag from any category

**Total: 2-4 tags per [item]**

---

## Selection Decision Tree

```
Start: Does [item] have [specific characteristic]?
├─ Yes → Must use Tag1_Name
└─ No → Does [item] have [other characteristic]?
    ├─ Yes → Use Tag2_Name
    └─ No → Use Tag3_Name
```

---

## Color Best Practices

1. **Use gradients within categories**: Dark → medium → light
2. **Maintain contrast**: Ensure WCAG AA compliance (4.5:1 ratio)
3. **Distinguish categories**: Use different base colors (blue, green, purple, orange)

**Recommended color values:**
- Blue: `0052cc`, `0066ff`, `3399ff`
- Green: `008754`, `00a86b`, `33d498`
- Purple: `6554c0`, `8066ff`, `997dff`
- Orange: `ff6b00`, `ff8c00`, `ffab33`

---

## Common Mistakes

❌ **Don't**: Use more than 4 tags (too many dilutes meaning)
✅ **Do**: Focus on 2-3 most relevant tags

❌ **Don't**: Mix tags from same category (e.g., 2 method tags)
✅ **Do**: Choose one representative tag per category max

❌ **Don't**: Use tags without understanding their definition
✅ **Do**: Refer to this guide when unsure

---

**Last updated**: [DATE]
```
