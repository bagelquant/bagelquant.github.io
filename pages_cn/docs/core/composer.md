---
layout: page
title: "Composer"
permalink: /zh/docs/core/composer/
lang: zh
ref: "docs-core-composer"
alternate_lang_url: /docs/core/composer/
nav: docs_zh
---

# Composer

## 概览

作曲家是一种多输入函数式操作：

```text
(Panel | Graph, ...) -> Graph
```

为每个公众提供签名、参数描述和示例
操作见[composer reference](../reference/composers/index.md)。

## 内置作曲家

```python
from bagelquant_core.composer import div, mean, weighted_mean

ratio = div(book, price, name="bm_ratio")
consensus = mean(value, quality, momentum, name="consensus")
prediction = weighted_mean(
    value,
    quality,
    momentum,
    weights=[0.4, 0.3, 0.3],
    name="prediction",
)
```

内置函数按行为分组：

|家庭|作曲家 |
| --- | --- |
|算术| `add`、`sub`、`mul`、`div` |
|聚合| `sum_frames`、`mean`、`product`、`minimum`、`maximum`、`weighted_sum`、`weighted_mean` |
| General | `project`, `mask`, `coalesce` |
| Scaling | `vol_scale` |
| Math | `power`, `power_df`, `and_`, `or_`, `not_`, `xand`, `xor`, `greater`, `greater_equal`, `less`, `power_df`0, `power_df`1 |
| Rolling | `rolling_corr`, `rolling_cov`, `rolling_ols`, `rolling_lasso`, `rolling_ridge`, `rolling_elastic_net` |
|横截面| `orthogonalize`、`group_rank`、`group_mean`、`group_max`、`group_min`、`group_median`、`group_std`、`group_demean`、`group_zscore`、`group_rankpct`、`group_rank`0 |

## 用户定义的作曲家

```python
import pandas as pd

from bagelquant_core.composer import composer


@composer
def average(*frames: pd.DataFrame) -> pd.DataFrame:
    return sum(frames) / len(frames)


combined = average(value, quality, momentum, name="combined")
```

内部执行运行时在执行之前对齐输入面板数据
作曲家。已对齐的输入在内部重用。

加权作曲家需要每个输入帧一个数字权重并计算
新框架而不改变他们的输入。 `weighted_mean(...)` 还需要一个
总重量非零。

滚动回归使用 `rolling_ols(y, *factors, window=...)` 和相同的
正则化变体的输入顺序。它们仅适合前面的行，然后预测
当前行。

比较和逻辑作曲家返回数字 `1.0` 和 `0.0` 面板，以便它们
输出仍然有效的图形输入。 `minimum` 和 `maximum` 也导出为
`min` 和 `max`； `sub`、`mul` 和 `div` 导出为 `subtract`，
`multiply`, and `divide`.
