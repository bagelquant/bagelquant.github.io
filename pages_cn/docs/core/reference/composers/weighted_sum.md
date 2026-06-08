---
layout: page
title: "weighted_sum"
permalink: /zh/docs/core/reference/composers/weighted_sum/
lang: zh
ref: "docs-core-reference-composers-weighted_sum"
alternate_lang_url: /docs/core/reference/composers/weighted_sum/
nav: docs_zh
---

# 加权和

```python
weighted_sum(*frames, weights, name=None, metadata=None)
```

返回一帧或多帧的加权和。

## 参数

**frames**：面板|图形
：一个或多个数字 `Panel` 或单输出 `Graph` 输入。
**weights**：序列[实数]
：每个输入帧一个数字权重。
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
from bagelquant_core.composer import weighted_sum

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = weighted_sum(left, right, weights=[0.25, 0.75]).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。
