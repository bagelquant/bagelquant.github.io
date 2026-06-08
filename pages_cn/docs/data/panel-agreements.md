---
layout: page
title: "Panel Agreements"
permalink: /zh/docs/data/panel-agreements/
lang: zh
ref: "docs-data-panel-agreements"
alternate_lang_url: /docs/data/panel-agreements/
nav: docs_zh
---

# 检索到的面板

`RetrievedPanel` 是中性数据层结果。它不是核心适配器并且
不导入或构造 `bagelquant-core` 对象。

它包含：

- `kind`: `numeric_panel` or `category_panel`
- `data`：pandas 数据帧
- `universe`：静态资产序列或动态成员数据帧
- `calendar`：排序的 pandas DatetimeIndex
- `dataset_name`：稳定输入名称
- `metadata`：提供者、请求、沿袭、字段和日历元数据

下游代码可以显式使用这些普通对象：

```python
from bagelquant_core import Domain, Panel

domain = Domain(calendar=retrieved.calendar, universe=retrieved.universe)
panel = Panel.from_domain(
    retrieved.data,
    domain,
    name=retrieved.dataset_name,
    metadata=retrieved.metadata,
)
```

这保留了单向依赖性并让核心负责
面板语义。
