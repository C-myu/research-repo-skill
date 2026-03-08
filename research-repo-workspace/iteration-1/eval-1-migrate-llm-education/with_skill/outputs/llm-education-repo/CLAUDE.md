# CLAUDE.md

**Repository memory** - Helps Claude Code understand how to collaborate with you on this project.

**Communication language**: English

---

## Repository Purpose

Curated literature collection for **LLM for Education** research.
- Centralized bibliography for applying Large Language Models to educational contexts
- Resource for writing related work and technical roadmaps

**What makes this repo unique**: Focus on practical applications of LLMs in education, including intelligent tutoring systems, automated feedback generation, personalized learning, and educational assessment. Covers both technical innovations and pedagogical implications.

---

## Primary Skills

Use these skills for ALL paper-related tasks:

| Skill | When to use |
|-------|-------------|
| `/search-papers` | User asks to search for papers, regular collection updates |
| `/add-paper` | User finishes reading a paper, provides [link/info] |

**Why skills?** They contain complete workflows - ensures consistency and single source of truth.

---

## Essential Principles

### Language
- User discussions & technical explanations: **English**
- Reading notes (`paper_notes/`): **English**
- README.md: English
- README_zh.md: Chinese (bilingual support)

### Git Workflow
**Commit**: Only `README.md` and `README_zh.md`
**Never commit**: `CLAUDE.md`, `.gitignore`, `paper_notes/`, reference `.md` files, chat history

**Commit format**:
- Add: `Add paper: Title (Venue Year)`
- Update: `Update paper: Title - description`
- Fix: `Fix: issue description`

---

## User Preferences

### Paper Collection Strategy
- Prioritize empirical studies with educational impact
- Include both technical LLM innovations and educational applications
- Track papers from AI/ML venues (NeurIPS, ICML, ACL, AAAI) and Education venues (CHI, CSCL, EDM, LAK)
- Maintain balance between cutting-edge LLM techniques and practical educational deployments

### Documentation Standards
- Summaries must be 2-3 sentences maximum
- Focus on educational outcomes and learning effectiveness
- Tag papers by educational application, LLM technique, and evaluation method
- Include personal insights in local notes (paper_notes/) only

---

## For Deeper Understanding

Reference documents (read when needed):
- [research-focus.md](research-focus.md) - Priority rationale & search strategies
- [classification-guide.md](classification-guide.md) - Tagging system & examples
