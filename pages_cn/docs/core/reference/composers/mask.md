---
layout: page
title: "mask"
permalink: /zh/docs/core/reference/composers/mask/
lang: zh
ref: "docs-core-reference-composers-mask"
alternate_lang_url: /docs/core/reference/composers/mask/
nav: docs_zh
---

# mask

```python
mask(frame, mask_frame, replace_value=nan, name=None, metadata=None)
```

替换掩码框架为 false 的值。

## 参数

**frame**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**mask_frame**：面板|图形
：屏蔽输入。诚实的细胞保留价值；错误或缺失的单元格将被替换。
**replace_value**：浮动，默认`nan`
：在掩码为假或缺失的情况下插入值。
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
from bagelquant_core.composer import mask

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = mask(left, right, replace_value=0).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。
