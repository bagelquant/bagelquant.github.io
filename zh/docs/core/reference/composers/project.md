---
layout: page
title: "project"
permalink: /zh/docs/core/reference/composers/project/
lang: zh
ref: "docs-core-reference-composers-project"
alternate_lang_url: /docs/core/reference/composers/project/
nav: docs_zh
---

# project

```python
project(frame, binary, name=None, metadata=None)
```

将值投影到二进制可用性框架等于 1 的单元格上。

## 参数

**frame**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**binary**：面板|图形
：二值投影输入。等于`1`的单元格被保留；其他细胞被掩盖。
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
from bagelquant_core.composer import project

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = project(left, right).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。
