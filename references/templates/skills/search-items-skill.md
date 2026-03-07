# Search [Items] Skill Template

Template for creating automated discovery workflow for research items.

---

```markdown
---
name: search-[items]
description: Search and collect latest [items] for [DOMAIN NAME] using priority-based strategy. Use when: (1) User asks to search for [items], (2) Regular [item] collection updates, or (3) Exploring new research directions
---

# Search [Items] for [Domain]

## Quick Workflow

1. Determine search scope with user
2. Execute web searches by priority
3. Filter duplicates and classify results
4. Update TODO.md
5. Report completion statistics

## Search Strategy

| Priority | Time Filter | Query Count | Focus |
|----------|-------------|-------------|-------|
| P1: [Core focus] | oneYear | 15-20 | [What makes this priority] |
| P2: [Secondary] | oneMonth | 10-15 | [What makes this priority] |
| P3: [Foundational] | noLimit | 8-10 | [What makes this priority] |

## Execution Steps

**Step 1: Determine scope**
- Ask user: "Regular update (one year) or comprehensive search (all time)?"
- Set time_filter and location parameters

**Step 2: Execute searches**
- Use `mcp__web-search-prime__web_search_prime` for each query
- Search by priority: P1 queries → P2 queries → P3 queries
- See references/queries.md for complete query list

**Step 3: Filter results**
- Check duplicates against README.md
- Extract metadata (title, authors, venue, year, link)
- Classify using priority decision tree from research-focus.md
- Suggest 2-4 tags based on classification-guide.md

**Step 4: Update TODO.md**
```markdown
## [Date] - Priority [N]

- **[Title]**
  - Authors: [List]
  - Venue: [Venue] [Year]
  - Link: [URL]
  - Type: Priority [N] - [Type]
  - Tags: [Suggested tags]
```

**Step 5: Report results**
- Total queries executed
- New items found
- Duplicates filtered
- Breakdown by priority

## Key References

- **Priority decision tree**: research-focus.md
- **Tag selection**: classification-guide.md
- **Search queries**: references/queries.md

---

**Note to skill creator**: When setting up this skill, create `references/queries.md` with domain-specific search queries organized by priority.
```

---

## Creation Steps

When generating this skill from this template:

1. **Replace placeholders** - Substitute all `[PLACEHOLDER]` values with domain-specific content
2. **Create skill directory** - `mkdir -p .claude/skills/search-[items]`
3. **Write SKILL.md** - Use the template above, replacing placeholders
4. **Create references directory** - `mkdir -p .claude/skills/search-[items]/references`
5. **Write references/queries.md** - Use the template below, populate with actual queries

**Validation** (optional):
- Run `/skill-creator` to validate the skill structure
- Check that SKILL.md follows frontmatter requirements
- Ensure references/queries.md is properly formatted

---

## Template Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[items]` | Plural resource type | "papers", "articles" |
| `[item]` | Singular resource type | "paper", "article" |
| `[DOMAIN NAME]` | Research domain | "AI for Mental Health" |
| `[Domain]` | Short domain name | "Mental Health AI" |
| `[Core focus]` | Priority 1 name | "Deep Learning Architectures" |
| `[Secondary]` | Priority 2 name | "Optimization Methods" |
| `[Foundational]` | Priority 3 name | "Core Algorithms" |

---

## Additional Files to Create

When generating this skill, also create `references/queries.md`:

```markdown
# Search Queries

Organized by priority level for [DOMAIN NAME].

## Priority 1 Queries (Core Focus)

**Time filter**: oneYear
**Expected results**: 15-20 queries

```
[Query 1]
[Query 2]
[Query 3]
...
```

## Priority 2 Queries (Secondary Focus)

**Time filter**: oneMonth
**Expected results**: 10-15 queries

```
[Query 1]
[Query 2]
[Query 3]
...
```

## Priority 3 Queries (Foundational)

**Time filter**: noLimit
**Expected results**: 8-10 queries

```
[Query 1]
[Query 2]
[Query 3]
...
```

---

**Search parameters**:
- Location: [us/cn] - Set based on domain
- Content size: medium
- Tool: mcp__web-search-prime__web_search_prime
```

**Note**: Populate queries during setup based on domain-specific research focus. Use setup-wizard.md Phase 4 for guidance on constructing effective queries.
