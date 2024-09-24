---
title: "Univariate Regression"
permalink: /math/advanced/econometrics/univariate-regression/
sidebar:
  nav: "econometrics"
use_math: true
---

## Introduction

Univariate regression is a fundamental econometric method that models the relationship between a single independent variable and a dependent variable. It serves as the building block for more complex regression models, such as multivariable regression and logistic regression. By examining the linear relationship between variables, univariate regression provides insights into the impact of the independent variable on the dependent variable.

## Basic Notation Concepts and Assumptions

### Basic Concepts

The univariate regression model seeks to estimate the relationship between the dependent variable $Y$ and the independent variable $X$. The model assumes a linear relationship between the variables, where the dependent variable is a function of the independent variable and an error term:

$$Y = \beta_0 + \beta_1 X + \epsilon$$

Notice, We assume the model exists for observations, but we never can obtain the true model. Therefore, we cannot find the true values of $\beta_0$ and $\beta_1$.

We use the date to **estimate** the values of $\beta_0$ and $\beta_1$, use hat on the intercept and the slope: $\hat{\beta_0}$ and $\hat{\beta_1}$ to distinguish the estimated values from the true values.

In general, the goal of regression analysis is to find the **best-fitting line** (best-fitting $\hat{\beta_0}$ and $\hat{\beta_1}$) of the data points.

> What is the best-fitting line? How do we find it?

### Notation

Variable:

- $Y$: Dependent variable
- $X$: Independent variable

Real Model(We can never know):

- $\beta_0$: Intercept for the real model
- $\beta_1$: Slope for the real model
- $\epsilon$: Error term

Estimated Model(Derived from the data):
- $\hat{\beta_0}$: Intercept for the estimated model
- $\hat{\beta_1}$: Slope for the estimated model
- $n$: Number of observations
- $y_i$: Dependent variable value for observation $i$
- $x_i$: Independent variable value for observation $i$
- $\hat{y_i}$: Predicted value of $\hat{y_i}$ = $\hat{\beta_0} + \hat{\beta_1}x_i$
- $\epsilon_i$: Residual term for observation $i$

> Difference between **Error** and **Redidual**? 
> - **Error** is the difference between the true value and the **true model prediction**, we can never know.
> - **Residual** is the difference between the true value and the **estimated model prediction**, is derived from the data.


### Best-fitting line

Naturally, we want the line to be as close as possible to all the data points. The most obvious way to measure it is to sum up all the **distance** between the line and the data points:

$$ \sum_{i=1}^{n} (y_i - \hat{y_i}) 
= \sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i) 
= \sum_{i=1}^{n} (\epsilon_i) $$

However, the distance can be positive or negative, and they can cancel each other out. Minimalizing the sum of the distance is not a good idea.

How about we use absolute value?

$$ \sum_{i=1}^{n} |y_i - \hat{y_i}|$$

It is a good idea, but it is not differentiable. Later, we will use differentiable functions to minimize the distance. 

The most common way to measure the distance is to use the **squared distance**:

$$ \sum_{i=1}^{n} (y_i - \hat{y_i})^2

= \sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i)^2$$

The problem of finding the best-fitting line is converted to:

1. Minimize the sum of the squared residuals
2. The squared residuals can be seen as a function of two variables: $\hat{\beta_0}$ and $\hat{\beta_1}$, because data set $x_i$ and $y_i$ are given.


### OLS

Our goal: Minimize function $S(\hat{\beta_0}, \hat{\beta_1}) = \sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i)^2$

Solution:

1. Take the partial derivative of $S$ with respect to $\hat{\beta_0}$ and $\hat{\beta_1}$, and set them to zero.

$$ \begin{cases}
\frac{\partial S}{\partial \hat{\beta_0}} = -2 \sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i) = 0 \\ 
\frac{\partial S}{\partial \hat{\beta_1}} = -2 \sum_{i=1}^{n} x_i(y_i - \hat{\beta_0} - \hat{\beta_1}x_i) = 0 
\end{cases}$$

2. Solve the system of equations to find $\hat{\beta_0}$ and $\hat{\beta_1}$.

$$ \begin{cases}
n\hat{\beta_0} + \hat{\beta_1} \sum_{i=1}^{n} x_i = \sum_{i=1}^{n} y_i \\
\hat{\beta_0} \sum_{i=1}^{n} x_i + \hat{\beta_1} \sum_{i=1}^{n} x_i^2 = \sum_{i=1}^{n} x_i y_i
\end{cases}$$

$$ \begin{cases}
\hat{\beta_1} = \frac{\sum_{i=1}^{n} x_i y_i - \hat{\beta_0} \sum_{i=1}^{n} x_i}{\sum_{i=1}^{n} x_i^2} \\
\hat{\beta_0} = \frac{\sum_{i=1}^{n} y_i - \hat{\beta_1} \sum_{i=1}^{n} x_i}{n}
\end{cases}$$

$$ \begin{cases}
\hat{\beta_1} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} \\
\hat{\beta_0} = \bar{y} - \hat{\beta_1}\bar{x}
\end{cases}$$

where $\bar{x}$ and $\bar{y}$ are the sample means of $x$ and $y$ respectively.

The solution is called the Ordinary Least Squares (OLS) estimator, which minimizes the sum of the squared residuals and provides the best-fitting line for the

### Assumptions

1. **Linearity**: The relationship between the dependent variable and the independent variable is linear in term of $\beta_0$ and $\beta_1$.
2. **Inadmisible variables**: The independent variable $X$ is not a perfect linear function of another variable, which would cause multicollinearity.
3. **Independence**: The error term $\epsilon$ is independent of the independent variable $X$.
4. **Zero conditional mean**: The expected value of the error term $\epsilon$ given the independent variable $X$ is zero.
5. **Homoscedasticity**: The variance of the error term $\epsilon$ is constant across all values of the independent variable $X$.
6. **Normality**: The error term $\epsilon$ follows a normal distribution.

> Combination of assumptions 3, 4, and 5 is called the **[Gauss-Markov theorem](https://en.wikipedia.org/wiki/Gauss–Markov_theorem)**.

Why do we need these assumptions? The assumptions ensure that the OLS estimator is the Best Linear Unbiased Estimator (BLUE), meaning it is unbiased, has the smallest variance among all linear unbiased estimators, and is consistent. Violation of these assumptions can lead to biased and inconsistent estimators.

We will discuss unbiased estimators later.

### MLE approach

Another way to estimate the parameters is to use the Maximum Likelihood Estimation (MLE) approach. The MLE approach assumes that the error term $\epsilon$ follows a normal distribution with mean 0 and variance $\sigma^2$:

$$ \epsilon \sim N(0, \sigma^2)$$

> The assumption follows the normality assumption in the OLS assumptions.

The likelihood function is defined as the probability density function of the error term, by assumption 3, we can multiply the probability density function of each observation:

$$ L(\beta_0, \beta_1, \sigma^2) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{\epsilon_i^2}{2\sigma^2}\right)\newline
= \frac{1}{(2\pi\sigma^2)^{n/2}} \exp\left(-\frac{1}{2\sigma^2} \sum_{i=1}^{n} \epsilon_i^2\right)\newline
= \frac{1}{(2\pi\sigma^2)^{n/2}} \exp\left(-\frac{1}{2\sigma^2} \sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i)^2\right)$$

The MLE approach seeks to maximize the likelihood function with respect to the parameters $\beta_0$, $\beta_1$, and $\sigma^2$. The maximization process involves taking the partial derivatives of the likelihood function with respect to the parameters and setting them to zero.

Solution, find maximum likelihood estimators:

$$ \ln{L} = -\frac{n}{2} \ln{2\pi} - \frac{n}{2} \ln{\sigma^2} - \frac{1}{2\sigma^2} \sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i)^2$$

Now, we can easily find the last term of the equation, $\sum_{i=1}^{n} (y_i - \hat{\beta_0} - \hat{\beta_1}x_i)^2$ is the same as the sum of the squared residuals in the OLS approach.

We can see that the MLE approach is equivalent to the OLS approach, and the OLS estimator is the Maximum Likelihood Estimator under the normality assumption.

