---
layout: page
title: "bagelquant-data"
permalink: /projects/bagelquant-data/
excerpt: "Provider-neutral data access, local lake snapshots, and panel retrieval."
lang: en
ref: "projects-bagelquant-data"
alternate_lang_url: /zh/projects/bagelquant-data/
---

`bagelquant-data` is the data layer for BagelQuant. It owns provider adapters,
local lake snapshots, metadata contracts, transformation pipelines, and
panel-shaped retrieval.

## What It Contains

- Provider registration and `DataRequest` objects.
- Local Parquet snapshot storage through `LocalDataLake`.
- `DataLakeManager` update and curation workflows.
- Lake-first `Loader` retrieval.
- `RetrievedPanel` handoff objects for downstream research packages.
- Tushare-specific update helpers.

## Documentation

- [Quick start](/docs/data/quick-start/)
- [Architecture and design](/docs/data/architecture/)
- [Public API](/docs/data/public-api/)
- [Internal documentation](/docs/data/internals/)
- [Backend API](/docs/data/backend-api/)
- [Tushare provider](/docs/data/providers/tushare/)
