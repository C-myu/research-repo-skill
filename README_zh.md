# 📚 Research Repo - AI 驱动的科研论文库构建工具

[![](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://claude.com/claude-code)
[![](https://img.shields.io/badge/成功率-100%25-green)](benchmark.md)
[![](https://img.shields.io/badge/提升幅度-+95%25-brightgreen)](benchmark.md)
[![](https://img.shields.io/badge/许可证-MIT-purple)](LICENSE)

中文 | [**English**](README.md)

> **创建技能的元技能**：Research Repo 不仅仅是一个论文追踪工具——它是一个 Claude Code 元技能，能够生成领域特定的科研工作流，具备自动化论文发现、分类和文档化能力。

---

## 🎯 解决的问题

**使用前**：论文散落在各处文件夹、组织方式不一致、手动搜索和追踪、零散的笔记导致见解丢失。

**使用后**：一个结构完整、AI 辅助的科研论文库，具备：
- 🔍 **自动化论文发现** - 通过 `/search-papers` 命令
- 📋 **标准化分类系统** - 基于优先级的组织方式
- 🤖 **AI 辅助工作流** - 通过 `/add-paper` 命令添加论文
- 📊 **可视化标签系统** - 颜色编码的分类体系
- 🔄 **清晰的 Git 集成** - 只跟踪公开内容

---

## ✨ 为什么选择 Research Repo？

### 🚀 经过验证的效果

在 3 个不同的研究领域测试，**成功率达到 100%**：

| 领域 | 使用 Skill | 不使用 Skill | 提升 |
|------|-----------|--------------|------|
| LLM 幻觉消除 | ✅ 100% | ❌ 0% | **+100%** |
| 合成数据同质化 | ✅ 100% | ❌ 0% | **+100%** |
| LLM 量化金融 | ✅ 100% | ⚠️ 14% | **+86%** |
| **平均** | **100%** | **4.8%** | **+95.2%** |

查看[基准测试结果](research-repo-workspace/iteration-2/benchmark.md)了解详细分析。

### 🎨 独特之处

**不只是文件模板**——Research Repo 创建**可执行的 AI 工作流**：

```
your-repo/
├── .claude/skills/          # ← 可调用的 AI 工作流
│   ├── search-papers/       #    运行：/search-papers
│   │   ├── SKILL.md         #    自动发现论文
│   │   └── references/queries.md
│   └── add-paper/           #    运行：/add-paper
│       ├── SKILL.md         #    添加论文并生成 2-3 句摘要
│       └── references/notes-template.md
├── research-focus.md        # ← 优先级驱动的搜索策略
├── classification-guide.md  # ← 颜色编码的标签系统
└── CLAUDE.md                # ← AI 助手指令
```

**传统方法**提供：
- `papers/`、`code/`、`data/` 文件夹
- 静态 README 模板
- 手动组织

**Research Repo** 提供：
- **可调用的 AI 技能**用于论文管理
- **基于优先级的搜索**（P1：最新核心，P2：最新辅助，P3：历史文献）
- **标准化 2-3 句摘要**（目的 → 方法 → 结果）
- **自动分类**和标签
- **Git 纪律**（个人笔记保留本地，精选内容公开）

---

## 🚀 快速开始

### 安装

```bash
# 方式 1：从 .skill 文件安装（推荐）
# 从 Releases 下载 research-repo.skill
/skill-install path/to/research-repo.skill

# 方式 2：克隆仓库
cd ~/.claude/skills/
git clone https://github.com/C-myu/research-repo-skill.git
```

### 创建你的第一个论文库

只需告诉 Claude 你的需求：

```bash
# 示例 1：计算机领域
"我想创建一个科研论文库来追踪 LLM 幻觉消除方面的论文。
重点关注：检测方法、对齐技术、评估基准。"

# 示例 2：跨学科领域
"帮我建立一个 AI 心理健康方向的科研论文库。
优先级：临床应用最高，然后是检测方法，最后是隐私保护技术。"

# 示例 3：细分领域
"构建一个量子计算在金融领域应用的文献追踪器。
重点领域：量子机器学习算法、量子优化交易、量子金融密码学。"
```

**约 2 分钟后**你将获得：
- ✅ 完整的论文库结构
- ✅ 领域特定的搜索查询（30-50 个）
- ✅ 颜色编码的标签系统（3-4 个类别，8-15 个标签）
- ✅ 两个可调用技能（`/search-papers`、`/add-paper`）
- ✅ Git 仓库已初始化
- ✅ 双语 README（英文 + 中文）

---

## 🛠️ 工作原理

### 优先级驱动的研究聚焦

Research Repo 按**优先级层级**而非仅按主题组织文献：

```
优先级 1（核心焦点）  → oneYear 过滤器，15-20 个查询
├─ 你必须保持最新关注的内容
└─ 时效性强的研究领域

优先级 2（支持研究）  → oneMonth 过滤器，10-15 个查询
├─ 重要但非关键
└─ 上下文相关的研究领域

优先级 3（基础文献）  → noLimit 过滤器，8-10 个查询
├─ 历史背景
└─ 你应该知道的经典论文
```

### 自动化工作流

**1. 发现**（`/search-papers`）
```
你：/search-papers

Claude：
✨ 正在执行 17 个 P1 查询（oneYear 过滤器）...
✨ 正在执行 15 个 P2 查询（oneMonth 过滤器）...
✨ 正在过滤重复项（与现有论文库对比）...
✨ 正在按优先级分类结果...
✨ 正在更新 TODO.md（发现 12 篇新论文）...

📊 结果：发现 12 篇新论文
   - P1（核心）：8 篇
   - P2（支持）：3 篇
   - P3（基础）：1 篇
```

**2. 添加**（`/add-paper`）
```
你：/add-paper

Claude：
📄 论文："Self-Check: Boosting Generative Reliability"
🏷️  优先级：P1 - 检测方法
🏷️  标签：Self-Verification, Consistency_Checking
📝 摘要：本文提出 SelfCheck，一种让 LLM 生成多个样本并使用自洽性
   来检测幻觉的方法。在 TruthfulQA 基准上实现 24.5% 的事实错误减少。

✨ 已在 paper_notes/ 创建阅读笔记
✨ 已更新 README.md 添加条目
✨ 已提交到 git："Add paper: SelfCheck (NeurIPS 2023)"
```

---

## 🎓 使用场景示例

### 学术研究

为学位论文或研究小组追踪论文：

```bash
# 博士生
"为我的 Few-shot Learning 博士论文创建一个科研论文库。
重点：元学习最高，然后是提示工程，最后是应用。"

# 研究实验室
"为我们 NLP 小组建立一个共享的论文库。
优先级：LLM 效率、多语言模型、评估方法。"
```

### 工业界研发

组织竞争情报和技术文献：

```bash
# 科技公司
"构建一个追踪 LLM Ops 研究的论文库。
重点领域：部署基础设施、监控、成本优化、A/B 测试。"

# 量化金融
"创建一个 ML 在交易中应用的科研追踪器。
优先级：时间序列预测最高，然后是情感分析，最后是投资组合优化。"
```

### 个人学习

为自学和探索策划论文：

```bash
# 领域转换者
"我是一个转向 AI 安全的软件工程师。
创建一个论文库帮助我学习这个领域。
重点：对齐研究最高，然后是可解释性，最后是鲁棒性。"

# 跨学科探索者
"我对 AI 在气候变化中的应用感兴趣。
追踪气候建模、排放优化、政策应用的论文。"
```

---

## 📊 架构设计

Research Repo 是一个**元技能**——它创建领域特定的技能：

```
research-repo（元技能）
│
├─ 生成 ─→ search-[domain] 技能
│            ├─ 自动化网页搜索
│            ├─ 基于优先级的查询
│            └─ 重复项检测
│
└─ 生成 ─→ add-[domain] 技能
             ├─ 分类工作流
             ├─ 标准化摘要
             └─ Git 集成
```

### 渐进式披露设计

通过分层设计实现高效的上下文加载：

- **第 1 层**：SKILL.md 元数据（~100 词）
- **第 2 层**：快速工作流指南（~200 行）
- **第 3 层**：详细参考文档（~1,500 行，按需加载）

这使 Claude 保持响应，同时在需要时提供全面指导。

---

## 🧪 验证测试

使用 skill-creator 方法进行严格测试：

- ✅ **3 轮测试迭代**，涵盖不同领域
- ✅ 每轮 **6 个并行测试**（with-skill vs without-skill）
- ✅ **19 个客观断言**验证
- ✅ 最终迭代 **100% 成功率**

查看 [research-repo-workspace/](research-repo-workspace/) 获取完整测试数据。

---

## 📚 文档

| 文档 | 用途 |
|------|------|
| [SKILL.md](research-repo/SKILL.md) | 主要技能定义 |
| [setup-wizard.md](research-repo/references/setup-wizard.md) | 交互式配置指南 |
| [faq.md](research-repo/references/faq.md) | 常见问题解答 |
| [templates/](research-repo/references/templates/) | 完整模板参考 |

---

## 🤝 贡献

欢迎贡献！感兴趣的领域：

- 🔧 **Bug 修复** - 使用测试用例报告问题
- ✨ **新功能** - 建议工作流改进
- 📖 **文档** - 扩展指南和示例
- 🧪 **测试** - 为新领域添加验证

欢迎在 GitHub 上提出 issue 或 pull request。

---

## 📄 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)

---

## 🌟 致谢

使用 Anthropic 的 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 框架构建。

---

<div align="center">

**😄Claude Code 为科研社区用 ❤️ 打造**

[⭐ 在 GitHub 上点赞](https://github.com/C-myu/research-repo-skill) •
[🐛 报告问题](https://github.com/C-myu/research-repo-skill/issues) •
[💡 建议功能](https://github.com/C-myu/research-repo-skill/discussions)

</div>
