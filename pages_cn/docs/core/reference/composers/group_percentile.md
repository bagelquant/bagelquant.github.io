---
layout: page
title: "group_percentile"
permalink: /zh/docs/core/reference/composers/group_percentile/
lang: zh
ref: "docs-core-reference-composers-group_percentile"
alternate_lang_url: /docs/core/reference/composers/group_percentile/
nav: docs_zh
---

# 组百分位数

```python
group_percentile(frame, group, name=None, metadata=None)
```

返回每组内按行的百分位数排名。

## 参数

**frame**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**group**：面板|图形
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
from bagelquant_core.composer import group_percentile

domain = Domain(calendar=pd.to_datetime(["2024-01-02"]), universe=["a", "b", "c"])
factor = Panel.from_domain(pd.DataFrame({"a": [1.0], "b": [3.0], "c": [8.0]}, index=domain.sessions), domain)
industry = CategoryPanel.from_domain(pd.DataFrame({"a": ["tech"], "b": ["tech"], "c": ["bank"]}, index=domain.sessions), domain)

result = group_percentile(factor, industry).compute().data
print(result)
```

## 说明

在操作运行之前，输入按索引和列对齐。

缺少的组标签被排除在组计算之外。
