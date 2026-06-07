---
layout: page
title: "orthogonalize"
permalink: /zh/docs/core/reference/composers/orthogonalize/
lang: zh
ref: "docs-core-reference-composers-orthogonalize"
alternate_lang_url: /docs/core/reference/composers/orthogonalize/
nav: docs_zh
---

# 正交化

```python
orthogonalize(frame, *factors, name=None, metadata=None)
```

将值投影到因子后返回逐行残差。

## 参数

**frame**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**factors**：面板|图形
：一个或多个因子 `Panel` 或单输出 `Graph` 输入。
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
from bagelquant_core.composer import orthogonalize

domain = Domain(calendar=pd.to_datetime(["2024-01-02"]), universe=["a", "b", "c"])
factor = Panel.from_domain(pd.DataFrame({"a": [1.0], "b": [3.0], "c": [5.0]}, index=domain.sessions), domain)
size = Panel.from_domain(pd.DataFrame({"a": [0.0], "b": [1.0], "c": [2.0]}, index=domain.sessions), domain)

result = orthogonalize(factor, size).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。
