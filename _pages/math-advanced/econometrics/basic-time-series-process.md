---
title: "Basic Time Series Process"
layout: page
permalink: /econometrics/basic-time-series-process/

nav: "econometrics"
---

Econometrics can be divided into two main branches: cross-sectional data analysis and time-series data analysis. We have already discussed cross-sectional data analysis in previous topics. When working with cross-sectional data, issues such as lack of independence or randomness in error terms (especially autocorrelation) and heteroscedasticity may arise. Time-series data analysis provides tools to address these challenges.

Time-series analysis is a statistical technique focused on data collected over time, often called trend analysis. Time series data consists of observations recorded at specific time intervals. There are three main types of data:

1. **Time series data**: Observations of a variable at different points in time.
2. **Cross-sectional data**: Observations collected at a single point in time across different entities.
3. **Pooled data**: A combination of time series and cross-sectional data.

## Basic Definitions

### White Noise

A random process $\{\epsilon_t\}$ is called white noise if $E(\epsilon_t) = 0$ and $E(\epsilon_t^2) = \sigma^2$ for all $t$, and $E(\epsilon_t \epsilon_s) = 0$ for all $t \neq s$.

### Strictly Stationary Process

A random process $\{y_t\}$ is strictly stationary if the joint distribution of $y_{t}, y_{t+1}, ..., y_{t+k}$ is the same as that of $y_{t+e}, y_{t+1+e}, ..., y_{t+k+e}$ for any $k$ and $e$ within the domain of the process.

### Weakly Stationary Process

A random process $\{y_t\}$ is weakly stationary if $E(y_t)$ is constant for all $t$, $Var(y_t)$ is constant for all $t$, and $Cov(y_t, y_{t+k})$ depends only on $k$ (the lag), not on $t$.

## Examples of Non-Stationary Processes

### Step Function

Consider the process:

$$
y_t = \begin{cases}
\alpha + \epsilon_t & \text{if } t \leq k, \\
\alpha + \beta + \epsilon_t & \text{if } t > k,
\end{cases}
$$

where $\epsilon_t$ is white noise.

Clearly, $E(y_t)$ is not constant for all $t$, so this process is neither strictly nor weakly stationary.

> An example is the interest rate, which may remain constant for a period and then shift to a new level.

### Random Walk

Consider the process:

$$
y_t = y_{t-1} + \epsilon_t,
$$

where $\epsilon_t$ is white noise.

For the mean:

$$
E(y_t) = E(y_{t-1}) + E(\epsilon_t) = E(y_{t-1}) = ... = E(y_0) = y_0.
$$

For the variance:

$$
Var(y_t) = Var(y_{t-1}) + Var(\epsilon_t) = Var(y_{t-1}) + \sigma^2.
$$

$$
Var(y_t) = Var(y_{t-2}) + 2\sigma^2 = ...
$$

Thus, $Var(y_t)$ increases with $t$, so this process is not stationary.

> Stock prices often follow a random walk: today's price equals yesterday's price plus random noise.

## Lag Operator

The lag operator $L$ is defined by:

$$
L y_t = y_{t-1}.
$$

The lag operator simplifies time series notation and has the following properties:

**Powers of the lag operator:**

$$L^2 y_t = L(L y_t) = y_{t-2}.$$

**Polynomials in the lag operator:**

$$
a(L) = a_0 + a_1 L + a_2 L^2 + ... + a_n L^n.
$$

$$
a(L) y_t = a_0 y_t + a_1 y_{t-1} + a_2 y_{t-2} + ... + a_n y_{t-n}.
$$

**Products of polynomials:**

$$
a(L) b(L) = (a_0 + a_1 L + ... + a_p L^p)(b_0 + b_1 L + ... + b_q L^q).
$$

**Inverse lag operator:**

$$
(1 - L)^{-1} (1 - L) = 1.
$$

If $|p| < 1$:

$$
(1 - pL)^{-1} = 1 + pL + p^2 L^2 + ...
$$

## Autoregressive Process

An autoregressive process of order $p$, denoted $AR(p)$, is:

$$
a(L) y_t = \epsilon_t,
$$

where $a(L)$ is a polynomial of order $p$.

That is:

$$
\sum_{i=0}^{p} a_i y_{t-i} = \epsilon_t,
$$

or equivalently:

$$
y_t = \alpha_1 y_{t-1} + \alpha_2 y_{t-2} + ... + \alpha_p y_{t-p} + \epsilon_t.
$$

For example, $AR(1)$:

$$
y_t = \alpha_1 y_{t-1} + \epsilon_t.
$$

## Moving Average Process

A moving average process of order $q$, denoted $MA(q)$, is:

$$
y_t = b(L) \epsilon_t,
$$

where $b(L)$ is a polynomial of order $q$.

That is:

$$
y_t = \epsilon_t + \beta_1 \epsilon_{t-1} + \beta_2 \epsilon_{t-2} + ... + \beta_q \epsilon_{t-q}.
$$

For example, $MA(1)$:

$$
y_t = \epsilon_t + \beta_1 \epsilon_{t-1}.
$$

## ARMA Process

An autoregressive moving average process of order $p$ and $q$, denoted $ARMA(p, q)$, is:

$$
a(L) y_t = b(L) \epsilon_t,
$$

where $a(L)$ is of order $p$ and $b(L)$ is of order $q$.

> An intercept term can be added to any of these models.

## Tests for Stationarity

### Dickey-Fuller (ADF) Test

For time series analysis, stationarity is essential; otherwise, results may be spurious. The Dickey-Fuller test checks for stationarity.

- $H_0$: The time series is non-stationary.
- $H_1$: The time series is stationary.

The test statistic is:

$$
ADF = \frac{\hat{\rho}}{SE(\hat{\rho})},
$$

where $\hat{\rho}$ is the estimated coefficient of the lagged dependent variable in the regression of $y_t$ on $y_{t-1}$, and $SE(\hat{\rho})$ is its standard error.

If the ADF statistic is less than the critical value, reject $H_0$ and conclude the series is stationary.

### KPSS Test

The Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test is another test for stationarity.

- $H_0$: The time series is stationary.
- $H_1$: The time series has a unit root (is non-stationary).

The test statistic is:

$$
KPSS = \frac{\sum_{t=1}^{T} S_t^2}{\hat{\sigma}^2},
$$

where $S_t$ is the cumulative sum of the series, and $\hat{\sigma}^2$ is the estimated variance.

> Note: The null and alternative hypotheses are reversed in the KPSS test compared to the ADF test. The KPSS $H_1$ is a unit root process, the opposite of stationarity. These tests may give conflicting results, so it is recommended to use both when checking for stationarity.

## Making Non-Stationary Series Stationary

### Differencing

Differencing transforms a non-stationary series into a stationary one:

$$
\Delta y_t = y_t - y_{t-1}.
$$

This is a first-order difference, which also approximates the derivative.

### Logarithmic Differencing

Logarithmic differencing is another method:

$$
\Delta y_t = \log y_t - \log y_{t-1}.
$$

### Second Differences

$$
\text{dif} (\text{dif}(y_t)) = (y_t - y_{t-1}) - (y_{t-1} - y_{t-2}) = y_t - 2y_{t-1} + y_{t-2}.
$$
