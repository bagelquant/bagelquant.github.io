from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent

PACKAGES = {
    "core": WORKSPACE / "bagelquant-core",
    "data": WORKSPACE / "bagelquant-data",
    "bt": WORKSPACE / "bagelquant-bt",
}

CURATED = {
    "core": [
        "index.md",
        "quick-start.md",
        ("02_architecture/bagelquant core architecture.md", "architecture.md"),
        "public-api.md",
        "internals.md",
        ("01_concepts/panel.md", "panel.md"),
        ("01_concepts/graph.md", "graph.md"),
        ("01_concepts/transformer.md", "transformer.md"),
        ("01_concepts/composer.md", "composer.md"),
        ("01_concepts/execution.md", "execution.md"),
        ("reference/index.md", "reference/index.md"),
        ("reference/transformers/index.md", "reference/transformers/index.md"),
        ("reference/composers/index.md", "reference/composers/index.md"),
    ],
    "data": [
        "index.md",
        "quick-start.md",
        "architecture.md",
        "public-api.md",
        "internals.md",
        "concepts.md",
        "contracts.md",
        "panel-agreements.md",
        ("backend-api.md", "backend-api.md"),
        ("providers/tushare.md", "providers/tushare.md"),
    ],
    "bt": [
        "index.md",
        "quick-start.md",
        "architecture.md",
        "public-api.md",
        "internals.md",
        "concepts.md",
        ("api.md", "api.md"),
        "transaction-costs.md",
        "factor-evaluation.md",
    ],
}

TITLES = {
    "index.md": "Overview",
    "quick-start.md": "Quick Start",
    "architecture.md": "Architecture And Design",
    "public-api.md": "Public API",
    "internals.md": "Internal Documentation",
    "panel.md": "Panel",
    "graph.md": "Graph",
    "transformer.md": "Transformer",
    "composer.md": "Composer",
    "execution.md": "Execution",
    "concepts.md": "Concepts",
    "contracts.md": "Data Contracts",
    "panel-agreements.md": "Panel Agreements",
    "backend-api.md": "Backend API",
    "tushare.md": "Tushare Provider",
    "api.md": "API",
    "transaction-costs.md": "Transaction Costs",
    "factor-evaluation.md": "Factor Evaluation",
}

ZH_TITLES = {
    "index.md": "概览",
    "quick-start.md": "快速开始",
    "architecture.md": "架构与设计",
    "public-api.md": "公开 API",
    "internals.md": "内部实现",
    "panel.md": "Panel",
    "graph.md": "Graph",
    "transformer.md": "Transformer",
    "composer.md": "Composer",
    "execution.md": "Execution",
    "concepts.md": "概念",
    "contracts.md": "数据契约",
    "panel-agreements.md": "Panel 对接约定",
    "backend-api.md": "后端 API",
    "tushare.md": "Tushare Provider",
    "api.md": "API",
    "transaction-costs.md": "交易成本",
    "factor-evaluation.md": "因子评估",
}


def read_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return text


def front_matter(title: str, permalink: str, lang: str, ref: str, alternate: str) -> str:
    return (
        "---\n"
        "layout: page\n"
        f'title: "{title}"\n'
        f"permalink: {permalink}\n"
        f"lang: {lang}\n"
        f'ref: "{ref}"\n'
        f"alternate_lang_url: {alternate}\n"
        f"nav: docs_{lang}\n"
        "---\n\n"
    )


def normalize_item(item: str | tuple[str, str]) -> tuple[str, str]:
    if isinstance(item, tuple):
        return item
    return item, item


def copy_doc(package: str, src_rel: str, dst_rel: str, lang: str) -> None:
    package_root = PACKAGES[package]
    src = package_root / "docs" / (Path("zh") / src_rel if lang == "zh" else src_rel)
    if not src.exists() and lang == "zh":
        src = package_root / "docs" / src_rel
    if not src.exists():
        return

    base_url = f"/docs/{package}/{dst_rel}".replace("\\", "/")
    if base_url.endswith("/index.md"):
        base_url = base_url[: -len("index.md")]
    else:
        base_url = base_url.removesuffix(".md") + "/"

    permalink = f"/zh{base_url}" if lang == "zh" else base_url
    alternate = base_url if lang == "zh" else f"/zh{base_url}"
    ref = f"docs-{package}-{dst_rel.removesuffix('.md').replace('/', '-')}"
    title_key = Path(dst_rel).name
    title = (ZH_TITLES if lang == "zh" else TITLES).get(title_key, Path(dst_rel).stem)

    target_root = ROOT / ("zh/docs" if lang == "zh" else "docs") / package
    target = target_root / dst_rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        front_matter(title, permalink, lang, ref, alternate) + read_body(src),
        encoding="utf-8",
    )


def main() -> None:
    for folder in [ROOT / "docs" / key for key in PACKAGES]:
        if folder.exists():
            shutil.rmtree(folder)
    for folder in [ROOT / "zh" / "docs" / key for key in PACKAGES]:
        if folder.exists():
            shutil.rmtree(folder)

    for package, items in CURATED.items():
        for item in items:
            src_rel, dst_rel = normalize_item(item)
            copy_doc(package, src_rel, dst_rel, "en")
            copy_doc(package, src_rel, dst_rel, "zh")
    for section in ["transformers", "composers"]:
        source_dir = PACKAGES["core"] / "docs" / "reference" / section
        for source in sorted(source_dir.glob("*.md")):
            rel = f"reference/{section}/{source.name}"
            copy_doc("core", rel, rel, "en")
            copy_doc("core", rel, rel, "zh")


if __name__ == "__main__":
    main()
