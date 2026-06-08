---
layout: page
title: "公开 API"
permalink: /zh/docs/bt/public-api/
lang: zh
ref: "docs-bt-public-api"
alternate_lang_url: /docs/bt/public-api/
nav: docs_zh
---

# 公开 API

稳定的公共API是从`bagelquant_bt`导出的。

## 入口点

```python
from bagelquant_bt import run_backtest, run_factor_evaluation, run_weight_backtest
```

- `run_backtest(signal, prices, *, kind, config=None)`：由 `kind` 调度。
- `run_weight_backtest(weights, prices, *, config)`：评估组合权重。
- `run_factor_evaluation(factor, prices, *, config)`：评估因子分数。

＃＃ 配置

```python
from bagelquant_bt import BacktestConfig, TransactionCostConfig

config = BacktestConfig(
    initial_capital=1_000_000,
    transaction_cost=TransactionCostConfig(rate=0.00015, min_fee=5.0),
    annualization=252,
    ic_method="spearman",
    quantiles=5,
    top_n=50,
)
```

- `initial_capital` 必须为正。
- `ic_method` may be `"spearman"` or `"pearson"`.
- `quantiles` 控制因子桶计数。
- `top_n` 控制 top-N 因子组合。

## Results

`BacktestResult` exposes:

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

`FactorEvaluationResult` exposes:

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

## 例外情况

- `BagelQuantBacktestError`：基础包错误。
- `BacktestConfigError`：无效配置。
- `InputValidationError`：输入帧无效或不兼容。
