# README Audit Prompt

You are auditing an entity README file for quality, consistency, and accuracy. Review the content and provide specific, actionable feedback.

## Entity Type: {entity_type}
## Entity Name: {entity_name}

---

## README Content

```markdown
{content}
```

---

## Audit Checklist

### Structure (required sections in order)

**For People:**
1. [ ] Frontmatter with type, title, last_contact, created, tags
2. [ ] `## Profile` with Role, Organization, Location, Relationship
3. [ ] `## Open Tasks` with tasks query
4. [ ] `## Recent Context` with dated ledger entries (reverse chronological)
5. [ ] `## Key Facts` (if any facts captured)

**For Customers:**
1. [ ] Frontmatter with type, title, last_contact, created, tags
2. [ ] `## Account Status` with Industry, Stage table
3. [ ] `## Key Contacts` with wikilinks to people
4. [ ] `## Open Tasks` with tasks query
5. [ ] `## Recent Context` with dated ledger entries (reverse chronological)
6. [ ] `## Opportunities` and `## Blockers` (if applicable)

**For Projects:**
1. [ ] Frontmatter with type, title, last_contact, created, tags
2. [ ] `## Status` with Owner, Stage table
3. [ ] `## Overview` with brief description
4. [ ] `## Open Tasks` with tasks query
5. [ ] `## Recent Context` with dated ledger entries (reverse chronological)

### Content Quality

1. [ ] **Profile/Status is specific** — not generic placeholders like "_Unknown_"
2. [ ] **Role/Organization is accurate** — matches what we know about this person/entity
3. [ ] **Recent Context entries are relevant** — directly about this entity, not tangential mentions
4. [ ] **Ledger is deduplicated** — no duplicate entries for the same source
5. [ ] **Ledger is reverse chronological** — most recent first
6. [ ] **Key Facts are unique** — not duplicated across multiple entity READMEs
7. [ ] **Tasks are actionable** — have owners, due dates where appropriate
8. [ ] **Wikilinks are valid** — point to existing entities

### Issues to Flag

- **REMOVE**: Entries that don't belong (wrong entity, tangential mentions)
- **MERGE**: Duplicate entries that should be consolidated
- **UPDATE**: Outdated information that needs refresh
- **ADD**: Missing information we should know about this entity
- **FIX**: Formatting issues, broken links, inconsistent structure

---

## Your Audit Response

Provide your audit in this format:

### Summary
One paragraph assessment of README quality (Good/Needs Work/Poor).

### Issues Found
List each issue with:
- **Type**: REMOVE / MERGE / UPDATE / ADD / FIX
- **Location**: Which section
- **Description**: What's wrong
- **Suggested Fix**: How to fix it

### Recommended Ledger Entries to Keep
List the entries that should remain in Recent Context (by date), with brief justification.

### Recommended Ledger Entries to Remove
List entries that should be removed, with reason (duplicate, wrong entity, tangential, etc.)

### Profile Updates Needed
Specific updates to Profile/Status section based on source material.

### Overall Score
Rate 1-5:
- 5: Complete, accurate, well-structured
- 4: Minor issues only
- 3: Needs some cleanup
- 2: Significant issues
- 1: Major rewrite needed
