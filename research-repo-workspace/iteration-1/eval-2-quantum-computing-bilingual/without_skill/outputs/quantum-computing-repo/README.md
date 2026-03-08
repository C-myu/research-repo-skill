# Quantum Computing Research Repository
# 量子计算研究仓库

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

### Overview

This repository tracks research papers in quantum computing with a focus on three main areas:

1. **Quantum Algorithms** (Highest Priority)
   - Quantum machine learning algorithms
   - Quantum optimization algorithms
   - Quantum cryptography protocols
   - Quantum simulation algorithms
   - Quantum error correction

2. **Quantum Hardware Construction**
   - Superconducting quantum computers
   - Trapped ion quantum computers
   - Photonic quantum computing
   - Topological quantum computing
   - Quantum control systems

3. **Quantum Applications**
   - Quantum chemistry simulations
   - Quantum finance applications
   - Quantum optimization in practice
   - Quantum sensing and metrology
   - Quantum networking

### Repository Structure

```
quantum-computing-repo/
├── papers/
│   ├── algorithms/          # Quantum algorithms papers
│   ├── hardware/            # Quantum hardware construction papers
│   └── applications/        # Quantum applications papers
├── templates/               # Paper note templates
├── .research-repo/          # Configuration and skills
│   ├── config.yaml          # Repository configuration
│   └── skills/              # Custom skills for paper analysis
├── README.md                # This file
└── README_zh.md             # Chinese version of README
```

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd quantum-computing-repo
   ```

2. **Add a new paper**
   ```bash
   # Use the research-repo skill to add a paper
   research-repo paper add --arxiv <arxiv-id> --category algorithms
   ```

3. **Search papers**
   ```bash
   research-repo paper search --query "quantum machine learning"
   ```

4. **Generate reading list**
   ```bash
   research-repo paper list --priority high --category algorithms
   ```

### Priority System

Papers are tagged with priority levels:
- **High**: Breakthrough results, fundamental algorithms
- **Medium**: Significant improvements, novel applications
- **Low**: Incremental improvements, specialized topics

### Contributing

This is a personal research repository. Papers are added based on relevance and impact on the field.

### Tags

- `quantum-algorithms` - Papers related to quantum algorithms
- `quantum-hardware` - Papers related to quantum hardware
- `quantum-applications` - Papers related to quantum applications
- `ml` - Machine learning applications
- `optimization` - Optimization algorithms
- `cryptography` - Cryptography protocols
- `error-correction` - Quantum error correction
- `superconducting` - Superconducting quantum computers
- `trapped-ion` - Trapped ion quantum computers
- `photonic` - Photonic quantum computing
- `topological` - Topological quantum computing
- `chemistry` - Quantum chemistry
- `finance` - Quantum finance
- `sensing` - Quantum sensing
- `networking` - Quantum networking

---

<a name="中文"></a>
## 中文

### 概述

本仓库追踪量子计算领域的研究论文，重点关注三个主要方向：

1. **量子算法**（最高优先级）
   - 量子机器学习算法
   - 量子优化算法
   - 量子密码学协议
   - 量子模拟算法
   - 量子纠错

2. **量子硬件构建**
   - 超导量子计算机
   - 离子阱量子计算机
   - 光量子计算
   - 拓扑量子计算
   - 量子控制系统

3. **量子应用**
   - 量子化学模拟
   - 量子金融应用
   - 实用量子优化
   - 量子传感与计量
   - 量子网络

### 仓库结构

```
quantum-computing-repo/
├── papers/
│   ├── algorithms/          # 量子算法论文
│   ├── hardware/            # 量子硬件构建论文
│   └── applications/        # 量子应用论文
├── templates/               # 论文笔记模板
├── .research-repo/          # 配置和技能
│   ├── config.yaml          # 仓库配置
│   └── skills/              # 论文分析自定义技能
├── README.md                # 本文件
└── README_zh.md             # 中文版README
```

### 快速开始

1. **克隆仓库**
   ```bash
   git clone <repository-url>
   cd quantum-computing-repo
   ```

2. **添加新论文**
   ```bash
   # 使用 research-repo 技能添加论文
   research-repo paper add --arxiv <arxiv-id> --category algorithms
   ```

3. **搜索论文**
   ```bash
   research-repo paper search --query "quantum machine learning"
   ```

4. **生成阅读列表**
   ```bash
   research-repo paper list --priority high --category algorithms
   ```

### 优先级系统

论文按优先级标记：
- **高（High）**：突破性结果、基础算法
- **中（Medium）**：重大改进、新颖应用
- **低（Low）**：渐进式改进、专业主题

### 贡献

这是个人研究仓库。根据论文的相关性和领域影响力添加论文。

### 标签

- `quantum-algorithms` - 量子算法相关论文
- `quantum-hardware` - 量子硬件相关论文
- `quantum-applications` - 量子应用相关论文
- `ml` - 机器学习应用
- `optimization` - 优化算法
- `cryptography` - 密码学协议
- `error-correction` - 量子纠错
- `superconducting` - 超导量子计算机
- `trapped-ion` - 离子阱量子计算机
- `photonic` - 光量子计算
- `topological` - 拓扑量子计算
- `chemistry` - 量子化学
- `finance` - 量子金融
- `sensing` - 量子传感
- `networking` - 量子网络

---

## License

MIT License - See LICENSE file for details
