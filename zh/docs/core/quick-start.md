---
layout: page
title: "快速开始"
permalink: /zh/docs/core/quick-start/
lang: zh
ref: "docs-core-quick-start"
alternate_lang_url: /docs/core/quick-start/
nav: docs_zh
---

# 快速开始

`bagelquant-core` 是 BagelQuant 研究的面板和图表基础。
当原始研究输入已经作为 pandas 数据提供并且您可以使用它时
想要可重复的因子逻辑。

## Install

```bash
uv add bagelquant-core
```

对于从此存储库进行本地开发：

```bash
uv run python example.py
```

## 建立一个域

`Domain` 定义每个输入使用的交易会话和资产范围
控制板。该软件包不下载日历或安全大师；来电者
从数据层提供它们。

```python
import pandas as pd

from bagelquant_core import Domain

domain = Domain(
    calendar=pd.bdate_range("2024-01-01", "2024-12-31"),
    universe=["AAPL", "MSFT"],
)
```

## 创建面板

`Panel.from_domain` 将原始帧与域对齐。行是会话，列是
是资产，价值是数字。

```python
from bagelquant_core import Panel

price = Panel.from_domain(price_df, domain, name="price")
book = Panel.from_domain(book_df, domain, name="book")
quality = Panel.from_domain(quality_df, domain, name="quality")
```

## 绘制因子图

变压器是一元运算。作曲家组合一个或多个输入。两个都
返回惰性 `Graph` 对象。

```python
from bagelquant_core.composer import div, weighted_sum
from bagelquant_core.transformer import rank, rolling_mean, winsorize, zscore

bm_ratio = div(book, price, name="bm_ratio")
bm_factor = rank(zscore(winsorize(bm_ratio)), name="bm_factor")
quality_factor = rank(zscore(quality), name="quality_factor")

prediction = weighted_sum(
    bm_factor,
    quality_factor,
    weights=[0.5, 0.5],
    name="prediction",
)

signal = rolling_mean(rank(prediction), window=20, name="signal")
```

## Execute

在下游图上调用 `compute()`。执行运行时评估
上游依赖项一次并缓存当前运行的中间面板。

```python
signal.compute()
result = signal.output
frame = result.data
```

使用 `frame` 作为下游组合构建或回测的输入。
