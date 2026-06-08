---
layout: page
title: "trim"
permalink: /zh/docs/core/reference/transformers/trim/
lang: zh
ref: "docs-core-reference-transformers-trim"
alternate_lang_url: /docs/core/reference/transformers/trim/
nav: docs_zh
---

# trim

```python
trim(source, lower, upper, name=None, metadata=None)
```

将超出固定下限和上限的值替换为 NaN。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**lower** : Real
：固定下限或下分位数，具体取决于操作。
**upper** : Real
：固定上界或上分位数，具体取决于操作。
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
from bagelquant_core.transformer import trim

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = trim(source, lower=-1, upper=1).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。
