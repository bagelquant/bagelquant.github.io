# BagelQuant Website

Static website infrastructure for bagelquant.com.

AI contributors start with [AGENTS.md](AGENTS.md) and the
[local rule index](.ai/README.md).

This repository is responsible for:

- Website rendering and deployment
- Jekyll configuration and layouts
- Theme and assets
- Aggregating content from external repositories
- Providing links to package documentation in the source repositories

This repository is **not the source of truth for knowledge content**.

## Local BagelQuant workspace

Content and the website are independent checkouts outside `bagelquant-workspace`.
The workspace pins Data/Core/BT/Workbench but does not supply website publication
inputs. Shared numerical data is never owned or published by this website.

## Architecture

The system separates content, code, and website infrastructure.

```text
bagelquant-content
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

The Pages workflow checks out `bagelquant-content` into `content/`.
Articles and public App pages stay in Content. Markdown pages without an explicit
layout use the site's default `content` layout.

Package documentation stays in Core/Data/BT. The site does not check out package
repositories, copy their docs, generate package pages or accept `docs-updated`.

Site-owned `docs/en/index.md` and `docs/cn/index.md` link to the GitHub documentation.
Their explicit permalinks retain `/content/en/docs/` and `/content/cn/docs/`, matching
the global navigation. These pages live outside the imported Content checkout.

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

## GitHub Actions

### bagelquant.github.io

Workflow:

```text
.github/workflows/jekyll.yml
```

Responsibilities:

- Checkout content repo
- Render site-owned documentation entrances
- Record Site and Content revisions
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

## Build provenance

Every Pages artifact includes `source-revisions.json` at its root. It records
this site and the exact Content commit checked out for that build, together with
tracked-change flags. Packages and the numerical workspace are not build inputs.
For a local check against sibling Site and Content checkouts, run
`python scripts/source_revisions.py --workspace .. --output _site/source-revisions.json`.
