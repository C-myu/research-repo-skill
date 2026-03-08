# CLAUDE.md

**Repository memory** - Helps Claude Code understand how to collaborate with you on this project.

**Communication language**: English

---

## Repository Purpose

Curated literature collection for **LLM for Education** research.
- Centralized bibliography for LLM applications in educational settings
- Resource for writing related work, technical roadmaps, and staying current with research

**What makes this repo unique**: Focus on empirical validation and practical deployment of LLMs in real educational contexts, not just theoretical proposals.

---

## Primary Skills

Use these skills for ALL paper-related tasks:

| Skill | When to use |
|-------|-------------|
| `/search-papers` | User asks to search for papers, regular collection updates |
| `/add-paper` | User finishes reading a paper, provides link/info |

**Why skills?** They contain complete workflows - ensures consistency and single source of truth.

---

## Essential Principles

### Language
- User discussions & technical explanations: **English**
- Reading notes (`paper_notes/`): **English**
- README.md: English

### Git Workflow
**Commit**: Only `README.md`
**Never commit**: `CLAUDE.md`, `.gitignore`, `paper_notes/`, reference `.md` files, chat history

**Commit format**:
- Add: `Add paper: Title (Venue Year)`
- Update: `Update paper: Title - description`
- Fix: `Fix: issue description`

---

## User Preferences

- Prefer papers with empirical validation over purely theoretical work
- Include both positive and negative results (failures are informative)
- Focus on papers that address real educational challenges, not just technical demonstrations
- Value interdisciplinary work combining AI/ML with educational science

---

## For Deeper Understanding

Reference documents (read when needed):
- [research-focus.md](research-focus.md) - Priority rationale & search strategies
- [classification-guide.md](classification-guide.md) - Tagging system & examples
