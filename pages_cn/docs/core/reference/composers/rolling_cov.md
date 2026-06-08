---
layout: page
title: "rolling_cov"
permalink: /zh/docs/core/reference/composers/rolling_cov/
lang: zh
ref: "docs-core-reference-composers-rolling_cov"
alternate_lang_url: /docs/core/reference/composers/rolling_cov/
nav: docs_zh
---

# 滚动_cov

```python
rolling_cov(lhs, rhs, window, min_periods=None, ddof=1, name=None, metadata=None)
```

返回相应列之间的滚动协方差。

## 参数

**lhs**：面板|图形
：左侧数字 `Panel` 或单输出 `Graph`。
**rhs**：面板|图形
：右侧数字 `Panel` 或单输出 `Graph`。
**window** : int
：以行为单位的正尾随窗口长度。
**min_periods**：整数 |无，默认 `None`
：产生值所需的最少观察次数。
**ddof** : int, 默认 `1`
：方差或标准差计算使用的自由度增量。
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
from bagelquant_core.composer import rolling_cov

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = rolling_cov(left, right, window=2).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。

滚动计算独立地沿着每个资产列运行。
