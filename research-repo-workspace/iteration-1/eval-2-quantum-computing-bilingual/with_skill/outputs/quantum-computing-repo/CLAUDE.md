# CLAUDE.md

**Repository memory** - Helps Claude Code understand how to collaborate with you on this project.

**Communication language**: English

---

## Repository Purpose

Curated literature collection for **Quantum Computing** research.
- Centralized bibliography for quantum algorithms, hardware, and applications
- Resource for writing related work and technical roadmaps

**What makes this repo unique**: Focuses on practical quantum computing research with emphasis on quantum algorithms (highest priority), hardware construction, and real-world applications. Bilingual support (English/Chinese) for broader accessibility.

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
- README_zh.md: Chinese (中文)

### Git Workflow
**Commit**: Only `README.md` and `README_zh.md`
**Never commit**: `CLAUDE.md`, `.gitignore`, `paper_notes/`, reference `.md` files, chat history

**Commit format**:
- Add: `Add paper: Title (Venue Year)`
- Update: `Update paper: Title - description`
- Fix: `Fix: issue description`

---

## User Preferences

- Priority focus on quantum algorithms (especially VQA, QAOA, quantum machine learning)
- Include experimental validation results when available
- Track both theoretical and experimental advances
- Maintain bilingual entries in README files

---

## For Deeper Understanding

Reference documents (read when needed):
- [research-focus.md](research-focus.md) - Priority rationale & search strategies
- [classification-guide.md](classification-guide.md) - Tagging system & examples
