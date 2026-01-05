from pipeline.context import ContextBundle
from pipeline.envelope import ContentEnvelope, ContentType


def test_cacheable_prefix_includes_persona_glossary_aliases(monkeypatch):
    # Force cached helpers off so we use the provided manifest/glossary data
    import pipeline.context as ctx
    monkeypatch.setattr(ctx, "_cached_glossary_context", None, raising=False)
    monkeypatch.setattr(ctx, "_cached_persona_context", None, raising=False)

    bundle = ContextBundle(
        persona="PERSONA: example persona text",
        people_manifest="| Name | Role |\n| --- | --- |\n| [[Alice Example]] | PM |\n",
        company_manifest="| Name | Role |\n| --- | --- |\n| [[Acme]] | Customer |\n",
        project_list=["Project X"],
        aliases={"alice": "Alice Example"},
    )

    prefix, prefix_hash = bundle.get_cacheable_prefix()

    assert "PERSONA" in prefix
    assert "PERSONA" in prefix
    assert "Alice Example" in prefix  # from people manifest/glossary
    assert "Acme" in prefix           # from company manifest/glossary
    assert "Project X" in prefix
    assert "alice → Alice Example" in prefix  # aliases included
    assert prefix_hash


def test_dynamic_suffix_includes_relevant_readmes():
    bundle = ContextBundle(
        relevant_readmes={
            "Alice Example": "Key Facts: great PM",
            "Acme": "Customer in cloud",
        }
    )

    suffix = bundle.get_dynamic_suffix()

    assert "Alice Example" in suffix
    assert "Customer in cloud" in suffix


def test_extraction_context_orders_prefix_before_suffix():
    bundle = ContextBundle(
        persona="PERSONA",
        people_manifest="| Name |\n| --- |\n| [[Alice Example]] |\n",
        aliases={"alice": "Alice Example"},
        relevant_readmes={"Alice Example": "Key Facts: great PM"},
    )

    context = bundle.get_extraction_context(compact=True)

    prefix = bundle.get_cacheable_prefix()[0]
    suffix = bundle.get_dynamic_suffix()

    assert context.startswith(prefix)
    if suffix:
        assert context.endswith(suffix)


def test_context_load_includes_fuzzy_matched_readmes(tmp_path):
    readme = tmp_path / "VAST" / "People" / "Jason Vallery" / "README.md"
    readme.parent.mkdir(parents=True, exist_ok=True)
    readme.write_text("# Jason Vallery\n\n## Key Facts\n- Works on Azure\n")

    aliases_dir = tmp_path / "Workflow" / "entities"
    aliases_dir.mkdir(parents=True, exist_ok=True)
    (aliases_dir / "aliases.yaml").write_text("Jason Vallery:\n  - JV\n  - Jason V\n")

    env = ContentEnvelope(
        source_path=tmp_path / "Inbox" / "Email" / "test.md",
        content_type=ContentType.EMAIL,
        raw_content="Met with JV about Azure storage.",
        date="2026-01-05",
        title="Test",
        participants=["J. Vallery"],
    )

    bundle = ContextBundle.load(tmp_path, env)

    assert any("Jason Vallery" in key for key in bundle.relevant_readmes.keys())
    assert "Works on Azure" in "\n".join(bundle.relevant_readmes.values())
