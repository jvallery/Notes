import os
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def _render(template_name: str, context: dict) -> str:
    templates_dir = Path(__file__).resolve().parents[1] / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)))

    def slugify(text):
        if not text:
            return ""
        text = str(text).lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        return text.strip("-")

    def strip_extension(path):
        if not path:
            return ""
        return os.path.splitext(str(path))[0]

    def basename(path):
        if not path:
            return ""
        return os.path.basename(str(path))

    env.filters["slugify"] = slugify
    env.filters["strip_extension"] = strip_extension
    env.filters["basename"] = basename

    return env.get_template(template_name).render(**context)


def test_customer_template_omits_empty_account_headers_and_tags():
    rendered = _render(
        "customer.md.j2",
        {
            "title": "Test",
            "date": "2026-01-05",
            "account": "",
            "participants": ["A", "B"],
            "summary": "Summary",
            "topics": [],
            "decisions": [],
            "tasks": [],
            "facts": [],
            "source": "email",
            "source_ref": "",
        },
    )

    assert "**Account**:" not in rendered
    assert "account/" not in rendered
    assert "[[]]" not in rendered


def test_projects_template_omits_empty_project_headers_and_tags():
    rendered = _render(
        "projects.md.j2",
        {
            "title": "Test",
            "date": "2026-01-05",
            "project": "",
            "participants": ["A", "B"],
            "summary": "Summary",
            "topics": [],
            "decisions": [],
            "tasks": [],
            "facts": [],
            "source": "email",
            "source_ref": "",
        },
    )

    assert "**Project**:" not in rendered
    assert "project/" not in rendered
    assert "[[]]" not in rendered

