---
title: "Factor Models"
permalink: /factor-models/
layout: splash
header:
  overlay_image: /assets/images/radio-telescope.png
---

For asset pricing model, there are two general approaches: equilibrium and arbitrage pricing models. 

The general idea of equilibrium models if everyone is rational, they will act in their own best interest, the overall market will achieve certain equilibrium, it normally requires some assumptions, and based on the assumptions, we can derive the equilibrium price. 

The arbitrage pricing model is based on the idea that if there is a mispricing in the market, arbitrageurs will take advantage of it, and the price will adjust to eliminate the arbitrage opportunity. A well-known example of an arbitrage pricing model is the Black-Scholes model, which is used to price options.

In this section, we will start will an equilibrium approach to derive the Capital Asset Pricing Model (CAPM), and then we will discuss the Arbitrage Pricing Theory (APT) and moved on to Factor Models. The model itself is quite simple and easy to understand. But as a quant, we need to understand the derivation process and analysis structure behind it, so we can construct our own models, and further implement them in the real world portfolio management.

## Short Intro to CAPM

The CAPM uses the "market returns" as the only factor to explain the expected return of an asset, written as:

$$
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
$$

where $E(R_i)$ is the expected return of asset $i$, $R_f$ is the risk-free rate, $\beta_i$ is the sensitivity of the asset's return to the market return, and $E(R_m)$ is the expected return of the market.

How do we establish this relationship? Why does this model make sense in the first place? In the CAPM section below, we will explore how we derive the CAPM. We are taking an equilibrium approach, and we will also discuss the assumptions behind it.

## Short Intro to Factor Models

Factor models are trying to explain the return of an asset based on a set of factors, if it follows a linear relationship, we can use the linear regression to estimate the parameters as follows:

$$
E(R_i) = \alpha + \beta_1 F_1 + \beta_2 F_2 + ... + \beta_n F_n
$$

where $E(R_i)$ is the expected return of asset $i$, $\alpha$ is the intercept, $\beta_1, \beta_2, ..., \beta_n$ are the factor loadings, and $F_1, F_2, ..., F_n$ are the factors. 

> We could treat the CAPM as a special case of factor models, where we only have one factor, the market return.

These factors can be macroeconomic variables such as interest rates, inflation rates, or other market indices, or company-specific variables such as earnings growth, dividend yield, or other financial ratios. Here is an example of a factor model, Fama-French 3-factor model(1992):

$$
E(R_i) = R_f + \beta_1 (E(R_m) - R_f) + \beta_2 SMB + \beta_3 HML
$$

where:

- $E(R_i)$ is the expected return of asset $i$.
- $R_f$ is the risk-free rate.
- $(E(R_m) - R_f)$ is the market risk premium.
- $SMB$ (Small minus big) is the size factor, which captures the return difference between small and large firms.
- $HML$ (High minus low) is the value factor, which captures the return difference between high and low book-to-market firms.

The Fama-French 3-factor model is an extension of the CAPM, which adds two additional factors to explain the expected return of an asset. The model suggests that small firms and value firms tend to outperform large firms and growth firms, respectively.


## Sections 

- [Derive CAPM](derive-capm.md)


