---
layout: page
title: "kelly_rank_boxcox"
permalink: /zh/docs/core/reference/transformers/kelly_rank_boxcox/
lang: zh
ref: "docs-core-reference-transformers-kelly_rank_boxcox"
alternate_lang_url: /docs/core/reference/transformers/kelly_rank_boxcox/
nav: docs_zh
---

# kelly_rank_boxcox

```python
kelly_rank_boxcox(source, window, lambda_=0, name=None, metadata=None)
```

对正值进行排名，应用 Box-Cox，然后估计凯利。

## 参数

**source**：面板|图形
: 输入数值型 `Panel` 或单输出 `Graph`。
**window** : int
：以行为单位的正尾随窗口长度。
**lambda_**：浮动，默认`0`
：Box-Cox lambda 参数。使用 `0` 作为对数极限。
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
from bagelquant_core.transformer import kelly_rank_boxcox

domain = Domain(calendar=pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"]), universe=["a", "b"])
source = Panel.from_domain(pd.DataFrame({"a": [1.0, 2.0, 4.0], "b": [2.0, 3.0, 8.0]}, index=domain.sessions), domain)

result = kelly_rank_boxcox(source, window=2).compute().data
print(result)
```

## 说明

行表示时间，列表示资产。
