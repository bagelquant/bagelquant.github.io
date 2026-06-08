---
layout: page
title: "rolling_median"
permalink: /zh/docs/core/reference/transformers/rolling_median/
lang: zh
ref: "docs-core-reference-transformers-rolling_median"
alternate_lang_url: /docs/core/reference/transformers/rolling_median/
nav: docs_zh
---

# 滚动中位数

```python
rolling_median(source, window, min_periods=None, name=None, metadata=None)
```

返回一段时间内的滚动中位数。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**window** : int
：以行为单位的正尾随窗口长度。
**min_periods**：整数 |无，默认 `None`
：产生值所需的最少观察次数。
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
from bagelquant_core.transformer import rolling_median

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = rolling_median(source, window=2).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。

滚动计算独立地沿着每个资产列运行。
