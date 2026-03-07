# 研究仓库设置技能 (Research Repository Setup Skill)

[![](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://claude.com/claude-code)
[![](https://img.shields.io/badge/Type-元技能-green)]()
[![](https://img.shields.io/badge/License-MIT-purple)]()

中文 | [**English**](README.md)

一个 Claude Code 元技能（meta-skill），用于创建和设置自动化研究仓库，适用于任何领域的学术论文整理。

## 🎯 功能介绍

这个技能帮助你创建结构完整的研究仓库，具备以下特性：

- ✅ **自动化论文发现工作流** - 基于优先级的搜索策略
- ✅ **标准化分类系统** - 可定制的标签和类别
- ✅ **AI 辅助文档编写** - 模板驱动的摘要和笔记
- ✅ **Git 集成工作流** - 整洁的版本控制，便于公开分享
- ✅ **渐进式公开设计** - 高效的上下文加载

## 📁 文件结构

```
research-repo/
├── SKILL.md                         # 主入口文件
└── references/                      # 按需加载的参考资料
    ├── setup-wizard.md              # 交互式配置向导
    ├── faq.md                       # 常见问题解答
    └── templates/                   # 模块化模板系统
        ├── core-files.md            # 核心配置文件
        ├── git-config.md            # Git 配置
        ├── readme-entry.md          # README 条目格式
        └── skills/
            ├── search-items-skill.md # 搜索工作流模板
            └── add-item-skill.md    # 添加工作流模板
```

## 🚀 快速开始

### 安装方法

#### 方式 1：从 Release 安装（推荐）
1. 从 [Releases](https://github.com/C-myu/research-repo-skill/releases) 下载 `research-repo.skill`
2. 在 Claude Code 中运行：`/skill-install path/to/research-repo.skill`

#### 方式 2：克隆仓库
```bash
cd ~/.claude/skills/
git clone https://github.com/C-myu/research-repo-skill.git
```

### 使用方法

安装完成后，对 Claude 说：

- "帮我创建一个 **AI 心理健康** 领域的研究仓库"
- "我想建立一个 **量子计算** 论文追踪系统"
- "为 **LLM 教育** 研究构建文献数据库"

技能会引导你完成：
1. 定义你的研究领域
2. 设置优先级和标签
3. 创建领域特定的搜索工作流
4. 配置 Git 集成

## 📖 主要特性

### 领域无关设计

适用于**任何**研究领域：
- 学术论文（计算机科学、医学、物理学等）
- 行业报告和白皮书
- 技术文档
- 博客文章和资讯

### 模块化模板系统

模板按模块拆分，实现高效的上下文加载：
- **core-files.md** - 主要配置（约400行）
- **git-config.md** - Git 设置（约60行）
- **skills/** - 技能特定模板（各约200行）

按需加载，仅在需要时读取相应内容。

### 自动化工作流

为你的领域创建两个核心技能：

1. **search-[items]**（如 search-papers）- 自动发现
   - 基于优先级的搜索查询
   - 时间过滤（最新 vs 历史）
   - 重复检测
   - TODO 列表更新

2. **add-[item]**（如 add-paper）- 标准化添加
   - 分类和标签
   - 模板驱动摘要
   - 本地阅读笔记
   - Git 提交

## 🎓 示例领域

技能包含适配示例：

- **AI-for-Climate-Change**
  - 优先级：气候建模 > 政策分析 > 碳追踪
  - 标签：排放、建模、政策、适应

- **LLM-for-Education**
  - 优先级：个性化学习 > 评估 > 内容生成
  - 标签：个性化、评估、辅导、多模态

- **Quantum-Computing-Papers**
  - 优先级：算法 > 硬件 > 应用
  - 标签：算法、硬件、密码学、模拟

## 🛠️ 开发

按照 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 指南构建：

- **渐进式公开** - 元数据 → SKILL.md → 参考资料
- **简洁设计** - 上下文只包含必要信息
- **模块化参考** - 按用途拆分，提高效率

### 验证

```bash
# 验证技能结构
python3 /path/to/skill-creator/scripts/quick_validate.py /path/to/research-repo
```

## 📚 文档

- **[SKILL.md](SKILL.md)** - 主要技能文档
- **[setup-wizard.md](references/setup-wizard.md)** - 分步配置指南
- **[faq.md](references/faq.md)** - 常见问题和故障排除
- **[templates/](references/templates/)** - 完整模板参考

## 🤝 贡献

欢迎贡献！请：

1. Fork 本仓库
2. 创建功能分支
3. 进行修改
4. 提交 Pull Request

对于重大更改，请先创建 Issue 讨论你想要修改的内容。

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

可以自由使用和修改以满足你的需求。

## 🌟 致谢

使用 Anthropic 的 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 框架构建。

---

**为研究社区用 ❤️ 制作**
