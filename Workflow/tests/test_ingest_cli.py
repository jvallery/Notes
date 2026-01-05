from pathlib import Path

from click.testing import CliRunner

from pipeline.envelope import ContentType
from scripts import ingest


def test_ingest_cli_routes(monkeypatch, tmp_path):
    calls = []

    class DummyBatch:
        def __init__(self):
            self.total = 0
            self.success = 0
            self.failed = 0
            self.skipped = 0
            self.results = []

    class DummyResult:
        def __init__(self, path):
            self.source_path = str(path)
            self.content_type = "email"
            self.success = True
            self.extraction = {}
            self.apply_result = None
            self.draft_reply = None
            self.errors = []

    class FakePipeline:
        def __init__(self, vault_root, dry_run, verbose, generate_outputs, force, trace_dir=None, show_cache_stats=False, log_metrics=True):
            calls.append(("init", vault_root, dry_run, verbose, generate_outputs, force, trace_dir, show_cache_stats, log_metrics))

        def process_file(self, path):
            calls.append(("file", Path(path)))
            return DummyResult(path)

        def process_type(self, ct):
            calls.append(("type", ct))
            return DummyBatch()

        def process_all(self):
            calls.append(("all", None))
            return DummyBatch()

        def process_sources(self, ct=None):
            calls.append(("sources", ct))
            return DummyBatch()

    monkeypatch.setattr(ingest, "UnifiedPipeline", FakePipeline)
    monkeypatch.setattr(ingest, "_display_result", lambda *args, **kwargs: None)
    monkeypatch.setattr(ingest, "_display_batch", lambda *args, **kwargs: None)

    runner = CliRunner()
    inbox_file = tmp_path / "Inbox" / "Email" / "foo.md"
    inbox_file.parent.mkdir(parents=True, exist_ok=True)
    inbox_file.write_text("hello")

    res = runner.invoke(ingest.main, ["--file", "Inbox/Email/foo.md", "--dry-run", f"--vault-root={tmp_path}"])
    assert res.exit_code == 0
    assert ("file", tmp_path / "Inbox" / "Email" / "foo.md") in calls
    assert calls[0][1] == tmp_path

    calls.clear()
    res = runner.invoke(ingest.main, ["--source", "--type", "email", "--dry-run", f"--vault-root={tmp_path}"])
    assert res.exit_code == 0
    assert ("sources", ContentType.EMAIL) in calls

    calls.clear()
    res = runner.invoke(ingest.main, ["--type", "transcript", "--dry-run", f"--vault-root={tmp_path}"])
    assert res.exit_code == 0
    assert ("type", ContentType.TRANSCRIPT) in calls
