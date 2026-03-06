# Add [Item] Skill Template

Template for creating standardized workflow to add new items to the repository.

---

```markdown
---
name: add-[item]
description: Add [items] to README with standardized format including classification, tagging, summaries, and git commits. Use when: (1) User finishes reading a [paper/item], (2) User provides [link/info], or (3) User wants to document [item] from TODO.md
version: 1.0.0
---

# Add [Item] to Repository

## Quick Workflow

1. Confirm [item] information
2. Determine [item] type/priority
3. Select tags (2-4 appropriate badges)
4. Write summary (2-3 sentences following template)
5. Create reading notes (detailed notes in item_notes/)
6. Update README.md and README_[lang].md (synchronized)
7. Git commit with standardized message

---

## Step 1: Confirm Information

Verify all metadata:

```markdown
Title: [Paper title]
Authors: [Author list]
Venue: [Conference/Journal]
Year: [Year]
Link: [arXiv/DOI URL]
arXiv ID: [if applicable]
DOI: [if applicable]
```

Ask user to confirm or correct.

---

## Step 2: Determine Type

Use decision tree from research-focus.md:

```
[Classification decision tree]
```

Determine:
- Priority level (1, 2, or 3)
- [Item category]

---

## Step 3: Select Tags

### Tag Selection Rules

**Required:**
- 1 primary tag from **[Category Name]** category

**Optional:**
- 1-2 method tags from **[Category Name]** category
- 1 additional tag from any category

**Total: 2-4 tags**

### Process

1. Read classification-guide.md
2. Identify appropriate tags based on [item] content
3. Present suggested tags to user
4. Confirm final selection

### Example

```
Based on the [item] content, suggested tags:
- Primary: Tag1_Name (Category 1)
- Methods: Tag2_Name (Category 2)
- Additional: Tag3_Name (Category 3)

Confirm? (y/n)
```

---

## Step 4: Write Summary

Use template based on [item] type:

### Type 1: [Core Type] Template

```markdown
Proposes [Framework], a [technique]-based system. Uses [method] for [capability].
Achieves [results] on [dataset].
```

### Type 2: [Secondary Type] Template

```markdown
Presents [Name] benchmark with [N] cases. Assesses [dimensions].
Reveals [limitations].
```

### Type 3: [Foundational] Template

```markdown
Focuses on [task] rather than [core capability]. Introduces [Method] for [capability].
Provides [benefit].
```

**Requirements:**
- 2-3 sentences maximum
- Start with purpose/contribution
- Include method/approach
- End with results/impact

---

## Step 5: Create Reading Notes

Create file in `item_notes/`:

**File naming**: `YYYY-MM-DD_[ItemTitle].md`

**Structure**:

```markdown
# [Item Title]

## 基本信息

- **作者**: [Author list]
- **机构**: [Institutions]
- **日期**: [Date]
- **链接**: [URL]
- **标签**: [Tags]
- **类型**: [Priority X - Type]

## 核心贡献

1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]
4. [Contribution 4]

## 方法详解

[Technical approach details]

## 实验结果

[Experimental results and data]

## 讨论要点

[Key insights from [item]]

## 创新与局限

**创新点:**
- [Innovation 1]
- [Innovation 2]

**局限性:**
- [Limitation 1]
- [Limitation 2]

## 与其他工作的关系

[Relationship to other work]

## 总结

[Overall evaluation and takeaways]
```

**Language**: Use [primary language] as specified in CLAUDE.md

---

## Step 6: Update README Files

### README.md Entry

Add to appropriate year/section:

```markdown
### [Month]

- **[Item Title]**

    ![Tag1](badge_url)
    ![Tag2](badge_url)
    ![Tag3](badge_url)

    > **Source:** [Venue] [Year] [[Link]](url)

    [2-3 sentence summary]
```

### README_[lang].md Entry

Translate and mirror the entry:

```markdown
### [Month in translated language]

- **[Item Title]**

    ![Tag1](badge_url)
    ![Tag2](badge_url)

    > **来源:** [Venue translated] [Year] [[链接]](url)

    [2-3 sentence summary in translated language]
```

**Synchronization rules**:
- Keep same structure
- Translate all text except proper nouns
- Maintain badge links
- Keep year/month sections aligned

---

## Step 7: Git Commit

### Stage Files

```bash
git add README.md README_[lang].md
```

**Never stage**: item_notes/, CLAUDE.md, .gitignore

### Commit Message

Use format:

```
Add [item]: [Title] ([Venue] [Year])
```

**Examples**:
- `Add paper: CARE (JMIR 2026)`
- `Add paper: PatientHub Framework (arXiv 2026)`

### Verify

```bash
git status  # Should only show README files
git commit -m "Add [item]: [Title] ([Venue] [Year])"
```

---

## Quality Checklist

Before completing:
- [ ] [Item] entry in correct year section
- [ ] Tags accurate and properly formatted (2-4 tags)
- [ ] Summary follows template (2-3 sentences)
- [ ] [Non-standard types explicitly noted]
- [ ] README_[lang].md synchronized
- [ ] Reading notes created in item_notes/ ([language], detailed)
- [ ] [Item] removed from TODO section
- [ ] Git commit message correct format
- [ ] Only README files staged (not item_notes/)

---

## Common Issues

**Q: What if [item] fits multiple priorities?**

A: Choose the highest priority it qualifies for. When in doubt, use the decision tree in research-focus.md.

**Q: Can I add more than 4 tags?**

A: Generally no. More than 4 dilutes the categorization. If truly necessary, discuss with user first.

**Q: What if venue is unknown?**

A: Use "arXiv" or "Preprint" with year. Update later if published version becomes available.

**Q: Should reading notes be in English or [language]?**

A: Follow CLAUDE.md language setting. If CLAUDE.md specifies [language] for notes, use that.

**Q: What if [item] is already in README but needs updating?**

A: Use "Update" commit format:
```
Update [item]: [Title] - [description of update]
```
```
