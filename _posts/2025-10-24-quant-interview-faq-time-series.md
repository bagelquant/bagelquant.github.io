---
title: "Quant Interview FAQ — Time Series Modeling"
layout: post
header:
  overlay_image: /assets/images/headers/time-series-header.png
  overlay_filter: 0.8
excerpt: "An interview-focused overview of time series analysis — from ARIMA and GARCH models to stationarity, autocorrelation, and forecasting diagnostics."
---

Time series modeling is at the heart of quantitative finance — from forecasting volatility and returns to estimating risk and building alpha models. Many interview questions test whether you understand not just how to fit an ARIMA or GARCH model, but also *why* and *when* to use them.

### 1. What is a time series and why is it different from cross-sectional data?

**Short Answer:**  
A time series is a sequence of data points observed over time (e.g., daily returns, prices, interest rates), where observations are **not independent** — they often exhibit trends, cycles, and autocorrelation.

**Key Difference:**  

- **Cross-sectional:** Different entities at one time (e.g., stock returns on the same day).  
- **Time-series:** Same entity over time (e.g., return history of a stock).

**Quant Implication:**  
Because of serial dependence, standard OLS assumptions (like iid errors) often fail — requiring specialized models like ARIMA or GARCH.

### 2. What is stationarity and why is it important?

**Definition:**  
A process $\{y_t\}$ is *weakly stationary* if:
$$
E[y_t] = \mu, \quad Var(y_t) = \sigma^2, \quad Cov(y_t, y_{t-k}) = \gamma_k
$$
for all $t$.

**Why It Matters:**  
Many statistical models (ARIMA, VAR) assume constant mean and variance. Non-stationary data (like prices) can lead to spurious regression results.

**Common Tests:**  

- Augmented Dickey–Fuller (ADF) test  
  - H0: unit root (non-stationary)
  - H1: stationary
- KPSS test  
  - H0: stationary
  - H1: unit root (non-stationary)
- Phillips–Perron test
  - H0: unit root (non-stationary)
  - H1: stationary

**Fixes:** Differencing, log transformation, or detrending.

### 3. Explain AR, MA, and ARMA models

| Model | Equation | Description |
|:--|:--|:--|
| AR(p) | $y_t = c + \sum_{i=1}^{p}\phi_i y_{t-i} + \epsilon_t$ | Autoregressive: depends on past values. |
| MA(q) | $y_t = c + \sum_{i=1}^{q}\theta_i \epsilon_{t-i} + \epsilon_t$ | Moving average: depends on past shocks. |
| ARMA(p,q) | Combination of AR and MA | Models short-term dependence. |

**Intuition:**  
AR captures persistence in levels, while MA captures shock propagation. Most financial returns are modeled as ARMA with low orders (e.g., AR(1), MA(1)).

### 4. What is an ARIMA model?

**Definition:**  
ARIMA combines autoregression, differencing, and moving average:
$$
ARIMA(p, d, q) \Rightarrow (1 - \phi_1L - \dots - \phi_pL^p)(1 - L)^d y_t = (1 + \theta_1L + \dots + \theta_qL^q)\epsilon_t
$$
where $L$ is the lag operator and $d$ is the differencing order.

**Interpretation:**  

- $p$: number of AR lags  
- $d$: number of differences (to achieve stationarity)  
- $q$: number of MA lags  

**Example:**  
An ARIMA(1,1,1) model is often used for log prices, since differencing removes the trend and models the residual structure.

---

### 5. What is autocorrelation and how do you test it?

**Autocorrelation (ACF):**
$$
\rho_k = \frac{Cov(y_t, y_{t-k})}{Var(y_t)}
$$
**Partial Autocorrelation (PACF):** Measures correlation after removing effects of intermediate lags.

**Testing Tools:**

- ACF/PACF plots for visual inspection  
- Ljung–Box Q-test for serial correlation  

**Rule of Thumb:**  

- ACF tailing off → AR behavior  
- PACF cutting off → AR order identification  

### 6. What is a GARCH model and why is it used?

**Motivation:**  
Volatility in financial returns clusters — periods of high and low variance alternate.

**Model:**  
$$
y_t = \sigma_t \epsilon_t, \quad \epsilon_t \sim N(0,1)
$$

$$
\sigma_t^2 = \omega + \alpha y_{t-1}^2 + \beta \sigma_{t-1}^2
$$
**Interpretation:**  

- $\alpha$: short-term reaction to shocks  
- $\beta$: persistence of volatility  
- $(\alpha + \beta)$ close to 1 → high volatility persistence  

**Extensions:**  
EGARCH (asymmetric shocks), GJR-GARCH (leverage effects).

### 7. What is cointegration?

**Concept:**  
Two non-stationary series (e.g., stock prices $A$ and $B$) are cointegrated if a linear combination is stationary:

$$
y_t - \beta x_t = \epsilon_t \quad \text{is stationary.}
$$

**Why It Matters:**  
Even if prices drift, their spread may revert — forming the basis for **statistical arbitrage** and **pairs trading**.

**Tests:**  
Engle–Granger two-step test, Johansen test.

### 8. How do you evaluate forecasting performance?

1. **In-sample fit:** AIC, BIC, log-likelihood.  
2. **Out-of-sample:** RMSE, MAE, MAPE, Diebold–Mariano test.  
3. **Backtesting:** rolling or expanding window evaluation.  
4. **Economic value:** profitability or Sharpe ratio of forecast-based strategy.

**Interview Tip:** Always emphasize *out-of-sample performance* — overfitting is a red flag in modeling.

### 9. What are common pitfalls in time series modeling?

- Overfitting by adding excessive lags  
- Ignoring non-stationarity or structural breaks  
- Misinterpreting correlation as causation  
- Using non-robust errors (heteroskedasticity)  
- Ignoring model stability under regime changes  

**Quant Application:**  
A good time-series model should adapt to market regimes, not just fit historical noise.

### 10. What are advanced extensions?

| Model | Description | Quant Use |
|:--|:--|:--|
| VAR / VECM | Multivariate dynamic systems | Macro and multi-asset modeling |
| State-Space / Kalman Filter | Time-varying parameters | Signal extraction, dynamic betas |
| Regime-Switching Models | Separate behavior by regime | Volatility clustering, crisis modeling |
| Long Memory (ARFIMA) | Slow decay autocorrelation | Volatility persistence |
| LSTM / Transformer | Deep learning for sequences | Forecasting nonlinear time dependencies |

### Summary

Time series models translate noisy market data into structured insight — capturing persistence, volatility, and mean reversion. In quant interviews, understanding how to move from **ARIMA to GARCH to regime-switching** shows both statistical rigor and market intuition.
