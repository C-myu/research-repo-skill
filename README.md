# Research Repository Setup Skill

[![](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://claude.com/claude-code)
[![](https://img.shields.io/badge/Type-Meta_Skill-green)]()
[![](https://img.shields.io/badge/License-MIT-purple)]()

[**中文文档**](README_zh.md) | English

A Claude Code meta-skill for creating and setting up automated research repositories for curating academic papers in any domain.

## 🎯 What It Does

This skill helps you create fully-structured research repositories with:

- ✅ **Automated paper discovery workflows** - Priority-based search strategies
- ✅ **Standardized classification systems** - Customizable tags and categories
- ✅ **AI-assisted documentation** - Template-driven summaries and notes
- ✅ **Git-integrated workflow** - Clean version control for public sharing
- ✅ **Progressive disclosure design** - Efficient context loading

## 📁 Structure

```
research-repo/
├── SKILL.md (283 lines)              # Main entry point
└── references/                        # On-demand reference materials
    ├── setup-wizard.md (590 lines)    # Interactive configuration guide
    ├── faq.md (220 lines)             # Common questions & answers
    └── templates/                     # Modular template system
        ├── core-files.md              # CLAUDE.md, research-focus.md, etc.
        ├── git-config.md              # .gitignore, LICENSE
        ├── readme-entry.md            # README entry format
        └── skills/
            ├── search-items-skill.md  # Search workflow template
            └── add-item-skill.md      # Add workflow template
```

## 🚀 Quick Start

### Installation

#### Option 1: Install from Release (Recommended)
1. Download `research-repo.skill` from [Releases](https://github.com/C-myu/research-repo-skill/releases)
2. In Claude Code, run: `/skill-install path/to/research-repo.skill`

#### Option 2: Clone Repository
```bash
cd ~/.claude/skills/
git clone https://github.com/C-myu/research-repo-skill.git
```

### Usage

Once installed, say to Claude:

- "Help me create a research repository for **AI in mental health**"
- "I want to set up a **quantum computing** paper tracker"
- "Build a literature database for **LLM education** research"

The skill will guide you through:
1. Defining your research domain
2. Setting up priorities and tags
3. Creating domain-specific search workflows
4. Configuring git integration

## 📖 Features

### Domain-Agnostic Design

Works for **any** research domain:
- Academic papers (computer science, medicine, physics, etc.)
- Industry reports and white papers
- Technical documentation
- Blog posts and articles

### Modular Template System

Templates are split for efficient context loading:
- **core-files.md** - Primary configuration (~400 lines)
- **git-config.md** - Git setup (~60 lines)
- **skills/** - Skill-specific templates (~200 lines each)

Load only what you need, when you need it.

### Automated Workflows

Two core skills are created for your domain:

1. **search-[items]** (e.g., search-papers) - Automated discovery
   - Priority-based search queries
   - Time filtering (recent vs. historical)
   - Duplicate detection
   - TODO list updates

2. **add-[item]** (e.g., add-paper) - Standardized addition
   - Classification and tagging
   - Template-driven summaries
   - Local reading notes
   - Git commits

## 🎓 Example Domains

The skill includes adaptation examples:

- **AI-for-Climate-Change**
  - Priorities: Climate modeling > Policy analysis > Carbon tracking
  - Tags: Emissions, Modeling, Policy, Adaptation

- **LLM-for-Education**
  - Priorities: Personalized learning > Assessment > Content generation
  - Tags: Personalization, Assessment, Tutoring, Multi-modal

- **Quantum-Computing-Papers**
  - Priorities: Algorithms > Hardware > Applications
  - Tags: Algorithms, Hardware, Cryptography, Simulation

## 🛠️ Development

Built with [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) guidelines:

- **Progressive disclosure** - Metadata → SKILL.md → references
- **Concise design** - Only essential information in context
- **Modular references** - Split by use case for efficiency

### Validation

```bash
# Validate the skill structure
python3 /path/to/skill-creator/scripts/quick_validate.py /path/to/research-repo
```

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Main skill documentation
- **[setup-wizard.md](references/setup-wizard.md)** - Step-by-step configuration guide
- **[faq.md](references/faq.md)** - Common questions and troubleshooting
- **[templates/](references/templates/)** - Complete template reference

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

Feel free to use and modify for your needs.

## 🌟 Acknowledgments

Built using the [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) framework by Anthropic.

---

**Made with ❤️ for the research community**
