# Reading List Template
# 阅读列表模板

[English](#english-list) | [中文](#中文列表)

---

<a name="english-list"></a>
## English Reading List

### High Priority Papers / 高优先级论文

#### Quantum Algorithms / 量子算法

{{#high_priority_algorithms}}
1. **{{title}}** ({{year}})
   - Authors: {{authors}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - Tags: {{tags}}
   - Added: {{date_added}}
{{/high_priority_algorithms}}

#### Quantum Hardware / 量子硬件

{{#high_priority_hardware}}
1. **{{title}}** ({{year}})
   - Authors: {{authors}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - Tags: {{tags}}
   - Added: {{date_added}}
{{/high_priority_hardware}}

#### Quantum Applications / 量子应用

{{#high_priority_applications}}
1. **{{title}}** ({{year}})
   - Authors: {{authors}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - Tags: {{tags}}
   - Added: {{date_added}}
{{/high_priority_applications}}

---

### Medium Priority Papers / 中优先级论文

{{#medium_priority}}
1. **{{title}}** ({{year}})
   - Authors: {{authors}}
   - Category: {{category}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - Tags: {{tags}}
   - Added: {{date_added}}
{{/medium_priority}}

---

### Recently Added Papers / 最近添加的论文

{{#recently_added}}
1. **{{title}}** ({{year}})
   - Authors: {{authors}}
   - Category: {{category}}
   - Priority: {{priority}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - Added: {{date_added}}
{{/recently_added}}

---

### Unread Papers / 未读论文

{{#unread}}
1. **{{title}}** ({{year}})
   - Authors: {{authors}}
   - Category: {{category}}
   - Priority: {{priority}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - Added: {{date_added}}
{{/unread}}

---

### Statistics / 统计

- Total Papers / 总论文数: {{total_papers}}
- Read Papers / 已读论文数: {{read_papers}}
- Unread Papers / 未读论文数: {{unread_papers}}
- High Priority / 高优先级: {{high_priority_count}}
- Medium Priority / 中优先级: {{medium_priority_count}}
- Low Priority / 低优先级: {{low_priority_count}}

#### By Category / 按分类

- Quantum Algorithms / 量子算法: {{algorithms_count}}
- Quantum Hardware / 量子硬件: {{hardware_count}}
- Quantum Applications / 量子应用: {{applications_count}}

---

<a name="中文列表"></a>
## 中文阅读列表

### 高优先级论文

#### 量子算法

{{#high_priority_algorithms}}
1. **{{title_zh}}** ({{year}})
   - 作者: {{authors}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - 标签: {{tags}}
   - 添加日期: {{date_added}}
{{/high_priority_algorithms}}

#### 量子硬件

{{#high_priority_hardware}}
1. **{{title_zh}}** ({{year}})
   - 作者: {{authors}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - 标签: {{tags}}
   - 添加日期: {{date_added}}
{{/high_priority_hardware}}

#### 量子应用

{{#high_priority_applications}}
1. **{{title_zh}}** ({{year}})
   - 作者: {{authors}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - 标签: {{tags}}
   - 添加日期: {{date_added}}
{{/high_priority_applications}}

---

### 中优先级论文

{{#medium_priority}}
1. **{{title_zh}}** ({{year}})
   - 作者: {{authors}}
   - 分类: {{category_zh}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - 标签: {{tags}}
   - 添加日期: {{date_added}}
{{/medium_priority}}

---

### 最近添加的论文

{{#recently_added}}
1. **{{title_zh}}** ({{year}})
   - 作者: {{authors}}
   - 分类: {{category_zh}}
   - 优先级: {{priority}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - 添加日期: {{date_added}}
{{/recently_added}}

---

### 未读论文

{{#unread}}
1. **{{title_zh}}** ({{year}})
   - 作者: {{authors}}
   - 分类: {{category_zh}}
   - 优先级: {{priority}}
   - arXiv: [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})
   - 添加日期: {{date_added}}
{{/unread}}

---

### 统计

- 总论文数: {{total_papers}}
- 已读论文数: {{read_papers}}
- 未读论文数: {{unread_papers}}
- 高优先级: {{high_priority_count}}
- 中优先级: {{medium_priority_count}}
- 低优先级: {{low_priority_count}}

#### 按分类

- 量子算法: {{algorithms_count}}
- 量子硬件: {{hardware_count}}
- 量子应用: {{applications_count}}

---

## Reading Goals / 阅读目标

### Weekly Goals / 每周目标

- [ ] Read {{weekly_goal}} high priority papers / 阅读 {{weekly_goal}} 篇高优先级论文
- [ ] Add notes for {{note_goal}} papers / 为 {{note_goal}} 篇论文添加笔记
- [ ] Review {{review_goal}} related papers / 回顾 {{review_goal}} 篇相关论文

### Monthly Goals / 每月目标

- [ ] Complete {{monthly_read}} papers from reading list / 完成阅读列表中的 {{monthly_read}} 篇论文
- [ ] Explore {{explore_goal}} new research areas / 探索 {{explore_goal}} 个新的研究领域
- [ ] Write {{summary_goal}} paper summaries / 撰写 {{summary_goal}} 篇论文总结

---

## Notes / 笔记

### Progress Tracking / 进度跟踪

{{#progress_notes}}
- {{date}}: {{note}}
{{/progress_notes}}

### Research Focus / 研究重点

Current focus areas / 当前重点领域:
{{#focus_areas}}
- {{.}}
{{/focus_areas}}

### Key Insights / 关键见解

{{#key_insights}}
1. {{date}}: {{insight}}
{{/key_insights}}
