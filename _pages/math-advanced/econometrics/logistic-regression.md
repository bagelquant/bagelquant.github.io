---
title: "Logistic Regression"
permalink: /econometrics/logistic-regression/
sidebar:
  nav: "econometrics"
---

We already discussed the case when the independent variables are categorical. Suppose now that the values of y are binary, i.e., y = 0 or 1. In this case, the normallity assumption of the residuals is not valid (only two possible values, not normal distribution), the typical statistical inference cannot be made.

Instead, we use a different model.

## 3.1 Sigmoid Function

Consider the following function:

$$
y = \frac{e^x}{1 + e^{x}} = \frac{1}{1 + e^{-x}},
$$

We observe that:

1. $0 \leq y \leq 1$,
2. $\lim_{x \to -\infty} y = 0$,
3. $\lim_{x \to \infty} y = 1$,
4. y is a continuous differentiable function.
5. y(0) = 0.5.

This function is called the **sigmoid function**. It is used to model the probability of a binary outcome.

Reverse engineering the sigmoid function, we have:

$$
x = \ln \left( \frac{y}{1 - y} \right).
$$

## 3.2 Regression Model

Given a binary outcome Y:

$$
Y = \begin{cases}
1 & \text{if some condition is met}, \\
0 & \text{otherwise}.
\end{cases}
$$

We can model the probability of Y = 1 as:

$$
p = P[Y = 1 | X],
$$

where:

- X are given observations of the independent variable,

let 

$$
p = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}.
$$

This implies that:

$$
\ln \left( \frac{p}{1 - p} \right) = \beta_0 + \beta_1 X.
$$

## 3.3 Maximum Likelihood Estimation

We need to estimate the parameters $\beta_0$ and $\beta_1$, the probability mass function of bernoulli distribution is:

$$
P[X=x] = p^x (1 - p)^{1 - x}.
$$

The likelihood function is:

$$L(\beta_0, \beta_1) = P[Y_1 = y_1, Y_2 = y_2, \ldots, Y_n = y_n], $$

$$= \prod_{i=1}^{n} p_i^{y_i} (1 - p_i)^{1 - y_i},$$

where:

- $p_i = p(x_i) = \frac{e^{\beta_0 + \beta_1 x_i}}{1 + e^{\beta_0 + \beta_1 x_i}}$,
- $Y_i$ is a random binary variable,
- $y_i$ is the observed value of $Y_i$.

The log-likelihood function is:

$$
\ln L(\beta_0, \beta_1) = \sum_{i=1}^{n} y_i \ln p_i + (1 - y_i) \ln (1 - p_i).
$$

The maximum likelihood estimation is to find the parameters $\beta_0$ and $\beta_1$ that maximize the log-likelihood function, by taking the partial derivatives of the log-likelihood function with respect to $\beta_0$ and $\beta_1$ and setting them to zero.

$$
\begin{cases}
\frac{\partial \ln L}{\partial \beta_0} = 0, \\
\frac{\partial \ln L}{\partial \beta_1} = 0,
\end{cases}
$$

$$
\begin{cases}
\sum_{i=1}^{n} (y_i - p_i) = 0, \\
\sum_{i=1}^{n} (y_i - p_i) x_i = 0,
\end{cases}
$$

$$
\begin{cases}
\bar{y} = \bar{p}, \\
\overline{xy} = \overline{xp}.
\end{cases}
$$

Since $p_i = \frac{e^{\beta_0 + \beta_1 x_i}}{1 + e^{\beta_0 + \beta_1 x_i}}$, this is a non-linear system of 2 equations with 2 unknowns. We can solve it using numerical methods, such as Newton-Raphson method.

In case of k independent variables, the model is:

$$
p_i = P[Y_i = 1 | X],
$$

$$
p_i = \frac{e^{\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_k x_{ik}}}{1 + e^{\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_k x_{ik}}}.
$$

Using the same method, we obtain the system:

$$
\begin{cases}
\bar{y} = \bar{p}, \\
\overline{x_j y} = \overline{x_j p}, \quad j = 1, 2, \ldots, k.
\end{cases}
$$

## 3.4 M categories of Y

With M categories of Y, and k independent variables, the model is, we have:

$$
P[Y_i = 1 | X] = \frac{e^{\beta_0^1 + \beta_1^1 x_1^1 + \beta_2^1 x_2^1 + \ldots + \beta_k^1 x_k^1}}{1 + e^{\beta_0^1 + \beta_1^1 x_1^1 + \beta_2^1 x_2^1 + \ldots + \beta_k^1 x_k^1}},
$$

$$
P[Y_i = j | X] = \frac{e^{\beta_0^j + \beta_1^j x_1^j + \beta_2^j x_2^j + \ldots + \beta_k^j x_k^j}}{1 + e^{\beta_0^j + \beta_1^j x_1^j + \beta_2^j x_2^j + \ldots + \beta_k^j x_k^j}}, \text{ for } j = 2, 3, \ldots, M-1,
$$

$$
P[Y_i = M | X] = 1 - \sum_{j=1}^{M-1} P[Y_i = j | X].
$$

In matrix form:

$$
P[Y_i = j | X] = \frac{1}{1 + e^{-\beta_j^T X_i}},
$$

$$
P[Y_i = M | X] = 1 - \sum_{j=1}^{M-1} \frac{1}{1 + e^{-\beta_j^T X_i}},
$$

where:

- $\beta_j = (\beta_0^j, \beta_1^j, \ldots, \beta_k^j)$,
- $X_i = (1, x_1^i, x_2^i, \ldots, x_k^i)$.

We also obtain:

$$
\beta^T X = log \left( \frac{P[Y_i = j | X]}{1 - P[Y_i = j | X]} \right).
$$

The likelihood function is:

$$
L(\beta_0^1, \beta_1^1, \ldots, \beta_k^1, \beta_0^2, \beta_1^2, \ldots, \beta_k^2, \ldots, \beta_0^{M-1}, \beta_1^{M-1}, \ldots, \beta_k^{M-1}) = \prod_{i=1}^{n} \prod_{j=1}^{M} P[Y_i = j | X_i]^{y_{ij}},
$$

where:

- $\beta_j = (\beta_0^j, \beta_1^j, \ldots, \beta_k^j)$,
- $y_{ij}$ is the observed value of $Y_i = j$.

Solving (k+1)(M-1) non-linear queations will give us the maximum likelihood estimation of the parameters. (By some numerical methods)

