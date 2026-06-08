---
layout: page
title: "min_max_scale"
permalink: /zh/docs/core/reference/transformers/min_max_scale/
lang: zh
ref: "docs-core-reference-transformers-min_max_scale"
alternate_lang_url: /docs/core/reference/transformers/min_max_scale/
nav: docs_zh
---

# 最小_最大_比例

```python
min_max_scale(source, name=None, metadata=None)
```

将每行缩放至 [0, 1]，对常量行使用 NaN。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
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
from bagelquant_core.transformer import min_max_scale

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = min_max_scale(source).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。
