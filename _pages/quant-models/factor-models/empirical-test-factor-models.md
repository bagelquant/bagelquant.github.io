---
title: "Empirical Test of Single Factor Models"
permalink: /factor-models/empirical-test-factor-models/
sidebar:
    nav: "factor-models"
---

In industry, factor models are primarily evaluated based on their profitability, with practitioners relying on data-driven approaches such as train-test splits, cross-validation, and other techniques to ensure robustness and generalizability. In contrast, academic research focuses on the theoretical properties of factor models, particularly their ability to explain the cross-sectional variation in asset returns.

With this academic perspective, we can formulate hypothesis tests for factor models. The first approach is to test the intercept ($\alpha$) of the factor model: if the model fully explains the cross-sectional variation in asset returns, the intercept should be close to zero (a time-series approach). The second approach involves testing the factor returns ($\lambda$) via cross-sectional regression: if the factor returns are significantly different from zero, the factors are useful in explaining return variation.

Testing a factor model is similar to testing the Capital Asset Pricing Model (CAPM) or conducting single-factor tests. Both time-series and cross-sectional regression methods are commonly used.

## Time-Series Regression Test

**Steps:**

1. **Estimate Factor Returns:** Construct factor-mimicking portfolios using sorting or other techniques to obtain factor returns.
2. **Run Time-Series Regression:**
    - A valid model should have intercepts close to zero.
    - Test the hypothesis $H_0: \alpha_1 = \alpha_2 = \ldots = \alpha_n = 0$ for all $n$ assets.

## Cross-Sectional Regression Test

**Steps:**

1. **Estimate Factor Loadings:**
    - **Example 1:** Use firm characteristics (e.g., size, book-to-market ratio).
    - **Example 2:** Use factor loadings estimated from previous time-series regressions (the "Fama-MacBeth" approach).
        - Note: Here, the time-series regression is used to estimate factor loadings, not to test the model.
2. **Run Cross-Sectional Regression:**
    - For each time period, the regression yields a set of factor returns (one per factor, $1$ to $k$).
    - Assuming independence and identical distribution (i.i.d.), multiple time periods provide multiple observations for estimating factor returns.
    - Use a t-test to determine if the mean factor returns are significantly different from zero.
    - Test the hypothesis $H_0: \lambda_i = 0$ for each factor $i$ ($i = 1, 2, \ldots, k$).

## Comparing Models

All factor models have limitations, but some are more "useful" than others. How can we determine which model is superior?

Barillas and Shanken (2017) suggest that a good factor model should:

- **Explain the Test Assets:** Compare the explanatory power of different models using the same set of assets.
- **Explain Other Models' Factor Returns:** Assess how well one model explains the factor returns of another model.

Several statistical methods can be used to evaluate these aspects:

- **GRS Test (Generalized Regression Specification)**
- **Mean–Variance Spanning:** Huberman and Kandel (1987)
- **$\alpha$-Testing**
- **Bayesian Methods:** Barillas and Shanken (2018)

Next up: [Well known factors and factor models](well-known-factors-and-factor-models.md)
