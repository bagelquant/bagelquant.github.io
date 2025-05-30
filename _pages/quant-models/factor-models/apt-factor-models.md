---
title: "APT and Factor Models"
permalink: /factor-models/apt-and-factor-models/
sidebar:
    nav: "factor-models"
---

## Arbitrage Pricing Theory (APT)

Either mean-variance analysis or CAPM is an equilibrium model, which means that it assumes that all investors are rational and risk-averse, and they all have the same information and act in their own best interest, and the market will achieve certain equilibrium.

This approach is logically sound, but it requires a lot of strong assumptions, such as some distributional assumptions, or some assumptions about the investors' utility functions, it could lead to some problems in practice. For example, here are some of the potential problems with the CAPM: 1. Existence of transaction cost and other trading frictions
2. Existence of non-tradable assets, e.g. human capital
3. Market portfolio is hard to identify, and it is not a well-defined concept

These problems drive us to look for alternative approaches, such as the Arbitrage Pricing Theory (APT).

APT is a relative pricing model, it is based on the idea that if there is a mispricing in the market, arbitrageurs will take advantage of it, and the price will adjust to eliminate the arbitrage opportunity. APT does not require the assumptions about investor preferences or the distribution of returns, it only requires that there are no arbitrage opportunities in the market.

## Factor Models

With no arbitrage opportunities, two assets with the same risk characteristics should have the same expected return, if not, arbitrageurs will take advantage of the mispricing and drive the price back to equilibrium. This leads us to the concept of factor models, the variation in asset returns may by driven by a set of systematic factors, which are common to all assets. If the expected returns of different assets (cross-sectionally) have a linear relationship with these factors, we can express the expected return of an asset as a linear combination of these factors.

We having $k$ factors, the factor stand for a return(random variable) $f_z$ for $z=1,2,...,k$, for any asset $r_i$, if have a factor loading $b_{iz}$ for factor $z$, we can express the return of asset(random variable) $i$ as a return generating process:

$$
\tilde r_i = E(\tilde r_i) + \sum_{z=1}^k b_{iz} \tilde f_z + \tilde \epsilon_i,
$$

where:

- $\tilde r_i$ is the random return of asset $i$.
- $E(\tilde r_i)$ is the expected return of asset $i$.
- $b_{iz}$ is the factor loading of asset $i$ for factor $z$.
- $\tilde f_z$ is the random return of factor $z$.
- $\epsilon_i$ is the idiosyncratic risk of asset $i$, which is uncorrelated with the factors.

>[!NOTE]
> This equation displays the linear relationship of random variables, below we will discuss the expected return of asset $i$.

We should have:

- $E(\tilde \epsilon_i) = 0$, which means the idiosyncratic risk has no expected return.
- $\tilde f_z$ has a zero mean and variance of 1, $E(\tilde f_z) = 0$ and $E(\tilde f_z^2) = 1$, which means the factors are standardized.
- $E(\tilde epsilon_i \tilde f_z) = 0$, which means the idiosyncratic risk is uncorrelated with the factors.
- $E(\tilde \epsilon_i \tilde \epsilon_j) = 0$, $i \neq j$ which means the idiosyncratic risks of different assets are uncorrelated.
- $E(\tilde f_z \tilde f_w) = 0$, $z \neq w$ which means the factors are uncorrelated.
- $E(\tilde epsilon_i ^2) \equiv s_i^2 < S^2 < \infty$, which means the idiosyncratic risk of asset $i$ is finite and positive, and it is less than some upper bound $S^2$.
- $E(\tilde r_i \tilde r_j) \equiv \sigma_{ij}$

## Expected Return of Asset

The expected return of asset $i$ is:

$$
E(\tilde r_i) = \lambda_0 + \sum_{z=1}^k b_{iz} \lambda_z + v_i.
$$

where:

- $\lambda_0$ is the intercept, it should be the risk-free rate $r_f$.
- $\lambda_z$ is the risk premium of factor $z$

And we have:

- $\sum_{i=1}^n v_i = 0$
- $\sum_{i=1}^n b_{iz} v_i = 0$, for all $z=1,2,...,k$.
- $\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n v_i^2 = 0$, which means the idiosyncratic risk is negligible in the large sample limit.

This is the equation we always see in the factor models, it shows that the expected return of asset $i$ is a linear combination of the risk premiums of the factors, once we figure out the factor loading and the risk premiums of the factors, we can estimate the expected return of asset $i$.

### Arbitrage Condition

If we have n assets with weights $W^n = (w_1, w_2, \ldots, w_n)$, an arbitrage opportunity could be defined as:

1. Zero initial investment, $\sum_{i=1}^n w_i = 0$.
2. Certain payoff as $n$ gets large (zero variance), $lim_{n \to \infty} \sum_{i=1}^n \sum_{j=1}^n w_i w_j \sigma_{ij} = 0$.
3. Positive expected return, $lim_{n \to \infty} \sum_{i=1}^n w_i E(\tilde r_i) > 0$.

## Usage of Factor Models

Now we have a framework to explain the expected return of an asset based on a set of factors, we could:

- Construct out own factor models
- And we could use the factor models to:
    - Predict asset returns -> Investment Strategy -> Portfolio Management
    - Identify mispriced assets -> Arbitrage Opportunities
    - Evaluate the performance of a portfolio
    - Risk Management
    - Construct a well-diversified portfolio

To construct a factor model, we need to identify the factors that drive the returns of the assets. This factors we can found in the literature, reports, or we can construct our own factors based on the data we have. The factors could be macroeconomic variables, industry-specific variables, or company-specific variables.

Normally, we will test:

- Single factor is significant or not,
- Add it to a multi-factor model, jointly test the significance of all factors.

>[!NOTE]
>We will discuss the single factor test in next section, and the multi-factor test in the following sections. Once we have a factor model, we can use it to various purposes, we will discuss the usage of factor models in the later sections, such as portfolio construction, risk management, and performance evaluation.

