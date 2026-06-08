---
layout: page
title: "Internal Documentation"
permalink: /zh/docs/bt/internals/
lang: zh
ref: "docs-bt-internals"
alternate_lang_url: /docs/bt/internals/
nav: docs_zh
---

# 内部文档

本页为维护者描述了实施细节。

## 重量回测流量

```text
validate weights and prices
    |
    v
align to common dates/assets
    |
    v
compute asset returns
    |
    v
compute gross portfolio returns
    |
    v
compute turnover and transaction costs
    |
    v
build BacktestResult
```

权重被解释为每个时间戳的目标权重。成本模型
使用权重变化和资本来估计名义交易。

## 因子评估 Flow

```text
validate factor and prices
    |
    v
compute forward returns
    |
    v
compute cross-sectional IC
    |
    v
compute quantile returns
    |
    v
build top-N weights
    |
    v
run nested weight backtest
```

嵌套的top-N回测重用了相同权重的回测引擎，这使得
成本和性能行为一致。

## 验证原则

对于非 DataFrame 输入、重复轴、
非数字值、空交叉点、无效配置值和不受支持
派遣种类。错误消息应命名有问题的输入。

## 可视化

绘图助手应该使用结果对象并返回 matplotlib 对象。
他们不应重新计算性能指标或改变结果数据。
