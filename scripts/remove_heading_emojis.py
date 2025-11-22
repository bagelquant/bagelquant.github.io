#!/usr/bin/env python3
"""
Scan `_posts` and `_pages` for Markdown files and remove emoji characters
from Markdown heading lines (lines starting with 1-6 `#`).
Creates a `.bak` backup for each modified file.
"""
import re
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]

# Emoji/unicode pictograph ranges (covers common emoji blocks)
emoji_ranges = (
    '\U0001F300-\U0001F6FF'  # Misc symbols & pictographs, emoticons, transport
    '\U0001F900-\U0001F9FF'  # Supplemental Symbols and Pictographs
    '\U0001FA70-\U0001FAFF'  # Symbols and Pictographs Extended-A
)
# Additional symbol ranges
extra_ranges = '\u2600-\u26FF\u2700-\u27BF\uFE0F'

emoji_pattern = re.compile('[%s%s]+' % (emoji_ranges, extra_ranges))

heading_re = re.compile(r'^(\s{0,3})(#{1,6})(\s*)(.*)$')

targets = []
for base in ('_posts', '_pages'):
    path = repo_root / base
    if path.exists():
        targets.append(path)

md_files = []
for t in targets:
    md_files.extend([p for p in t.rglob('*.md')])

modified = []
for f in md_files:
    text = f.read_text(encoding='utf-8')
    lines = text.splitlines()
    new_lines = []
    changed = False
    for line in lines:
        m = heading_re.match(line)
        if m:
            prefix_ws, hashes, space_after, rest = m.groups()
            # remove emojis from heading text
            new_rest = emoji_pattern.sub('', rest)
            # normalize spaces after removing emojis
            new_rest = re.sub(r'\s{2,}', ' ', new_rest).strip()
            if new_rest != rest:
                changed = True
                # if rest becomes empty, keep a single space to avoid malformed heading
                if new_rest == '':
                    new_line = f"{prefix_ws}{hashes}{space_after}"
                else:
                    new_line = f"{prefix_ws}{hashes}{space_after}{new_rest}"
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
