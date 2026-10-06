"""Record the exact independent sources consumed by a Pages build."""

import argparse
import json
import subprocess
from pathlib import Path


def source_revisions(sources: dict[str, Path]) -> dict:
    records = {}
    for name, path in sources.items():
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path, text=True).strip()
        changed = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=path, text=True).strip()
        records[name] = {"commit": revision, "tracked_changes": bool(changed)}
    return {"schema": "bagelquant-site-sources.v1", "sources": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, help="Use sibling repositories for a local validation")
    parser.add_argument("--output", type=Path, default=Path("_site/source-revisions.json"))
    args = parser.parse_args()
    site = Path(__file__).resolve().parents[1]
    if args.workspace:
        sources = {name: args.workspace.resolve() / name for name in ("bagelquant.github.io", "bagelquant-content")}
    else:
        sources = {"bagelquant.github.io": site, "bagelquant-content": site / "content"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(source_revisions(sources), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
