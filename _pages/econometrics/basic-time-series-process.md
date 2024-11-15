---
title: "Basic Time Series Process"
permalink: /econometrics/basic-time-series-process/
sidebar:
  nav: "econometrics"
---

Econometric could be devided into two main branches: cross-sectional data analysis and time-series data analysis. We already discussed the cross-sectional data analysis in the previous topics. When dealing with cross-sectional data, we could face possible issues like no independence or randomness of error terms (in particular, autocorrelation), heteroscedasticity. Time-series data analysis could be a solution to these issues.

Time-series data analysis is a statistical technique that deals with time series data, or trend analysis. Time series data means that data is in a series of particular time periods or intervals. The data is considered in three types:

1. **Time series data**: A set of observations on the values that a variable takes at different times.
2. **Cross-sectional data**: Data collected at the same point in time.
3. **Pooled data**: A combination of time series data and cross-sectional data.

## 4.1 Basic Definitions

### White Noise

Random process ${\epsilon_t}$ is called white noise if $E(\epsilon_t) = 0$ and $E(\epsilon_t^2) = \sigma^2$ for all $t$ and $E(\epsilon_t \epsilon_s) = 0$ for t, s = 0, 1, 2, ..., t ≠ s.

### Strictly Stationary Process

Random process ${y_t}$ is said to be strictly stationary if the joint distribution of $y_{t}, y_{t+1}, ..., y_{t+k}$ is the same as that of $y_{t+e}, y_{t+1+e}, ..., y_{t+k+e}$ for any k, e within the domain of the process.

### Weakly Stationary Process

Random process ${y_t}$ is said to be weakly stationary if the $E(y_t)$ is constant for all t, $Var(y_t)$ is constant for all t, and $Cov(y_t, y_{t+k})$ is constant for all t and k, within the domain of the process.

## 4.2 Example of non-stationary process

### Step Function

Consider the following process:

$$
y_t = \begin{cases}
\alpha + \epsilon_t & \text{if } t \leq k, \\
\alpha + \beta + \epsilon_t & \text{if } t > k,
\end{cases}
$$

where $\epsilon_t$ is white noise.

clearly, $E(y_t)$ is not constant for all t, so this process is neither strictly nor weakly stationary.

> Interest rate could be a good example of this process. The interest rate is constant for a period of time, then it changes to another constant rate.

### Random Walk

Consider the following process:

$$
y_t = y_{t-1} + \epsilon_t,
$$

where $\epsilon_t$ is white noise.

For $E(y_t)$:

$$
E(y_t) = E(y_{t-1}) + E(\epsilon_t) = E(y_{t-1}) = E(y_{t-2}) = ... = E(y_0) = y_0.
$$

For $Var(y_t)$:

$$
Var(y_t) = Var(y_{t-1}) + Var(\epsilon_t) = Var(y_{t-1}) + \sigma^2.
$$

$$
Var(y_t) = Var(y_{t-2}) + \sigma^2 + \sigma^2 = Var(y_{t-2}) + 2\sigma^2.
$$

Clearly, $Var(y_t)$ is depends on t, so this process is neither strictly nor weakly stationary.

> Stock price could be a good example of this process. The stock price today could be the stock price yesterday plus some random noise.

## 4.3 Lag Operator

The lag operator $L$ is defined as:

$$
L y_t = y_{t-1}.
$$

The lag operator could be used to simplify the notation of time series models, it has the following properties:

**Power the lag operator**

$$L^2 y_t = L(L y_t) = L y_{t-1} = y_{t-2}.$$

**Polynomials in the lag operator**

$$
a(L) = a_0 + a_1 L + a_2 L^2 + ... + a_n L^n.
$$

$$
a(L) y_t = a_0 y_t + a_1 y_{t-1} + a_2 y_{t-2} + ... + a_n y_{t-n}.
$$

**products of polynomials in the lag operator**

$$
a(L) b(L) = (a_0 + a_1 L + a_2 L^2 + ... + a_p L^p)(b_0 + b_1 L + b_2 L^2 + ... + b_q L^q).
$$

**Some lag operators can be inverted, we define the $(1 - L)^{-1}$ operator as**:

$$
(1 - L)^{-1} (1 - L) = (1 - L)(1 - L)^{-1} = 1.
$$

if $\|p\| < 1$, then:

$$
(1 - pL)^{-1} = 1 + pL + p^2 L^2 + ...
$$

## 4.4 Autoregressive Process

The autoregressive process of order p, denoted as $AR(p)$, is defined as:

$$
a(L) y_t = \epsilon_t,
$$

where $a(L)$ is of order p.

That is:

$$
\sum_{i=0}^{p} a_i y_{t-i} = \epsilon_t,
$$

we can change the coefficients, and rewrite the $AR(p)$ process as:

$$
y_t = \alpha_1 y_{t-1} + \alpha_2 y_{t-2} + ... + \alpha_p y_{t-p} + \epsilon_t.
$$

For example, the $AR(1)$ process is:

$$
y_t = \alpha_1 y_{t-1} + \epsilon_t.
$$

## 4.5 Moving Average Process

The moving average process of order q, denoted as $MA(q)$, is defined as:

$$
y_t = b(L) \epsilon_t,
$$

where $b(L)$ is of order q.

That is:

$$
y_t = \epsilon_t + \beta_1 \epsilon_{t-1} + \beta_2 \epsilon_{t-2} + ... + \beta_q \epsilon_{t-q}.
$$

For example, the $MA(1)$ process is:

$$
y_t = \epsilon_t + \beta_1 \epsilon_{t-1}.
$$

## 4.6 ARMA Process

The autoregressive moving average process of order p and q, denoted as $ARMA(p, q)$, is defined as:

$$
a(L) y_t = b(L) \epsilon_t,
$$

where $a(L)$ is of order p, and $b(L)$ is of order q.


> For all this models, an intercept term could be added.

## 4.7 Tests for Stationarity

### DF(ADF) Test

For time series analysis, we require the data to be stationary, otherwise, the results could be spurious. The Dickey-Fuller test is a statistical test to check the stationarity of a time series.

The hypotheses of the Dickey-Fuller test are:

$$
H_0: \text{The time series is non-stationary.}
$$

$$
H_1: \text{The time series is stationary.}
$$

The test statistic is:

$$
\text{ADF} = \frac{\hat{\rho}}{SE(\hat{\rho})},
$$

where $\hat{\rho}$ is the estimated coefficient of the lagged dependent variable in the regression of $y_t$ on $y_{t-1}$, and $SE(\hat{\rho})$ is the standard error of the estimated coefficient.

If the ADF statistic is less than the critical value, we reject the null hypothesis and conclude that the time series is stationary.

### KPSS Test

Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test is another test for stationarity. The hypotheses of the KPSS test are:

$$
H_0: \text{The time series is stationary.}
$$

$$
H_1: \text{The time series is unit-root process.}
$$

The test statistic is:

$$
\text{KPSS} = \frac{\sum_{t=1}^{T} S_t^2}{\hat{\sigma}^2},
$$

where $S_t$ is the cumulative sum of the time series, and $\hat{\sigma}^2$ is the estimated variance of the time series.

> Note that the null and alternative hypotheses are reversed in the KPSS test compared to the ADF test. Also the H1 of the KPSS test is a unit-root process, which is the opposite of stationarity.

> Theses tests could conflict with each other, so it is recommended to use both tests to check the stationarity of the time series.

## 4.8 Conversion of Non-Stationary to Stationary

### Differencing

Differencing is a method to convert a non-stationary time series to a stationary time series. The differenced series is defined as:

$$
\Delta y_t = y_t - y_{t-1}.
$$

This is a first-order difference, also approximating the derivative of the time series.

### Logarithmic Differencing

Logarithmic differencing is another method to convert a non-stationary time series to a stationary time series. The logarithmic differenced series is defined as:

$$
\Delta y_t = \log y_t - \log y_{t-1}.
$$

### 2-nd derivatives approximation

$$
\text{dif}(\text{dif}(y_t)) = (y_t - y_{t-1}) - (y_{t-1} - y_{t-2}) = y_t - 2y_{t-1} + y_{t-2}.
$$

## 4.9 ARIMA-GARCH Model

The Autoregressive Integrated Moving Average-Generalized Autoregressive Conditional Heteroskedasticity (ARIMA-GARCH) model is a combination of the ARIMA model and the GARCH model. The ARIMA model is used to model the time series, and the GARCH model is used to model the volatility of the time series.

The ARIMA-GARCH model is defined as:

$$
y_t = x_t + \epsilon_t,
$$

where:

- {$y_t$} is the time series,
- {$x_t$} mean reverting process,
- {$\epsilon_t$} is the error term,

and:

$$
\epsilon_t = \sigma_t z_t, \quad z_t \sim D(0, 1),
$$

- $D(0, 1)$ is a distribution with mean 0 and variance 1, e.g., the standard normal distribution,
- $\sigma_t$ is the time-varying volatility that follows ARMA model,

$$
\sigma_t^2 = \omega + \alpha_1 \epsilon_{t-1}^2 + \alpha_2 \epsilon_{t-2}^2 + ... + \beta_1 \sigma_{t-1}^2 + \beta_2 \sigma_{t-2}^2 + ....
$$

