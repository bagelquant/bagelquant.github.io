---
layout: page
title: "公开 API"
permalink: /zh/docs/core/public-api/
lang: zh
ref: "docs-core-public-api"
alternate_lang_url: /docs/core/public-api/
nav: docs_zh
---

# 公开 API

稳定的公共API是从`bagelquant_core`导出的，
`bagelquant_core.transformer`, and `bagelquant_core.composer`.

## 顶级对象

- `Domain`：交易会话加上静态或动态资产会员资格。
- `Panel`：与 `Domain` 对齐的不可变数字按资产时间数据。
- `CategoryPanel`：与 `Domain` 对齐的不可变时间资产标签数据。
- `Graph`：由 Transformer 和 Composer 生成的惰性派生逻辑。

```python
from bagelquant_core import CategoryPanel, Domain, Graph, Panel
```

## 变形金刚

Transformer 接受一个 `Panel` 或 `Graph` 并返回一个 `Graph`。

```python
from bagelquant_core.transformer import rank, winsorize, zscore

factor = rank(zscore(winsorize(raw_panel)), name="factor")
```

生成的变压器参考位于
[`docs/reference/transformers/index.md`](reference/transformers/index.md).

## Composers

Composer 接受一个或多个 `Panel` 或 `Graph` 输入并返回 `Graph`。

```python
from bagelquant_core.composer import div, weighted_sum

ratio = div(book, price, name="book_to_price")
prediction = weighted_sum(ratio, quality, weights=[0.6, 0.4])
```

生成的作曲家参考位于
[`docs/reference/composers/index.md`](reference/composers/index.md).

## 自定义操作

当项目特定的逻辑应该像内置逻辑一样时使用装饰器
运营。

```python
import pandas as pd

from bagelquant_core.composer import composer
from bagelquant_core.transformer import transformer


@transformer
def demean(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.sub(frame.mean(axis=1), axis=0)


@composer
def average(*frames: pd.DataFrame) -> pd.DataFrame:
    return sum(frames) / len(frames)
```

## 兼容性边界

公共 API 是面向 DataFrame 和 `Panel` 的。 `bagelquant-core`不拥有
数据检索、提供商凭证、持久性、组合模拟或
应用程序用户界面。
