---
title: "Quant Interview FAQ — Backtesting & Performance Evaluation"
layout: post
header:
  overlay_image: /assets/images/headers/backtesting-dark.png
  overlay_filter: 0.4
excerpt: "A practical guide to backtesting and performance evaluation — understanding turnover, slippage, alpha decay, and the mechanics behind robust strategy testing."
---

Backtesting is the backbone of quantitative research. It’s where ideas become data-driven strategies and where many good ideas are filtered out. Interviewers will test your understanding of not just how to run a backtest, but also how to diagnose bias, evaluate performance, and ensure robustness.

### 1. What is backtesting and why is it important?

**Definition:**  
Backtesting is the process of applying a trading strategy to historical data to simulate how it would have performed.

**Purpose:**  
- Validate whether a signal or model has predictive power  
- Estimate returns, risk, and performance stability  
- Diagnose overfitting, assumptions, and hidden biases  

A backtest is only useful if it accurately reflects *realistic trading conditions* — otherwise, it’s just curve-fitting to historical noise.

### 2. What is slippage and why does it matter?

**Definition:**  
Slippage is the difference between the expected execution price and the actual execution price.

**Sources of slippage:**  
- Bid–ask spread  
- Market impact  
- Latency and order queue positioning  
- Rapid price moves after a signal triggers  

**Modeling slippage:**  
Simplified:
$$
\text{Slippage Cost} = \text{Trade Size} \times (\text{Market Price} - \text{Execution Price})
$$

In more advanced setups:
- **Kyle’s lambda model** for impact  
- **Almgren–Chriss** optimal execution framework  
- Volume-based impact models  

**Interview Tip:** Always emphasize that ignoring slippage leads to overly optimistic backtest results.

### 3. What is turnover and how is it computed?

**Definition:**  
Turnover measures how frequently a portfolio’s positions change, representing trading intensity (and thus cost).

**Formula:**
$$
\text{Turnover}_t = \frac{1}{2} \sum_i |w_{i,t} - w_{i,t-1}|
$$

**Interpretation:**  
- High turnover → more trading, more transaction costs  
- Low turnover → more stable portfolio, lower cost  

**Use cases:**
- Constraint in portfolio optimization  
- Metric for execution cost modeling  
- Stability diagnostic for factor strategies  

### 4. What is alpha decay?

**Definition:**  
Alpha decay measures how quickly a signal loses predictive power after it is discovered or after it is generated.

**Types:**
1. **Post-discovery decay:** Alpha degrades as more capital crowds the signal.  
2. **Signal timing decay:** Alpha weakens as execution is delayed.

**Empirical Example:**  
A signal with strong 1-day predictive return may decay to zero by day 3.

**Quantifying alpha decay:**  
Compute IC or return spread over different holding periods:
$$
\text{Decay}(k) = IC_{t+k}
$$

Strategies with slow decay → easier to execute, less sensitive to slippage.  
Fast-decay signals → require low latency and aggressive execution.

### 5. What are the key performance metrics in backtesting?

| Metric | Meaning | Purpose |
|:--|:--|:--|
| CAGR | Annualized return | Long-term growth |
| Volatility | Std. dev. of returns | Measures risk |
| Sharpe Ratio | Excess return per unit risk | Risk-adjusted performance |
| Sortino Ratio | Downside-only version of Sharpe | Asymmetric payoff strategies |
| Max Drawdown | Worst peak-to-trough drop | Tail risk & resilience |
| Calmar Ratio | CAGR / Drawdown | Drawdown-aware performance |
| Hit Rate | % of positive-return trades | Stability |
| Win/Loss Ratio | Avg win ÷ avg loss | Trade distribution |



### 8. What is realistic transaction cost modeling?

Good backtests include:
- **Bid–ask spread cost**  
- **Market impact proportional to trade size**  
- **Variable commissions (based on region/asset)**  
- **Short borrow fees**  
- **Slippage models based on volatility & volume**  

A common simplified model:
$$
\text{Cost} = a \cdot |w_t - w_{t-1}| + b \cdot (|w_t - w_{t-1}|)^2
$$
where \(a\) models linear costs and \(b\) models market impact.

### 9. What makes a backtest “too good to be true”?

Red flags:
- Extremely high Sharpe (>3 in equities)  
- Low drawdown with high return (unrealistic)  
- Zero or near-zero turnover  
- No parameter sensitivity  
- Smooth PnL curve with no volatility  
- Gains persisting across all regimes without explanation  

Interviewers may ask you to critique a “perfect” backtest. Mention:

> “It likely suffers from overfitting, unrealistic assumptions, or hidden data leakage.”

