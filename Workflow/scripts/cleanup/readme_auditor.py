#!/usr/bin/env python3
"""
README Auditor: Use AI to review and clean up README files.

This script:
1. Reads a README file
2. Sends it through the audit prompt
3. Returns specific recommendations for cleanup
"""

import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)


def load_audit_prompt() -> str:
    """Load the audit prompt template."""
    prompt_path = Path(__file__).parent.parent.parent / 'prompts' / 'audit-readme.md'
    return prompt_path.read_text()


def audit_readme(path: Path, entity_type: str, client: OpenAI) -> dict:
    """Audit a single README file."""
    content = path.read_text()
    entity_name = path.parent.name
    
    prompt_template = load_audit_prompt()
    prompt = prompt_template.format(
        entity_type=entity_type,
        entity_name=entity_name,
        content=content
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a meticulous knowledge management auditor. Review the README and provide specific, actionable feedback."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    
    return {
        'entity_name': entity_name,
        'entity_type': entity_type,
        'path': str(path),
        'audit': response.choices[0].message.content
    }


def find_readmes(vault_root: Path, entity_type: str = None, limit: int = None) -> list:
    """Find README files to audit."""
    readmes = []
    
    if entity_type in (None, 'people'):
        people_dir = vault_root / 'VAST' / 'People'
        if people_dir.exists():
            for readme in people_dir.glob('*/README.md'):
                readmes.append((readme, 'people'))
    
    if entity_type in (None, 'customer'):
        customers_dir = vault_root / 'VAST' / 'Customers and Partners'
        if customers_dir.exists():
            for readme in customers_dir.glob('*/README.md'):
                readmes.append((readme, 'customer'))
    
    if entity_type in (None, 'projects'):
        projects_dir = vault_root / 'VAST' / 'Projects'
        if projects_dir.exists():
            for readme in projects_dir.glob('*/README.md'):
                readmes.append((readme, 'projects'))
    
    if limit:
        readmes = readmes[:limit]
    
    return readmes


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Audit README files with AI')
    parser.add_argument('--type', type=str, choices=['people', 'customer', 'projects'],
                        help='Entity type to audit')
    parser.add_argument('--name', type=str, help='Specific entity name to audit')
    parser.add_argument('--limit', type=int, help='Limit number of READMEs to audit')
    parser.add_argument('--output', type=str, help='Output file for audit results')
    args = parser.parse_args()
    
    vault_root = Path(__file__).parent.parent.parent.parent
    client = OpenAI()
    
    if args.name:
        # Find specific entity
        readmes = []
        for entity_type in ['people', 'customer', 'projects']:
            for path, etype in find_readmes(vault_root, entity_type):
                if path.parent.name.lower() == args.name.lower():
                    readmes = [(path, etype)]
                    break
            if readmes:
                break
        if not readmes:
            print(f"Entity not found: {args.name}")
            return
    else:
        readmes = find_readmes(vault_root, args.type, args.limit)
    
    print(f"Auditing {len(readmes)} READMEs...\n")
    
    results = []
    for i, (path, entity_type) in enumerate(readmes, 1):
        print(f"[{i}/{len(readmes)}] Auditing {path.parent.name}...")
        try:
            result = audit_readme(path, entity_type, client)
            results.append(result)
            print("  ✓ Complete")
        except Exception as e:
            print(f"  ✗ Error: {e}")
            results.append({
                'entity_name': path.parent.name,
                'entity_type': entity_type,
                'path': str(path),
                'error': str(e)
            })
    
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(results, indent=2))
        print(f"\nResults saved to {output_path}")
    else:
        # Print results
        for result in results:
            if 'error' in result:
                continue
            print(f"\n{'='*60}")
            print(f"Entity: {result['entity_name']} ({result['entity_type']})")
            print(f"{'='*60}")
            print(result['audit'])


if __name__ == '__main__':
    main()
