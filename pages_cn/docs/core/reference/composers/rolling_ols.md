---
layout: page
title: "rolling_ols"
permalink: /zh/docs/core/reference/composers/rolling_ols/
lang: zh
ref: "docs-core-reference-composers-rolling_ols"
alternate_lang_url: /docs/core/reference/composers/rolling_ols/
nav: docs_zh
---

# 滚动_ols

```python
rolling_ols(y, *factors, window, name=None, metadata=None)
```

根据先前滚动窗口上拟合的因子预测 y。

## 参数

**y**：面板|图形
：因变量 `Panel` 或单输出 `Graph`。
**factors**：面板|图形
：一个或多个因子 `Panel` 或单输出 `Graph` 输入。
**window** : int
：以行为单位的正尾随窗口长度。
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
from bagelquant_core.composer import rolling_ols

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = rolling_ols(left, right, window=2).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。

滚动计算独立地沿着每个资产列运行。

该模型仅适合先前的行并预测当前行。
