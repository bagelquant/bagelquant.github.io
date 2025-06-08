---
title: "From Optimized Utility to Mean-Variance Analysis"
permalink: /mean-variance/from-optimized-utility-to-mean-variance-analysis/
sidebar:
    nav: "mean-variance"
---

Mean-variance optimization is at the heart of modern portfolio theory. The basic idea is straightforward:

- Maximize gain, using expected return as the measure of gain
- Minimize risk, using variance as the measure of risk

You can either fix the expected return and minimize risk, or fix the risk and maximize expected return. If you plot expected return against risk (variance) on a 2D graph, the "better" portfolios are those in the top left corner.

The objective is simple: for a target expected return $E[\tilde r_p]$ (expected portfolio return), find the portfolio with the minimum variance. The optimization problem can be written as:

$$
\begin{align*}
\min_{\boldsymbol W}  \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W), \\
\text{s.t. } \boldsymbol W^T \boldsymbol 1 = 1, \\
\boldsymbol W^T \boldsymbol \mu = E[\tilde r_p], \\
\end{align*}
$$

where:

- $\boldsymbol W$ is the vector of portfolio weights
- $\boldsymbol V$ is the covariance matrix of asset returns
- $\boldsymbol \mu$ is the vector of expected returns
- $\boldsymbol 1$ is a vector of ones
- $E[\tilde r_p]$ is the target expected return of the portfolio

This problem minimizes portfolio variance subject to the constraints that weights sum to 1 and the expected return matches the target. The solution gives the optimal weights for each asset.

But before solving this optimization, a key question remains: why use variance as the measure of risk? Is the mean-variance approach always reasonable? To answer this, we revisit utility theory to show when mean-variance optimization is justified.

## Taylor Expansion of the Utility Function

A utility function mathematically represents an investor's preferences over different levels of wealth. "Utility" measures the satisfaction or happiness derived from wealth. A risk-averse investor has an increasing, concave utility function, and their optimal choice is to maximize expected utility of wealth. The utility function is a central concept in economics and finance, explaining how individuals make decisions under uncertainty. For more details, see the [Utility Theory](https://bagelquant.com/quant-models/utility-theory/) section.

Consider the Taylor expansion of the utility function around the mean wealth $E[\tilde W]$:

$$
u(\tilde W) = u(E[\tilde W]) + u'(E[\tilde W]) (\tilde W - E[\tilde W]) + \frac{1}{2} u''(E[\tilde W]) (\tilde W - E[\tilde W])^2 + R_3,$$

where $R_3$ is the remainder term. The first two terms are linear and quadratic, respectively. Taking expectations on both sides gives:

$$
\begin{align*}
E[u(\tilde W)] = u(E[\tilde W]) + \frac{1}{2} u''(E[\tilde W]) E[(\tilde W - E[\tilde W])^2] + E[R_3], \\
E[u(\tilde W)] = u(E[\tilde W]) + \frac{1}{2} u''(E[\tilde W]) \text{Var}(\tilde W) + E[R_3].
\end{align*}
$$

If $E[R_3] = 0$, expected utility depends only on the mean and variance of wealth. In this case, mean-variance optimization is justified. Otherwise, higher-order terms affect expected utility, and the mean-variance approach may not be accurate.

Now, consider the $E[R_3]$ term:

$$
E[R_3] = \sum_{n=3}^{\infty} \frac{1}{n!} u^{(n)}(E[\tilde W]) E[(\tilde W - E[\tilde W])^n],
$$

to ensure $E[R_3] = 0$, we need either:

1. $u^{(n)}(E[\tilde W]) = 0$ for all $n \ge 3$, or
2. $E[(\tilde W - E[\tilde W])^n] = 0$ for all $n \ge 3$.

The first condition is satisfied by a quadratic utility function. The second is satisfied if wealth is normally distributed, since higher moments are zero. In both cases, mean-variance optimization is reasonable.

## Quadratic Utility Function Example

Consider the quadratic utility function:

$$
\begin{cases}
u(z) = z - \frac{b}{2} z^2, \quad b > 0 \\
u' = 1 - b z, \quad 1 - b z > 0\\
u'' = -b. \\
u^{(n)} = 0, \ n \ge 3.
\end{cases}
$$

Here, $E[R_3] = 0$, so mean-variance optimization is justified.

## Normal Distribution Example

The moments of a normal distribution are:

$$
\begin{cases}
E[\tilde W] = \mu, \\
\text{Var}(\tilde W) = \sigma^2, \\
E[(\tilde W - E[\tilde W])^n] = 0, \ n \ge 3.
\end{cases}
$$

Again, $E[R_3] = 0$, so mean-variance optimization is justified.

## Conclusion

In summary, mean-variance optimization is reasonable when the utility function is quadratic or wealth is normally distributed. In these cases, higher-order moments do not affect expected utility, and the mean-variance approach is accurate. In other situations, higher-order moments matter and mean-variance optimization may not be precise.

In practice, neither of these assumptions is strictly satisfied. However, higher-order effects are usually small, so mean-variance optimization remains a good approximation and is widely used in real-world portfolio management.
