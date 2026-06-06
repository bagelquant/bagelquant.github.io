---
layout: page
title: "bagelquant-core"
permalink: /zh/projects/bagelquant-core/
excerpt: "Panel data, lazy graph logic, and reusable operations for quantitative research."
lang: zh
ref: "projects-bagelquant-core"
alternate_lang_url: /projects/bagelquant-core/
---

> 本页是 [/projects/bagelquant-core/](/projects/bagelquant-core/) 的中文版本。专有名词和代码标识保持英文，以便和包 API 对齐。

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

- [Quick start](/zh/docs/core/quick-start/)
- [Architecture and design](/zh/docs/core/architecture/)
- [Public API](/zh/docs/core/public-api/)
- [Internal documentation](/zh/docs/core/internals/)
- [Transformer reference](/zh/docs/core/reference/transformers/)
- [Composer reference](/zh/docs/core/reference/composers/)
