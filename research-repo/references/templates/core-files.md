# Core Repository Files

This file contains templates for the core configuration files in a research repository.

---

## Template Placeholder Guide

The following placeholders are used throughout the templates below. Replace them with your domain-specific values when setting up your repository.

| Placeholder | Description | Examples |
|-------------|-------------|----------|
| `[DOMAIN NAME]` | Your research area/domain | "AI for Mental Health", "LLM for Education" |
| `[LANGUAGE]` | Primary language for communication | "English", "中文" |
| `[item]` / `[items]` | Resource type noun (singular/plural) | "paper" / "papers", "article" / "articles", "resource" / "resources" |
| `[ITEM]` | Uppercase version of resource type | "Paper", "Article", "Resource" |
| `[DATE]` | Current date in YYYY-MM-DD format | "2026-03-06" |
| `[LANG]` | Language code for secondary README | "zh" (Chinese), "es" (Spanish) |
| `[item_notes]` / `[paper_notes]` | Directory name for local notes | "item_notes", "paper_notes" |

---

## Table of Contents

1. [CLAUDE.md](#claude-md) - Primary AI assistant instructions
2. [research-focus.md](#research-focus-md) - Detailed research priorities
3. [classification-guide.md](#classification-guide-md) - Tagging system

---

## CLAUDE.md

```markdown
# CLAUDE.md

**Repository memory** - Helps Claude Code understand how to collaborate with you on this project.

**Communication language**: [LANGUAGE]

---

## Repository Purpose

Curated literature collection for **[DOMAIN NAME]** research.
- Centralized bibliography for [specific focus area]
- Resource for writing related work and technical roadmaps

**What makes this repo unique**: [Brief description]

---

## Primary Skills

Use these skills for ALL [item]-related tasks:

| Skill | When to use |
|-------|-------------|
| `/search-[items]` | User asks to search for [items], regular collection updates |
| `/add-[item]` | User finishes reading a [item], provides [link/info] |

**Why skills?** They contain complete workflows - ensures consistency and single source of truth.

---

## Essential Principles

### Language
- User discussions & technical explanations: **[LANGUAGE]**
- Reading notes (`item_notes/`): **[LANGUAGE]**
- README.md: English
- README_[LANG].md: [Secondary language]

### Git Workflow
**Commit**: Only `README.md` and `README_[LANG].md`
**Never commit**: `CLAUDE.md`, `.gitignore`, `item_notes/`, reference `.md` files, chat history

**Commit format**:
- Add: `Add [item]: Title (Venue Year)`
- Update: `Update [item]: Title - description`
- Fix: `Fix: issue description`

---

## User Preferences

[Optional - customize based on your work style]

---

## For Deeper Understanding

Reference documents (read when needed):
- [research-focus.md](research-focus.md) - Priority rationale & search strategies
- [classification-guide.md](classification-guide.md) - Tagging system & examples
```

---

## research-focus.md

```markdown
# Research Focus

This document explains the research priorities and collection strategy for [DOMAIN NAME].

---

## Priority System

### Priority 1: [Core Focus Name]

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

### Priority 2: [Secondary Focus Name]

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

### Priority 3: [Foundational Work Name]

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

## Priority Decision Tree

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

- **Don't**: Use more than 4 tags (too many dilutes meaning)
- **Do**: Focus on 2-3 most relevant tags

- **Don't**: Mix tags from same category (e.g., 2 method tags)
- **Do**: Choose one representative tag per category max

- **Don't**: Use tags without understanding their definition
- **Do**: Refer to this guide when unsure

---

```
