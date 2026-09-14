"""Render the public project directory from its reviewed inventory."""
import argparse
import datetime
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def render(data):
    datetime.date.fromisoformat(data['reviewed_on'])
    owner = data['owner']
    if not re.fullmatch(r'[A-Za-z0-9-]+', owner):
        raise ValueError('Invalid owner')
    seen = set()
    groups = {}
    for project in data['projects']:
        name = project['name']
        if not re.fullmatch(r'[A-Za-z0-9_.-]+', name) or name in seen:
            raise ValueError(f'Invalid or duplicate project: {name}')
        seen.add(name)
        path = project['entry']
        if path.startswith('/') or '..' in path.split('/') or '\\' in path:
            raise ValueError(f'Invalid entry: {path}')
        for key in ('summary', 'verification', 'entry_label', 'group'):
            if not project[key] or any(c in project[key] for c in '\n\r|'):
                raise ValueError(f'Invalid table field: {name}/{key}')
        groups.setdefault(project['group'], []).append(project)
    lines = [
        '# Project Directory', '',
        f"Review date: {data['reviewed_on']}. {len(seen)} public repositories.", '',
        '[Profile](https://github.com/' + owner + ') | [Engineering notes](ENGINEERING.md)', '',
        'The review covers repository structure, README content, selected implementation files,',
        'and workflow records. It is not a full code audit or an end-to-end run of every app.', '',
        'Entries describe the review snapshot. Follow each repository for current status.', ''
    ]
    for group, projects in groups.items():
        lines += [f'## {group}', '', '| 项目与入口 | 实现重点 | 验证与边界 |', '| --- | --- | --- |']
        for p in projects:
            url = f"https://github.com/{owner}/{p['name']}"
            entry = url + '/blob/main/' + quote(p['entry'], safe='/')
            lines.append(f"| [{p['name']}]({url}) · [{p['entry_label']}]({entry}) | {p['summary']} | {p['verification']} |")
        lines.append('')
    lines += ['## Maintenance', '',
              'Edit `projects.json`, then run `python scripts/catalog.py`.',
              'CI runs `python scripts/catalog.py --check` to detect drift and invalid entries.',
              'This check validates the local catalog, not live repository availability or application behavior.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    rendered = render(json.loads((ROOT / 'projects.json').read_text(encoding='utf-8')))
    destination = ROOT / 'PROJECTS.md'
    if args.check:
        if not destination.exists() or destination.read_text(encoding='utf-8') != rendered:
            raise SystemExit('PROJECTS.md is stale. Run python scripts/catalog.py')
        print('Project catalog is valid and up to date.')
    else:
        destination.write_text(rendered, encoding='utf-8')


if __name__ == '__main__':
    main()
