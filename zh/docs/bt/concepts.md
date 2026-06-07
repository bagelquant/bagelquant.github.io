---
layout: page
title: "概念"
permalink: /zh/docs/bt/concepts/
lang: zh
ref: "docs-bt-concepts"
alternate_lang_url: /docs/bt/concepts/
nav: docs_zh
---

# 概念

## 责任边界

`bagelquant-bt` 有一项工作：根据每日价格评估研究成果。

它不导入 `bagelquant-core` 或 `bagelquant-data`。

- `bagelquant-core` 拥有信号构造和研究逻辑。
- `bagelquant-data` 拥有数据访问和存储。
- `bagelquant-bt` 拥有评估、交易成本、摘要和图表。

这使得回溯测试器对于任何可以产生
按资产划分的日期 `DataFrame`。

## 数据框形状

价格、权重和因子得分使用相同的按资产日期的形状：

```text
index:   daily dates
columns: assets
values:  numeric prices, weights, or factor scores
```

价格被解释为收盘价。

对于权重回测，值是组合权重。负权重是
allowed.

对于细胞因子评估，数值是横截面分数。更高的分数
被认为更适合分位数和 TOP N 测试。

## 计时约定

该包使用无前瞻约定：

```text
weight or factor at date t -> earns close-to-close return from t to t+1
```

这意味着最终价格日期不能产生已实现的远期回报，并且是
从回报计算中删除。

## Alignment

`bagelquant-bt` 通过交叉日期和资产来调整价格和信号值。

It rejects:

- 重复的日期
- 重复资产
- 非数字值
- 空日期重叠
- 空资产重叠
- 非DataFrame信号输入
