#!/usr/bin/env python3
"""Test the apply phase to debug the string indices error."""

import traceback
from pathlib import Path

vault_root = Path('/Users/jason.vallery/Documents/Notes')
from pipeline.adapters import AdapterRegistry
from pipeline.context import ContextBundle
from pipeline.extract import UnifiedExtractor
from pipeline.patch import PatchGenerator
from pipeline.apply import TransactionalApply

# Test one file - use Walmart which should have NO existing note
p = vault_root / 'Inbox/Transcripts/2025-11-05 - Walmart Analytics.md'

registry = AdapterRegistry.default()
envelope = registry.parse(p)
context = ContextBundle.load(vault_root, envelope)
extractor = UnifiedExtractor(vault_root)
extraction = extractor.extract(envelope, context)
patch_gen = PatchGenerator(vault_root)
plan = patch_gen.generate(extraction)

print("Plan meeting_note_path:", plan.meeting_note_path)
print("Plan meeting_note type:", type(plan.meeting_note))
print("Plan patches count:", len(plan.patches))

# Try apply directly to get full traceback
applier = TransactionalApply(vault_root, dry_run=False)
try:
    result = applier.apply(plan, p)
    print(f"Result: {result}")
    print(f"Files created: {result.files_created}")
    print(f"Files modified: {result.files_modified}")
except Exception as e:
    print(f"FAILED: {e}")
    traceback.print_exc()
