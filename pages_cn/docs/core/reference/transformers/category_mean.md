---
layout: page
title: "category_mean"
permalink: /zh/docs/core/reference/transformers/category_mean/
lang: zh
ref: "docs-core-reference-transformers-category_mean"
alternate_lang_url: /docs/core/reference/transformers/category_mean/
nav: docs_zh
---

# 类别_平均值

```python
category_mean(source, categories, name=None, metadata=None)
```

将每个资产值替换为其每行中的类别平均值。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**categories**：面板|图形
：匹配包含行组标签的 `CategoryPanel`。
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

from bagelquant_core import CategoryPanel, Domain, Panel
from bagelquant_core.transformer import category_mean

domain = Domain(calendar=pd.to_datetime(["2024-01-02"]), universe=["a", "b", "c"])
factor = Panel.from_domain(pd.DataFrame({"a": [1.0], "b": [3.0], "c": [8.0]}, index=domain.sessions), domain)
industry = CategoryPanel.from_domain(pd.DataFrame({"a": ["tech"], "b": ["tech"], "c": ["bank"]}, index=domain.sessions), domain)

result = category_mean(factor, industry).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。

缺少的组标签被排除在组计算之外。
