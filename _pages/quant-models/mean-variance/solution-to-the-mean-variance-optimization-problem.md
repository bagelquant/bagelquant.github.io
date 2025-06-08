---
title: "Solution to the Mean-Variance Optimization Problem"
permalink: /mean-variance/solution-to-the-mean-variance-optimization-problem/
sidebar:
    nav: "mean-variance"
---

The mean-variance optimization problem can be summarized as follows:

- Minimize the portfolio's variance
- Subject to the constraints that the weights sum to 1
- And the expected return equals a target value

We first consider investing only in risky assets; the risk-free asset will be added later. Mathematically, the optimization problem is:

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

Note: The $\frac{1}{2}$ factor is included to simplify derivative calculations; it does not affect the optimization result.

Note: Boldface denotes vectors and matrices, and $T$ indicates the transpose.

## Lagrange Multiplier Method

To solve this optimization problem, we use the Lagrange multiplier method. Introduce two multipliers, $\lambda$ and $\gamma$, for the two constraints. The Lagrangian is:

$$
\mathcal{L}(\boldsymbol W, \lambda, \gamma) = \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W) + \lambda [E[\tilde r_p] - \boldsymbol W^T \boldsymbol \mu] + \gamma (1 - \boldsymbol W^T \boldsymbol 1)
$$

The first-order conditions (FOC) are:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial \boldsymbol W} = \boldsymbol V \boldsymbol W - \lambda \boldsymbol \mu - \gamma \boldsymbol 1 = 0, \\
\frac{\partial \mathcal{L}}{\partial \lambda} = E[\tilde r_p] - \boldsymbol W^T \boldsymbol \mu = 0, \\
\frac{\partial \mathcal{L}}{\partial \gamma} = 1 - \boldsymbol W^T \boldsymbol 1 = 0.
\end{align*}
$$

This system consists of three equations with three unknowns: $\boldsymbol W$, $\lambda$, and $\gamma$. Solving yields the optimal portfolio weights:

$$
\begin{align*}
\lambda = \frac{C \cdot E[\tilde r_p] - A}{D}, \\
\gamma = \frac{B - A \cdot E[\tilde r_p]}{D}, \\
\boldsymbol W = \lambda \boldsymbol V^{-1} \boldsymbol \mu + \gamma \boldsymbol V^{-1} \boldsymbol 1,
\end{align*}
$$

where:

- $A = \boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol \mu = \boldsymbol \mu^T \boldsymbol V^{-1} \boldsymbol 1$
- $B = \boldsymbol \mu^T \boldsymbol V^{-1} \boldsymbol \mu$
- $C = \boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1$
- $D = BC - A^2$

All of $A$, $B$, $C$, and $D$ are scalars. The optimal weights $\boldsymbol W$ are a linear combination of the expected returns and the covariance matrix. We can further simplify:

$$
\boldsymbol W = \boldsymbol g + \boldsymbol h \cdot E[\tilde r_p],
$$

where:

- $\boldsymbol g = \frac{1}{D} \left( B \cdot \boldsymbol V^{-1} \boldsymbol 1 - A \cdot \boldsymbol V^{-1} \boldsymbol \mu \right)$
- $\boldsymbol h = \frac{1}{D} \left( C \cdot \boldsymbol V^{-1} \boldsymbol \mu - A \cdot \boldsymbol V^{-1} \boldsymbol 1 \right)$

Although the formula may look complex, $\boldsymbol g$ and $\boldsymbol h$ are just two vectors determined by $\boldsymbol V$ and $\boldsymbol \mu$, and the optimal weights are a simple linear function of the target expected return.

## Minimum Variance Portfolio (MVP)

The minimum variance portfolio (MVP) is the portfolio with the lowest possible variance, without any constraint on expected return. Following the same steps as above, but omitting the expected return constraint, we have:

$$
\begin{align*}
\min_{\boldsymbol W}  \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W), \\
\text{s.t. } \boldsymbol W^T \boldsymbol 1 = 1,
\end{align*}
$$

The Lagrangian is:

$$
\mathcal{L}(\boldsymbol W, \gamma) = \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W) + \gamma (1 - \boldsymbol W^T \boldsymbol 1)
$$

The FOC is:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial \boldsymbol W} = \boldsymbol V \boldsymbol W - \gamma \boldsymbol 1 = 0, \\
\frac{\partial \mathcal{L}}{\partial \gamma} = 1 - \boldsymbol W^T \boldsymbol 1 = 0.
\end{align*}
$$

The solution is:

$$
\begin{align*}
\gamma = \frac{1}{C} = \frac{1}{\boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1}, \\
\boldsymbol W = \frac{\boldsymbol V^{-1} \boldsymbol 1}{C} = \frac{\boldsymbol V^{-1} \boldsymbol 1}{\boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1}
\end{align*}
$$

where $C = \boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1$. The optimal weights $\boldsymbol W$ are a linear function of the inverse covariance matrix and the vector of ones. The variance of the minimum variance portfolio equals $\gamma = \frac{1}{C}$ (explored further in the next section).

> The same result can be obtained by analyzing the variance and expected return of all optimal portfolios and finding the minimum variance portfolio (MVP). See [Efficient Frontier without Risk-Free Asset](https://bagelquant.com/mean-variance/efficient-frontier-without-risk-free-asset/) for details.

## Conclusion

In summary:

- We derived the weights of the optimal portfolio for any given expected return
- We derived the weights of the minimum variance portfolio (MVP)
