# CLAUDE.md

**Repository memory** - Helps Claude Code understand how to collaborate with you on this project.

**Communication language**: English

---

## Repository Purpose

Curated literature collection for **AI for Mental Health** research.
- Centralized bibliography for multi-turn dialogue systems for mental health support
- Resource for writing related work and technical roadmaps

**What makes this repo unique**: Focused on AI-powered conversational agents and dialogue systems that provide mental health support, therapy, counseling, and emotional well-being assistance through multi-turn interactions.

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
- README_zh.md: Chinese (optional translation)

### Git Workflow
**Commit**: Only `README.md` and `README_zh.md`
**Never commit**: `CLAUDE.md`, `.gitignore`, `paper_notes/`, reference `.md` files, chat history

**Commit format**:
- Add: `Add paper: Title (Venue Year)`
- Update: `Update paper: Title - description`
- Fix: `Fix: issue description`

---

## User Preferences

- Focus on practical, implementable systems rather than purely theoretical work
- Include both fully-developed systems and research prototypes
- Prioritize work with empirical validation and user studies
- Include foundational dialogue systems research when relevant to mental health applications

---

## For Deeper Understanding

Reference documents (read when needed):
- [research-focus.md](research-focus.md) - Priority rationale & search strategies
- [classification-guide.md](classification-guide.md) - Tagging system & examples
