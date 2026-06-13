# BagelQuant Website

Static website infrastructure for bagelquant.com.

This repository is responsible for:

- Website rendering and deployment
- Jekyll configuration and layouts
- Theme and assets
- Aggregating content from external repositories
- Publishing documentation from package repositories

This repository is **not the source of truth for knowledge content**.

## Architecture

The system separates content, code, and website infrastructure.

```text
bagelquant-content
    ↓
bagelquant.github.io
    ↓
GitHub Pages

bagelquant-core/docs
    ↓
bagelquant.github.io
    ↓
GitHub Pages

bagelquant-data/docs
    ↓
bagelquant.github.io
    ↓
GitHub Pages

bagelquant-bt/docs
    ↓
bagelquant.github.io
    ↓
GitHub Pages
```

## Repository Responsibilities

### bagelquant.github.io

Website infrastructure.

Contains:

```text
_layouts/
_includes/
assets/
.github/workflows/
_config.yml
```

Responsible for:

- Build
- Routing
- Deployment
- Theme
- Aggregating content

No knowledge content should be authored here.

### bagelquant-content

Knowledge and public content repository.

Contains:

```text
en/
cn/
```

Example:

```text
bagelquant-content/

en/
    learn/
    research/

cn/
    learn/
    research/
```

Responsible for:

- Learn section
- Research notes
- Blog content
- Public articles

Author content here using Obsidian.

### Package Repositories

Documentation stays with source code.

Example:

```text
bagelquant-core/

docs/
    en/
    cn/
```

Same structure for:

```text
bagelquant-data
bagelquant-bt
```

Responsible for:

- API docs
- Architecture docs
- Concepts
- Package usage

## Website Content Structure

During build:

```text
bagelquant.github.io/

content/

    en/

        learn/

        docs/

            index.md

            core/

            data/

            bt/

    cn/

        learn/

        docs/

            index.md

            core/

            data/

            bt/
```

The `content/` tree is checked out from `bagelquant-content` during the Pages
workflow. Package docs and the docs root `index.md` pages are generated during
that workflow before Jekyll builds the site.

Do not edit generated content.

Markdown pages without an explicit front matter `layout` use the site default
`content` layout. This lets package docs remain plain Markdown in their source
repositories while rendering with the website article layout.

Package docs also get path-scoped navigation panels from `_data/navigation.yml`.
Docs `index.md` pages are normalized during the Pages workflow to use the
`index` layout instead of the default `content` layout.

## Sync and Build Flow

### Public Content

```text
Edit content
↓
Push bagelquant-content
↓
trigger-site.yml
↓
repository_dispatch
↓
bagelquant.github.io
↓
Build
↓
Deploy
↓
bagelquant.com updates
```

### Package Documentation

```text
Edit package docs
↓
Push package repo
↓
trigger-site.yml
↓
repository_dispatch
↓
bagelquant.github.io
↓
Collect docs
↓
Build
↓
Deploy
```

## GitHub Actions

### bagelquant.github.io

Workflow:

```text
.github/workflows/jekyll.yml
```

Responsibilities:

- Checkout content repo
- Checkout package repos
- Collect docs
- Generate docs root index pages
- Normalize docs index pages to the index layout
- Build Jekyll
- Deploy Pages

Triggers:

```yaml
on:
  push:
    branches:
      - main

  workflow_dispatch:

  repository_dispatch:
    types:
      - content-updated
      - docs-updated
```

### Content Repository

Workflow:

```text
.github/workflows/trigger-site.yml
```

File:

```yaml
name: Trigger BagelQuant site rebuild

on:
  push:
    branches:
      - main

  workflow_dispatch:

jobs:
  trigger-site:
    runs-on: ubuntu-latest

    steps:
      - name: Trigger site rebuild
        uses: peter-evans/repository-dispatch@v4
        with:
          token: ${{ secrets.BAGELQUANT_TRIGGER_TOKEN }}
          repository: bagelquant/bagelquant.github.io
          event-type: content-updated
```

### Package Repositories

Workflow:

```text
.github/workflows/trigger-site.yml
```

File:

```yaml
name: Trigger BagelQuant site rebuild

on:
  push:
    branches:
      - main
    paths:
      - "docs/**"

  workflow_dispatch:

jobs:
  trigger-site:
    runs-on: ubuntu-latest

    steps:
      - name: Trigger site rebuild
        uses: peter-evans/repository-dispatch@v4
        with:
          token: ${{ secrets.BAGELQUANT_TRIGGER_TOKEN }}
          repository: bagelquant/bagelquant.github.io
          event-type: docs-updated
```

## Site Build Process

Inside `bagelquant.github.io/.github/workflows/jekyll.yml`:

```yaml
- name: Checkout content
  uses: actions/checkout@v4
  with:
    repository: bagelquant/bagelquant-content
    path: content

- name: Checkout bagelquant-core
  uses: actions/checkout@v4
  with:
    repository: bagelquant/bagelquant-core
    path: external/bagelquant-core

- name: Checkout bagelquant-data
  uses: actions/checkout@v4
  with:
    repository: bagelquant/bagelquant-data
    path: external/bagelquant-data

- name: Checkout bagelquant-bt
  uses: actions/checkout@v4
  with:
    repository: bagelquant/bagelquant-bt
    path: external/bagelquant-bt
```

Collect docs:

```yaml
- name: Collect package docs
  run: |
    mkdir -p content/en/docs/core
    mkdir -p content/cn/docs/core

    mkdir -p content/en/docs/data
    mkdir -p content/cn/docs/data

    mkdir -p content/en/docs/bt
    mkdir -p content/cn/docs/bt

    cp -R external/bagelquant-core/docs/en/. content/en/docs/core/ || true
    cp -R external/bagelquant-core/docs/cn/. content/cn/docs/core/ || true

    cp -R external/bagelquant-data/docs/en/. content/en/docs/data/ || true
    cp -R external/bagelquant-data/docs/cn/. content/cn/docs/data/ || true

    cp -R external/bagelquant-bt/docs/en/. content/en/docs/bt/ || true
    cp -R external/bagelquant-bt/docs/cn/. content/cn/docs/bt/ || true

    cat > content/en/docs/index.md <<'EOF'
    ---
    layout: index
    title: "Docs"
    excerpt: "Package documentation for the BagelQuant ecosystem."
    lang: en
    ref: docs
    alternate_lang_url: /content/cn/docs/
    ---

    Package documentation for the BagelQuant ecosystem.

    1. [bagelquant-data](data/) - Provider-neutral data access, local data lake management, provider integrations, and panel data contracts.
    2. [bagelquant-core](core/) - Shared research kernel for panel data, lazy graph execution, transformers, and reusable operations.
    3. [bagelquant-bt](bt/) - Backtesting and factor evaluation tools for measuring research outputs and portfolio weights.
    EOF

    cat > content/cn/docs/index.md <<'EOF'
    ---
    layout: index
    title: "文档"
    excerpt: "BagelQuant 生态系统的包文档。"
    lang: zh
    ref: docs
    alternate_lang_url: /content/en/docs/
    ---

    BagelQuant 生态系统的包文档。

    1. [bagelquant-data](data/) - 提供中立的数据访问、本地数据湖管理、数据源集成和面板数据契约。
    2. [bagelquant-core](core/) - 面板数据、惰性图执行、转换器和可复用操作的共享研究内核。
    3. [bagelquant-bt](bt/) - 用于衡量研究输出和组合权重的回测与因子评估工具。
    EOF

    find content/en/docs content/cn/docs -name index.md -print0 | while IFS= read -r -d '' index_file; do
      if ! head -n 1 "$index_file" | grep -q '^---$'; then
        tmp_file="$(mktemp)"
        {
          printf -- '---\nlayout: index\n---\n\n'
          cat "$index_file"
        } > "$tmp_file"
        mv "$tmp_file" "$index_file"
      fi
    done
```

## Local Development

Recommended workspace:

```text
Developer/

notes/

    publish/

    personal/

    work/

    journal/

bagelquant-content/

bagelquant.github.io/

bagelquant-core/

bagelquant-data/

bagelquant-bt/
```

Optional local symlink:

```bash
cd bagelquant.github.io

ln -s ../bagelquant-content content
```

Run locally:

```bash
bundle exec jekyll serve
```

Open:

```text
http://localhost:4000
```

## Writing Guidelines

### Internal Links

Use relative markdown links.

Example:

```md
[Kelly Criterion](../portfolio/kelly-criterion.md)
```

Avoid:

```md
[Kelly Criterion](/learn/...)
```

Reason:

- Works in Obsidian
- Works in Jekyll
- One source for both

### URLs

Use permalink for public URLs.

Example:

```yaml
---
permalink: /learn/techniques/portfolio/kelly-criterion/
---
```

## Manual Rebuild

If site does not refresh:

```text
bagelquant.github.io
→ Actions
→ Deploy Jekyll site to Pages
→ Run workflow
```

Do not run:

```text
pages-build-deployment
```

It is managed internally by GitHub.

## Design Principles

```text
Source of Truth
≠
Website
≠
Code
```

Author once.

Publish automatically.
