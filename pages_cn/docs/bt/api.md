---
layout: page
title: "API"
permalink: /zh/docs/bt/api/
lang: zh
ref: "docs-bt-api"
alternate_lang_url: /docs/bt/api/
nav: docs_zh
---

# API

## `run_backtest`

```python
run_backtest(signal, prices, *, kind, config=None)
```

分派到正确的评估路径。

- `kind="weights"` calls `run_weight_backtest`
- `kind="factor"` calls `run_factor_evaluation`

需要 `config`，因为交易成本最低费用要求
`initial_capital`.

## `run_weight_backtest`

```python
run_weight_backtest(weights, prices, *, config)
```

将 DataFrame 评估为组合权重。

返回值 `BacktestResult`.

重要字段：

- `weights`
- `asset_returns`
- `gross_returns`
- `net_returns`
- `gross_cumulative_returns`
- `net_cumulative_returns`
- `gross_value`
- `net_value`
- `turnover`
- `transaction_costs`
- `summary`

## `run_factor_evaluation`

```python
run_factor_evaluation(factor, prices, *, config)
```

将数据帧评估为因子分数。

返回值 `FactorEvaluationResult`.

重要字段：

- `factor`
- `forward_returns`
- `ic`
- `ic_mean`
- `ic_std`
- `icir`
- `quantile_returns`
- `quantile_cumulative_returns`
- `top_minus_bottom`
- `top_n_weights`
- `top_n_backtest`

## Config

```python
BacktestConfig(
    initial_capital=1_000_000,
    transaction_cost=TransactionCostConfig(rate=0.00015, min_fee=5.0),
    annualization=252,
    ic_method="spearman",
    quantiles=5,
    top_n=50,
)
```

`initial_capital` 必须为正。

`ic_method` may be `"spearman"` or `"pearson"`.

## 数据帧边界

第一个参数必须是数字 `pandas.DataFrame`。

行是日期，列是资产，值是权重或因子分数。
