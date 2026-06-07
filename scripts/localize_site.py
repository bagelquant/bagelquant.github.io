from __future__ import annotations

import re
import json
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_EXTS = {".md", ".html"}
SKIP_DIRS = {"_includes", "_layouts", "_site", "assets", "scripts", "vendor", "zh"}
SKIP_FILES = {"search.json"}

TITLE_TRANSLATIONS = {
    "BagelQuant": "BagelQuant",
    "Home": "首页",
    "Quick Start": "快速开始",
    "Learn": "学习",
    "Learning Roadmap": "学习路线图",
    "Research": "研究",
    "Projects": "项目",
    "Docs": "文档",
    "App": "应用",
    "About Me": "关于我",
    "Search": "搜索",
    "Overview": "概览",
    "Architecture": "架构",
    "Public API": "公开 API",
    "Internals": "内部实现",
    "Reference": "参考",
    "Backend API": "后端 API",
    "Concepts": "概念",
    "Factor Evaluation": "因子评估",
    "Transaction Costs": "交易成本",
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
    "Foundations": "基础知识",
    "Finance": "金融",
    "Models": "模型",
    "Techniques": "技术方法",
    "Probability": "概率论",
    "Statistics": "统计学",
    "Linear Algebra": "线性代数",
    "Calculus": "微积分",
    "Optimization": "优化",
    "Stochastic Calculus": "随机微积分",
    "Asset Pricing": "资产定价",
    "Execution": "执行",
    "Market Microstructure": "市场微观结构",
    "Modern Portfolio Theory": "现代投资组合理论",
    "Portfolio Construction": "组合构建",
    "Risk Models": "风险模型",
    "Econometrics": "计量经济学",
    "Fama-MacBeth": "Fama-MacBeth",
    "GMM": "GMM",
    "OLS": "OLS",
    "Panel Regression": "面板回归",
    "Time Series": "时间序列",
    "Machine Learning": "机器学习",
    "Boosting": "Boosting",
    "Neural Networks": "神经网络",
    "Regularized Linear Models": "正则化线性模型",
    "Transformers": "Transformers",
    "Tree Models": "树模型",
    "Evaluation": "评估",
    "Cross Validation": "交叉验证",
    "Information Coefficient": "信息系数",
    "Quantile Analysis": "分位数组分析",
    "Turnover": "换手率",
    "Transformations": "变换",
    "Anscombe": "Anscombe",
    "Box-Cox": "Box-Cox",
    "Freeman-Tukey": "Freeman-Tukey",
    "Rank Normalization": "排序归一化",
    "Kelly Criterion": "Kelly 准则",
    "Position Sizing": "仓位 sizing",
    "Risk Parity": "风险平价",
    "Volatility Targeting": "波动率目标",
    "bagelquant-core": "bagelquant-core",
    "bagelquant-data": "bagelquant-data",
    "bagelquant-bt": "bagelquant-bt",
    "Introduction to Quant Equity": "量化股票研究导论",
    "Complete Workflow": "完整工作流",
    "Alpha Research in 30 Minutes": "30 分钟上手 Alpha 研究",
    "Factor Models in 30 Minutes": "30 分钟上手因子模型",
    "Portfolio Construction in 30 Minutes": "30 分钟上手组合构建",
    "Machine Learning for Alpha": "机器学习与 Alpha",
}

EXCERPT_TRANSLATIONS = {
    "Quantitative equity research, from first principles to investable portfolios.": "从基础原理到可投资组合的量化股票研究。",
    "A guided introduction to quantitative equity portfolio management.": "量化股票组合管理的引导式入门。",
    "Mathematical, statistical, financial, and modeling foundations for quant equity research.": "量化股票研究所需的数学、统计、金融与建模基础。",
    "Research outputs, reproductions, factor experiments, and portfolio cases.": "研究输出、复现、因子实验和组合案例。",
    "Documentation for the BagelQuant open-source ecosystem.": "BagelQuant 开源生态文档。",
}

EXACT_LINE_TRANSLATIONS = {
    "Use this roadmap according to the problem in front of you:": "可以根据手头的问题使用这条路线图：",
    "The practical companion is [Research](/research/).": "实践配套内容见 [研究](/zh/research/)。",
    "This section is for newcomers who want a fast, practitioner-oriented map of quantitative equity research before going deeper.": "本节面向希望先快速建立实践地图、再深入学习量化股票研究的新读者。",
    "Recommended reading order:": "推荐阅读顺序：",
    "This section is under development.": "本节仍在建设中。",
    "Software documentation now lives under": "软件文档现在位于",
    "Search the site": "搜索网站",
    "Enter text to search pages and posts.": "输入文本搜索页面和文章。",
    "Search...": "搜索...",
    "Return the absolute value of each element.": "返回每个元素的绝对值。",
    "Rows represent time and columns represent assets.": "行表示时间，列表示资产。",
    "Input numeric `Panel` or single-output `Graph`.": "输入数值型 `Panel` 或单输出 `Graph`。",
    "Optional graph-node name. A generated name is used when omitted.": "可选的图节点名称。省略时会自动生成名称。",
    "Optional metadata stored on the graph node.": "可选的图节点元数据。",
    "Lazy single-output graph. Call `.compute()` to materialize a `Panel`.": "惰性单输出图。调用 `.compute()` 可物化为 `Panel`。",
    "Learn probability, statistics, linear algebra, and optimization.": "学习概率论、统计学、线性代数和优化。",
    "Study asset pricing, factor models, risk models, and portfolio construction.": "学习资产定价、因子模型、风险模型和组合构建。",
    "Build econometric baselines before moving to machine learning.": "在进入机器学习之前，先建立计量经济学基线。",
    "Add evaluation and portfolio techniques as your research workflow matures.": "随着研究工作流成熟，再加入评估方法和组合技术。",
}

PHRASES = {
    "What is BagelQuant?": "BagelQuant 是什么？",
    "The Quant Equity Workflow": "量化股票研究工作流",
    "Start Here": "从这里开始",
    "Projects and Docs": "项目与文档",
    "Future App": "未来应用",
    "Explore:": "探索：",
    "Data -> Factor -> Prediction -> Portfolio -> Backtest": "数据 -> 因子 -> 预测 -> 组合 -> 回测",
    "Data → Factor → Prediction → Portfolio → Backtest": "数据 -> 因子 -> 预测 -> 组合 -> 回测",
    "Introduction to Quantitative Equity Management": "量化股票管理导论",
    "Factor Models in 30 Minutes": "30 分钟上手因子模型",
    "Alpha Research in 30 Minutes": "30 分钟上手 Alpha 研究",
    "Portfolio Construction in 30 Minutes": "30 分钟上手组合构建",
    "Machine Learning for Alpha": "机器学习与 Alpha",
    "Complete Workflow": "完整工作流",
    "Parameters": "参数",
    "Returns": "返回值",
    "Examples": "示例",
    "Notes": "说明",
    "Overview": "概览",
    "Architecture": "架构",
    "Quick Start": "快速开始",
    "Public API": "公开 API",
    "Internals": "内部实现",
    "Reference": "参考",
    "Backend API": "后端 API",
    "Concepts": "概念",
    "Factor Evaluation": "因子评估",
    "Transaction Costs": "交易成本",
    "quantitative equity research": "量化股票研究",
    "quantitative equity": "量化股票",
    "portfolio construction": "组合构建",
    "portfolio management": "组合管理",
    "factor models": "因子模型",
    "factor model": "因子模型",
    "risk models": "风险模型",
    "risk model": "风险模型",
    "machine learning": "机器学习",
    "asset pricing": "资产定价",
    "linear algebra": "线性代数",
    "stochastic calculus": "随机微积分",
    "probability": "概率论",
    "statistics": "统计学",
    "optimization": "优化",
    "econometric": "计量经济学",
    "portfolio": "组合",
    "Portfolio": "组合",
    "prediction": "预测",
    "Prediction": "预测",
    "factor": "因子",
    "Factor": "因子",
    "data": "数据",
    "Data": "数据",
    "backtest": "回测",
    "Backtest": "回测",
    "research": "研究",
    "Research": "研究",
    "workflow": "工作流",
    "Workflow": "工作流",
    "newcomers": "新读者",
    "practitioner-oriented": "面向实践",
}

TRANSLATE_CACHE: dict[str, str] = {}
LAST_TRANSLATE_AT = 0.0

DISCLAIMER_RE = re.compile(
    r"^>\s*(?:本页是|æœ¬é¡µæ˜¯)\s+\[[^\]]*\]\([^)]+\)\s+.*(?:中文版本|ä¸­æ–‡ç‰ˆæœ¬).*API.*(?:对齐|å¯¹é½).*?$"
)


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


def title_from_path(path: Path, fallback: str) -> str:
    if fallback:
        return fallback
    stem = path.parent.name if path.name.startswith("index.") else path.stem
    return stem.replace("-", " ").replace("_", " ").title()


def translate_title(title: str) -> str:
    return TITLE_TRANSLATIONS.get(title, title)


def protect_codeish(text: str) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}

    def stash(match: re.Match[str]) -> str:
        key = f"BQPH{len(protected)}"
        protected[key] = match.group(0)
        return key

    text = re.sub(r"!?\[[^\]]*\]\([^)]+\)", stash, text)
    text = re.sub(r'href="[^"]*"', stash, text)
    text = re.sub(r'src="[^"]*"', stash, text)
    text = re.sub(r'url: "[^"]*"', stash, text)
    text = re.sub(r"`[^`]*`", stash, text)
    text = re.sub(r"\*\*[A-Za-z_][A-Za-z0-9_]*\*\*", stash, text)
    text = re.sub(r"\b[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_]*\b", stash, text)
    return text, protected


def restore_codeish(text: str, protected: dict[str, str]) -> str:
    for key, value in protected.items():
        text = text.replace(key, value)
    return text


def replace_phrase(text: str, src: str, dst: str) -> str:
    if re.fullmatch(r"[A-Za-z][A-Za-z ]*[A-Za-z]", src):
        pattern = r"(?<![A-Za-z_])" + re.escape(src) + r"(?![A-Za-z_])"
        return re.sub(pattern, dst, text)
    return text.replace(src, dst)


def translate_link_label(label: str) -> str:
    plain = label.strip()
    if plain.startswith("`") and plain.endswith("`"):
        return label
    translated = TITLE_TRANSLATIONS.get(plain, plain)
    for src in sorted(PHRASES, key=len, reverse=True):
        translated = replace_phrase(translated, src, PHRASES[src])
    return translated


def translate_markdown_link_labels(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        marker = "!" if match.group(1) else ""
        label = translate_link_label(match.group(2))
        return f"{marker}[{label}]({match.group(3)})"

    return re.sub(r"(!?)\[([^\]]+)\]\(([^)]+)\)", replace, text)


def needs_translation(text: str) -> bool:
    visible = re.sub(r"BQPH\d+", "", text)
    letters = len(re.findall(r"[A-Za-z]", visible))
    cjk = len(re.findall(r"[\u4e00-\u9fff]", visible))
    return letters >= 10 and letters > cjk


def fetch_google_translation(text: str) -> str:
    query = urllib.parse.urlencode(
        {
            "client": "gtx",
            "sl": "en",
            "tl": "zh-CN",
            "dt": "t",
            "q": text,
        }
    )
    url = "https://translate.googleapis.com/translate_a/single?" + query
    with urllib.request.urlopen(url, timeout=12) as response:
        raw = response.read().decode("utf-8")
    payload = json.loads(raw)
    return "".join(part[0] for part in payload[0] if part and part[0])


def google_translate(text: str) -> str:
    if text in TRANSLATE_CACHE:
        return TRANSLATE_CACHE[text]
    try:
        translated = fetch_google_translation(text)
    except Exception:
        return text
    TRANSLATE_CACHE[text] = translated
    return translated


def local_translate_candidate(text: str) -> tuple[str, dict[str, str]]:
    translated, protected = protect_codeish(translate_markdown_link_labels(text))
    for src in sorted(PHRASES, key=len, reverse=True):
        translated = replace_phrase(translated, src, PHRASES[src])
    translated = translated.replace("Machine 学习ing", "机器学习")
    translated = translated.replace("machine 学习ing", "机器学习")
    translated = translated.replace("因子 Models", "因子模型")
    translated = translated.replace("组合 Construction", "组合构建")
    return translated, protected


def translate_inline(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return text
    plain = stripped
    prefix = ""
    list_match = re.match(r"^(\d+\.\s+)(.*)$", plain)
    if list_match:
        prefix = list_match.group(1)
        plain = list_match.group(2)
    elif plain.startswith(": "):
        prefix = ": "
        plain = plain[2:]

    if plain in EXACT_LINE_TRANSLATIONS:
        return text.replace(stripped, prefix + EXACT_LINE_TRANSLATIONS[plain])

    translated, protected = local_translate_candidate(text)
    if needs_translation(translated):
        translated = google_translate(translated)
    return restore_codeish(translated, protected)


def collect_translation_candidates(body: str) -> set[str]:
    body = strip_disclaimer_lines(body)
    candidates: set[str] = set()
    in_code = False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped or stripped.startswith("{%") or stripped.startswith("<script"):
            continue

        plain = stripped
        list_match = re.match(r"^(\d+\.\s+)(.*)$", plain)
        if list_match:
            plain = list_match.group(2)
        elif plain.startswith(": "):
            plain = plain[2:]
        if plain in EXACT_LINE_TRANSLATIONS:
            continue

        candidate, _protected = local_translate_candidate(line)
        if needs_translation(candidate):
            candidates.add(candidate)
    return candidates


def prefetch_translations(strings: set[str]) -> None:
    missing = sorted(s for s in strings if s not in TRANSLATE_CACHE)
    if not missing:
        return
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_map = {executor.submit(fetch_google_translation, s): s for s in missing}
        for future in as_completed(future_map):
            source = future_map[future]
            try:
                TRANSLATE_CACHE[source] = future.result()
            except Exception:
                TRANSLATE_CACHE[source] = source


def strip_disclaimer_lines(body: str) -> str:
    kept = []
    skip_blank = False
    for line in body.splitlines():
        if DISCLAIMER_RE.match(line.strip()):
            skip_blank = True
            continue
        if skip_blank and not line.strip():
            skip_blank = False
            continue
        skip_blank = False
        kept.append(line)
    return "\n".join(kept).lstrip()


def translate_body(body: str) -> str:
    body = strip_disclaimer_lines(body)
    in_code = False
    in_script = False
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            lines.append(line)
            continue
        if stripped.startswith("<script"):
            in_script = True
            lines.append(line)
            continue
        if in_script:
            lines.append(line)
            if "</script>" in stripped:
                in_script = False
            continue
        if in_code or stripped.startswith("{%") or "{{" in line or "{%" in line:
            lines.append(line)
            continue
        lines.append(rewrite_internal_links(translate_inline(line)))
    return "\n".join(lines).rstrip() + "\n"


def zh_internal_url(url: str) -> str:
    if not url.startswith("/"):
        return url
    if url.startswith(("/zh/", "/assets/", "/search.json")):
        return url
    if url in {"/favicon.ico", "/favicon.svg", "/site.webmanifest", "/apple-touch-icon.png"}:
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


def update_english(path: Path) -> tuple[str, str, str, dict[str, str], list[str]]:
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
    path.write_text(build_front_matter(raw, updates) + strip_disclaimer_lines(body).rstrip() + "\n", encoding="utf-8")
    return en, ref, body, fm, raw


def write_chinese(path: Path, en_url: str, ref: str, body: str, fm: dict[str, str], raw: list[str]) -> None:
    raw_title = title_from_path(path, fm.get("title", ""))
    updates = {
        "title": translate_title(raw_title),
        "permalink": zh_url(en_url),
        "lang": "zh",
        "ref": ref,
        "alternate_lang_url": en_url,
    }
    if fm.get("nav", "").endswith("_en"):
        updates["nav"] = fm["nav"][:-3] + "_zh"
    if "excerpt" in fm:
        updates["excerpt"] = EXCERPT_TRANSLATIONS.get(fm["excerpt"], translate_inline(fm["excerpt"]))

    target = zh_path_for(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_front_matter(raw, updates) + translate_body(body), encoding="utf-8")


def main() -> None:
    pages: list[tuple[Path, str, str, str, dict[str, str], list[str]]] = []
    candidates: set[str] = set()
    for path in public_pages():
        en_url, ref, body, fm, raw = update_english(path)
        pages.append((path, en_url, ref, body, fm, raw))
        candidates.update(collect_translation_candidates(body))
    prefetch_translations(candidates)
    for path, en_url, ref, body, fm, raw in pages:
        write_chinese(path, en_url, ref, body, fm, raw)


if __name__ == "__main__":
    main()
