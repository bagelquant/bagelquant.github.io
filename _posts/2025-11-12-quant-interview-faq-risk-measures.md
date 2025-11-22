---
title: "Quant Interview FAQ — Risk Measures"
layout: post
header:
  overlay_image: /assets/images/headers/risk-measures-dark.png
  overlay_filter: 0.4
excerpt: "A practical overview of key portfolio risk measures — from VaR and CVaR to drawdown, Sharpe ratio, Sortino, and the Kelly criterion — essential tools for understanding performance under uncertainty."
---

Quantitative finance is built around one central challenge: **how to measure and control risk**. Whether you’re evaluating a portfolio’s downside exposure or comparing risk-adjusted performance, understanding common risk metrics is crucial for both interviews and real-world trading.

### 1. What is Value at Risk (VaR)?

**Definition:**  
Value at Risk estimates the maximum loss over a given time horizon at a specified confidence level.

**Mathematically:**  
For a portfolio return $R_p$,
$$
P(R_p < -VaR_\alpha) = \alpha
$$
Example: A 1-day 95% VaR of \$1 million means there’s a 5% chance the portfolio will lose more than \$1M in a day.

**Methods to estimate:**
1. **Parametric (Variance–Covariance):** assumes normality.
2. **Historical Simulation:** uses empirical distribution of past returns.
3. **Monte Carlo Simulation:** models return distribution via repeated sampling.

**Limitations:**  
VaR ignores tail losses beyond the cutoff and is not subadditive (violates diversification principle).

### 2. What is Conditional Value at Risk (CVaR)?

**Definition:**  
Also called *Expected Shortfall (ES)*, CVaR measures the *average loss* beyond the VaR threshold:
$$
CVaR_\alpha = E[R_p | R_p < -VaR_\alpha]
$$
**Interpretation:**  
While VaR tells you the loss threshold, CVaR tells you the *expected loss when things go wrong*.

**Advantages:**
- Coherent risk measure (satisfies subadditivity).
- Better captures tail risk — especially important for non-normal returns.

**Common in:**  
Stress testing, portfolio optimization under tail constraints.

### 3. What is Maximum Drawdown?

**Definition:**  
The largest peak-to-trough decline in portfolio value over time:
$$
MDD = \max_{t} \left( \frac{P_{peak} - P_{trough}}{P_{peak}} \right)
$$
**Intuition:**  
Represents worst-case cumulative loss an investor would have experienced.

**Usage:**  
- Measures *path-dependent* risk, not just endpoint losses.
- Common in hedge fund reporting and strategy backtests.

**Drawdown-based metrics:**  
- **Calmar Ratio:** $\text{Return} / \text{Max Drawdown}$  
- **Pain Ratio:** $\text{Average Return} / \text{Average Drawdown}$  

### 4. What is the Sharpe Ratio?

**Definition:**  
Measures risk-adjusted return using total volatility as the risk proxy:
$$
Sharpe = \frac{E[R_p - R_f]}{\sigma_p}
$$
**Interpretation:**  
How much excess return you earn per unit of total risk.

**Limitations:**
- Penalizes upside volatility as well as downside.
- Sensitive to non-normal returns and autocorrelation.

**Interview Tip:**  
If asked how to improve Sharpe, mention *position sizing, diversification, and turnover control* — not just maximizing raw return.

### 5. What is the Sortino Ratio?

**Definition:**  
A refinement of Sharpe that penalizes only downside volatility:
$$
Sortino = \frac{E[R_p - R_f]}{\sigma_d}, \quad \sigma_d = \sqrt{E[(\min(R_p - R_f, 0))^2]}
$$
**Intuition:**  
Rewards asymmetric return profiles (strategies with limited downside but high upside).

**Used in:**  
Performance evaluation for options, hedge funds, or asymmetric payoff strategies.

### 6. What is the Kelly Criterion?

**Definition:**  
Maximizes the expected logarithm of wealth (geometric growth rate):
$$
f^* = \frac{p(b+1) - 1}{b}
$$
where:
- $p$: probability of win  
- $b$: odds (profit per unit bet)

**Continuous version:**
$$
f^* = \frac{\mu - r_f}{\sigma^2}
$$
**Intuition:**  
Determines the optimal fraction of capital to invest in a risky asset to maximize long-run growth.

**Pros:**  
- Log-optimal, maximizes compounded returns.  
**Cons:**  
- Highly sensitive to estimation error, can lead to extreme leverage if $\mu/\sigma$ is misestimated.

### 7. How do VaR, CVaR, and Drawdown differ conceptually?

| Measure | Focus | Type | Pros | Cons |
|:--|:--|:--|:--|:--|
| VaR | Threshold loss | Quantile-based | Simple, widely used | Ignores tail losses |
| CVaR | Average tail loss | Tail-based | Coherent, tail-sensitive | Harder to estimate |
| Drawdown | Peak-to-trough | Path-based | Intuitive, dynamic | Not distributional |


### 8. How are these measures applied in practice?

- **Risk management:** daily VaR/CVaR reporting for trading desks.  
- **Portfolio construction:** minimize CVaR or drawdown instead of variance.  
- **Hedge fund analytics:** Sortino and Calmar ratios for performance review.  
- **Trading strategy sizing:** Kelly or fractional Kelly for leverage control.  

**Quant Tip:** Many modern strategies use **CVaR optimization** as a robust alternative to variance-based mean–variance optimization.

### 9. What are coherent risk measures?

A risk measure $\rho(X)$ is **coherent** if it satisfies:
1. **Monotonicity:** If $X_1 \le X_2$, then $\rho(X_1) \ge \rho(X_2)$  
2. **Translation Invariance:** $\rho(X + a) = \rho(X) - a$  
3. **Positive Homogeneity:** $\rho(\lambda X) = \lambda \rho(X)$  
4. **Subadditivity:** $\rho(X + Y) \le \rho(X) + \rho(Y)$  

**VaR** fails subadditivity; **CVaR** satisfies all four — hence it’s coherent.

### 10. How to combine return and risk metrics effectively?

For interviews, emphasize that risk and return are inseparable:
- **Sharpe / Sortino:** Risk-adjusted reward.  
- **VaR / CVaR:** Tail exposure.  
- **Drawdown:** Path-dependent resilience.  
- **Kelly:** Optimal growth under repeated bets.  

In portfolio design, practitioners often balance these through **multi-objective optimization**, e.g. maximizing Sharpe while constraining CVaR and drawdown.

