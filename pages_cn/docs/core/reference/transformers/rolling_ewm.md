---
layout: page
title: "rolling_ewm"
permalink: /zh/docs/core/reference/transformers/rolling_ewm/
lang: zh
ref: "docs-core-reference-transformers-rolling_ewm"
alternate_lang_url: /docs/core/reference/transformers/rolling_ewm/
nav: docs_zh
---

# 滚动_ewm

```python
rolling_ewm(source, com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, name=None, metadata=None)
```

[`ewm_mean`](./ewm_mean.md) 的别名。返回指数加权平均值。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**com**：浮动|无，默认 `None`
：质心衰减参数。只提供一个衰减参数。
**span**：浮动|无，默认 `None`
：跨度衰减参数。只提供一个衰减参数。
**halflife**：浮动|无，默认 `None`
：半衰期衰减参数。只提供一个衰减参数。
**alpha**：浮动|无，默认 `None`
：平滑或正则化参数，取决于操作。
**min_periods** : int, 默认 `0`
：产生值所需的最少观察次数。
**adjust** : 布尔值，默认 `True`
：是否除以衰减调节因子。
**ignore_na** : 布尔值，默认 `False`
：计算权重时是否忽略缺失值。
**name**：str |无，默认 `None`
: 可选的图节点名称。省略时会自动生成名称。
**metadata**：映射[str，任意] |无，默认 `None`
: 可选的图节点元数据。

## 返回值

**Graph**
: 惰性单输出图。调用 `.compute()` 可物化为 `Panel`。

## 示例

```python
import pandas as pd

from bagelquant_core import Domain, Panel
from bagelquant_core.transformer import rolling_ewm

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = rolling_ewm(source, span=2).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。

滚动计算独立地沿着每个资产列运行。
