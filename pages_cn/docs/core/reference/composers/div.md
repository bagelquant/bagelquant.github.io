---
layout: page
title: "div"
permalink: /zh/docs/core/reference/composers/div/
lang: zh
ref: "docs-core-reference-composers-div"
alternate_lang_url: /docs/core/reference/composers/div/
nav: docs_zh
---

# div

```python
div(lhs, rhs, name=None, metadata=None)
```

将第一帧除以第二帧。

## 参数

**lhs**：面板|图形
：左侧数字 `Panel` 或单输出 `Graph`。
**rhs**：面板|图形
：右侧数字 `Panel` 或单输出 `Graph`。
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
from bagelquant_core.composer import div

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
left = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)
right = Panel.from_domain(pd.DataFrame({"a": [1.0, 1.0, 2.0], "b": [1.0, 2.0, 4.0]}, index=domain.sessions), domain)

result = div(left, right).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。
