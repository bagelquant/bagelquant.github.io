---
layout: page
title: "Architecture And Design"
permalink: /zh/docs/bt/architecture/
lang: zh
ref: "docs-bt-architecture"
alternate_lang_url: /docs/bt/architecture/
nav: docs_zh
---

# 架构 And Design

`bagelquant-bt` 是 DataFrame-first 评估包。

```text
prices + weights/factor scores
    |
    v
input validation
    |
    v
returns, turnover, costs, IC, quantiles
    |
    v
result dataclasses
    |
    v
visualization helpers
```

＃＃ 哲学

- 将研究生成保持在回测器之外。
- 将数据帧视为公共边界。
- 使交易成本明确且可重复。
- 返回结构化结果对象而不是打印报告。
- 将可视化保持为结果对象上的薄层。

## Structure

- `inputs`：框架验证、对齐和数字检查。
- `returns`：资产回报和累积回报效用。
- `costs`：营业额和交易成本计算。
- `engine`：权重回测编排和公共调度。
- `factor`：信息系数、分位数和top-N评估。
- `performance`：汇总指标。
- `results`：用于下游检查的数据类。
- `visualization`：绘图助手。

## 数据 Boundary

输入行是日期，列是资产。重量框架包含目标
重量。 因子框架包含横截面分数。价格框架包含
用于计算回报的数字价格。

该包不导入`bagelquant-data`或`bagelquant-core`；来电者
在评估之前将这些输出调整为数据帧。
