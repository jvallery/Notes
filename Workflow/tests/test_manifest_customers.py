import json
from pathlib import Path

from scripts import manifest_sync
from scripts import enrich_customer
from scripts.utils.frontmatter import parse_frontmatter


def test_generate_customers_manifest_includes_stage_and_role():
    entries = [
        manifest_sync.CustomerEntry(
            name="Acme",
            type="customer",
            stage="Active",
            industry="AI",
            my_role="account-owner",
            last_contact="2026-01-01",
            context="Strategic AI design partner",
        )
    ]
    manifest = manifest_sync.generate_customers_manifest(entries)
    assert "| Name | Type | Stage | Industry | My Role | Last Contact | Context |" in manifest
    assert "Acme" in manifest and "account-owner" in manifest and "Active" in manifest


def test_scan_customers_folder_parses_frontmatter_and_status(tmp_path, monkeypatch):
    customers_dir = tmp_path / "VAST" / "Customers and Partners" / "Acme"
    customers_dir.mkdir(parents=True)
    readme = customers_dir / "README.md"
    readme.write_text(
        """---
account_type: customer
industry: manufacturing
status: Active
my_role: account-owner
last_contact: 2026-01-01
tags:
  - industry/manufacturing
---
# Acme

## Account Status
| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Industrial |
"""
    )
    monkeypatch.setattr(manifest_sync, "VAST_CUSTOMERS", customers_dir.parent)
    
    entries = manifest_sync.scan_customers_folder()
    assert len(entries) == 1
    entry = entries[0]
    assert entry.type == "customer"
    assert entry.stage == "Active"
    # Prefers frontmatter industry, not table fallback
    assert entry.industry == "manufacturing"
    assert entry.my_role == "account-owner"
    assert entry.last_contact == "2026-01-01"


def test_enrich_customer_from_readme_updates_manifest_and_cache(tmp_path, monkeypatch):
    customers_root = tmp_path / "VAST" / "Customers and Partners"
    account_dir = customers_root / "Contoso"
    account_dir.mkdir(parents=True)
    readme = account_dir / "README.md"
    readme.write_text("---\ntitle: Contoso\n---\n# Contoso\n\nPlaceholder body.")
    
    manifest_path = customers_root / "_MANIFEST.md"
    cache_dir = tmp_path / "Workflow" / "_cache"
    glossary_path = cache_dir / "glossary.json"
    
    # Patch manifest_sync globals
    monkeypatch.setattr(manifest_sync, "VAST_CUSTOMERS", customers_root)
    monkeypatch.setattr(manifest_sync, "CUSTOMERS_MANIFEST", manifest_path)
    monkeypatch.setattr(manifest_sync, "CACHE_DIR", cache_dir)
    monkeypatch.setattr(manifest_sync, "GLOSSARY_CACHE", glossary_path)
    
    # Patch enrich_customer globals
    monkeypatch.setattr(enrich_customer, "VAST_CUSTOMERS", customers_root)
    monkeypatch.setattr(enrich_customer, "CUSTOMERS_MANIFEST", manifest_path)
    monkeypatch.setattr(enrich_customer, "CACHE_DIR", cache_dir)
    monkeypatch.setattr(enrich_customer, "GLOSSARY_CACHE", glossary_path)
    
    def fake_scan():
        fm, _ = parse_frontmatter(readme.read_text())
        return [
            manifest_sync.CustomerEntry(
                name="Contoso",
                type=fm.get("account_type", ""),
                industry=fm.get("industry", ""),
                stage=fm.get("status", ""),
                my_role=fm.get("my_role", ""),
                last_contact=fm.get("last_contact", ""),
                context="",
            )
        ]
    
    monkeypatch.setattr(manifest_sync, "scan_customers_folder", fake_scan)
    monkeypatch.setattr(enrich_customer, "scan_customers_folder", fake_scan)
    fake_glossary = {
        "version": "test",
        "generated_at": "now",
        "people": [],
        "projects": [],
        "customers": [
            {
                "name": "Contoso",
                "type": "customer",
                "industry": "Energy",
                "stage": "Active",
                "my_role": "account-owner",
                "last_contact": "2026-01-05",
            }
        ],
    }
    monkeypatch.setattr(manifest_sync, "build_glossary_cache", lambda: fake_glossary)
    monkeypatch.setattr(enrich_customer, "build_glossary_cache", lambda: fake_glossary)
    
    class FakeResponse:
        def __init__(self, payload):
            self.choices = [
                type("Choice", (), {"message": type("Msg", (), {"content": json.dumps(payload)})()})
            ]
    
    class FakeClient:
        class chat:
            class completions:
                @staticmethod
                def create(*args, **kwargs):
                    return FakeResponse(
                        {
                            "account_type": "customer",
                            "industry": "Energy",
                            "stage": "Active",
                            "my_role": "account-owner",
                            "last_contact": "2026-01-05",
                            "context": "Energy AI design partner",
                        }
                    )
    
    result = enrich_customer.enrich_from_readme("Contoso", client=FakeClient())
    assert not result.errors
    
    fm, _ = parse_frontmatter(readme.read_text())
    assert fm.get("account_type") == "customer"
    assert fm.get("industry") == "Energy"
    assert fm.get("status") == "Active"
    assert fm.get("my_role") == "account-owner"
    assert fm.get("last_contact") == "2026-01-05"
    
    manifest_content = manifest_path.read_text()
    assert "| Contoso | customer | Active | Energy | account-owner | 2026-01-05" in manifest_content
    assert glossary_path.exists()
    glossary = json.loads(glossary_path.read_text())
    assert any(c["name"] == "Contoso" for c in glossary.get("customers", []))
