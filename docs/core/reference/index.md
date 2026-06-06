---
layout: page
title: "Overview"
permalink: /docs/core/reference/
lang: en
ref: "docs-core-reference-index"
alternate_lang_url: /zh/docs/core/reference/
nav: docs_en
---

# API Reference

BagelQuant operations build lazy graphs from `Panel` inputs.

- [Transformer reference](./transformers/index.md): 85 public operations
- [Composer reference](./composers/index.md): 49 public operations

The reference pages are generated from the exported API and curated
documentation metadata. Regenerate them after changing the operation catalog:

```bash
uv run python scripts/generate_operator_reference.py
```
