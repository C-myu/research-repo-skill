# Quantum Computing Research

Curated literature collection for Quantum Computing research. Serves as:
- Centralized bibliography for quantum algorithms, hardware, and applications
- Resource for writing related work in academic papers
- Reference for technical roadmaps and research trends

**Focus Areas:**
- **Quantum Algorithms** (highest priority): Novel algorithms, VQA, QAOA, quantum ML
- **Quantum Hardware**: Processor design, qubit technologies, error correction
- **Quantum Applications**: Chemistry, finance, optimization, and practical use cases

**Language:** English | [中文](README_zh.md)

---

## 2026

### January

*No papers added yet. Use `/search-papers` to start collecting research.*

---

## 2025

### December

*No papers added yet.*

---

## Repository Structure

```
quantum-computing-repo/
├── README.md              # This file (English)
├── README_zh.md           # Chinese version
├── TODO.md                # Papers to review
├── CLAUDE.md              # AI assistant instructions
├── research-focus.md      # Research priorities and search strategy
├── classification-guide.md # Tagging system
├── paper_notes/           # Local reading notes (not committed)
└── .claude/skills/
    ├── search-papers/     # Paper discovery skill
    └── add-paper/         # Paper addition skill
```

---

## How to Use This Repository

### For Paper Discovery
```
/search-papers
```
This will search for latest quantum computing papers by priority (algorithms > hardware > applications).

### For Adding Papers
```
/add-paper
```
Use after reading a paper to add it with standardized format, classification, and tags.

---

## Tag System

Papers are tagged by category (see [classification-guide.md](classification-guide.md)):

**Application Domain** (Green):
- ![Chemistry](https://img.shields.io/badge/Chemistry-008754)
- ![Finance](https://img.shields.io/badge/Finance-00a86b)
- ![Optimization](https://img.shields.io/badge/Optimization-33d498)
- ![Fundamental](https://img.shields.io/badge/Fundamental-66e5b8)

**Method** (Purple):
- ![VQA](https://img.shields.io/badge/VQA-6554c0)
- ![Optimization](https://img.shields.io/badge/Optimization-8066ff)
- ![Machine_Learning](https://img.shields.io/badge/Machine_Learning-997dff)
- ![Cryptography](https://img.shields.io/badge/Cryptography-aa88ff)

**Data Type** (Blue):
- ![Benchmark](https://img.shields.io/badge/Benchmark-0052cc)
- ![Simulation](https://img.shields.io/badge/Simulation-0066ff)
- ![Real_World](https://img.shields.io/badge/Real_World-3399ff)

**Special Properties** (Orange):
- ![Error_Correction](https://img.shields.io/badge/Error_Correction-ff6b00)
- ![Fault_Tolerant](https://img.shields.io/badge/Fault_Tolerant-ff8c00)
- ![NISQ](https://img.shields.io/badge/NISQ-ffab33)
- ![Hybrid](https://img.shields.io/badge/Hybrid-ffcc66)

---

## Research Priorities

**Priority 1: Quantum Algorithms** (Highest)
- Novel quantum algorithms and theoretical advances
- Variational algorithms (VQE, QAOA)
- Quantum machine learning and optimization
- Time filter: Last year

**Priority 2: Quantum Hardware**
- Processor architecture and qubit technologies
- Error correction and fault tolerance
- Time filter: Last month

**Priority 3: Quantum Applications**
- Real-world applications and case studies
- Quantum-classical hybrid approaches
- Time filter: No limit

See [research-focus.md](research-focus.md) for detailed search strategies and decision trees.

---

## Contributing

This repository uses AI-assisted curation with Claude Code Skills. Papers are added through standardized workflows ensuring:
- Consistent classification by priority
- Appropriate tagging (2-4 tags per paper)
- Bilingual entries (English/Chinese)
- Git-tracked changes with commit messages

---

## License

MIT License - See [LICENSE](LICENSE) for details.
