---
title: "Univariate Regression"
permalink: /math/advanced/econometrics/univariate-regression/
sidebar:
  nav: "econometrics"
---

## Introduction

Univariate regression is a fundamental econometric method that models the relationship between a single independent variable and a dependent variable. It serves as the building block for more complex regression models, such as multivariable regression and logistic regression. By examining the linear relationship between variables, univariate regression provides insights into the impact of the independent variable on the dependent variable.

For random variables $x$ and $y$, the univariate regression model can be expressed as:

$$y = \beta_0 + \beta_1x + \epsilon$$

where:

- $y$ is the dependent variable.
- $x$ is the independent variable.
- $\beta_0$ is the intercept.
- $\beta_1$ is the slope.
- $\epsilon$ is the error term.

This model express the linear relationship between $x$ and $y$, but we don't know the true values of $\beta_0$ and $\beta_1$. Our goal is to estimate these parameters using sample data and construct a regression line that best fits the data.

## 1.1 How to find beta_0 and beta_1

### First try

We could minimize the sum of residuals: $\sum_{i=1}^{n} \epsilon_i$, but this would not be a good approach because the residuals could cancel each other out. 

### Second try

In order to avoid the problem of residuals cancelling each other out, we could minimize the absolute value of the residuals: $\sum_{i=1}^{n} |\epsilon_i|$. However, this would lead to a non-differentiable function, making it difficult to find the optimal solution.

### Third try

The most common approach is to minimize the sum of squared residuals, which is known as the Ordinary Least Squares (OLS) method. The sum of squared residuals is given by:

$$\sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2$$

> Notice the hat on $\hat\beta_0$ and $\hat\beta_1$ to indicate that they are estimators of the true parameters $\beta_0$ and $\beta_1$. We will never truly know the $\beta_0$ and $\beta_1$ values, but we can estimate them using the OLS method.

> Same for $\hat{\epsilon_i}$, which is the residual for the $i$-th observation, not the true error term $\epsilon$.

## 1.2 OLS Estimation

$\hat{\beta_0}$ and $\hat{\beta_1}$ are the OLS estimators of $\beta_0$ and $\beta_1$, respectively. They are obtained by minimizing the sum of squared residuals:

$$\text{min } S(\beta_0, \beta_1) = \sum_{i=1}^{n} \epsilon_i = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2$$

The solution for this problem is:

$$\begin{cases}
\hat{\beta_0} &= \bar{y} - \hat{\beta_1}\bar{x} \\
\hat{\beta_1} &= \frac{\bar{x}\bar{y} - \overline{xy}}{\bar{x}^2 - \overline{x^2}} = \frac{cov(x, y)}{var(x)}
\end{cases}$$

where:

- $\bar{x}$ is the mean of the independent variable $x$.
- $\bar{y}$ is the mean of the dependent variable $y$.
- $\overline{xy}$ is the mean of the product of $x$ and $y$.
- $\overline{x^2}$ is the mean of the square of $x$.
- $cov(x, y)$ is the covariance between $x$ and $y$.
- $var(x)$ is the variance of $x$.

> The OLS estimators $\hat{\beta_0}$ and $\hat{\beta_1}$ are unbiased and consistent estimators of the true parameters $\beta_0$ and $\beta_1$.

### Proof of OLS Estimators

$$ min \sum_{i=1}^{n} \epsilon_i^2 = min \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2 $$

Taking the partial derivatives with respect to $\beta_0$ and $\beta_1$:

$$ \begin{cases}
\frac{\partial S}{\partial \beta_0} &= -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i) = 0 \\
\frac{\partial S}{\partial \beta_1} &= -2 \sum_{i=1}^{n} x_i(y_i - \beta_0 - \beta_1x_i) = 0
\end{cases} $$

$$ 
\begin{cases}
n\bar{y} - n\beta_0 - \bar{x} \beta_1 = 0 \\
n\overline{xy} - n\beta_0\bar{x} - n\overline{x^2}\beta_1 = 0
\end{cases}
$$

Solving for $\beta_0$ and $\beta_1$:

$$
\begin{cases}
\beta_0 &= \bar{y} - \beta_1\bar{x} \\
\beta_1 &= \frac{\overline{xy} - \bar{x}\bar{y}}{\overline{x^2} - \bar{x}^2}
\end{cases}
$$



















