---
layout: page
title: "因子评估"
permalink: /zh/docs/bt/factor-evaluation/
lang: zh
ref: "docs-bt-factor-evaluation"
alternate_lang_url: /docs/bt/factor-evaluation/
nav: docs_zh
---

# 因子评估

因子评估将因子数据框视为横截面分数。

分数越高越好。

## IC and ICIR

对于每个日期，`bagelquant-bt` 计算之间的横截面相关性
`t` 日期的因子得分以及从 `t` 到 `t+1` 的资产回报。

默认 IC 方法是 Spearman 等级相关：

```python
BacktestConfig(initial_capital=1_000_000, ic_method="spearman")
```

`icir` is:

```text
mean(IC) / standard_deviation(IC)
```

## Quantile 返回值

每天，资产都会根据因子评分进行排序并分为分位数。

每个分位数回报是资产的等权平均远期回报
那个桶。

顶部-底部差价为：

```text
highest_quantile_return - lowest_quantile_return
```

## TOP N 回测

TOP N 回测将因子得分转换为仅多头等权重：

```text
top N assets each day -> 1 / N weight each
```

由此产生的重量框架通过与重量框架相同的回测引擎
正常的组合权重 DataFrame，包括交易成本。
