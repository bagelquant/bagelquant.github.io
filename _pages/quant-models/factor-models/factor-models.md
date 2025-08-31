---
title: "Factor Models"
permalink: /factor-models/
sidebar:
    nav: "factor-models"
---

In asset pricing, there are two main approaches: equilibrium models and arbitrage pricing models.

Equilibrium models are based on the idea that if everyone acts rationally in their own best interest, the market will reach an equilibrium. These models typically require certain assumptions, and under those assumptions, we can derive equilibrium prices.

Arbitrage pricing models, on the other hand, are founded on the principle that if there is a mispricing in the market, arbitrageurs will exploit it, causing prices to adjust and eliminate the arbitrage opportunity. A well-known example is the Black-Scholes model, which is used to price options.

In this section, we begin with the equilibrium approach to derive the Capital Asset Pricing Model (CAPM), then discuss the Arbitrage Pricing Theory (APT), and finally move on to factor models. While the models themselves are conceptually straightforward, as quants, it is important to understand the derivation process and analytical structure behind them. This knowledge enables us to construct our own models and implement them in real-world portfolio management.

## Short Introduction to CAPM

The CAPM uses the market return as the sole factor to explain the expected return of an asset:

$$
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
$$

where $E(R_i)$ is the expected return of asset $i$, $R_f$ is the risk-free rate, $\beta_i$ is the sensitivity of the asset's return to the market return, and $E(R_m)$ is the expected return of the market.

How do we establish this relationship? Why does this model make sense? In the CAPM section below, we will explore the derivation of the CAPM using the equilibrium approach and discuss its underlying assumptions.

## Short Introduction to Factor Models

Factor models aim to explain the return of an asset based on a set of factors. If the relationship is linear, we can use linear regression to estimate the parameters:

$$
E(R_i) = \alpha + \beta_1 F_1 + \beta_2 F_2 + ... + \beta_n F_n
$$

where $E(R_i)$ is the expected return of asset $i$, $\alpha$ is the intercept, $\beta_1, \beta_2, ..., \beta_n$ are the factor loadings, and $F_1, F_2, ..., F_n$ are the factors.

> The CAPM can be viewed as a special case of factor models, with the market return as the only factor.

These factors can include macroeconomic variables such as interest rates, inflation, or other market indices, as well as company-specific variables like earnings growth, dividend yield, or financial ratios. For example, the Fama-French 3-factor model (1992) is written as:

$$
E(R_i) = R_f + \beta_1 (E(R_m) - R_f) + \beta_2 SMB + \beta_3 HML
$$

where:

- $E(R_i)$ is the expected return of asset $i$.
- $R_f$ is the risk-free rate.
- $(E(R_m) - R_f)$ is the market risk premium.
- $SMB$ (Small minus Big) is the size factor, capturing the return difference between small and large firms.
- $HML$ (High minus Low) is the value factor, capturing the return difference between high and low book-to-market firms.

The Fama-French 3-factor model extends the CAPM by adding two additional factors to better explain expected returns. It suggests that small firms and value firms tend to outperform large firms and growth firms, respectively.

This section provides a comprehensive overview of factor models from academic and theoretical perspectives. It covers the key concepts, methodologies, and empirical findings related to factor models, offering a solid foundation for understanding their application in finance.

You could navigate all topics at left sidebar.

Other related reads:

1. A more practical approach example of factor model implementation can be found in the [Factor Model in China Stock Market](https://bagelquant.com/factor-model-in-china/) project.
2. A comprehensive literature review on factor models can be found in the [Factor Models Literature Review](https://bagelquant.com/factor-models-literature-review/) post.
