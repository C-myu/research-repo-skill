# Paper Note Template
# 论文笔记模板

[English](#english-content) | [中文](#中文内容)

---

<a name="english-content"></a>
## English Content

### Basic Information / 基本信息

**Title / 标题**: {{title}}
**Title (Chinese) / 标题（中文）**: {{title_zh}}

**Authors / 作者**:
{{#authors}}
- {{.}}
{{/authors}}

**Year / 年份**: {{year}}

**Venue / 发表场合**: {{venue}}
**Venue (Chinese) / 发表场合（中文）**: {{venue_zh}}

**Links / 链接**:
{{#arxiv_id}}
- arXiv: https://arxiv.org/abs/{{arxiv_id}}
{{/arxiv_id}}
{{#doi}}
- DOI: https://doi.org/{{doi}}
{{/doi}}

**Category / 分类**: {{category}}
**Priority / 优先级**: {{priority}}

**Tags / 标签**:
{{#tags}}
- `{{.}}`
{{/tags}}

---

### Abstract / 摘要

{{abstract}}

### Chinese Abstract / 中文摘要

{{abstract_zh}}

---

### Key Contributions / 主要贡献

{{#key_contributions}}
1. {{.}}
{{/key_contributions}}

### Main Contributions (Chinese) / 主要贡献（中文）

{{#key_contributions_zh}}
1. {{.}}
{{/key_contributions_zh}}

---

### Methodology / 方法

{{methodology}}

### Methodology (Chinese) / 方法（中文）

{{methodology_zh}}

---

### Key Results / 主要结果

{{#key_results}}
- {{.}}
{{/key_results}}

### Key Results (Chinese) / 主要结果（中文）

{{#key_results_zh}}
- {{.}}
{{/key_results_zh}}

---

### Strengths / 优点

{{#strengths}}
- {{.}}
{{/strengths}}

### Strengths (Chinese) / 优点（中文）

{{#strengths_zh}}
- {{.}}
{{/strengths_zh}}

---

### Limitations / 局限性

{{#limitations}}
- {{.}}
{{/limitations}}

### Limitations (Chinese) / 局限性（中文）

{{#limitations_zh}}
- {{.}}
{{/limitations_zh}}

---

### Future Work / 未来工作

{{#future_work}}
- {{.}}
{{/future_work}}

### Future Work (Chinese) / 未来工作（中文）

{{#future_work_zh}}
- {{.}}
{{/future_work_zh}}

---

### Personal Notes / 个人笔记

{{notes}}

### Personal Notes (Chinese) / 个人笔记（中文）

{{notes_zh}}

---

### Related Papers / 相关论文

{{#related_papers}}
- [{{title}}]({{arxiv_id}})
{{/related_papers}}

### Related Papers (Chinese) / 相关论文（中文）

{{#related_papers}}
- [{{title_zh}}]({{arxiv_id}})
{{/related_papers}}

---

### Reading Status / 阅读状态

**Date Added / 添加日期**: {{date_added}}
**Date Read / 阅读日期**: {{date_read}}
**Rating / 评分**: {{rating}} / 5

**Understanding Level / 理解程度**:
- [ ] Fully understand / 完全理解
- [ ] Mostly understand / 大部分理解
- [ ] Partially understand / 部分理解
- [ ] Need to re-read / 需要重读

**Relevance / 相关性**:
- [ ] Highly relevant / 高度相关
- [ ] Somewhat relevant / 部分相关
- [ ] Not directly relevant / 不直接相关

---

### Questions & Discussion / 问题与讨论

{{questions}}

### Questions & Discussion (Chinese) / 问题与讨论（中文）

{{questions_zh}}

---

<a name="中文内容"></a>
## 中文内容

### 基本信息

**标题**: {{title}}
**标题（中文）**: {{title_zh}}

**作者**:
{{#authors}}
- {{.}}
{{/authors}}

**年份**: {{year}}

**发表场合**: {{venue}}
**发表场合（中文）**: {{venue_zh}}

**链接**:
{{#arxiv_id}}
- arXiv: https://arxiv.org/abs/{{arxiv_id}}
{{/arxiv_id}}
{{#doi}}
- DOI: https://doi.org/{{doi}}
{{/doi}}

**分类**: {{category}}
**优先级**: {{priority}}

**标签**:
{{#tags}}
- `{{.}}`
{{/tags}}

---

### 摘要

{{abstract_zh}}

---

### 主要贡献

{{#key_contributions_zh}}
1. {{.}}
{{/key_contributions_zh}}

---

### 方法

{{methodology_zh}}

---

### 主要结果

{{#key_results_zh}}
- {{.}}
{{/key_results_zh}}

---

### 优点

{{#strengths_zh}}
- {{.}}
{{/strengths_zh}}

---

### 局限性

{{#limitations_zh}}
- {{.}}
{{/limitations_zh}}

---

### 未来工作

{{#future_work_zh}}
- {{.}}
{{/future_work_zh}}

---

### 个人笔记

{{notes_zh}}

---

### 相关论文

{{#related_papers}}
- [{{title_zh}}]({{arxiv_id}})
{{/related_papers}}

---

### 阅读状态

**添加日期**: {{date_added}}
**阅读日期**: {{date_read}}
**评分**: {{rating}} / 5

**理解程度**:
- [ ] 完全理解
- [ ] 大部分理解
- [ ] 部分理解
- [ ] 需要重读

**相关性**:
- [ ] 高度相关
- [ ] 部分相关
- [ ] 不直接相关

---

### 问题与讨论

{{questions_zh}}
