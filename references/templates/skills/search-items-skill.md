# Search [Items] Skill Template

Template for creating automated discovery workflow for research items.

---

```markdown
---
name: search-[items]
description: Search and collect latest [items] for [DOMAIN NAME] using priority-based strategy. Use when: (1) User asks to search for [items], (2) Regular [item] collection updates, or (3) Exploring new research directions in [domain]
version: 1.0.0
---

# Search [Items] for [Domain]

## Quick Workflow

1. Determine search scope (recent vs. comprehensive)
2. Execute web searches using prioritized queries
3. Filter and classify results
4. Update TODO.md with newly found [items]
5. Report completion statistics

---

## Search Strategy

### Priority Levels

**Priority 1: [Core focus]**
- Time filter: oneYear
- Query count: 15-20
- Focus: [What makes this priority]

**Priority 2: [Secondary focus]**
- Time filter: oneMonth
- Query count: 10-15
- Focus: [What makes this priority]

**Priority 3: [Foundational]**
- Time filter: noLimit
- Query count: 8-10
- Focus: [What makes this priority]

---

## Step 1: Determine Search Scope

Ask user:
- "Regular update (one year) or comprehensive search (all time)?"
- "Any specific subdomain to focus on?"

Set parameters accordingly:
```python
time_filter = "oneYear"  # or "oneMonth" or "noLimit"
location = "us"  # or "cn" based on domain
content_size = "medium"
```

---

## Step 2: Execute Searches

### Priority 1 Queries

```
[Query 1]
[Query 2]
[Query 3]
...
[Query 15-20]
```

For each query:
```python
mcp__web-search-prime__web_search_prime(
    search_query=query,
    search_recency_filter=time_filter,
    location=location,
    content_size=content_size
)
```

### Priority 2 Queries

```
[Query 1]
...
[Query 10-15]
```

### Priority 3 Queries

```
[Query 1]
...
[Query 8-10]
```

---

## Step 3: Filter Results

For each search result:

### A. Check Duplicates

Search README.md for existing entries:
```python
# Check if paper title already exists
if title in readme_titles:
    skip("Duplicate")
```

### B. Extract Information

Extract:
- Title
- Authors
- Venue/Conference
- Year
- Link
- Abstract/Summary

### C. Classify Type

Use decision tree from research-focus.md:
```
[Classification logic]
```

Mark as:
- Priority 1, 2, or 3
- [Item type: paper/article/preprint/etc.]

---

## Step 4: Update TODO.md

Add new entries to TODO.md:

```markdown
## [Date] - [Priority]

### [Subdomain if applicable]

- **[Paper Title]**
  - Authors: [Author list]
  - Venue: [Venue] [Year]
  - Link: [URL]
  - Type: [Priority X] - [Brief description]
  - Tags: [Suggested tags]

```

---

## Step 5: Report Results

Provide summary:
```
✅ Search completed
📊 Results:
  - Total queries executed: N
  - New [items] found: N
  - Duplicates filtered: N
  - Breakdown by priority:
    - Priority 1: N
    - Priority 2: N
    - Priority 3: N

📝 TODO.md updated with N new [items]
```

---

## Quality Checks

Before updating TODO.md:
- [ ] Checked for duplicates in README.md
- [ ] Extracted all metadata (title, authors, venue, year, link)
- [ ] Classified using decision tree
- [ ] Suggested appropriate tags (2-4)
- [ ] Added to TODO.md in correct format

---

## Common Issues

**No results for query**
→ Check search terms, try broader keywords

**Many irrelevant results**
→ Refine query with more specific terms

**Duplicate titles in different venues**
→ Include both if substantially different (e.g., conference vs. journal version)
```
