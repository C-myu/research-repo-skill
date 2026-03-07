# Add [Item] Skill Template

Template for creating standardized workflow to add new items to the repository.

---

## Table of Contents

1. [SKILL.md Template](#skillmd-template) - Complete skill definition template
2. [Creation Steps](#creation-steps) - How to generate the skill from this template
3. [Template Placeholders](#template-placeholders) - Placeholder value reference table
4. [Additional Files to Create](#additional-files-to-create) - Notes template structure

---

## SKILL.md Template

Complete skill definition template for the add-[item] skill. Copy this content into the skill's SKILL.md file after replacing placeholders.

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

## Basic Information

- **Authors**: [Author list]
- **Institutions**: [Institutions]
- **Date**: [Date]
- **Link**: [URL]
- **Tags**: [Tags]
- **Type**: [Priority X - Type]

## Core Contributions

1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]
4. [Contribution 4]

## Method Details

[Technical approach details]

## Experimental Results

[Experimental results and data]

## Key Discussion Points

[Key insights from [item]]

## Innovations and Limitations

**Innovations:**
- [Innovation 1]
- [Innovation 2]

**Limitations:**
- [Limitation 1]
- [Limitation 2]

## Relationship to Other Work

[Relationship to other work]

## Summary

[Overall evaluation and takeaways]
```

**Note**: This template is in English. Customize section headings and structure to match the primary language specified in CLAUDE.md during skill setup.
```
