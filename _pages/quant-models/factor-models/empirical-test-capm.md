---
title: "Derive CAPM"
permalink: /factor-models/empirical-test-capm/
sidebar:
    nav: "factor-models"
---

The CAPM model states:

$$
E(\tilde r_i) - r_f = \beta_i (E(\tilde r_m) - r_f)
$$

where:

- $E(\tilde r_i)$ is the expected return of asset $i$.
- $r_f$ is the risk-free rate.
- $\beta_i$ is the sensitivity of the asset's return to the market return.
- $E(\tilde r_m)$ is the expected return of the market.

> As usual, we use a tilde, as in $\tilde r$, to denote a random variable, and $r$ to denote a deterministic variable. For example, $\tilde r_i$ is the random return of asset $i$, and $r_i$ is the deterministic return of asset $i$.

The model implies:

- The relationship between the expected return of an asset and its beta is linear.
- Beta is a complete measure of the risk of security $i$; no other risk measure is needed.
- The market risk premium is positive, i.e., $E(\tilde r_m) - r_f > 0$.

The CAPM aims to explain the variation in expected returns across different assets; in other words, it is a cross-sectional model. At time $t$, asset $i$ has an intrinsic property $\beta_i$. In a regression sense, $\beta_i$ is an independent variable, the market risk premium is the slope, and the expected return of each asset is the dependent variable.

## Problems with Testing CAPM

When testing the CAPM empirically, we face several challenges:

1. Expected returns are not observable.
2. Errors-in-variables problem: the independent variable $\beta_i$ is not directly observable and must be estimated from historical data. Estimation error affects the regression results.
3. Market portfolio is unobservable: Roll's critique states that the true market portfolio cannot be observed, so we use a proxy (e.g., the S&P 500 index), which may not accurately represent the market portfolio, affecting the results.
4. Conditional information: CAPM assumes beta is constant over time, but in reality, beta may change due to market conditions or firm characteristics, impacting the regression.

As we can see, there is no direct way to obtain either the independent or dependent variable, and estimation error will affect the regression. Several approaches exist to estimate these variables. Below, we discuss the most common approaches to test the unconditional CAPM (i.e., CAPM with constant beta).

## Time-Series Approach

Black, Jensen, and Scholes (1972) proposed a time-series approach to test the CAPM:

1. Estimate beta for each stock.
2. Group stocks into $m$ portfolios (10 in their case) based on beta. Obtain the time series of returns for each portfolio.
3. For each portfolio $i$, run the time-series regression:

$$
r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{m,t} - r_{f,t}) + \epsilon_{i, t},
$$

using observations from $t = 1, 2, ..., T$.

Then test:

$$
H_0: \alpha_0 = \alpha_1 = \dots = \alpha_m = 0.
$$

This approach assumes that $\beta_i$ does not change over time. Each timestamp is an observation, and regression is used to estimate $\beta_i$. If the CAPM holds, $\beta_i$ should be the only factor driving expected return variation, and the joint test of the $\alpha$s should yield zero. Using group-sorted portfolios instead of individual stocks reduces noise and makes $\beta_i$ more stable.

> They concluded that the null hypothesis $H_0$ cannot be rejected.

Time-series regression only provides an estimate of $\beta$s. However, the CAPM describes a cross-sectional effect. In theory, we should use $\beta$s as independent variables in a cross-sectional regression. The cross-section approach first estimates $\beta$s using time-series regression, then uses the estimated $\beta$s as independent variables in a cross-sectional regression for each timestamp $t$.

## Cross-Section Approach (Fama and MacBeth Two-Stage Procedure)

1. Estimate beta for each stock.
2. Sort stocks into $m$ portfolios, then estimate the portfolio betas (same as in the time-series approach).
3. Using the estimated betas as independent variables, run a cross-sectional regression for each timestamp $t$:

$$
r_{i, t} - r_{f, t} = \gamma_{0,t} + \gamma_{1,t}\beta_i + \gamma_{2,t} \beta_i^2 + \gamma_{3,t}s_i + \epsilon_{i, t},
$$

for $i = 1, 2, ..., m$.

4. Repeat steps (1)–(3) for each timestamp $t$. This yields multiple observations for hypothesis testing (each timestamp is an observation):

- $\gamma_0 = 0$
- $\gamma_1 = E(\tilde r_m - r_f)$
- $\gamma_2 = 0$
- $\gamma_3 = 0$

The benefit of the cross-section approach is that it is easy to add more factors to the model. In this case, we add a non-linear effect to the cross-sectional regression.

Their results:

- There is a trade-off between return and risk ($\gamma_1 > 0$).
- The linearity assumption cannot be rejected ($\gamma_2 = 0$).
- The hypothesis that the market portfolio is the only systematic risk for stock returns cannot be rejected.
