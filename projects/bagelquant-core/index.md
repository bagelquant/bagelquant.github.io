---
layout: page
title: "bagelquant-core"
permalink: /projects/bagelquant-core/
excerpt: "Panel data, lazy graph logic, and reusable operations for quantitative research."
lang: en
ref: "projects-bagelquant-core"
alternate_lang_url: /zh/projects/bagelquant-core/
---

`bagelquant-core` is the shared research kernel for the BagelQuant ecosystem.
It turns aligned panel data into lazy graph logic that can be composed,
executed, cached, and reused.

## What It Contains

- `Domain`, `Panel`, and `CategoryPanel` data containers.
- Lazy `Graph` objects for factor, prediction, and weight logic.
- Transformer functions for unary panel operations.
- Composer functions for multi-input operations.
- Internal execution runtime and operation metadata.

## Documentation

- [Quick start](/docs/core/quick-start/)
- [Architecture and design](/docs/core/architecture/)
- [Public API](/docs/core/public-api/)
- [Internal documentation](/docs/core/internals/)
- [Transformer reference](/docs/core/reference/transformers/)
- [Composer reference](/docs/core/reference/composers/)
