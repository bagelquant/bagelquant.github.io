---
layout: page
title: "Transformer"
permalink: /zh/docs/core/transformer/
lang: zh
ref: "docs-core-transformer"
alternate_lang_url: /docs/core/transformer/
nav: docs_zh
---

# 变压器

## 概览

变压器是一元函数式的操作：

```text
Panel | Graph -> Graph
```

为每个公众提供签名、参数描述和示例
操作见[transformer reference](../reference/transformers/index.md)。

## 内置变压器

```python
from bagelquant_core.transformer import (
    rank,
    rolling_mean,
    signed_log1p,
    winsorize,
    zscore,
)

factor = rank(zscore(winsorize(raw_factor)), name="factor")
smoothed = rolling_mean(factor, window=20, name="smoothed")
compressed = signed_log1p(smoothed, name="compressed")
```

内置函数按行为分组：

|家庭|变形金刚|
| --- | --- |
| Basic | `identity`, `abs_value`, `negate`, `diff`, `pct_change` |
|缺失值 | `fillna`、`fillna_zero`、`ffill`、`bfill` |
|更换| `replace_non_nan`、`non_nan_to_one`、`non_nan_to_zero` |
| Rolling | `rolling_mean`, `rolling_std`, `rolling_min`, `rolling_max`, `rolling_sum`, `ewm_mean`, `ewm_std`, `ewm_var` |
| Power | `power`, `signed_power`, `sqrt` |
|对数| `log`、`log1p`、`signed_log1p` |
|标准化| `rank`、`zscore`、`winsorize`、`min_max_scale` |
| Category | `category_demean`, `category_mean`, `category_rank`, `category_zscore` |
| General | `nonnans`, `notnan`, `denoise`, `posonly`, `negonly`, `lag`, `delta`, `rate_of_change`, `remove_repeated`, `date_age_constraint`, `notnan`0, `notnan`1 |
|翻译 | `demean`、`translate_to_pos` |
| Rank | `rankpct`, `nrank`, `logrank` |
| Outliers | `truncate`, `trim`, `trim_quantile` |
|方差稳定| `boxcox`、`anscombe`、`freeman`、`fisher` |
|三角| `sin`、`cos`、`arcsin`、`arccos`、`trig`、`arctanh`、`arctan` |
|凯利准则| `kelly`、`kelly_nonan_standardize`、`kelly_rank_boxcox`、`kelly_rescaling_weight` |

## Basic

基本操作是逐元素的或在代表时间的行上运行：

|变压器|行为 |
| --- | --- |
| `identity(source)` |返回输入值不变。 |
| `abs_value(source)` |返回绝对值。 |
| `negate(source)` |负值。 |
| `diff(source, periods=1)` |计算一段时间内的差异。 |
| `pct_change(source, periods=1)` |计算随时间变化的分数，例如价格面板的回报。 |

## 缺失值

缺失值操作保留面板形状：

|变压器|行为 |
| --- | --- |
| `fillna(source, value=0)` |用数字标量填充 `NaN` 值。 |
| `fillna_zero(source)` |用零填充 `NaN` 值。 |
| `ffill(source, limit=None)` |随着时间的推移向前填充。 |
| `bfill(source, limit=None)` |随着时间的推移向后填充。 |

`ffill` 和 `bfill` 接受可选的正 `limit`。

＃＃ 替代品

替换操作保留缺失值并替换现有值：

|变压器|行为 |
| --- | --- |
| `replace_non_nan(source, value=...)` |将每个非 `NaN` 值替换为数字标量。 |
| `non_nan_to_one(source)` |将每个非 `NaN` 值替换为 1。 |
| `non_nan_to_zero(source)` |将每个非 `NaN` 值替换为零。 |

这些操作对于可用性掩模和持续曝光非常有用。

## Rolling

滚动操作在代表时间的行上运行：

|变压器|行为 |
| --- | --- |
| `rolling_mean(source, window, min_periods=None)` |滚动算术平均值。 |
| `rolling_std(source, window, min_periods=None, ddof=1)` |滚动标准差。 |
| `rolling_min(source, window, min_periods=None)` |滚动最小值。 |
| `rolling_max(source, window, min_periods=None)` |滚动最大值。 |
| `rolling_sum(source, window, min_periods=None)` |滚动总和。 |
| `ewm_mean(source, ...)` |熊猫指数加权平均值。 |
| `ewm_std(source, ...)` | Pandas 指数加权标准差。 |
| `ewm_var(source, ...)` | Pandas 指数加权方差。 |

EWM 操作遵循 pandas 语义，并且只需要一个衰减参数：
`com`、`span`、`halflife` 或 `alpha`。他们还接受 `min_periods`，
`adjust` 和 `ignore_na`。 `ewm_std` 和 `ewm_var` 另外接受 `bias`。

## Power

|变压器|行为 |
| --- | --- |
| `power(source, exponent)` |将值提高到指数。 |
| `signed_power(source, exponent)` |将绝对值提高为指数，同时保留符号。 |
| `sqrt(source)` |计算平方根，对于负值返回 `NaN`。 |

## 对数

|变压器|行为 |
| --- | --- |
| `log(source)` |计算自然对数，对于非正值返回 `NaN`。 |
| `log1p(source)` |计算 `log(1 + value)`，对于等于或低于 `-1` 的值返回 `NaN`。 |
| `signed_log1p(source)` | Calculate `sign(value) * log(1 + abs(value))`. |

## 标准化

规范化操作跨列运行，这些列代表资产：

|变压器|行为 |
| --- | --- |
| `rank(source)` |计算每行的百分位数排名。 |
| `zscore(source)` |计算每行的 z 分数。 |
| `winsorize(source, lower=0.01, upper=0.99)` |将每一行剪切到其分位数边界。 |
| `min_max_scale(source)` |将每行缩放至 `[0, 1]`。 |
| `normalize(source)` |将每行缩放至 `[-1, 1]`。 |
| `net_scale(source)` |按正值和负值的行总和独立缩放正值和负值。 |

常量行生成未定义标准化的 `NaN` 值。

## 扩展滚动操作

滚动系列还包括 `rolling_var`、`rolling_skew`、`rolling_kurt`、
`rolling_median`, `rolling_rank`, `rolling_percentile`, and `rolling_zscore`.
`rolling_ewm` 和 `rolling_ew_std` 是半衰期兼容的别名
通用 EWM 操作，而 `rolling_ewm_fw` 则呈指数级扩展
加权平均值。

## Category

类别操作接受数字源和匹配的 `CategoryPanel`。
类别面板可能包含行业、部门或国家等字符串
labels:

```python
import pandas as pd

from bagelquant_core import CategoryPanel
from bagelquant_core.transformer import category_demean, category_rank

industry = CategoryPanel.from_domain(
    pd.DataFrame(...),
    domain,
    name="industry",
)

industry_neutral = category_demean(raw_factor, industry)
industry_ranked = category_rank(raw_factor, industry)
```

|变压器|行为 |
| --- | --- |
| `category_demean(source, categories)` |减去每行中的每个类别平均值。 |
| `category_mean(source, categories)` |将值替换为每行中的类别平均值。 |
| `category_rank(source, categories)` |计算每个类别和行内的百分位数排名。 |
| `category_zscore(source, categories)` |计算每个类别和行内的 z 分数。 |

虽然类别操作是用变压器导出的，但它们消耗了两个
对齐输入并在内部表示为多输入图节点。

## 用户定义的变压器

```python
import pandas as pd

from bagelquant_core.transformer import transformer


@transformer
def demean(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.sub(frame.mean(axis=1), axis=0)


centered = demean(price, name="centered")
```

修饰函数在执行期间接收 `DataFrame`，但接受
当研究人员构建工作流程时为 `Panel` 或 `Graph`。

配置参数存储在图形规范和缓存键中。
