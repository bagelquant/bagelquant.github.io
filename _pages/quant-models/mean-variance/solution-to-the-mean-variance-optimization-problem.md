---
title: "Solution to the Mean-Variance Optimization Problem"
permalink: /mean-variance/solution-to-the-mean-variance-optimization-problem/
sidebar:
    nav: "mean-variance"
---

The mean-variance optimization problem:

- Minimize the portfolio's variance
- Subject to the constraints that the weights sum to 1
- And the expected return equals the target expected return

We first only consider the investing only in risky assets, and we will add the risk-free asset later. In mathematical terms, the optimization problem can be expressed as:

$$
\begin{align*}
\min_{\boldsymbol W}  \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W), \\
\text{s.t. } \boldsymbol W^T \boldsymbol 1 = 1, \\
\boldsymbol W^T \boldsymbol \mu = E[\tilde r_p], \\
\end{align*}
$$

Where:
- $\boldsymbol W$ is the weight vector of the portfolio
- $\boldsymbol V$ is the covariance matrix of the asset returns
- $\boldsymbol \mu$ is the vector of expected returns
- $\boldsymbol 1$ is a vector of ones
- $E[\tilde r_p]$ is the target expected return of the portfolio

> Note: $\frac{1}{2}$ is used to simplify the derivative calculation, it will not affect the optimization result.

> Note: We use boldface to denote vectors and matrices, and we use the transpose operator $T$ to denote the transpose of a vector or matrix.

## Lagrange Multiplier Method

To solve the optimization problem, we can use the Lagrange multiplier method. We introduce two Lagrange multipliers, $\lambda$ and $\gamma$, for the two constraints. The Lagrangian function is given by:

$$
\mathcal{L}(\boldsymbol W, \lambda, \gamma) = \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W) + \lambda [E[\tilde r_p] - \boldsymbol W^T \boldsymbol \mu] + \gamma (1 - \boldsymbol W^T \boldsymbol 1)
$$

First Order condition (FOC) is given by:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial \boldsymbol W} = \boldsymbol V \boldsymbol W - \lambda \boldsymbol \mu - \gamma \boldsymbol 1 = 0, \\
\frac{\partial \mathcal{L}}{\partial \lambda} = E[\tilde r_p] - \boldsymbol W^T \boldsymbol \mu = 0, \\
\frac{\partial \mathcal{L}}{\partial \gamma} = 1 - \boldsymbol W^T \boldsymbol 1 = 0.
\end{align*}
$$

That is three equations with three unknowns $\boldsymbol W$, $\lambda$, and $\gamma$. We can solve the equations to find the optimal weights for the portfolio, the result is:

$$
\begin{align*}
\lambda = \frac{C \cdot E[\tilde r_p] - A}{D}, (scalar)\\
\gamma = \frac{B - A \cdot E[\tilde r_p]}{D}, (scalar)\\
\boldsymbol W = \lambda \boldsymbol V^{-1} \boldsymbol \mu + \gamma \boldsymbol V^{-1} \boldsymbol 1, (N \times 1)\\
\end{align*}
$$

where:

- $A = \boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol \mu = \boldsymbol \mu^T \boldsymbol V^{-1} \boldsymbol 1$
- $B = \boldsymbol \mu^T \boldsymbol V^{-1} \boldsymbol \mu$
- $C = \boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1$
- $D = BC - A^2$

A, B, C, D are all scalars, we use them to simplify the notation. The optimal weights $\boldsymbol W$ are a linear combination of the expected returns and the covariance matrix of the asset returns. We could further simplify $\boldsymbol W$ as:

$$
\boldsymbol W = \boldsymbol g + \boldsymbol h \cdot E[\tilde r_p],
$$

where:

- $\boldsymbol g = \frac{1}{D} \left( B \cdot \boldsymbol V^{-1} \boldsymbol 1 - A \cdot \boldsymbol V^{-1} \boldsymbol \mu \right)$, $N \times 1$ vector
- $\boldsymbol h = \frac{1}{D} \left( C \cdot \boldsymbol V^{-1} \boldsymbol \mu - A \cdot \boldsymbol V^{-1} \boldsymbol 1 \right)$, $N \times 1$ vector

It is seems like a complex formula, but if we ignore all computation details, $\boldsymbol g$ and $\boldsymbol h$ are just two vectors we already known (given $\boldsymbol V$ and $\boldsymbol \mu$), and the optimal weights are just a simple linear function.

## Minimum Variance Portfolio (MVP)

The minimum variance portfolio (MVP) is the portfolio that minimizes the variance of the portfolio return, without any constraints on the expected return. We could follow the same stps as above, remove the constraint of expected return, and we have:

$$
\begin{align*}
\min_{\boldsymbol W}  \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W), \\
\text{s.t. } \boldsymbol W^T \boldsymbol 1 = 1, \\
\end{align*}
$$

The Lagrangian function is given by:

$$
\mathcal{L}(\boldsymbol W, \gamma) = \frac{1}{2} (\boldsymbol W^T \boldsymbol V \boldsymbol W) + \gamma (1 - \boldsymbol W^T \boldsymbol 1)
$$

The FOC is given by:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial \boldsymbol W} = \boldsymbol V \boldsymbol W - \gamma \boldsymbol 1 = 0, \\
\frac{\partial \mathcal{L}}{\partial \gamma} = 1 - \boldsymbol W^T \boldsymbol 1 = 0.
\end{align*}
$$

The solution is:

$$
\begin{align*}
\gamma = \frac{1}{C} = \frac{1}{\boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1}, (scalar)\\
\boldsymbol W = \frac{\boldsymbol V^{-1} \boldsymbol 1}{C} = \frac{\boldsymbol V^{-1} \boldsymbol 1}{\boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1}, (N \times 1)\\
\end{align*}
$$

where $C = \boldsymbol 1^T \boldsymbol V^{-1} \boldsymbol 1$. The optimal weights $\boldsymbol W$ are a linear function of the inverse of the covariance matrix and the vector of ones. 

> We could obtain the same result by analyzing the variance and expected return of all optimal portfolios, and find the minimum variance portfolio(MVP). You could find the details in the next section [Efficient Frontier without Risk-Free Asset](https://bagelquant.com/mean-variance/efficient-frontier-without-risk-free-asset/).


## Conclusion

We found: 

- Weights of the optimal portfolio for any given expected return
- Weights of the minimum variance portfolio (MVP)



























