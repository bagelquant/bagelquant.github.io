---
title: "Quant Interview FAQ — Portfolio Optimization"
layout: post
header:
  overlay_image: /assets/images/headers/portfolio-optimization-dark.png
  overlay_filter: 0.8
excerpt: "From Markowitz mean–variance theory to Black–Litterman and robust optimization frameworks."
---

Portfolio optimization is a cornerstone of modern finance — bridging statistical modeling and decision-making under uncertainty. In quant interviews, it’s a common topic that tests your ability to translate theory into implementable allocation models.

### 1. What is the mean–variance optimization framework?

**Short Answer:**  
Proposed by Harry Markowitz (1952), mean–variance optimization seeks to maximize expected return for a given level of risk — or equivalently, minimize variance for a given expected return.

**Formulation:**
$$
\begin{aligned}
\min_w \quad & w' \Sigma w \\
\text{s.t.} \quad & w' \mu = \mu_p, \quad w' \mathbf{1} = 1
\end{aligned}
$$

**Interpretation:**  
- $w$: portfolio weights  
- $\mu$: vector of expected returns  
- $\Sigma$: covariance matrix of returns  
- $\mu_p$: target portfolio return  

Solving this yields the **efficient frontier**, a curve representing optimal trade-offs between risk and return.

### 2. What is the efficient frontier?

The efficient frontier is the set of portfolios that offers the **highest expected return for each risk level**.  

- Portfolios below the frontier are suboptimal (inefficient).  
- Portfolios above it are **unattainable** given current assets.

When a risk-free asset is introduced, the **Capital Market Line (CML)** becomes the tangent line to the efficient frontier — representing combinations of the risk-free asset and the tangency portfolio.

### 3. What are the main assumptions behind mean–variance optimization?

1. Returns are jointly normally distributed.  
2. Investors care only about mean and variance.  
3. Covariance matrix is stable and accurately estimated.  
4. No transaction costs or short-selling limits (in the simplest version).

**Interview Tip:** Mention that in practice, these assumptions rarely hold — estimation error and non-stationarity are major problems.

### 4. What are common extensions or constraints in optimization?

| Constraint | Description | Impact |
|:--|:--|:--|
| No short selling | $w_i \ge 0$ | Improves interpretability, reduces leverage |
| Leverage cap | $\sum \|w_i\| \le L$ | Controls exposure |
| Turnover limit | $\|w_t - w_{t-1}\| \le \delta$ | Reduces trading cost |
| Sector / asset bounds | $\alpha_i \le w_i \le \beta_i$ | Enforces diversification |

Adding constraints typically converts the quadratic program into a **convex optimization problem**, solvable by standard methods (e.g., CVXOPT).

### 5. What is the Black–Litterman model?

**Motivation:**  
Traditional mean–variance optimization is highly sensitive to expected returns $\mu$. Black–Litterman (1992) incorporates investor *views* into the equilibrium returns implied by the market.

**Framework:**
$$
\mu_{BL} = \pi + \tau \Sigma P'(P \tau \Sigma P' + \Omega)^{-1}(q - P\pi)
$$
where:  
- $\pi$: equilibrium (market-implied) returns  
- $P$: matrix expressing investor views  
- $q$: expected returns from those views  
- $\Omega$: uncertainty in views  
- $\tau$: scaling parameter for prior confidence

**Intuition:**  
It blends prior (market equilibrium) and subjective views into posterior expected returns — producing more stable and diversified allocations.

### 6. What is robust portfolio optimization?

**Concept:**  
Accounts for estimation uncertainty in inputs ($\mu$, $\Sigma$).  
Instead of optimizing for one point estimate, it optimizes for the **worst-case scenario** within a confidence region.

**Formulation:**
$$
\min_w \max_{\mu \in \mathcal{U}} -w'\mu + \lambda w'\Sigma w
$$
where $\mathcal{U}$ is an uncertainty set (e.g., ellipsoidal or box-shaped).

**Effect:**  
- Leads to more conservative portfolios.  
- Reduces sensitivity to noisy data.  
- Often results in lower turnover and higher out-of-sample Sharpe ratio.

### 7. What is risk parity and how does it differ?

**Idea:**  
Allocate capital so that each asset contributes equally to total portfolio risk:
$$
RC_i = w_i (\Sigma w)_i
$$
where $RC_i$ is the risk contribution of asset $i$.

**Contrast:**  
- Mean–variance focuses on returns.
- Risk parity ignores expected returns and balances *risk exposure* instead.

Commonly used in macro and multi-asset strategies.

### 8. How do you evaluate optimized portfolios?

1. **Risk metrics:** volatility, VaR, CVaR, drawdown  
2. **Performance ratios:** Sharpe, Sortino, Information ratio  
3. **Diversification:** Herfindahl–Hirschman Index (HHI)  
4. **Stability:** turnover, sensitivity to input changes  
5. **Out-of-sample backtesting:** rolling optimization window

**Quant Tip:** Interviewers often ask about **robustness** — how you handle instability in covariance or expected returns.

### 9. What are practical issues in implementation?

- Estimation error dominates small-sample covariance estimates.  
- Shrinkage estimators (Ledoit–Wolf) or factor-based covariances help.  
- Transaction costs, liquidity, and execution constraints can’t be ignored.  
- Portfolio rebalancing frequency affects performance and turnover.

### 10. What are modern extensions of portfolio optimization?

| Approach | Description | Example Use |
|:--|:--|:--|
| Bayesian Optimization | Posterior over expected returns | Black–Litterman |
| Machine Learning | Return prediction + robust optimization | Forecast-driven allocation |
| Scenario Optimization | Stress-test under different market regimes | Risk management |
| Hierarchical Risk Parity (HRP) | Tree-based diversification | High-dimensional portfolios |
| Multi-Objective Optimization | Joint risk–return–cost tradeoff | Real-world portfolios |


