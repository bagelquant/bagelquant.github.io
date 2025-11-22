#!/usr/bin/env python3
"""
Remove manual numeric prefixes from H2/ H3 headings in markdown files.
Creates a .bak backup for each modified file.
"""
import re
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]

pattern = re.compile(r'^(#{2,3})(\s*)([0-9]+(?:\.[0-9]+)*[)\.]?\s+)(.*)$')

md_files = [p for p in repo_root.rglob('*.md') if '_site' not in p.parts]

modified = []
for f in md_files:
    text = f.read_text(encoding='utf-8')
    lines = text.splitlines()
    new_lines = []
    changed = False
    for line in lines:
        m = pattern.match(line)
        if m:
            # keep heading markers and the rest after numbering
            new_line = f"{m.group(1)}{m.group(2)}{m.group(4)}"
            if new_line != line:
                changed = True
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    if changed:
        bak = f.with_suffix(f.suffix + '.bak')
        bak.write_text(text, encoding='utf-8')
        f.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
        try:
            rel = str(f.relative_to(repo_root))
        except Exception:
            rel = str(f)
        modified.append(rel)

print('Modified files:')
for m in modified:
    print(m)
print(f'Total modified: {len(modified)}')
