---
title: "Multivariable Regression"
permalink: /econometrics/multivariable-regression/
sidebar:
  nav: "econometrics"
---

Compared to univariable regression, multivariable regression incorporates multiple independent variables into the model. The relationship remains linear, but now more than one independent variable is considered. The general form is:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \ldots + \beta_nx_n + \epsilon,
$$

where:

- $y$ is the dependent variable,
- $x_1, x_2, \ldots, x_n$ are the independent variables,
- $\beta_0, \beta_1, \ldots, \beta_n$ are the coefficients,
- $\epsilon$ is the error term.

This model can be expressed in matrix notation as:

$$
y = X\beta + \epsilon,
$$

where:

- $y$ is the vector of dependent variable values,
- $X$ is the matrix of independent variables (including a column of ones for the intercept), $X \in \mathbb{R}^{n \times (k+1)}$,
- $\beta$ is the vector of coefficients, $\beta \in \mathbb{R}^{k+1}$.

## 2.1 OLS Estimators

The ordinary least squares (OLS) estimators for the multivariable regression model are:

$$
\hat{\beta} = (X^T X)^{-1}X^Ty,
$$

where:

- $\hat{\beta}$ is the vector of OLS estimators,
- $X$ is the matrix of independent variables (with intercept),
- $y$ is the vector of observed dependent variable values.

### Derivation of OLS Estimators

The OLS method minimizes the sum of squared errors:

$$
\min S(\beta) = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_{i1} - \ldots - \beta_nx_{in})^2.
$$

In matrix form, this becomes:

$$
\min S(\beta) = (y - X\beta)^T(y - X\beta) = y^Ty - 2y^TX\beta + \beta^TX^TX\beta.
$$

Taking the derivative with respect to $\beta$ and setting it to zero yields:

$$
\frac{\partial S(\beta)}{\partial \beta} = -2X^Ty + 2X^TX\beta = 0
$$

$$
X^TX\beta = X^Ty
$$

$$
\hat{\beta} = (X^TX)^{-1}X^Ty
$$

## 2.2 F-test

The F-test evaluates the joint significance of the independent variables. The hypotheses are:

$$
H_0: \beta_1 = \beta_2 = \ldots = \beta_n = 0
$$

$$
H_1: \text{At least one } \beta_i \neq 0, \quad i = 1, 2, \ldots, n
$$

The F-statistic is:

$$
F = \frac{MSE}{MSR} = \frac{SSE/k}{SSR/(n-k-1)}
$$

where:

- $MSE$ is the mean squared error,
- $MSR$ is the mean squared residual,
- $SSE$ is the sum of squared errors (explained),
- $SSR$ is the sum of squared residuals.

The F-test is one-tailed; reject $H_0$ if the calculated F-statistic exceeds the critical value.

> The F-test checks the joint significance of all independent variables, while the t-test checks the significance of each variable individually. Sometimes, their results may conflict.

## 2.3 Gauss-Markov Assumptions

The Gauss-Markov assumptions for multivariable regression are similar to those for univariable regression, with an added focus on the variability of independent variables (no perfect multicollinearity):

1. **Linearity in parameters**: The model is linear in the coefficients.
2. **No perfect multicollinearity**: No independent variable is a perfect linear combination of others. Otherwise, $X^TX$ is not invertible and OLS estimators do not exist.
3. **Independence and randomness of errors**: The error term is independent and random.
4. **Zero conditional mean**: The expected value of the error term is zero given the independent variables.
5. **Homoscedasticity**: The error term has constant variance.
6. **Normality of errors**: The error term is normally distributed.

The procedure for checking these assumptions is the same as in univariable regression.

## 2.4 Violations of Gauss-Markov Assumptions

- **Linearity in parameters**: If the relationship is not linear, consider a nonlinear model.
- **No perfect multicollinearity**: If present, remove one of the linearly dependent variables. In practice, high (but not perfect) multicollinearity can be addressed by normalizing variables, using principal component analysis (PCA), or removing highly correlated variables.
- **Independence and randomness of errors**: If violated, estimators are biased and inconsistent. Consider changing the model or using robust standard errors.
- **Zero conditional mean**: This is checked using residuals; by OLS construction, the mean residual is always zero.
- **Homoscedasticity**: If violated, use robust standard errors or Generalized Least Squares (GLS).
- **Normality of errors**: If violated, inference based on normality may be biased.

## 2.5 Generalized Least Squares (GLS)

> This section is supplementary and was not covered in the course, but GLS is useful when errors are not homoscedastic.

GLS estimates the model when the error term has non-constant variance:

$$
y = X\beta + \epsilon
$$

The GLS estimator is:

$$
\hat{\beta}_{GLS} = (X^TWX)^{-1}X^TWy
$$

where $W$ is a diagonal weight matrix with the inverse of the error variances on the diagonal:

$$
W =
\begin{bmatrix}
\frac{1}{\sigma_1^2} & 0 & \ldots & 0 \\
0 & \frac{1}{\sigma_2^2} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & \frac{1}{\sigma_n^2}
\end{bmatrix}
$$

GLS estimators are more efficient than OLS when errors are heteroscedastic.

## 2.6 Overfitting

- If $n = k + 1$, the model fits the data perfectly ($R^2 = 1$), but is overfitted and should not be used for prediction.
- If $n < k + 1$, the model is overfitted and not valid.

## 2.7 $R^2$ and Adjusted $R^2$

Adding more independent variables always increases $R^2$, so it is not suitable for comparing models with different numbers of variables. The adjusted $R^2$ is a better metric:

$$
R^2_{adj} = 1 - \frac{(1 - R^2)(n - 1)}{n - k - 1}
$$

where:

- $R^2_{adj}$ is the adjusted $R^2$,
- $R^2$ is the coefficient of determination,
- $n$ is the number of observations,
- $k$ is the number of independent variables.

Adjusted $R^2$ penalizes the addition of unnecessary variables. It is mainly used for model comparison, not for direct interpretation.

> When comparing models, always check that assumptions are met and that individual t-tests for variables are significant.

## 2.8 Categorical Data

Categorical variables represent categories. There are two common ways to encode them:

### Option 1: Computer Science / Machine Learning

Assign each category a number from $0$ to $n-1$ (where $n$ is the number of categories), then use binary coding.

- *Advantage*: Saves memory.

### Option 2: Econometrics

Use binary (dummy) variables, with the first category as the base. Each other category gets its own indicator variable.

- *Advantage*: Easier interpretation.

### Interpreting Categorical Variables

Consider the model:

$$
y = \beta_0 + \beta_1x_1
$$

where

$$
x_1 = \begin{cases}
1 & \text{if the category is A}, \\
0 & \text{otherwise}
\end{cases}
$$

$\hat{\beta}_1$ estimates the difference in the dependent variable for category A compared to the base category, holding all else constant.
