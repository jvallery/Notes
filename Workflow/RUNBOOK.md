# Operational Runbook

> **Last Updated**: 2025-01-XX  
> **Purpose**: Recovery procedures and daily operation checklists for the vault automation pipeline.

---

## Table of Contents

1. [Daily Run Checklist](#daily-run-checklist)
2. [Rollback Procedures](#rollback-procedures)
3. [Common Failure Modes](#common-failure-modes)
4. [Emergency Recovery](#emergency-recovery)

---

## Daily Run Checklist

### Pre-Flight (Before Running Pipeline)

```bash
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
```

| Check              | Command                                                                 | Expected                                       |
| ------------------ | ----------------------------------------------------------------------- | ---------------------------------------------- |
| ✅ Git clean       | `git status`                                                            | Working tree clean (or only .obsidian changes) |
| ✅ Venv active     | `which python`                                                          | Points to `.venv/bin/python`                   |
| ✅ API key set     | `echo $OPENAI_API_KEY \| head -c10`                                     | Shows `sk-...` prefix                          |
| ✅ Config valid    | `python -c "from scripts.utils.config import load_config; print('OK')"` | Prints `OK`                                    |
| ✅ Inbox has files | `ls -la ../Inbox/Transcripts/ ../Inbox/Email/`                          | Shows pending files                            |

### Dry Run (Preview Changes)

```bash
# See what would be processed without making changes
python scripts/ingest.py --all --dry-run -v
```

Review output for:

- Correct file classification (transcript vs email)
- Expected entity matches
- No obvious parsing errors

### Execute Pipeline

```bash
# Standard run (transactional - all or nothing)
python scripts/ingest.py --all --draft-replies --enrich

# Scope by content type
python scripts/ingest.py --type email
python scripts/ingest.py --type transcript

# Re-process archived sources (after prompt/schema changes)
python scripts/ingest.py --source --type email --force
```

### Post-Run Review

| Check              | Command                        | Action                      |
| ------------------ | ------------------------------ | --------------------------- |
| Review changes     | `git diff HEAD~1`              | Verify changes look correct |
| Check dashboards   | Open `TASKS.md` in Obsidian    | Confirm tasks populated     |
| Find flagged items | Search `#needs-review`         | Resolve ambiguous entities  |
| Check failed       | `ls ../Inbox/_failed/`         | Investigate any failures    |
| Push changes       | `git push`                     | Manual push after review    |

---

## Rollback Procedures

### Apply Phase Failure

**The Apply phase is transactional - if it fails, it auto-rollbacks.**

If you need to manually rollback after a successful Apply:

```bash
# 1. Find the pre-apply commit
git log --oneline -10

# 2. Identify the commit BEFORE the [auto] commit
# Example output:
#   a1b2c3d [auto] Processed: meeting.md, email.md
#   e4f5g6h Previous commit

# 3. Soft reset to undo (keeps changes staged for review)
git reset --soft HEAD~1

# 4. Or hard reset to fully undo
git reset --hard HEAD~1

# 5. If sources were archived, restore them
mv ../Inbox/_archive/YYYY-MM-DD/*.md ../Inbox/Transcripts/
```

### Backfill Failure

```bash
# Backfill creates a new branch before making changes
git branch -a | grep backfill

# If on a backfill branch, switch back to main
git checkout main

# Delete the failed backfill branch
git branch -D backfill-YYYYMMDD-HHMMSS

# Backups are in .workflow_backups/
ls .workflow_backups/
```

### Migration Failure

```bash
# Migration backs up modified READMEs
# Backups are in .workflow_backups/migration-{run_id}/

# 1. Find the migration run
ls .workflow_backups/

# 2. Restore specific files
cp .workflow_backups/migration-*/path/to/README.md ../VAST/People/Name/README.md

# 3. Or use git to restore all
git checkout -- ../VAST/ ../Personal/
```

### Restore from Backup Directory

All operations create backups before modifying files:

```bash
# Structure: .workflow_backups/{run_id}/{vault-relative-path}
# Example: .workflow_backups/20250103-140530/VAST/People/Jeff Denworth/README.md

# Find backups
find .workflow_backups -name "*.md" -type f

# Restore a specific file
cp ".workflow_backups/20250103-140530/VAST/People/Jeff Denworth/README.md" \
   "../VAST/People/Jeff Denworth/README.md"

# Cleanup old backups (after confirming success)
rm -rf .workflow_backups/20250103-*/
```

---

## Common Failure Modes

### "Git working directory has uncommitted content changes"

**Cause**: Apply requires a clean git tree in content directories.

**Solution**:

```bash
# Check what's dirty
git status

# Option 1: Commit pending changes first
git add -A -- ../Inbox/ ../VAST/ ../Personal/
git commit -m "WIP: uncommitted changes"

# Option 2: Stash and continue
git stash

# Option 3: Force run (not recommended)
python scripts/apply.py --allow-dirty
```

### "Entity not found: will create _NEW_ prefix"

**Cause**: Extraction mentioned a person/project/account not in the vault.

**Solution**:

1. After run, search for `_NEW_` folders
2. Decide if this is a typo or genuinely new entity
3. Either rename the folder or create proper README

```bash
# Find new entities
find ../VAST ../Personal -name "_NEW_*" -type d
```

### "OPENAI_API_KEY environment variable not set"

**Solution**:

```bash
# Check .env file exists
cat .env

# If missing, create it
cp .env.example .env
# Edit .env and add your key

# Or export directly
export OPENAI_API_KEY=sk-your-key-here
```

### "Extraction failed: rate limit exceeded"

**Cause**: Too many API calls in short period.

**Solution**:

```bash
# Wait 60 seconds and retry
sleep 60
python scripts/extract.py --all --verbose

# Or process one file at a time
python scripts/extract.py --file ../Inbox/Transcripts/specific-file.md
```

### "No changeplan found for source"

**Cause**: Extraction succeeded but plan phase wasn't run.

**Solution**:

```bash
# Check if extraction exists
ls ../Inbox/_extraction/*.extraction.json

# Run plan phase
python scripts/plan.py --all --verbose
```

---

## Emergency Recovery

### Complete Reset to Last Known Good State

```bash
# 1. Find a good commit
git log --oneline -20

# 2. Reset to it
git reset --hard <commit-hash>

# 3. Clean up extraction artifacts
rm -rf ../Inbox/_extraction/*.json
rm -rf .workflow_backups/*

# 4. Restore archived sources if needed
# (check git diff to see what was moved)
```

### Recover from Corrupted README

```bash
# 1. Check git history for the file
git log --oneline -- "../VAST/People/Name/README.md"

# 2. Restore a specific version
git show <commit>:"VAST/People/Name/README.md" > ../VAST/People/Name/README.md

# 3. Or use the template
python scripts/migration/runner.py --create-readme "../VAST/People/Name"
```

### API Key Compromised

```bash
# 1. Immediately revoke key at https://platform.openai.com/api-keys

# 2. Generate new key

# 3. Update .env
echo "OPENAI_API_KEY=sk-new-key" > .env

# 4. Check git history for accidental commits
git log -p --all -S 'sk-' -- .env
```

---

## Quick Reference

| Scenario          | Command                                                      |
| ----------------- | ------------------------------------------------------------ |
| Preview changes   | `python scripts/ingest.py --all --dry-run -v`                |
| Process all       | `python scripts/ingest.py --all --draft-replies --enrich`    |
| Undo last commit  | `git reset --hard HEAD~1`                                    |
| Find backups      | `ls .workflow_backups/`                                      |
| Check failed      | `ls ../Inbox/_failed/`                                       |
| Find new entities | `find .. -name "_NEW_*" -type d`                             |
| Restore archives  | `mv ../Inbox/_archive/YYYY-MM-DD/*.md ../Inbox/Transcripts/` |

---

## Contact

For issues beyond this runbook, check:

- [DESIGN.md](DESIGN.md) - Architecture decisions
- [README.md](README.md) - Full documentation
- Git history - `git log --oneline -20`
