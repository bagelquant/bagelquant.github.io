---
title: "Covariance Matrices and Portfolio Risk"
permalink: /probability/covariance-matrices-and-portfolio-risk/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

If you've ever seen a heatmap of correlations across a universe of stocks, you have already met the object that drives most portfolio risk: the **covariance matrix**. It tells you which assets tend to move together and which ones really diversify each other.

Portfolio risk is not just about individual asset volatilities; it is fundamentally driven by **covariances** between assets. The **covariance matrix** summarizes how assets co-move and is central to modern portfolio theory.

## Covariance Matrix

Let $R = (R_1, \dots, R_n)^T$ be a random vector of asset returns with mean vector $\mu$.

The **covariance matrix** $\Sigma$ is the $n \times n$ matrix with entries

$$
\Sigma_{ij} = \operatorname{Cov}(R_i, R_j) = E[(R_i - \mu_i)(R_j - \mu_j)].
$$

Properties:

- $\Sigma$ is symmetric ($\Sigma_{ij} = \Sigma_{ji}$).
- $\Sigma$ is positive semi-definite: for any $w$, $w^T \Sigma w \ge 0$.

## Portfolio Variance

For a portfolio with weight vector $w$ (summing to 1 for a fully invested portfolio), the portfolio return is

$$
R_p = w^T R.
$$

The portfolio mean and variance are:

- $E[R_p] = w^T \mu$,
- $\operatorname{Var}(R_p) = w^T \Sigma w$.

This quadratic form is the foundation of **mean-variance optimization**: choose $w$ to balance expected return and risk. Optimization engines in practice do nothing more mysterious than evaluating and comparing such quadratic forms under different constraints.

## Interpretation of Covariance Terms

Expanding $w^T \Sigma w$:

$$
\operatorname{Var}(R_p) = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \Sigma_{ij}.
$$

This shows how portfolio risk depends on:

- Individual variances $\Sigma_{ii} = \operatorname{Var}(R_i)$,
- Covariances between assets $\Sigma_{ij}$, $i \ne j$.

Diversification benefits arise when covariances (and correlations) between assets are low or negative.

## Estimating Covariance Matrices

In practice, $\Sigma$ is unknown and must be estimated from data, often via the **sample covariance matrix**:

$$
\hat{\Sigma} = \frac{1}{T-1} \sum_{t=1}^T (R_t - \bar{R})(R_t - \bar{R})^T,
$$

where $R_t$ is the return vector at time $t$ and $\bar{R}$ is the sample mean.

High-dimensional estimation (many assets, limited history) introduces challenges, leading to techniques like shrinkage estimators and factor models. Much of practical risk modeling is about taming noisy covariance estimates without losing the key structure they encode.

Next Topic: [Copulas and Modeling Dependence](copulas-and-dependence.md)
