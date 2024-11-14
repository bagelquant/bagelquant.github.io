---
title: "Multivariable Regression"
permalink: /econometrics/multivariable-regression/
sidebar:
  nav: "econometrics"
---

Comparing to univariable regression, multivariable regression is adding more independent variables to the model. The model is still linear, but the number of independent variables is more than one. The model is as follows:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \ldots + \beta_nx_n + \epsilon,
$$

where:

- $y$ is the dependent variable,
- $x_1, x_2, \ldots, x_n$ are the independent variables,
- $\beta_0, \beta_1, \ldots, \beta_n$ are the coefficients,
- $\epsilon$ is the error term.

The model can be written in matrix form as:

$$
y = X\beta + \epsilon,
$$

where:

- $y$ is the dependent variable,
- $X$ is the vector of independent variables and the constant term, $X \in \mathbb{R}^{k+1}$,
- $\beta$ is the vector of coefficients, $\beta \in \mathbb{R}^{k+1}$,

## 2.1 OLS Estimators

The OLS estimators for the multivariable regression model are:

$$
\hat{\beta} = (X^T X)^{-1}X^Ty,
$$

where:

- $\hat{\beta}$ is the vector of OLS estimators,
- $X$ is the matrix of independent variables and the constant term, observations in rows and variables in columns, $X \in \mathbb{R}^{n \times (k+1)}$,
- $y$ is the vector of dependent variable, $y \in \mathbb{R}^{n}$.

### Proof of OLS Estimators

We can obtain the OLS estimators utilizing the same technique as in univariable regression. The objective is to minimize the sum of squared errors:

$$
\text{min } S(\beta_0, \beta_1, \ldots, \beta_n) = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_{i1} - \ldots - \beta_nx_{in})^2.
$$

Taking the derivative of the sum of squared errors with respect to each coefficient and setting them to zero, we can obtain the OLS estimators by solving a system of linear equations.

In matrix form, the solution will be more concise, the objective becomes:

$$
\text{min } S(\beta) = (y - X\beta)^T(y - X\beta),
$$

$$
= y^Ty - 2y^TX\beta + \beta^TX^TX\beta.
$$

Taking the derivative of the sum of squared errors with respect to $\beta$ and setting it to zero, we can obtain the OLS estimators:

$$
\frac{\partial S(\beta)}{\partial \beta} = -2X^Ty + 2X^TX\beta = 0,
$$

$$
X^TX\beta = X^Ty,
$$

$$
\hat{\beta} = (X^TX)^{-1}X^Ty.
$$

## 2.2 F-test

The F-test for the multivariable regression model is to test the joint significance of the independent variables. The null hypothesis is:

$$
H_0: \beta_1 = \beta_2 = \ldots = \beta_n = 0.
$$

$$
H_1: \text{At least one } \beta_i \neq 0, i = 1, 2, \ldots, n.
$$

The test statistic is:

$$
F = \frac{MSE}{MSR} = \frac{SSE/k}{SSR/(n-k-1)},
$$

where:

- $MSE$ is the mean squared estimation,
- $MSR$ is the mean squared residual,
- $SSE$ is the sum of squared estimation,
- $SSR$ is the sum of squared residual.

The F-test is a one-tailed test, and we can reject the null hypothesis if the calculated F-statistic is greater than the critical value.

> The relationship between the F-test and the t-test is that the F-test is equivalent to multiple t-tests. The F-test is used to test the joint significance of the independent variables, while the t-test is used to test the significance of each independent variable individually.

> Sometimes, the results from the F-test and the t-test may be conflicting. 

## 2.3 Gauss-Markov Assumptions

The Gauss-Markov assumptions for the multivariable regression model are the same as the univariable regression model. Except for the assumption of no multicollinearity, which is switched to the assumption of variability in the independent variables.

1. **Linearity in parameters**: The model is linear in the parameters.
2. **No perfect multicollinearity**: No independent variable can be a linear function of one or more other independent variables. Otherwise, the matrix $X^TX$ will not be invertible, and the OLS estimators will not exist.
3. **Independence and randomness of the error term**: The error term is independent and random.
4. **Zero conditional mean**: The expected value of the error term is zero given the independent variables. 
5. **Homoscedasticity**: The variance of the error term is constant.
6. **Normality of the error term**: The error term is normally distributed.

Procedure to check the Gauss-Markov assumptions is same as the univariable regression model.

## 2.4 Violation of Gauss-Markov Assumptions

1. **Linearity in parameters**

If the relationship between the dependent variable and the independent variables is not linear, we should consider change the model to a non-linear model.

2. **No perfect multicollinearity**

If there is perfect multicollinearity, we should remove one of the independent variables that are linearly dependent on others.

In real-world data, it is rare to have perfect multicollinearity. However, we may have multicollinearity (det<sup>2</sup>$(X^TX) \approx 0$), we could:

- Normalize the independent variables,
- Use principal component analysis (PCA) to reduce the dimensionality of the independent variables,
- Remove one or more independent variables that are highly correlated with others.

3. **Independence and randomness of the error term**

If the error term is not independent and random, the estimators will be biased and inconsistent. 

We could consider:

- Change the model,
- Instead of standard errors, use robust standard errors.

4. **Zero conditional mean**

We use residual to check this assumption. The expected value of the residual is always zero by OLS construction.

5. **Homoscedasticity**

If the variance of the error term is not constant, the estimators will be biased and inconsistent.

We could consider:

- Instead of standard errors, use robust standard errors,
- Instead of OLS, use Generalized Ordinary Least Squares (GLS) to estimate the model.

6. **Normality of the error term**

If the error term is not normally distributed, all inference based on the normality assumption will be biased.

## 2.5 Generalized Ordinary Least Squares (GLS)

> This section was not covered in the course, but it is a useful method to estimate the model when the error term is not homoscedastic.

Generalized Ordinary Least Squares (GLS) is a method to estimate the model when the error term is not homoscedastic. The model is:

$$
y = X\beta + \epsilon,
$$

where:

- $y$ is the dependent variable,
- $X$ is the matrix of independent variables and the constant term, $X \in \mathbb{R}^{n \times (k+1)}$,
- $\beta$ is the vector of coefficients, $\beta \in \mathbb{R}^{k+1}$,
- $\epsilon$ is the error term.

The GLS estimators are:

$$
\hat{\beta}_{GLS} = (X^TWX)^{-1}X^TWy,
$$

where:

- $\hat{\beta}_{GLS}$ is the vector of GLS estimators,
- $W$ is the weight matrix, $W \in \mathbb{R}^{n \times n}$.

The weight matrix $W$ is a diagonal matrix with the inverse of the variance of the error term on the diagonal. The weight matrix $W$ is:

$$
W =
\begin{bmatrix}
\frac{1}{\sigma_1^2} & 0 & \ldots & 0 \\
0 & \frac{1}{\sigma_2^2} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & \frac{1}{\sigma_n^2}
\end{bmatrix},
$$

where:

- $\sigma_1^2, \sigma_2^2, \ldots, \sigma_n^2$ are the variance of the error term.

The GLS estimators are more efficient than the OLS estimators when the error term is not homoscedastic.

## 2.6 Overfitting

- if $n = k + 1$, the model is perfectly fitted to the data, $R^2 = 1$. But the model is overfitted, you should not use this model to predict new data.
- if $n < k + 1$, the model is overfitting.

## 2.7 R-squared and Adjusted R-squared

Adding independent variables to the model will always increase the $R^2$ value. The $R^2$ value is not a good measure to compare models with different numbers of independent variables. 

Why? Because adding one or more independent variables always can achieve at least the same minimum sum of squared errors, by using the same independent variables as the model with fewer independent variables, adding more independent variables can only improve the $R^2$ value.

The adjusted $R^2$ value is a better measure to compare models with different numbers of independent variables. The adjusted $R^2$ value is:

$$
R^2_{adj} = 1 - \frac{(1 - R^2)(n - 1)}{n - k - 1},
$$

where:

- $R^2_{adj}$ is the adjusted $R^2$ value,
- $R^2$ is the $R^2$ value,
- $n$ is the number of observations,
- $k$ is the number of independent variables.

The adjusted $R^2$ value penalizes the $R^2$ value for adding more independent variables to the model.

However, adjusted $R^2$ value does not have a direct interpretation as $R^2$ value. We use it to compare models with different numbers of independent variables.

> When comparing models, we should also check all assumptions are met, and individual t-tests for indepent variables are significant.

## 2.8 Categorical data

Categorical data is data that represents categories, typically we use one of binary coding to represent categorical data in the model.

**Option 1: In CS, ML**

Assign each category from 0 to $n-1$, where $n$ is the number of categories. Then convert to binary coding.

- Advantage: save computor memory.

**Option 2: In Econometrics**

Convert to binary coding directly, assume the first category is the base category, assign one's to each category.

> See handwritten notes for an example.

- Advantage: easy to interpret.

### Interpretation of the categorical data

Consider the model:

$$
y = \beta_0 + \beta_1x_1,
$$

where:
$$
x_1 = \begin{cases}
1 & \text{if the category is A}, \\
0 & \text{Otherwise}.
\end{cases}
$$

$\hat{\beta_1}$: It's estimated that the dependent variable with category A is $\hat{\beta_1}$ higher opposed to the base category, given all other factors are same.

