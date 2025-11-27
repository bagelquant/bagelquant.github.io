---
title: "Joint Distributions, Covariance, and Correlation"
permalink: /probability/joint-distributions-and-covariance/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

Quantitative finance is inherently multivariate: portfolios hold many assets, risk factors interact, and returns move together. To describe these relationships, we need **joint distributions** and measures of dependence like covariance and correlation.

## Joint Distributions

Let $(X, Y)$ be a pair of random variables.

### Discrete Case

If $X$ and $Y$ are discrete, the **joint pmf** is

$$
P(X = x, Y = y) = p_{X,Y}(x, y).
$$

The **marginal** pmfs are obtained by summing out the other variable:

- $p_X(x) = \sum_y p_{X,Y}(x, y)$
- $p_Y(y) = \sum_x p_{X,Y}(x, y)$

### Continuous Case

If $X$ and $Y$ are continuous, the **joint pdf** is $f_{X,Y}(x, y)$, and for any region $C \subset \mathbb{R}^2$,

$$
P\big((X, Y) \in C\big) = \iint_C f_{X,Y}(x, y) \, dx \, dy.
$$

The marginals are

- $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy$
- $f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx$

### Independence

$X$ and $Y$ are **independent** if

$$
P(X \in A, Y \in B) = P(X \in A) P(Y \in B)
$$

for all sets $A$ and $B$. In terms of densities or pmfs:

- Discrete: $p_{X,Y}(x, y) = p_X(x) p_Y(y)$.
- Continuous: $f_{X,Y}(x, y) = f_X(x) f_Y(y)$.

Independence is a strong assumption and often violated in financial data, but it provides a useful baseline model.

## Covariance and Correlation Revisited

Given random variables $X$ and $Y$ with finite second moments, the **covariance** is

$$
\operatorname{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])].
$$

The **correlation** is

$$
\rho_{X,Y} = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X) \, \operatorname{Var}(Y)}}.
$$

Key facts:

- $\rho_{X,Y} \in [-1, 1]$.
- $\rho_{X,Y} = 0$ implies uncorrelatedness but **not** independence in general.
- If $(X, Y)$ are jointly normal, zero correlation **does** imply independence.

In portfolio theory, covariance and correlation determine how combining assets affects overall risk.

### A Two-Asset Toy Example

Consider a simple discrete model with two assets and three equally likely scenarios (each with probability $1/3$). Returns (in decimal form) are:

| Scenario | $R_1$ | $R_2$ |
|----------|------:|------:|
|   1      |  0.10 |  0.05 |
|   2      | -0.05 | -0.02 |
|   3      |  0.02 |  0.01 |

Compute expected returns:

$$
E[R_1] = \frac{1}{3}(0.10 - 0.05 + 0.02) = \frac{0.07}{3}, \quad
E[R_2] = \frac{1}{3}(0.05 - 0.02 + 0.01) = \frac{0.04}{3}.
$$

Now compute covariance:

$$
\operatorname{Cov}(R_1,R_2) = E[(R_1 - E[R_1])(R_2 - E[R_2])]
                             = \sum_{s=1}^3 (R_{1,s} - E[R_1])(R_{2,s} - E[R_2])\, P_s.
$$

You can work this out numerically to see that the covariance is positive: when $R_1$ is above its mean, $R_2$ also tends to be above its mean in these scenarios.

Finally, form a 50/50 portfolio with weights $w=(0.5, 0.5)^T$. The portfolio return is

$$
R_p = 0.5 R_1 + 0.5 R_2.
$$

Its variance is

$$
\operatorname{Var}(R_p) = w^T \Sigma w = 0.5^2\,\operatorname{Var}(R_1) + 0.5^2\,\operatorname{Var}(R_2) + 2\cdot 0.5\cdot 0.5\,\operatorname{Cov}(R_1,R_2).
$$

This makes explicit how the covariance term contributes to (or reduces) portfolio risk compared to holding each asset separately.

## Covariance Matrices and Portfolios

For an $n$-dimensional random vector $R = (R_1, \dots, R_n)^T$ of asset returns, the **covariance matrix** $\Sigma$ is defined by

$$
\Sigma_{ij} = \operatorname{Cov}(R_i, R_j).
$$

If $w$ is a vector of portfolio weights (summing to 1 for a fully invested portfolio), the portfolio return is $R_p = w^T R$, and

- Expected return: $E[R_p] = w^T E[R]$.
- Variance: $\operatorname{Var}(R_p) = w^T \Sigma w$.

This quadratic form is central to mean-variance optimization.

## Joint Distributions in Finance

Examples of joint distributions in quantitative finance include:

- Joint distribution of multiple asset returns in a portfolio
- Joint distribution of risk factors (e.g., equity indices, interest rates, FX rates)
- Joint distribution of default times in a credit portfolio

Later in the course, we will introduce specific multivariate models, such as the **multivariate normal distribution** and **copulas**, to capture realistic dependence structures.

## Summary

In this article we:

- Defined joint distributions for discrete and continuous random variables
- Reviewed independence in the multivariate context
- Revisited covariance and correlation as measures of linear dependence
- Connected joint distributions and covariance matrices directly to portfolio modeling

Joint distributions provide the framework needed to move from single-asset risk to realistic multi-asset portfolios.

Next Topic: [The Normal Distribution and the Central Limit Phenomenon](normal-distribution-and-clt.md)
