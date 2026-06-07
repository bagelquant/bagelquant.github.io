---
layout: page
title: "概览"
permalink: /zh/docs/bt/
lang: zh
ref: "docs-bt"
alternate_lang_url: /docs/bt/
nav: docs_zh
---

# bagelquant-bt 文档

`bagelquant-bt` 衡量研究成果。它不会建立信号，但它会建立信号
不检索市场数据。

预期的工作流程是：

```text
daily data -> factor or weights DataFrame -> bagelquant-bt result
```

该包是 DataFrame-first 的。价格和信号值必须是数字
`pandas.DataFrame` objects.

## 主要入口点

```python
from bagelquant_bt import BacktestConfig, run_backtest

result = run_backtest(
    weights,
    prices,
    kind="weights",
    config=BacktestConfig(initial_capital=1_000_000),
)
```

当第一个参数是组合权重时使用 `kind="weights"`。

当第一个参数是因子分数时使用 `kind="factor"`。

## Docs

- [概念](concepts.md)
- [API](api.md)
- [Transaction costs](transaction-costs.md)
- [因子 evaluation](factor-evaluation.md)
