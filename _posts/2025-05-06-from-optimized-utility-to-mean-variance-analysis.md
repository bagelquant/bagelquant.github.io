---
title: "From Optimized Utility to Mean-Variance Analysis"
permalink: /mean-variance/from-optimized-utility-to-mean-variance-analysis/
sidebar:
    nav: "mean-variance"
---

Mean-variance optimization is the core of modern portfolio theory, the basic idea is to:

- Maximize the gain <=> using expected return as the measure of gain
- Minimize the risk <=> using variance as the measure of risk

Either we could fix the expected return and minimize the risk, or we could fix the risk and maximize the expected return. If we plot the expected return and risk (variance) on a 2D graph, we could easily argue the top left corner is the "better" portfolio.

The target is really simple, for target expected return $E[\tilde r_p]$ (Expected portfolio return), we want to find the portfolio with the minimum variance. The optimization problem could be written as:

$$
\begin{align*}
\min_{\boldsymbol W}  \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W), \\
\text{s.t. } \boldsymbol W^T \boldsymbol 1 = 1, \\
\boldsymbol W^T \boldsymbol \mu = E[\tilde r_p], \\
\end{align*}
$$

where:

- $\boldsymbol W$ is the weight vector of the portfolio
- $\boldsymbol V$ is the covariance matrix of the asset returns
- $\boldsymbol \mu$ is the vector of expected returns
- $\boldsymbol 1$ is a vector of ones
- $E[\tilde r_p]$ is the target expected return of the portfolio

The problem is minimizing the variance of the portfolio subject to the constraints that the weights sum to 1 and the expected return equals the target expected return. The solution to this problem will give us the optimal weights for each asset in the portfolio.

Before we solve the optimization problem, there is a question remains: why using variance as the measure of risk? is this mean-variance approach reasonable? We will implement the utility theory again, to show in which situation the mean-variance approach is reasonable.

## Taylor Expansion of Utility Function

Consider the Taylor expansion of the utility function around the mean wealth level $E[\tilde W]$:

$$
u(\tilde W) = u(E[\tilde W]) + u'(E[\tilde W]) (\tilde W - E[\tilde W]) + \frac{1}{2} u''(E[\tilde W]) (\tilde W - E[\tilde W])^2 + R_3,
$$

where $R_3$ is the remainder term of the Taylor expansion. The first two terms are the linear and quadratic terms, respectively. Taking the expectation of both sides, we have:

$$
\begin{align*}
E[u(\tilde W)] = u(E[\tilde W]) + \frac{1}{2} u''(E[\tilde W]) E[(\tilde W - E[\tilde W])^2] + E[R_3], \\
E[u(\tilde W)] = u(E[\tilde W]) + \frac{1}{2} u''(E[\tilde W]) \text{Var}(\tilde W) + E[R_3].

\end{align*}
$$

When $E[R_3] = 0$, we have the expected utility is purely determined by the mean and variance of the wealth. This is the case where mean-variance optimization is reasonable. Otherwise, we have higher order terms could affect the expected utility, and the mean-variance optimization approach is not accurate.

Now we consider the $E[R_3]$ term:

$$
E[R_3] = \sum_{n=3}^{\infty} \frac{1}{n!} u^{(n)}(E[\tilde W]) E[(\tilde W - E[\tilde W])^n],
$$

to make sure $E[R_3] = 0$, we need to have the following conditions:

1. eiter $u^{(n)}(E[\tilde W]) = 0$ for all $n \ge 3$, or
2. $E[(\tilde W - E[\tilde W])^n] = 0$ for all $n \ge 3$.

Example for first condition is a quadratic utility function, which is a special case of the utility function. The example for second condition is a normal distribution, if the wealth is normally distributed, then the higher order moments are zero. In this case, the mean-variance optimization is reasonable.

## Quadratic Utility Function Example

Consider the quadratic utility function:

$$
\begin{cases}
u(z) = z - \frac{b}{2} z^2, \ \ \ \ \ b > 0 \\
u' = 1 - b z, \ \ \ \ \ \ \ \ \ \ \ 1 - b z > 0\\
u'' = -b. \\
u^{(n)} = 0, n \ge 3.
\end{cases}
$$

Then the $E[R_3]$ term is zero. The mean-variance optimization is reasonable in this case. 

## Normal Distribution Example

The moments of a normal distribution are:

$$
\begin{cases}
E[\tilde W] = \mu, \\
\text{Var}(\tilde W) = \sigma^2, \\
E[(\tilde W - E[\tilde W])^n] = 0, n \ge 3.
\end{cases}
$$

Then the $E[R_3]$ term is zero. The mean-variance optimization is reasonable in this case.

## Conclusion

In conclusion, the mean-variance optimization is reasonable when the utility function is quadratic or the wealth is normally distributed. In these cases, the higher order moments do not affect the expected utility, and the mean-variance optimization approach is accurate. In other cases, we need to consider the higher order moments and the mean-variance optimization approach may not be accurate.

In real life, the neither of the two assumptions is hardly satisfied. However, the higher order effects are usually small, and the mean-variance optimization approach is still a good approximation. Therefore, the mean-variance optimization approach is widely used in practice.

