---
layout: page
title: "bagelquant-data"
permalink: /zh/projects/bagelquant-data/
excerpt: "Provider-neutral data access, local lake snapshots, and panel retrieval."
lang: zh
ref: "projects-bagelquant-data"
alternate_lang_url: /projects/bagelquant-data/
---

> 本页是 [/projects/bagelquant-data/](/projects/bagelquant-data/) 的中文版本。专有名词和代码标识保持英文，以便和包 API 对齐。

`bagelquant-data` is the data layer for BagelQuant. It owns provider adapters,
local lake snapshots, metadata contracts, transformation pipelines, and
panel-shaped retrieval.

## What It Contains

- Provider registration and `数据Request` objects.
- Local Parquet snapshot storage through `Local数据Lake`.
- `数据LakeManager` update and curation workflows.
- Lake-first `Loader` retrieval.
- `RetrievedPanel` handoff objects for downstream research packages.
- Tushare-specific update helpers.

## Documentation

- [Quick start](/zh/docs/data/quick-start/)
- [Architecture and design](/zh/docs/data/architecture/)
- [Public API](/zh/docs/data/public-api/)
- [Internal documentation](/zh/docs/data/internals/)
- [Backend API](/zh/docs/data/backend-api/)
- [Tushare provider](/zh/docs/data/providers/tushare/)
