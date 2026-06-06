from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_EXTS = {".md", ".html"}
SKIP_DIRS = {"_includes", "_layouts", "_site", "assets", "scripts", "zh"}
SKIP_FILES = {"search.json"}

TITLE_TRANSLATIONS = {
    "BagelQuant": "BagelQuant",
    "Home": "首页",
    "Quick Start": "快速开始",
    "Learn": "学习",
    "Research": "研究",
    "Projects": "项目",
    "Docs": "文档",
    "App": "应用",
    "About Me": "关于我",
    "Search": "搜索",
    "bagelquant-core": "bagelquant-core",
    "bagelquant-data": "bagelquant-data",
    "bagelquant-bt": "bagelquant-bt",
    "Introduction to Quant Equity": "量化股票研究导论",
    "Complete Workflow": "完整工作流",
    "Alpha Research in 30 Minutes": "30 分钟上手 Alpha 研究",
    "Factor Models in 30 Minutes": "30 分钟上手因子模型",
    "Portfolio Construction in 30 Minutes": "30 分钟上手组合构建",
    "Machine Learning for Alpha": "机器学习与 Alpha",
    "Foundations": "基础知识",
    "Finance": "金融",
    "Models": "模型",
    "Techniques": "技术方法",
    "Data": "数据",
    "Factors": "因子",
    "Prediction": "预测",
    "Portfolio": "组合",
    "Backtest": "回测",
    "Paper Notes": "论文笔记",
    "Reproductions": "复现",
    "Factor Library": "因子库",
    "Portfolio Cases": "组合案例",
    "Experiments": "实验",
}

PHRASES = {
    "What is BagelQuant?": "BagelQuant 是什么？",
    "The Quant Equity Workflow": "量化股票研究工作流",
    "Start Here": "从这里开始",
    "Projects and Docs": "项目与文档",
    "Future App": "未来应用",
    "About Me": "关于我",
    "Recommended reading order:": "推荐阅读顺序：",
    "Explore:": "探索：",
    "This section is under development.": "本节仍在建设中。",
    "Software documentation now lives under": "软件文档现在位于",
    "Search the site": "搜索网站",
    "Enter text to search pages and posts.": "输入文本搜索页面和文章。",
    "Search...": "搜索...",
    "Data": "数据",
    "Factor": "因子",
    "Prediction": "预测",
    "Portfolio": "组合",
    "Backtest": "回测",
    "Quick Start": "快速开始",
    "Learn": "学习",
    "Research": "研究",
    "Projects": "项目",
    "Docs": "文档",
    "App": "应用",
}

EXCERPT_TRANSLATIONS = {
    "Quantitative equity research, from first principles to investable portfolios.": "从基础原理到可投资组合的量化股票研究。",
    "Research outputs, reproductions, factor experiments, and portfolio cases.": "研究输出、复现、因子实验和组合案例。",
    "Documentation for the BagelQuant open-source ecosystem.": "BagelQuant 开源生态文档。",
}


def public_pages() -> list[Path]:
    pages: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in PUBLIC_EXTS:
            continue
        rel = path.relative_to(ROOT)
        if rel.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        pages.append(path)
    return sorted(pages)


def split_front_matter(text: str) -> tuple[dict[str, str], str, list[str]]:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text, []
    match = re.match(r"\A---\n(.*?)\n---[ \t]*\n?", text, flags=re.S)
    if not match:
        return {}, text, []
    raw_lines = match.group(1).splitlines()
    body = text[match.end():].lstrip()
    data: dict[str, str] = {}
    for line in raw_lines:
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data, body, raw_lines


def build_front_matter(raw_lines: list[str], updates: dict[str, str]) -> str:
    seen = set()
    out: list[str] = []
    for line in raw_lines:
        if ":" not in line or line.startswith(" "):
            out.append(line)
            continue
        key = line.split(":", 1)[0].strip()
        if key in updates:
            value = updates[key]
            if key in {"title", "excerpt", "ref"}:
                out.append(f'{key}: "{value}"')
            else:
                out.append(f"{key}: {value}")
            seen.add(key)
        else:
            out.append(line)
    for key, value in updates.items():
        if key in seen:
            continue
        if key in {"title", "excerpt", "ref"}:
            out.append(f'{key}: "{value}"')
        else:
            out.append(f"{key}: {value}")
    return "---\n" + "\n".join(out).rstrip() + "\n---\n\n"


def infer_url(path: Path, fm: dict[str, str]) -> str:
    permalink = fm.get("permalink", "").strip()
    if permalink:
        return permalink if permalink.endswith("/") else permalink + "/"
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.md":
        return "/"
    if rel.endswith("/index.md") or rel.endswith("/index.html"):
        return "/" + rel.rsplit("/", 1)[0] + "/"
    return "/" + re.sub(r"\.(md|html)$", "/", rel)


def ref_for(url: str) -> str:
    value = url.strip("/").replace("/", "-")
    return value or "home"


def zh_url(en_url: str) -> str:
    return "/zh/" if en_url == "/" else "/zh" + en_url


def zh_path_for(path: Path) -> Path:
    return ROOT / "zh" / path.relative_to(ROOT)


def translate_title(title: str) -> str:
    return TITLE_TRANSLATIONS.get(title, title)


def translate_body(body: str, en_url: str) -> str:
    in_code = False
    lines: list[str] = [
        f"> 本页是 [{en_url}]({en_url}) 的中文版本。专有名词和代码标识保持英文，以便和包 API 对齐。",
        "",
    ]
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            lines.append(line)
            continue
        if in_code or stripped.startswith("{%") or stripped.startswith("<script"):
            lines.append(line)
            continue
        translated = line
        for src, dst in PHRASES.items():
            translated = translated.replace(src, dst)
        translated = translated.replace("Data â†’ Factor â†’ Prediction â†’ Portfolio â†’ Backtest", "数据 -> 因子 -> 预测 -> 组合 -> 回测")
        translated = translated.replace("Data -> Factor -> Prediction -> Portfolio -> Backtest", "数据 -> 因子 -> 预测 -> 组合 -> 回测")
        translated = rewrite_internal_links(translated)
        lines.append(translated)
    return "\n".join(lines).rstrip() + "\n"


def zh_internal_url(url: str) -> str:
    if not url.startswith("/"):
        return url
    if url.startswith(("/zh/", "/assets/", "/search.json")):
        return url
    if url in {"/favicon.ico", "/favicon.svg", "/site.webmanifest"}:
        return url
    return "/zh/" if url == "/" else "/zh" + url


def rewrite_internal_links(line: str) -> str:
    line = re.sub(
        r"\]\((/[^)\"']*)\)",
        lambda match: "](" + zh_internal_url(match.group(1)) + ")",
        line,
    )
    line = re.sub(
        r'href="(/[^"]*)"',
        lambda match: 'href="' + zh_internal_url(match.group(1)) + '"',
        line,
    )
    line = re.sub(
        r'url: "(/[^"]*)"',
        lambda match: 'url: "' + zh_internal_url(match.group(1)) + '"',
        line,
    )
    return line


def update_english(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    fm, body, raw = split_front_matter(text)
    inner_fm, inner_body, inner_raw = split_front_matter(body)
    if inner_raw:
        fm = {**inner_fm, **fm}
        raw = inner_raw
        body = inner_body
    if not raw:
        raw = ["layout: page"]
    en = infer_url(path, fm)
    ref = ref_for(en)
    updates = {
        "lang": "en",
        "ref": ref,
        "alternate_lang_url": zh_url(en),
    }
    path.write_text(build_front_matter(raw, updates) + body, encoding="utf-8")
    return en, ref, body


def write_chinese(path: Path, en_url: str, ref: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    fm, _body, raw = split_front_matter(text)
    title = translate_title(fm.get("title", path.stem.replace("-", " ").title()))
    updates = {
        "title": title,
        "permalink": zh_url(en_url),
        "lang": "zh",
        "ref": ref,
        "alternate_lang_url": en_url,
    }
    if "excerpt" in fm:
        updates["excerpt"] = EXCERPT_TRANSLATIONS.get(fm["excerpt"], translate_title(fm["excerpt"]))
    target = zh_path_for(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        build_front_matter(raw, updates) + translate_body(body, en_url),
        encoding="utf-8",
    )


def main() -> None:
    for path in public_pages():
        en_url, ref, body = update_english(path)
        write_chinese(path, en_url, ref, body)


if __name__ == "__main__":
    main()
