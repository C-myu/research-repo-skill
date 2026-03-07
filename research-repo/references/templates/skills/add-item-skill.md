# Add [Item] Skill Template

Template for creating standardized workflow to add new items to the repository.

---

```markdown
---
name: add-[item]
description: Add [items] to README with standardized format including classification, tagging, summaries, and git commits. Use when: (1) User finishes reading a [paper/item], (2) User provides [link/info], or (3) User wants to document [item] from TODO.md
---

# Add [Item] to Repository

## Quick Workflow

1. Confirm [item] information
2. Determine priority and type
3. Select tags (2-4)
4. Write summary (2-3 sentences)
5. Create reading notes
6. Update README files
7. Git commit

## Execution Steps

**Step 1: Confirm information**
- Verify title, authors, venue, year, link
- Ask user to confirm or correct

**Step 2: Determine type**
- Use priority decision tree from research-focus.md
- Classify as Priority 1/2/3

**Step 3: Select tags**
- Consult classification-guide.md
- Select 2-4 tags following selection rules
- Confirm with user

**Step 4: Write summary**
- 2-3 sentences maximum
- Structure: Purpose → Method → Results
- See readme-entry.md for guidelines

**Step 5: Create reading notes**
- File: `item_notes/YYYY-MM-DD_Title.md`
- Use [primary language] from CLAUDE.md
- Follow template structure in references/notes-template.md

**Step 6: Update README files**
- Add entry to README.md (English)
- Add translated entry to README_[lang].md
- Follow format in readme-entry.md
- Keep year/month sections synchronized

**Step 7: Git commit**
- Stage: `git add README.md README_[lang].md`
- Commit: `Add [item]: [Title] ([Venue] [Year])`
- Verify: Only README files staged

## Key References

- **Priority classification**: research-focus.md
- **Tag selection**: classification-guide.md
- **Entry format**: readme-entry.md
- **Language settings**: CLAUDE.md
- **Reading notes template**: references/notes-template.md

---

**Note to skill creator**: When setting up this skill, create `references/notes-template.md` with the reading notes structure template for this domain.
```

---

## Creation Steps

When generating this skill from this template:

1. **Replace placeholders** - Substitute all `[PLACEHOLDER]` values with domain-specific content
2. **Create skill directory** - `mkdir -p .claude/skills/add-[item]`
3. **Write SKILL.md** - Use the template above, replacing placeholders
4. **Create references directory** - `mkdir -p .claude/skills/add-[item]/references`
5. **Write references/notes-template.md** - Use the template below, customize structure if needed

**Validation** (optional):
- Run `/skill-creator` to validate the skill structure
- Check that SKILL.md follows frontmatter requirements
- Ensure references/notes-template.md is properly formatted

---

## Template Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[item]` | Singular resource type | "paper", "article" |
| `[items]` | Plural resource type | "papers", "articles" |
| `[lang]` | Secondary language code | "zh", "es" |

---

## Additional Files to Create

When generating this skill, also create `references/notes-template.md`:

```markdown
# Reading Notes Template

File: `item_notes/YYYY-MM-DD_Title.md`

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

**Language**: Use primary language specified in CLAUDE.md
```

**Note**: Customize the template structure above based on domain-specific needs during skill setup.
