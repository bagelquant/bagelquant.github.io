---
title: "The Central Limit Theorem in Depth"
permalink: /probability/central-limit-theorem/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

We briefly met the Central Limit Theorem (CLT) when we introduced the normal distribution. It is one of those results that looks technical at first glance but ends up secretly powering a lot of the "normality" assumptions you see in finance.

## Statement of the CLT

Let $X_1, X_2, \dots$ be i.i.d. random variables with

- Mean $\mu = E[X_1]$,
- Variance $\sigma^2 = \operatorname{Var}(X_1) \in (0, \infty)$.

Define the standardized sum

$$
Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}}.
$$

The **Central Limit Theorem** states that

$$
Z_n \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty.
$$

Equivalently, for any real $z$,

$$
P(Z_n \le z) \xrightarrow[n \to \infty]{} \Phi(z),
$$

where $\Phi$ is the standard normal cdf.

## Interpretation

The CLT tells us that **sums (or averages) of many independent, identically distributed variables are approximately normal**, regardless of the original distribution, as long as the variance is finite.

For the sample average

$$
\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i,
$$

we can rewrite

$$
\sqrt{n} \, \frac{\bar{X}_n - \mu}{\sigma} \xrightarrow{d} N(0, 1).
$$

This implies that for large $n$, $\bar{X}_n$ is approximately normal with mean $\mu$ and variance $\sigma^2 / n$. In practice, this is why so many estimation errors and aggregated quantities are modeled as Gaussian, even when the underlying data are not.

## CLT in Practice: Confidence Intervals

Suppose we observe returns $R_1, \dots, R_n$ assumed i.i.d. with mean $\mu$ and variance $\sigma^2$. The sample mean

$$
\bar{R}_n = \frac{1}{n} \sum_{i=1}^n R_i
$$

approximately follows

$$
\bar{R}_n \approx N\left(\mu, \frac{\sigma^2}{n}\right)
$$

for large $n$.

If we estimate $\sigma^2$ by the sample variance, we can construct approximate confidence intervals for $\mu$. This is the bread and butter of empirical finance: you run a backtest, compute an average excess return, and then ask, "Is this signal real, or could it be noise?" The CLT is what turns that vague question into a quantitative statement.

## Limitations and Caveats

While powerful, the CLT has limitations that are especially relevant in finance:

- **Finite variance required:** Heavy-tailed distributions with infinite variance may not satisfy the classical CLT.
- **Speed of convergence:** For small $n$ or very skewed/heavy-tailed data, the normal approximation may be poor.
- **Dependence:** If data are strongly dependent (e.g., autocorrelated volatility), more advanced versions of the CLT are needed.

In financial applications, it is worth checking assumptions and validating normal approximations empirically—especially in the tails, where risk actually lives.

Next Topic: [Inequalities and Concentration Bounds](concentration-inequalities.md)
