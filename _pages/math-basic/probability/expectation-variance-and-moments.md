---
title: "Expectation, Variance, and Moments"
permalink: /probability/expectation-variance-and-moments/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

If you open any risk report, you will see a few familiar statistics staring back at you: "expected return", "volatility", sometimes "skew" and "kurtosis". These numbers are all different ways of summarizing the shape of a random variable's distribution.

Expectation and variance capture the **center** and **spread**. Higher-order moments (skewness and kurtosis) start to tell you about asymmetry and tails. In quantitative finance, these moments underpin everyday concepts like risk, diversification, and "fat tails".

This article puts all of these ideas—expectation, variance, covariance, and moments—into a single, unified picture that works for both discrete and continuous random variables.

## Expectation

Let $X$ be a random variable with distribution $P$. The **expectation** (or mean) of $X$, if it exists, is defined as

- **Discrete case:**
  $$
  E[X] = \sum_x x \, P(X = x).
  $$

- **Continuous case:**
  $$
  E[X] = \int_{-\infty}^{\infty} x \, f_X(x) \, dx,
  $$
  where $f_X$ is the pdf of $X$.

More generally, for a function $g$:

- Discrete:
  $$
  E[g(X)] = \sum_x g(x) \, P(X = x).
  $$

- Continuous:
  $$
  E[g(X)] = \int_{-\infty}^{\infty} g(x) \, f_X(x) \, dx.
  $$

Expectation is a **linear operator**:

$$
E[aX + bY] = a E[X] + b E[Y]
$$

for any random variables $X$, $Y$ (on the same probability space) and constants $a$, $b$, provided the expectations exist.

## Variance and Standard Deviation

The **variance** of $X$ measures how spread out $X$ is around its mean $\mu = E[X]$:

$$
\operatorname{Var}(X) = E[(X - \mu)^2].
$$

An equivalent and often more convenient formula is

$$
\operatorname{Var}(X) = E[X^2] - (E[X])^2.
$$

The **standard deviation** is $\sigma = \sqrt{\operatorname{Var}(X)}$.

For a portfolio return $R_p$, variance and standard deviation are core risk measures. In mean-variance optimization, you typically maximize $E[R_p]$ for a given $\operatorname{Var}(R_p)$.

## Covariance and Correlation

For random variables $X$ and $Y$ with finite second moments, the **covariance** is

$$
\operatorname{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])].
$$

Alternatively,

$$
\operatorname{Cov}(X, Y) = E[XY] - E[X] E[Y].
$$

The **correlation** is the normalized covariance:

$$
\rho_{X,Y} = \operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X) \, \operatorname{Var}(Y)}}.
$$

Covariance and correlation are fundamental for portfolio construction:

- Diversification benefits come from assets with low or negative correlation.
- The covariance matrix of asset returns is a core input to risk models.

## Moments and Central Moments

The **$k$-th moment** of $X$ (about zero) is

$$
E[X^k], \quad k = 1, 2, 3, \dots
$$

The **$k$-th central moment** (about the mean) is

$$
E[(X - E[X])^k].
$$

Important examples:

- First moment: $E[X]$ (mean)
- Second central moment: $E[(X - E[X])^2]$ (variance)
- Third central moment: related to **skewness** (asymmetry)
- Fourth central moment: related to **kurtosis** (tail thickness / peakedness)

## Skewness and Kurtosis (Qualitative View)

While precise formulas exist, here we focus on intuition:

- **Skewness** measures asymmetry:
  - Positive skew: longer right tail (large gains more likely than large losses).
  - Negative skew: longer left tail (large losses more likely than large gains).

- **Kurtosis** measures tail thickness and peakness relative to a normal distribution:
  - High kurtosis: more mass in the tails and sometimes at the center ("fat tails").
  - Financial returns often exhibit excess kurtosis compared to the normal.

In risk management, skewness and kurtosis help identify strategies that have rare but severe losses (e.g., selling options) even if their mean return looks attractive.

## Expectation in Vector and Matrix Form

For a random vector $X = (X_1, \dots, X_n)^T$:

- The **mean vector** is $E[X] = (E[X_1], \dots, E[X_n])^T$.
- The **covariance matrix** $\Sigma$ has entries
  $$
  \Sigma_{ij} = \operatorname{Cov}(X_i, X_j).
  $$

For a portfolio with weight vector $w$ and return vector $R$:

- Expected portfolio return: $E[w^T R] = w^T E[R]$.
- Portfolio variance: $\operatorname{Var}(w^T R) = w^T \Sigma \, w$.

This connects probability (moments) directly to linear algebra and portfolio theory. Once you are fluent in this vector-and-matrix view, reading mean–variance or factor-model papers becomes much more straightforward.

Next Topic: [Joint Distributions, Covariance, and Correlation](joint-distributions-and-covariance.md)
