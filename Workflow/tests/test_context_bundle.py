from pipeline.context import ContextBundle


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
