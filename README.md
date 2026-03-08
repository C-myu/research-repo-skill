# 📚 Research Repo - AI-Powered Research Repository Builder

[![](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://claude.com/claude-code)
[![](https://img.shields.io/badge/Success_Rate-100%25-green)](benchmark.md)
[![](https://img.shields.io/badge/Improvement-+95%25-brightgreen)](benchmark.md)
[![](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

[**中文文档**](README_zh.md) | English

> **A Meta-Skill for Creating Skills**: Research Repo is not just a paper tracker - it's a Claude Code meta-skill that generates domain-specific research workflows with automated paper discovery, classification, and documentation capabilities.

---

## 🎯 Problem It Solves

**Before**: Research papers scattered across folders, inconsistent organization, manual search and tracking, lost insights in disconnected notes.

**After**: A fully-structured, AI-assisted research repository with:
- 🔍 **Automated paper discovery** via `/search-papers` command
- 📋 **Standardized classification** with priority-based organization
- 🤖 **AI-assisted workflows** for adding papers via `/add-paper` command
- 📊 **Visual tagging system** with color-coded categories
- 🔄 **Clean git integration** - only public content tracked

---

## ✨ Why Research Repo?

### 🚀 Proven Results

Tested across 3 diverse research domains with **100% success rate**:

| Domain | With Skill | Without Skill | Improvement |
|--------|-----------|--------------|-------------|
| LLM Hallucination Mitigation | ✅ 100% | ❌ 0% | **+100%** |
| Synthetic Data Homogenization | ✅ 100% | ❌ 0% | **+100%** |
| LLM Quantitative Finance | ✅ 100% | ⚠️ 14% | **+86%** |
| **Average** | **100%** | **4.8%** | **+95.2%** |

See [benchmark results](research-repo-workspace/iteration-2/benchmark.md) for detailed analysis.

### 🎨 What Makes It Different

**Not just file templates** - Research Repo creates **functional AI workflows**:

```
your-repo/
├── .claude/skills/          # ← AI workflows you can invoke
│   ├── search-papers/       #    Run: /search-papers
│   │   ├── SKILL.md         #    Discovers papers automatically
│   │   └── references/queries.md
│   └── add-paper/           #    Run: /add-paper
│       ├── SKILL.md         #    Adds papers with 2-3 sentence summaries
│       └── references/notes-template.md
├── research-focus.md        # ← Priority-driven search strategy
├── classification-guide.md  # ← Color-coded tagging system
└── CLAUDE.md                # ← AI assistant instructions
```

**Traditional approach** gives you:
- `papers/`, `code/`, `data/` folders
- Static README templates
- Manual organization

**Research Repo** gives you:
- **Invocable AI skills** for paper management
- **Priority-based search** (P1: recent core, P2: recent supporting, P3: historical)
- **Standardized 2-3 sentence summaries** (Purpose → Method → Results)
- **Automated classification** and tagging
- **Git discipline** (personal notes stay local, curated content goes public)

---

## 🚀 Quick Start

### Installation

```bash
# Option 1: Install from .skill file (recommended)
# Download research-repo.skill from Releases
/skill-install path/to/research-repo.skill

# Option 2: Clone repository
cd ~/.claude/skills/
git clone https://github.com/C-myu/research-repo-skill.git
```

### Create Your First Repository

Just tell Claude what you need:

```bash
# Example 1: Computer Science domain
"I want to create a research repository for tracking
LLM hallucination mitigation papers. Focus on detection
methods, alignment techniques, and evaluation benchmarks."

# Example 2: Interdisciplinary domain
"Help me set up a research repository for AI in mental health.
Priorities: clinical applications highest, then detection methods,
then privacy-preserving techniques."

# Example 3: Niche domain
"Build a literature tracker for quantum computing in finance.
Focus areas: quantum ML algorithms, quantum optimization for
trading, and quantum cryptography for fintech."
```

**What you get** in ~2 minutes:
- ✅ Complete repository structure
- ✅ Domain-specific search queries (30-50 queries)
- ✅ Color-coded tagging system (3-4 categories, 8-15 tags)
- ✅ Two invocable skills (`/search-papers`, `/add-paper`)
- ✅ Git repository initialized
- ✅ Bilingual README (English + Chinese)

---

## 🛠️ How It Works

### Priority-Driven Research Focus

Research Repo organizes your literature by **priority tiers**, not just topics:

```
Priority 1 (Core Focus)     → oneYear filter, 15-20 queries
├─ What you must stay current on
└─ Time-sensitive research areas

Priority 2 (Supporting)     → oneMonth filter, 10-15 queries
├─ Important but not critical
└─ Contextual research areas

Priority 3 (Foundational)   → noLimit filter, 8-10 queries
├─ Historical context
└─ Seminal papers you should know
```

### Automated Workflows

**1. Discovery** (`/search-papers`)
```
You: /search-papers

Claude:
✨ Executing 17 P1 queries (oneYear filter)...
✨ Executing 15 P2 queries (oneMonth filter)...
✨ Filtering duplicates against existing repository...
✨ Classifying results by priority...
✨ Updating TODO.md with 12 new papers...

📊 Results: 12 new papers found
   - P1 (Core): 8 papers
   - P2 (Supporting): 3 papers
   - P3 (Foundational): 1 paper
```

**2. Addition** (`/add-paper`)
```
You: /add-paper

Claude:
📄 Paper: "Self-Check: Boosting Generative Reliability"
🏷️  Priority: P1 - Detection Method
🏷️  Tags: Self-Verification, Consistency_Checking
📝 Summary: This paper proposes SelfCheck, a method where LLMs
   generate multiple samples and use self-consistency to detect
   hallucinations. Achieves 24.5% reduction in factual errors
   on TruthfulQA benchmark.

✨ Created reading notes in paper_notes/
✨ Updated README.md with entry
✨ Committed to git: "Add paper: SelfCheck (NeurIPS 2023)"
```

---

## 🎓 Example Use Cases

### Academic Research

Track papers for your thesis or research group:

```bash
# PhD student
"Create a research repo for my PhD on few-shot learning.
Focus: meta-learning highest, then prompt engineering,
then applications."

# Research lab
"Set up a shared repository for our NLP group.
Priorities: LLM efficiency, multilingual models,
evaluation methods."
```

### Industry R&D

Organize competitive intelligence and technical literature:

```bash
# Tech company
"Build a repository for tracking LLM ops research.
Focus areas: deployment infrastructure, monitoring,
cost optimization, A/B testing."

# Quantitative finance
"Create a research tracker for ML in trading.
Priorities: time-series forecasting highest, then
sentiment analysis, then portfolio optimization."
```

### Personal Learning

Curate papers for self-study and exploration:

```bash
# Domain switcher
"I'm a software engineer transitioning to AI safety.
Create a repository to help me learn the field.
Focus: alignment research highest, then interpretability,
then robustness."

# Interdisciplinary explorer
"I'm interested in AI for climate change.
Track papers on climate modeling, emissions optimization,
and policy applications."
```

---

## 📊 Architecture

Research Repo is a **meta-skill** - it creates domain-specific skills:

```
research-repo (meta-skill)
│
├─ Generates ─→ search-[domain] skill
│              ├─ Automated web search
│              ├─ Priority-based queries
│              └─ Duplicate detection
│
└─ Generates ─→ add-[domain] skill
               ├─ Classification workflow
               ├─ Standardized summaries
               └─ Git integration
```

### Progressive Disclosure Design

Efficient context loading through layered design:

- **Layer 1**: SKILL.md metadata (~100 words)
- **Layer 2**: Quick workflow guide (~200 lines)
- **Layer 3**: Detailed references (~1,500 lines, on-demand)

This keeps Claude responsive while providing comprehensive guidance when needed.

---

## 🧪 Validation

Rigorously tested with skill-creator methodology:

- ✅ **3 test iterations** with diverse domains
- ✅ **6 parallel test runs** per iteration (with-skill vs without-skill)
- ✅ **19 objective assertions** validated
- ✅ **100% success rate** in final iteration

See [research-repo-workspace/](research-repo-workspace/) for complete test data.

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [SKILL.md](research-repo/SKILL.md) | Main skill definition |
| [setup-wizard.md](research-repo/references/setup-wizard.md) | Interactive configuration guide |
| [faq.md](research-repo/references/faq.md) | Common questions |
| [templates/](research-repo/references/templates/) | Complete template reference |

---

## 🤝 Contributing

Contributions welcome! Areas of interest:

- 🔧 **Bug fixes** - Report issues with test cases
- ✨ **New features** - Suggest workflow improvements
- 📖 **Documentation** - Expand guides and examples
- 🧪 **Testing** - Add validation for new domains

Feel free to open issues or pull requests on GitHub.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🌟 Acknowledgments

Built with [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) framework by Anthropic.

---

<div align="center">

**Made with ❤️ for the research community by Claude Code**

*Turn paper chaos into organized knowledge*

[⭐ Star us on GitHub](https://github.com/C-myu/research-repo-skill) •
[🐛 Report issues](https://github.com/C-myu/research-repo-skill/issues) •
[💡 Suggest features](https://github.com/C-myu/research-repo-skill/discussions)

</div>
