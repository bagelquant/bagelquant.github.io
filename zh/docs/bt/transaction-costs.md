---
layout: page
title: "交易成本"
permalink: /zh/docs/bt/transaction-costs/
lang: zh
ref: "docs-bt-transaction-costs"
alternate_lang_url: /docs/bt/transaction-costs/
nav: docs_zh
---

# 交易成本

默认成本模型为：

```python
TransactionCostConfig(rate=0.00015, min_fee=5.0)
```

即每笔交易资产 0.015%，每笔交易资产的最低费用为 5.0。

＃＃ 计算

对于每个日期和资产：

```text
delta_weight = abs(current_weight - previous_weight)
traded_notional = delta_weight * portfolio_value_before_trade
raw_fee = traded_notional * rate
fee = max(raw_fee, min_fee) when traded_notional > 0
```

每日总费用在交易前除以组合价值：

```text
cost_return = total_fee / portfolio_value_before_trade
net_return = gross_return - cost_return
```

具有成本意识的组合价值使用净回报随着时间的推移而复合。

## 结果字段

`BacktestResult.transaction_costs` contains:

- `traded_asset_count`
- `traded_notional`
- `raw_fee`
- `min_fee_adjustment`
- `total_fee`
- `cost_return`

每次回测都包括总的无成本结果和净成本调整结果。
