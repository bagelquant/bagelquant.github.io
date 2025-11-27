---
title: Least Squares and Regression
permalink: /linear-algebra/least-squares-and-regression/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## Introduction to Linear Regression

**Linear Regression** is one of the most fundamental and widely used statistical techniques in both academic research and practical applications, especially in quantitative finance. It aims to model the relationship between a dependent variable (or response variable) and one or more independent variables (or explanatory variables) by fitting a linear equation to observed data.

The goal is to find the "best-fit" line (or hyperplane) that minimizes the sum of the squared differences between the observed values and the values predicted by the linear model. This method is known as **Ordinary Least Squares (OLS)**.

## The Linear Regression Model

Consider a simple linear regression model with one independent variable:

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i
$$

where:
*   $y_i$ is the $i$-th observation of the dependent variable.
*   $x_i$ is the $i$-th observation of the independent variable.
*   $\beta_0$ is the intercept.
*   $\beta_1$ is the slope coefficient.
*   $\epsilon_i$ is the error term, representing unobserved factors and noise.

For multiple linear regression with $p$ independent variables, the model becomes:

$$$
y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \epsilon_i
$$$

## Linear Regression using Linear Algebra

Linear algebra provides a concise and powerful framework for formulating and solving multiple linear regression problems.

Let $N$ be the number of observations and $p$ be the number of independent variables (excluding the intercept). We can express the model in matrix form:

$$$
\mathbf{y} = X\boldsymbol{\beta} + \boldsymbol{\epsilon}
$$$

where:
*   $\mathbf{y}$ is an $N \times 1$ vector of dependent variable observations: $\mathbf{y} = \begin{pmatrix} y_1 \\ \vdots \\ y_N \end{pmatrix}$.
*   $X$ is an $N \times (p+1)$ design matrix of independent variables. The first column of $X$ is typically a column of ones (for the intercept term $\beta_0$):
    $$$
    X = \begin{pmatrix}
    1 & x_{11} & x_{12} & \cdots & x_{1p} \\
    1 & x_{21} & x_{22} & \cdots & x_{2p} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    1 & x_{N1} & x_{N2} & \cdots & x_{Np}
    \end{pmatrix}
    $$$
*   $\boldsymbol{\beta}$ is a $(p+1) \times 1$ vector of regression coefficients: $\boldsymbol{\beta} = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_p \end{pmatrix}$.
*   $\boldsymbol{\epsilon}$ is an $N \times 1$ vector of error terms: $\boldsymbol{\epsilon} = \begin{pmatrix} \epsilon_1 \\ \vdots \\ \epsilon_N \end{pmatrix}$.

## The Least Squares Solution

The objective of OLS is to find the vector of coefficients $\hat{\boldsymbol{\beta}}$ that minimizes the sum of squared residuals (errors). The sum of squared residuals can be written as:

$$$
SSR = \sum_{i=1}^N (y_i - \hat{y}_i)^2 = \| \mathbf{y} - X\hat{\boldsymbol{\beta}} \|^2 = (\mathbf{y} - X\hat{\boldsymbol{\beta}})^T (\mathbf{y} - X\hat{\boldsymbol{\beta}})
$$$

To find the $\hat{\boldsymbol{\beta}}$ that minimizes this quantity, we differentiate $SSR$ with respect to $\hat{\boldsymbol{\beta}}$ and set the result to zero. This leads to the **normal equations**:

$$$
X^T X \hat{\boldsymbol{\beta}} = X^T \mathbf{y}
$$$

If the matrix $X^T X$ is invertible (which it is, provided the columns of $X$ are linearly independent), then the least squares estimate for $\boldsymbol{\beta}$ is given by:

$$$
\hat{\boldsymbol{\beta}} = (X^T X)^{-1} X^T \mathbf{y}
$$$

This elegant matrix formula provides a direct solution for the regression coefficients. The term $(X^T X)^{-1} X^T$ is also known as the **pseudo-inverse** of $X$ if $X$ has linearly independent columns.

## Assumptions of OLS

For $\hat{\boldsymbol{\beta}}$ to be the Best Linear Unbiased Estimator (BLUE) and for hypothesis testing to be valid, several assumptions are typically made about the error term $\boldsymbol{\epsilon}$:

1.  **Linearity:** The relationship between $y$ and $X$ is linear.
2.  **No perfect multicollinearity:** The columns of $X$ are linearly independent, so $X^T X$ is invertible.
3.  **Homoscedasticity:** The variance of the error terms is constant across all observations.
4.  **No autocorrelation:** The error terms are uncorrelated with each other.
5.  **Zero conditional mean:** The expected value of the error term is zero, conditional on $X$.
6.  **Normality (for inference):** The error terms are normally distributed.

Violations of these assumptions can lead to biased or inefficient estimates and invalid statistical inferences.

## Least Squares and Regression in Quant Finance

Linear regression is arguably the most used statistical tool in quantitative finance:

*   **Factor Models:** Explaining asset returns. The Capital Asset Pricing Model (CAPM) and Fama-French three-factor model are prime examples. Here, $y$ would be asset returns, and $X$ would contain market risk premium, size factor, value factor, etc. The $\beta$ coefficients represent the asset's exposure to these factors.
*   **Risk Analysis:** Measuring sensitivities (betas) to market, industry, or macroeconomic factors is a direct application.
*   **Hedging:** Determining hedge ratios often involves regressing the returns of a portfolio against the returns of a hedging instrument.
*   **Arbitrage Pricing Theory (APT):** Regressing asset returns against various systematic risk factors.
*   **Performance Attribution:** Decomposing a portfolio's return into components attributable to different investment decisions or market segments.
*   **Valuation:** Using regression to find relationships between company fundamentals and stock prices.
*   **Yield Curve Modeling:** Regressing bond yields against different maturities to estimate parameters of a yield curve model (e.g., Nelson-Siegel).

The ability to formulate and solve regression problems using linear algebra is fundamental for any quantitative finance professional. It forms the basis for understanding more advanced econometric and machine learning models.

