---
layout: page
title: "max"
permalink: /zh/docs/core/reference/composers/max/
lang: zh
ref: "docs-core-reference-composers-max"
alternate_lang_url: /docs/core/reference/composers/max/
nav: docs_zh
---

# max

```python
max(*frames, name=None, metadata=None)
```

[`maximum`](./maximum.md) 的别名。返回按元素排列的最大值。

## 参数

**frames**：面板|图形
：一个或多个数字 `Panel` 或单输出 `Graph` 输入。
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
from bagelquant_core.composer import max

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = max(left, right).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。
