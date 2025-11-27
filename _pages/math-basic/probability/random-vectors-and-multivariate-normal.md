---
title: "Random Vectors and Multivariate Normal"
permalink: /probability/random-vectors-and-multivariate-normal/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

Real portfolios rarely live in one dimension. Even the simplest equity book juggles dozens of stocks, factors, and risk drivers at once. When you look at a risk report with a covariance matrix and factor exposures, you are implicitly thinking in terms of **random vectors** and their joint distribution.

**Random vectors** and the **multivariate normal distribution** provide a natural mathematical framework for these multi-dimensional problems.

## Random Vectors

An $n$-dimensional **random vector** is

$$
X = (X_1, X_2, \dots, X_n)^T,
$$

where each $X_i$ is a random variable on the same probability space.

The **mean vector** is

$$
E[X] = (E[X_1], \dots, E[X_n])^T,
$$

and the **covariance matrix** $\Sigma$ has entries

$$
\Sigma_{ij} = \operatorname{Cov}(X_i, X_j).
$$

For any deterministic vector $w \in \mathbb{R}^n$, the linear combination $w^T X$ is a scalar random variable with

- $E[w^T X] = w^T E[X]$,
- $\operatorname{Var}(w^T X) = w^T \Sigma w$.

This is exactly the structure used in mean-variance portfolio theory, where $X$ is the vector of asset returns and $w$ is the vector of portfolio weights. Any time you compute portfolio volatility from a covariance matrix, you are applying these formulas.

## Multivariate Normal Distribution

An $n$-dimensional random vector $X$ has a **multivariate normal distribution** with mean vector $\mu$ and covariance matrix $\Sigma$, written $X \sim N_n(\mu, \Sigma)$, if every linear combination $w^T X$ is univariate normal for all $w \in \mathbb{R}^n$.

When $\Sigma$ is positive definite, the density of $X$ is

$$
f_X(x) = \frac{1}{(2\pi)^{n/2} |\Sigma|^{1/2}} \exp\!\left( -\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu) \right).
$$

Key properties:

- Any subset of components of a multivariate normal vector is again multivariate normal.
- Any linear transformation $Y = A X + b$ (for matrix $A$ and vector $b$) is multivariate normal.
- Zero covariance implies independence: if $\operatorname{Cov}(X_i, X_j) = 0$ in the multivariate normal case, then $X_i$ and $X_j$ are independent.

## Application: Portfolio Returns

Let $R = (R_1, \dots, R_n)^T$ be the vector of asset returns in a single period. A common modeling assumption is

$$
R \sim N_n(\mu, \Sigma).
$$

Then for any portfolio weights $w$:

- Portfolio return: $R_p = w^T R$ is normal with mean $w^T \mu$ and variance $w^T \Sigma w$.

This is the probabilistic backbone of **mean-variance optimization** and many risk models. Once you are comfortable with random vectors in the Gaussian world, you are ready to think about richer dependence structures and non-normal joint behavior.

Next Topic: [Covariance Matrices and Portfolio Risk](covariance-matrices-and-portfolio-risk.md)
