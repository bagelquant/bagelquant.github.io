---
layout: page
title: "rolling_lasso"
permalink: /zh/docs/core/reference/composers/rolling_lasso/
lang: zh
ref: "docs-core-reference-composers-rolling_lasso"
alternate_lang_url: /docs/core/reference/composers/rolling_lasso/
nav: docs_zh
---

# 滚动套索

```python
rolling_lasso(y, *factors, window, alpha=1.0, max_iter=1000, tolerance=1e-08, name=None, metadata=None)
```

返回先验窗口套索回归预测。

## 参数

**y**：面板|图形
：因变量 `Panel` 或单输出 `Graph`。
**factors**：面板|图形
：一个或多个因子 `Panel` 或单输出 `Graph` 输入。
**window** : int
：以行为单位的正尾随窗口长度。
**alpha**：浮动，默认`1.0`
：平滑或正则化参数，取决于操作。
**max_iter** : int, 默认 `1000`
：最大坐标下降迭代。
**tolerance**：浮动，默认`1e-08`
：坐标下降的收敛容差。
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
from bagelquant_core.composer import rolling_lasso

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = rolling_lasso(left, right, window=2).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。

滚动计算独立地沿着每个资产列运行。

该模型仅适合先前的行并预测当前行。
