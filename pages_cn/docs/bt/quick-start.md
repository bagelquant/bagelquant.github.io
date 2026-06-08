---
layout: page
title: "快速开始"
permalink: /zh/docs/bt/quick-start/
lang: zh
ref: "docs-bt-quick-start"
alternate_lang_url: /docs/bt/quick-start/
nav: docs_zh
---

# 快速开始

`bagelquant-bt` 评估研究成果。它不检索数据，并且
不产生因子信号。输入是数字 pandas DataFrame。

## Install

```bash
uv add bagelquant-bt
```

## Weight 回测

当信号帧已包含组合权重时，请使用 `kind="weights"`。
行是日期，列是资产，值是目标权重。

```python
from bagelquant_bt import BacktestConfig, run_backtest

result = run_backtest(
    weights,
    prices,
    kind="weights",
    config=BacktestConfig(initial_capital=1_000_000),
)

result.summary
result.net_cumulative_returns
```

## 因子评估

当第一帧包含横截面因子分数时使用 `kind="factor"`。
该软件包计算前向回报、信息系数、分位数
返回，以及前 N 个回测。

```python
from bagelquant_bt import BacktestConfig, run_backtest

result = run_backtest(
    factor_scores,
    prices,
    kind="factor",
    config=BacktestConfig(
        initial_capital=1_000_000,
        quantiles=5,
        top_n=50,
    ),
)

result.ic_mean
result.top_minus_bottom
```

## 交易成本

```python
from bagelquant_bt import BacktestConfig, TransactionCostConfig

config = BacktestConfig(
    initial_capital=1_000_000,
    transaction_cost=TransactionCostConfig(rate=0.00015, min_fee=5.0),
)
```

最低费用需要 `initial_capital`，以便引擎可以转换重量
营业额转化为名义交易额。
