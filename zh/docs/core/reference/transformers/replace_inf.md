---
layout: page
title: "replace_inf"
permalink: /zh/docs/core/reference/transformers/replace_inf/
lang: zh
ref: "docs-core-reference-transformers-replace_inf"
alternate_lang_url: /docs/core/reference/transformers/replace_inf/
nav: docs_zh
---

# 替换_inf

```python
replace_inf(source, name=None, metadata=None)
```

用 NaN 替换正无穷大和负无穷大。

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
from bagelquant_core.transformer import replace_inf

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = replace_inf(source).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。
