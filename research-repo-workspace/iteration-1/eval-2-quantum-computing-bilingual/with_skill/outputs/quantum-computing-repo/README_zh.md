# 量子计算研究

量子计算研究的精选文献集合。用于：
- 量子算法、硬件和应用的中心化参考书目
- 撰写学术论文相关工作部分的资源
- 技术路线图和研究趋势的参考资料

**关注领域：**
- **量子算法**（最高优先级）：新型算法、变分量子算法、量子机器学习
- **量子硬件**：处理器设计、量子比特技术、错误纠正
- **量子应用**：化学、金融、优化和实际用例

**语言：** [English](README.md) | 中文

---

## 2026年

### 一月

*尚未添加论文。使用 `/search-papers` 开始收集研究。*

---

## 2025年

### 十二月

*尚未添加论文。*

---

## 仓库结构

```
quantum-computing-repo/
├── README.md              # 本文件（英文版）
├── README_zh.md           # 中文版
├── TODO.md                # 待审阅论文
├── CLAUDE.md              # AI 助手指令
├── research-focus.md      # 研究优先级和搜索策略
├── classification-guide.md # 标签系统
├── paper_notes/           # 本地阅读笔记（不提交）
└── .claude/skills/
    ├── search-papers/     # 论文发现技能
    └── add-paper/         # 论文添加技能
```

---

## 如何使用本仓库

### 论文发现
```
/search-papers
```
按优先级搜索最新的量子计算论文（算法 > 硬件 > 应用）。

### 添加论文
```
/add-paper
```
阅读论文后使用此命令，以标准化格式添加论文，包括分类和标签。

---

## 标签系统

论文按类别标记（参见 [classification-guide.md](classification-guide.md)）：

**应用领域**（绿色）：
- ![Chemistry](https://img.shields.io/badge/Chemistry-008754) 化学
- ![Finance](https://img.shields.io/badge/Finance-00a86b) 金融
- ![Optimization](https://img.shields.io/badge/Optimization-33d498) 优化
- ![Fundamental](https://img.shields.io/badge/Fundamental-66e5b8) 基础

**方法**（紫色）：
- ![VQA](https://img.shields.io/badge/VQA-6554c0) 变分量子算法
- ![Optimization](https://img.shields.io/badge/Optimization-8066ff) 优化方法
- ![Machine_Learning](https://img.shields.io/badge/Machine_Learning-997dff) 机器学习
- ![Cryptography](https://img.shields.io/badge/Cryptography-aa88ff) 密码学

**数据类型**（蓝色）：
- ![Benchmark](https://img.shields.io/badge/Benchmark-0052cc) 基准
- ![Simulation](https://img.shields.io/badge/Simulation-0066ff) 仿真
- ![Real_World](https://img.shields.io/badge/Real_World-3399ff) 真实世界

**特殊属性**（橙色）：
- ![Error_Correction](https://img.shields.io/badge/Error_Correction-ff6b00) 错误纠正
- ![Fault_Tolerant](https://img.shields.io/badge/Fault_Tolerant-ff8c00) 容错
- ![NISQ](https://img.shields.io/badge/NISQ-ffab33) 含噪中等规模量子
- ![Hybrid](https://img.shields.io/badge/Hybrid-ffcc66) 混合

---

## 研究优先级

**优先级 1：量子算法**（最高）
- 新型量子算法和理论进展
- 变分算法（VQE、QAOA）
- 量子机器学习和优化
- 时间过滤器：最近一年

**优先级 2：量子硬件**
- 处理器架构和量子比特技术
- 错误纠正和容错
- 时间过滤器：最近一月

**优先级 3：量子应用**
- 实际应用和案例研究
- 量子-经典混合方法
- 时间过滤器：无限制

参见 [research-focus.md](research-focus.md) 了解详细的搜索策略和决策树。

---

## 贡献

本仓库使用 AI 辅助策展，通过 Claude Code Skills 实现。论文通过标准化工作流程添加，确保：
- 按优先级一致分类
- 适当的标签（每篇论文 2-4 个标签）
- 双语条目（英文/中文）
- 带提交消息的 Git 跟踪更改

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)
