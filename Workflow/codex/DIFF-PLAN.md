# Patch Plan (Diff‑Style)

Apply these diffs in order. Keep changes minimal and focused.

1) Preserve backup structure

- File: `Workflow/scripts/utils/fs.py`

```diff
 def backup_file(source: Path, backup_dir: Path) -> Path:
-    backup_path = backup_dir / source.name
+    # Preserve vault‑relative structure to avoid collisions
+    from .config import vault_root as _vr
+    vault = _vr()
+    rel = source.resolve().relative_to(vault.resolve())
+    backup_path = backup_dir / rel
     backup_path.parent.mkdir(parents=True, exist_ok=True)
     shutil.copy2(source, backup_path)
     return backup_path
```

2) Stage content dirs atomically

- File: `Workflow/scripts/utils/git_ops.py`

```diff
+def add_content_dirs_all(repo_path: Path | None = None) -> None:
+    if repo_path is None:
+        repo_path = vault_root()
+    code, _, stderr = _run_git(repo_path, "add", "-A", "--", *CHECKED_PATHS)
+    if code != 0:
+        raise RuntimeError(f"git add -A failed: {stderr}")
```

- File: `Workflow/scripts/apply.py`

```diff
- from scripts.utils import ..., add_files, commit, ...
+ from scripts.utils import ..., add_content_dirs_all, commit, ...

      # Stage files
-     add_files(self.vault_root, all_files)
+     add_content_dirs_all(self.vault_root)
```

3) Backfill extractor → Responses API

- File: `Workflow/scripts/backfill/extractor.py`

```diff
- response = client.chat.completions.create(
-     model=model,
-     messages=[{"role":"system","content":"..."},{"role":"user","content":prompt}],
-     temperature=0.1,
-     store=False,
- )
- response_text = response.choices[0].message.content or ""
- # strip fences ... json.loads(...)
+ from pydantic import BaseModel, Field
+ class BackfillLite(BaseModel):
+     summary: str = ""
+     mentions: dict = Field(default_factory=lambda: {"people":[],"projects":[],"accounts":[]})
+     person_details: dict = Field(default_factory=dict)
+     project_details: dict = Field(default_factory=dict)
+     customer_details: dict = Field(default_factory=dict)
+     tasks: list = Field(default_factory=list)
+     decisions: list = Field(default_factory=list)
+     key_facts: list = Field(default_factory=list)
+     topics_discussed: list = Field(default_factory=list)
+
+ response = client.responses.parse(
+     model=model,
+     input=[{"role":"system","content":"You extract rich structured data from notes. Return JSON only."},
+            {"role":"user","content":prompt}],
+     text_format=BackfillLite,
+     temperature=0.1,
+     store=False,
+ )
+ result = response.output_parsed.model_dump()
```

4) Enforce StrictUndefined + shared filters in backfill entities rendering

- File: `Workflow/scripts/backfill/entities.py`

```diff
- env = Environment(loader=FileSystemLoader(str(templates_dir)))
+ from scripts.utils.templates import get_template_env
+ env = get_template_env()
```

5) Path safety in backfill joins

- Files: `Workflow/scripts/backfill/*.py`

```diff
- rel_path = str(note_path.relative_to(vault))
+ from scripts.utils.paths import safe_relative_path
+ rel_path = str(safe_relative_path(vault, note_path))
```

6) Standards checker – README mode

- File: `Workflow/scripts/utils/standards_check.py`

```diff
 def check_filename(filename: str, context: str = "note") -> list[str]:
@@
     elif context == "email":
         ...
+    elif context == "readme":
+        # Relax dated note pattern for README.md
+        if filename != "README.md":
+            issues.append("Invalid README filename")
```

Then in Apply CREATE, pass `context="readme"` when `target.name == "README.md"`.
