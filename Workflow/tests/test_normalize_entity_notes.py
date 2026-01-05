from scripts.normalize_entity_notes import normalize_frontmatter_dict


def test_normalize_frontmatter_sets_type_entity_and_cleans_tags():
    fm = {
        "type": "customer",
        "person": "",
        "account": "",
        "tags": ["type/customer", "person/", "account/", "generated", "generated"],
    }

    out = normalize_frontmatter_dict(
        fm,
        entity_key="person",
        entity_name="John Doe",
        note_type="people",
    )

    assert out["type"] == "people"
    assert out["person"] == "John Doe"
    assert out["tags"][0] == "type/people"
    assert "type/customer" not in out["tags"]
    assert "person/" not in out["tags"]
    assert "account/" not in out["tags"]
    assert out["tags"].count("generated") == 1

