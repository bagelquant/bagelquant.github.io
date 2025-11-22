---
title: "Logistic Regression"
layout: page
permalink: /econometrics/logistic-regression/

nav: "econometrics"
---

Previously, we discussed cases where the independent variables are categorical. Now, suppose the dependent variable $y$ is binary, i.e., $y = 0$ or $1$. In this scenario, the normality assumption of the residuals does not hold (since there are only two possible values, not a normal distribution), and standard statistical inference is not applicable.

Instead, we use a different approach: logistic regression.

## Sigmoid Function

Consider the following function:

$$
y = \frac{e^x}{1 + e^{x}} = \frac{1}{1 + e^{-x}},
$$

We observe that:

1. $0 \leq y \leq 1$,
2. $\lim_{x \to -\infty} y = 0$,
3. $\lim_{x \to \infty} y = 1$,
4. $y$ is a continuous and differentiable function,
5. $y(0) = 0.5$.

This function is called the **sigmoid function**. It is commonly used to model the probability of a binary outcome.

By inverting the sigmoid function, we obtain:

$$
x = \ln \left( \frac{y}{1 - y} \right).
$$

## Regression Model

Given a binary outcome $Y$:

$$
Y = \begin{cases}
1 & \text{if some condition is met}, \\
0 & \text{otherwise}.
\end{cases}
$$

We model the probability that $Y = 1$ as:

$$
p = P[Y = 1 \mid X],
$$

where $X$ represents the independent variables.

Let

$$
p = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}.
$$

This implies:

$$
\ln \left( \frac{p}{1 - p} \right) = \beta_0 + \beta_1 X.
$$

## Maximum Likelihood Estimation

To estimate the parameters $\beta_0$ and $\beta_1$, recall the probability mass function of the Bernoulli distribution:

$$
P[X=x] = p^x (1 - p)^{1 - x}.
$$

The likelihood function for $n$ observations is:

$$
L(\beta_0, \beta_1) = P[Y_1 = y_1, Y_2 = y_2, \ldots, Y_n = y_n] = \prod_{i=1}^{n} p_i^{y_i} (1 - p_i)^{1 - y_i},
$$

where:

- $p_i = p(x_i) = \frac{e^{\beta_0 + \beta_1 x_i}}{1 + e^{\beta_0 + \beta_1 x_i}}$,
- $Y_i$ is a random binary variable,
- $y_i$ is the observed value of $Y_i$.

The log-likelihood function is:

$$
\ln L(\beta_0, \beta_1) = \sum_{i=1}^{n} y_i \ln p_i + (1 - y_i) \ln (1 - p_i).
$$

Maximum likelihood estimation seeks the values of $\beta_0$ and $\beta_1$ that maximize the log-likelihood. This is done by setting the partial derivatives of the log-likelihood with respect to $\beta_0$ and $\beta_1$ to zero:

$$
\begin{cases}
\frac{\partial \ln L}{\partial \beta_0} = 0, \\
\frac{\partial \ln L}{\partial \beta_1} = 0,
\end{cases}
$$

which leads to:

$$
\begin{cases}
\sum_{i=1}^{n} (y_i - p_i) = 0, \\
\sum_{i=1}^{n} (y_i - p_i) x_i = 0,
\end{cases}
$$

or equivalently:

$$
\begin{cases}
\bar{y} = \bar{p}, \\
\overline{xy} = \overline{xp}.
\end{cases}
$$

Since $p_i = \frac{e^{\beta_0 + \beta_1 x_i}}{1 + e^{\beta_0 + \beta_1 x_i}}$, this is a nonlinear system of two equations with two unknowns. It is typically solved using numerical methods, such as the Newton-Raphson method.

For $k$ independent variables, the model generalizes to:

$$
p_i = P[Y_i = 1 \mid X],
$$

$$
p_i = \frac{e^{\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_k x_{ik}}}{1 + e^{\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_k x_{ik}}}.
$$

The resulting system is:

$$
\begin{cases}
\bar{y} = \bar{p}, \\
\overline{x_j y} = \overline{x_j p}, \quad j = 1, 2, \ldots, k.
\end{cases}
$$

## Multiclass Case: $M$ Categories of $Y$

When $Y$ has $M$ categories and $k$ independent variables, the model becomes:

$$
P[Y_i = 1 \mid X] = \frac{e^{\beta_0^1 + \beta_1^1 x_1^1 + \beta_2^1 x_2^1 + \ldots + \beta_k^1 x_k^1}}{1 + e^{\beta_0^1 + \beta_1^1 x_1^1 + \beta_2^1 x_2^1 + \ldots + \beta_k^1 x_k^1}},
$$

$$
P[Y_i = j \mid X] = \frac{e^{\beta_0^j + \beta_1^j x_1^j + \beta_2^j x_2^j + \ldots + \beta_k^j x_k^j}}{1 + e^{\beta_0^j + \beta_1^j x_1^j + \beta_2^j x_2^j + \ldots + \beta_k^j x_k^j}}, \quad \text{for } j = 2, 3, \ldots, M-1,
$$

$$
P[Y_i = M \mid X] = 1 - \sum_{j=1}^{M-1} P[Y_i = j \mid X].
$$

In matrix notation:

$$
P[Y_i = j \mid X] = \frac{1}{1 + e^{-\beta_j^T X_i}},
$$

$$
P[Y_i = M \mid X] = 1 - \sum_{j=1}^{M-1} \frac{1}{1 + e^{-\beta_j^T X_i}},
$$

where:

- $\beta_j = (\beta_0^j, \beta_1^j, \ldots, \beta_k^j)$,
- $X_i = (1, x_1^i, x_2^i, \ldots, x_k^i)$.

We also have:

$$
\beta^T X = \log \left( \frac{P[Y_i = j \mid X]}{1 - P[Y_i = j \mid X]} \right).
$$

The likelihood function is:

$$
L(\beta_0^1, \beta_1^1, \ldots, \beta_k^1, \ldots, \beta_0^{M-1}, \beta_1^{M-1}, \ldots, \beta_k^{M-1}) = \prod_{i=1}^{n} \prod_{j=1}^{M} P[Y_i = j \mid X_i]^{y_{ij}},
$$

where:

- $\beta_j = (\beta_0^j, \beta_1^j, \ldots, \beta_k^j)$,
- $y_{ij}$ is the observed value indicating $Y_i = j$.

Solving $(k+1)(M-1)$ nonlinear equations yields the maximum likelihood estimates of the parameters, typically using numerical methods.

Next up: [Basic Time Series Process](basic-time-series-process.md)
