# Research Repository FAQ

Common questions and answers about setting up and using research repositories.

---

## Language and Localization

**Q: Should I keep the bilingual structure?**

A: Only if your target audience uses both languages. Otherwise, use a single README.md.

**Q: What if I want to support more than 2 languages?**

A: Create additional README files (README_es.md, README_fr.md, etc.) and synchronize them with README.md. Update CLAUDE.md to list all supported languages.

---

## Priority and Classification

**Q: How many priority levels should I have?**

A: 3 levels is optimal: (1) Core focus, (2) Supporting research, (3) Foundational work. More levels create confusion and make classification difficult.

**Q: What if an item fits multiple priorities?**

A: Choose the highest priority it qualifies for. When in doubt, use the decision tree in research-focus.md to guide classification.

**Q: Can I change priorities later?**

A: Yes. Priorities should evolve as your research focus shifts. Update research-focus.md and CLAUDE.md, then review existing items for reclassification if needed.

---

## Domain Adaptation

**Q: What if my domain doesn't have clear "papers"?**

A: Adapt the pattern: replace "papers" with "items", "resources", "tools", "articles", or whatever fits your domain. The workflow remains the same - only terminology changes.

**Q: Can I use this for non-academic research?**

A: Yes! This pattern works for any curated knowledge base: industry reports, blog posts, code repositories, design patterns, technical documentation, etc.

**Q: What if my domain changes over time?**

A: Update CLAUDE.md and research-focus.md to reflect new priorities. Consider creating a new repository if the domain shift is substantial.

---

## File Management

**Q: Should I include paper_notes/ in git?**

A: No. Keep notes local for personal insights without polluting the public repository. The README contains polished summaries for sharing.

**Q: How do I migrate existing notes?**

A: Create paper_notes/ and move existing files there. Then use add-[item] skill to create polished README entries based on your notes.

**Q: What about images, PDFs, or other assets?**

A: Add them to .gitignore and keep locally. If you need to share assets, consider:
- Linking to external sources (arXiv, DOI)
- Creating a separate assets repository
- Using GitHub Releases for large files

---

## Tags and Classification

**Q: Can I add more than 4 tags to an item?**

A: Generally no. More than 4 dilutes the categorization. If truly necessary, discuss with user first and consider updating classification-guide.md.

**Q: What if I need a new tag that doesn't fit existing categories?**

A: Add it to the appropriate category in classification-guide.md, or create a new category if needed. Update color scheme and badge URLs accordingly.

**Q: How do I handle emerging topics that don't fit existing tags?**

A: Create new tags in classification-guide.md. Consider adding a "Emerging" or "Other" category for topics that haven't stabilized yet.

---

## Git Workflow

**Q: What if I accidentally committed paper_notes/ or CLAUDE.md?**

A: Remove them from git history:
```bash
git rm -r --cached paper_notes/
git rm --cached CLAUDE.md
git commit -m "Remove local files from tracking"
```

**Q: Should I use branches?**

A: Recommended workflow:
- Main branch: Published README entries only
- Feature branches: For batch additions or major reorganizations
- Direct commits: Acceptable for single-item additions

**Q: What's the commit message format for updates?**

A: Use these formats:
- Add: `Add paper: Title (Venue Year)`
- Update: `Update paper: Title - description of update`
- Fix: `Fix: issue description`
- Remove: `Remove paper: Title - reason`

---

## Skills and Workflow

**Q: When should I use /search-[items] vs manual search?**

A: Use /search-[items] for:
- Regular collection updates
- Comprehensive domain searches
- When you want automated TODO updates

Manual search is fine for quick lookups or following citation trails.

**Q: Can I customize the skills for my specific workflow?**

A: Absolutely. The skill templates are starting points. Modify them to fit your workflow, but keep the core structure (search → classify → add → commit).

**Q: What if I don't need both search-[items] and add-[item] skills?**

A: You can create a combined skill, but separating them has advantages:
- Search can be automated/scheduled
- Add workflow is interactive and user-driven
- Each skill stays focused and concise

---

## Quality and Maintenance

**Q: How do I ensure consistent quality across entries?**

A: Follow these practices:
- Always use the add-[item] skill (enforces templates)
- Review classification-guide.md when unsure
- Use the summary templates (2-3 sentences)
- Have Claude validate against quality checklist

**Q: How often should I update the repository?**

A: Depends on your domain:
- Fast-moving (AI/ML): Weekly or bi-weekly
- Moderate (most fields): Monthly
- Slow-moving: Quarterly

**Q: What if I fall behind on documenting items?**

A: Use the search skill to catch up:
1. Run /search-[items] with noLimit time filter
2. Review TODO.md for backlog
3. Batch process using /add-[item]

---

## Collaboration and Sharing

**Q: Can multiple people contribute to one repository?**

A: Yes. For collaboration:
- Agree on priorities and tags upfront
- Keep CLAUDE.md synced across contributors
- Use pull requests for review
- Consider documenting contribution guidelines

**Q: Should I make my repository public?**

A: Consider:
- **Public**: Good for visibility, collaboration, portfolio
- **Private**: Better for sensitive/proprietary research

You can always start private and go public later.

**Q: How do I credit contributors?**

A: Options:
- Add contributors section to README
- Use git commit attribution
- Add .github/CODEOWNERS file
- Create CONTRIBUTORS.md file

---

## Troubleshooting

**Q: Search returns no results**

A: Check:
- Search terms are relevant to your domain
- Time filter isn't too restrictive
- Location setting matches your domain (us/cn)
- Try broader or alternative search terms

**Q: Too many irrelevant results**

A: Refine by:
- Adding more specific keywords
- Using quotation marks for phrases
- Adjusting time filter to recent work
- Excluding common terms with minus operator

**Q: Classification is ambiguous**

A: Use the decision tree in research-focus.md:
1. Start with the highest priority criteria
2. If it matches, classify there
3. If not, move to next priority
4. Document edge cases in research-focus.md

---

**Last updated**: 2026-03-06
