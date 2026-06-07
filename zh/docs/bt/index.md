---
layout: content-list
title: "概览"
permalink: /zh/docs/bt/
lang: zh
ref: "docs-bt"
alternate_lang_url: /docs/bt/
nav: docs_zh
---

`bagelquant-bt` 衡量研究成果。它不会建立信号，但它会建立信号
不检索市场数据。

预期的工作流程是：

```
daily data -> factor or weights DataFrame -> bagelquant-bt result
```

该包是 DataFrame-first 的。价格和信号值必须是数字
`pandas.DataFrame` objects.
