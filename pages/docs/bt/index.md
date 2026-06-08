---
layout: content-list
title: "Overview"
permalink: /docs/bt/
lang: en
ref: "docs-bt"
alternate_lang_url: /zh/docs/bt/
nav: docs_en
---

`bagelquant-bt` measures research outputs. It does not build signals and it does
not retrieve market data.

The expected workflow is:

```
daily data -> factor or weights DataFrame -> bagelquant-bt result
```

The package is DataFrame-first. Prices and signal values must be numeric
`pandas.DataFrame` objects.
