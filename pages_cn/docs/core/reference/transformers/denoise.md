---
layout: page
title: "denoise"
permalink: /zh/docs/core/reference/transformers/denoise/
lang: zh
ref: "docs-core-reference-transformers-denoise"
alternate_lang_url: /docs/core/reference/transformers/denoise/
nav: docs_zh
---

# denoise

```python
denoise(source, threshold=1e-12, name=None, metadata=None)
```

将绝对值很小的值替换为零。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**threshold**：浮动，默认`1e-12`
：非负大小，低于该值的值将替换为零。
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
from bagelquant_core.transformer import denoise

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = denoise(source, threshold=1e-6).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。
