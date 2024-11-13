---
title: "Univariate Regression"
permalink: /econometrics/univariate-regression/
sidebar:
  nav: "econometrics"
---

## Introduction

Univariate regression is a fundamental econometric method that models the relationship between a single independent variable and a dependent variable. It serves as the building block for more complex regression models, such as multivariable regression and logistic regression. By examining the linear relationship between variables, univariate regression provides insights into the impact of the independent variable on the dependent variable.

For random variables $x$ and $y$, the univariate regression model can be expressed as:

$$y = \beta_0 + \beta_1x + \epsilon,$$

where:

- $y$ is the dependent variable,
- $x$ is the independent variable,
- $\beta_0$ is the intercept,
- $\beta_1$ is the slope,
- $\epsilon$ is the error term.

This model express the linear relationship between $x$ and $y$, but we don't know the true values of $\beta_0$ and $\beta_1$. Our goal is to estimate these parameters using sample data and construct a regression line that best fits the data.

## 1.1 How to find beta_0 and beta_1

**First try**:

We could minimize the sum of residuals: $\sum_{i=1}^{n} \epsilon_i$, but this would not be a good approach because the residuals could cancel each other out. 

**Second try**:

In order to avoid the problem of residuals cancelling each other out, we could minimize the absolute value of the residuals: $\sum_{i=1}^{n} \|\epsilon_i\|$. However, this would lead to a non-differentiable function, making it difficult to find the optimal solution.

**Best approach**:

The most common approach is to minimize the sum of squared residuals, which is known as the Ordinary Least Squares (OLS) method. The sum of squared residuals is given by:

$$\sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

> Notice the hat on $\hat\beta_0$ and $\hat\beta_1$ to indicate that they are estimators of the true parameters $\beta_0$ and $\beta_1$. We will never truly know the $\beta_0$ and $\beta_1$ values, but we can estimate them using the OLS method.

> Same for $\hat{\epsilon_i}$, which is the residual for the $i$-th observation, not the true error term $\epsilon$.

## 1.2 OLS Estimation

$\hat{\beta_0}$ and $\hat{\beta_1}$ are the OLS estimators of $\beta_0$ and $\beta_1$, respectively. They are obtained by minimizing the sum of squared residuals:

$$\text{min } S(\beta_0, \beta_1) = \sum_{i=1}^{n} \epsilon_i = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

The solution for this problem is:

$$\begin{cases}
\hat{\beta_0} &= \bar{y} - \hat{\beta_1}\bar{x} \\
\hat{\beta_1} &= \frac{\bar{x}\bar{y} - \overline{xy}}{\bar{x}^2 - \overline{x^2}} = \frac{cov(x, y)}{var(x)}
\end{cases}$$

where:

- $\bar{x}$ is the mean of the independent variable $x$,
- $\bar{y}$ is the mean of the dependent variable $y$,
- $\overline{xy}$ is the mean of the product of $x$ and $y$,
- $\overline{x^2}$ is the mean of the square of $x$,
- $cov(x, y)$ is the covariance between $x$ and $y$,
- $var(x)$ is the variance of $x$.

> The OLS estimators $\hat{\beta_0}$ and $\hat{\beta_1}$ are unbiased and consistent estimators of the true parameters $\beta_0$ and $\beta_1$.

### Proof of OLS Estimators

Solving for $\hat{\beta_0}$ and $\hat{\beta_1}$ involves minimizing the sum of squared residuals:

$$ min \sum_{i=1}^{n} \epsilon_i^2 = min \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2 .$$

Taking the partial derivatives with respect to $\beta_0$ and $\beta_1$:

$$ \begin{cases}
\frac{\partial S}{\partial \beta_0} &= -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i) = 0, \\
\frac{\partial S}{\partial \beta_1} &= -2 \sum_{i=1}^{n} x_i(y_i - \beta_0 - \beta_1x_i) = 0,
\end{cases} $$

$$ 
\begin{cases}
n\bar{y} - n\beta_0 - \bar{x} \beta_1 = 0, \\
n\overline{xy} - n\beta_0\bar{x} - n\overline{x^2}\beta_1 = 0.
\end{cases}
$$

Solving for $\beta_0$ and $\beta_1$:

$$
\begin{cases}
\beta_0 &= \bar{y} - \beta_1\bar{x}, \\
\beta_1 &= \frac{\overline{xy} - \bar{x}\bar{y}}{\overline{x^2} - \bar{x}^2}.
\end{cases}
$$

### Properties of OLS Estimators

1. **Unbiasedness**: The OLS estimators are unbiased, meaning that their expected values are equal to the true parameters:

$$E(\hat{\beta_0}) = \beta_0, E(\hat{\beta_1}) = \beta_1.$$

2. **Consistency**: The OLS estimators are consistent, meaning that they converge in probability to the true parameters as the sample size increases:

$$\hat{\beta_0} \xrightarrow{p} \beta_0, \ \hat{\beta_1} \xrightarrow{p} \beta_1.$$

3. **Efficiency**: The OLS estimators are efficient, meaning that they have the smallest variance among all unbiased estimators:

$$var(\hat{\beta_0}) \leq var(\tilde{\beta_0}), var(\hat{\beta_1}) \leq var(\tilde{\beta_1}).$$

4. **Normality**: Under certain conditions, the OLS estimators are normally distributed:

$$\hat{\beta_0} \sim N(\beta_0, \sigma^2_{\beta_0}), \hat{\beta_1} \sim N(\beta_1, \sigma^2_{\beta_1}).$$

Other properties include:

- Sum of residuals is zero: $\sum_{i=1}^{n} \hat{\epsilon_i} = 0$,
- $\sum_{i=1}^{n} x_i\hat{\epsilon_i} = 0$.

## 1.3 Gauss-Markov Assumptions

The Gauss-Markov theorem outlines the conditions under which the OLS estimator is the Best Linear Unbiased Estimator (BLUE). The assumptions are:

1. **Linearity**: The relationship between the dependent variable $y$ and the independent variable $x$ is linear.
2. **Variability in the Independent Variable**: The independent variable $x$ has non-zero variance.
3. **Independence and Randomness of error terms**.
4. **Zero Conditional Mean of Error Terms**: $E(\epsilon_i | x_i) = 0, i = 1, 2, ..., n$.
5. **Homoscedasticity of Error Terms**: $var(\epsilon_i | x_i) = \sigma^2, i = 1, 2, ..., n$.
6. **Normality of Error Terms**: The error terms $\epsilon_i$ are normally distributed, with mean zero and $\sigma^2$ variance, $\epsilon_i \sim N(0, \sigma^2)$.

If these assumptions are met, the OLS estimator is the Best Linear Unbiased Estimator (BLUE), meaning that it is unbiased, has the smallest variance among all linear unbiased estimators, and is normally distributed.

## 1.4 MLE Approach

The OLS estimators can also be derived using the Maximum Likelihood Estimation (MLE) approach. The likelihood function is given by:

$$L(\beta_0, \beta_1) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y_i - \beta_0 - \beta_1x_i)^2}{2\sigma^2}\right).$$

> By assumption 3, the error terms $\epsilon_i$ are independent and identically distributed (i.i.d.), which allows us to write the likelihood function as a product of the individual likelihoods.

The log-likelihood function is:

$$\ln L(\beta_0, \beta_1) = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

Maximizing the log-likelihood function with respect to $\beta_0$ and $\beta_1$ is equivalent to minimizing the sum of squared residuals, leading to the OLS estimators.

> Notice the last part is the same as the sum of squared residuals, solving for MLE estimators is equivalent to solving for OLS estimators.

## 1.5 Variability in Data SST SSE SSR

> Note: The notation used here is same as in the lecture, is may change depending on the source.

**Total Sum of Squares (SST)**: Measures the total variability in the dependent variable $y$:

$$SST = \sum_{i=1}^{n} (y_i - \bar{y})^2.$$

**Sum of Squared Estimation/Explained (SSE)**: Measures the variability explained by the regression model:

$$SSE = \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2.$$

**Sum of Squared Residuals (SSR)**: Measures the unexplained variability in the dependent variable:

$$SSR = \sum_{i=1}^{n} \hat{\epsilon}_i^2 = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2.$$

The relationship between SST, SSE, and SSR is:

$$SST = SSE + SSR.$$

### The coefficient of determination $R^2$

It describes the proportion of the total variability in the dependent variable $y$ that is explained by the regression model. It is given by:

$$R^2 = \frac{SSE}{SST} = 1 - \frac{SSR}{SST}.$$

### Proof: SST = SSE + SSR

$$SST = \sum_{i=1}^{n} (y_i - \bar{y})^2 = \sum_{i=1}^{n} (y_i - \hat{y}_i + \hat{y}_i - \bar{y})^2.$$

Expanding the square:

$$SST = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + 2\sum_{i=1}^{n} (y_i - \hat{y}_i)(\hat{y}_i - \bar{y}) + \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2.$$

The second term is zero because:

$$\sum_{i=1}^{n} (y_i - \hat{y}_i)(\hat{y}_i - \bar{y}) =  \sum_{i=1}^{n} \epsilon_i(\hat{\beta}_0 + \hat{\beta}_1x_i - \bar{y})$$

$$= \sum_{i=1}^{n} \epsilon_i\hat{\beta}_0 + \sum_{i=1}^{n} \epsilon_i\hat{\beta}_1x_i - \sum_{i=1}^{n} \epsilon_i\bar{y} = 0.$$

> Remember that $\sum_{i=1}^{n} \epsilon_i = 0$ and $\sum_{i=1}^{n} x_i\epsilon_i = 0$.


Therefore:

$$SST = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 = SSR + SSE.$$

## 1.6 Biased on SST

I will add this part later

## 1.7 Hypothesis Testing on Beta_1

Recall: t-distribution - student's distribution

$$ T = \frac{Z}{\sqrt{\frac{Y}{D}}} ,$$

where:

- $Z \sim N(0, 1)$,
- $Y \sim \chi^2(D)$,
- $Z$ and $Y$ are independent.

When $D \rightarrow \infty$, the t-distribution converges to the standard normal distribution.

A t-test is used to test the significance of the slope coefficient $\beta_1$. The null hypothesis is:

$$H_0: \beta_1 = 0,$$
$$H_1: \beta_1 \neq 0/$$

The test statistic is given by:

$$t = \frac{\hat{\beta}_1 - \beta_1}{SE(\hat{\beta}_1)} \sim t(n-k-1),$$

where:

- $\hat{\beta}_1$ is the estimated slope coefficient,
- $\beta_1$ is the hypothesized value of the slope coefficient under the null hypothesis, typically zero,
- $SE(\hat{\beta}_1)$ is the standard error of the slope coefficient,
- $n$ is the sample size,
- $k$ is the number of independent variables in the regression model, for univariate regression $k = 1$.

The t-statistic follows a t-distribution with $n-k-1$ degrees of freedom. We reject the null hypothesis if the absolute value of the t-statistic is greater than the critical value of the t-distribution at the desired significance level.

## 1.8 F-test

We define:

**MSE**: Mean Squared Estimator

$$MSE = \frac{SSE}{k}, \text{ where } k = 1.$$

**MSR**: Mean Squared Error

$$MSR = \frac{SSR}{n-k-1}.$$

> The notation used here may be different from other sources. e.g. $MSE$ in machine learning is the Mean Squared Error, $MSE = \frac{SSR}{n}$.

For the F-test, the null hypothesis is:

$$H_0: \beta_1 = 0,$$
$$H_1: \beta_1 \neq 0.$$

The test statistic is given by:

$$F = \frac{MSE}{MSR} = \frac{SSE/k}{SSR/(n-k-1)} \sim F(k, n-k-1),$$

where:

- $k$ is the number of independent variables in the regression model, for univariate regression $k = 1$,
- $n$ is the sample size.

The F-statistic follows an F-distribution with $k$ and $n-k-1$ degrees of freedom. We reject the null hypothesis if the F-statistic is greater than the critical value of the F-distribution at the desired significance level.

## 1.9 Test based on correlation coefficient

The correlation coefficient $\rho$:

$$\rho = \frac{cov(x, y)}{\sqrt{var(x)var(y)}} = \frac{E[(x - E(x))(y - E(y))]}{\sqrt{E[(x - E(x))^2]E[(y - E(y))^2]}}$$

$$= \frac{E[(x - E(x))(\beta_0 + \beta_1x - E(\beta_0 + \beta_1x ))]}{\sqrt{E[(x - E(x))^2]E[(\beta_0 + \beta_1x - E(\beta_0 + \beta_1x ))^2]}}$$

$$= \frac{E[(x - E(x))(\beta_1x - \beta_1E(x))]}{\sqrt{E[(x - E(x))^2]E[(\beta_1x - \beta_1E(x))^2]}}$$

$$= \frac{\beta_1E[(x - E(x)^2]}{\sqrt{\beta_1E[(x - E(x))^2]E[(x - E(x))^2]}} 
$$

$$
= \frac{\beta_1}{\sqrt{\beta_1^2}} = \frac{\beta_1}{|\beta_1|}.
$$

Therefore,
$$\rho = \begin{cases} 
1, & \text{if } \beta_1 > 0, \\
-1, & \text{if } \beta_1 < 0.
\end{cases}$$

Sample correlation coefficient $R$:

$$R_{x, y} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}.$$

The test statistic is given by:

$$t = \frac{R_{x,y}\sqrt{n-k-1}}{\sqrt{1 - R_{x,y}^2}} \sim t(n-k-1).$$

The Hypothese are:

$$H_0: R_{x,y} = 0,$$
$$H_1: R_{x,y} \neq 0.$$

> This test is equivalent to the t-test on $\beta_1$. Same test statistic will be obtained.

## 1.10 Interval estimator of beta_1

$\hat{\beta}_1$ is point estimator of $\beta_1$. The interval estimator is given by:

$$(\hat{\beta}_1 - t_{\alpha/2}(n-2)SE(\hat{\beta}_1), \ \hat{\beta}_1 + t_{\alpha/2}(n-2)SE(\hat{\beta}_1)),$$

where:

- $t_{\alpha/2}(n-2)$ is the critical value of the t-distribution at the desired significance level $\alpha/2$ with $n-2$ degrees of freedom,
- $SE(\hat{\beta}_1)$ is the standard error of the slope coefficient.

## 1.11 t-test on beta_0

The t-test on the intercept $\beta_0$ is similar to the t-test on the slope coefficient $\beta_1$. The null hypothesis is:

$$H_0: \beta_0 = 0,$$
$$H_1: \beta_0 \neq 0.$$

The interval estimator of $\beta_0$ is given by:

$$(\hat{\beta}_0 - t_{\alpha/2}(n-2)SE(\hat{\beta}_0), \ \hat{\beta}_0 + t_{\alpha/2}(n-2)SE(\hat{\beta}_0)),$$

where:

- $t_{\alpha/2}(n-2)$ is the critical value of the t-distribution at the desired significance level $\alpha/2$ with $n-2$ degrees of freedom,
- $SE(\hat{\beta}_0)$ is the standard error of the intercept.

## 1.12 Subjective check of assumptions

1. **Linearity**: Check the scatter plot of the dependent variable $y$ against the independent variable $x$ to see if the relationship is linear. OLS assumes a linear relationship between the variables.
2. **Variability in the Independent Variable**: Check if the independent variable $x$ has non-zero variance. If the independent variable does not vary, it cannot explain the variability in the dependent variable.
3. **Independence and Randomness of Error Terms**: We used residuals to check this assumption. We can plot the residuals against the independent variable $x$ to see if there is any pattern or correlation, if there is a trend, the assumption is violated.
4. **Zero Conditional Mean of Error Terms**: We used residuals to check this assumption, the OLS has zero conditional mean by construction.
5. **Homoscedasticity of Error Terms**: We used residuals to check this assumption. We can plot the residuals against the fitted values to see if the variance of the residuals is constant across all values of the independent variable.
6. **Normality of Error Terms**: We used residuals to check this assumption. We can plot a Q-Q plot (Normal Probability Plot) of the residuals to see if they follow a normal distribution, if the points lie on a straight line, the residuals are normally distributed.

Constructing of the Q-Q plot:

1. Sort the residuals in ascending order, $e_{(1)} \leq e_{(2)} \leq ... \leq e_{(i)} \leq ... \leq e_{(n)}$.
2. Calculate the theoretical probability of the normal distribution using the quantile function, $(i - 0.5)/n$.
3. Theorical quantile: $z_{(i)} = \Phi^{-1}((i - 0.5)/n)$.
4. Plot the theoretical quantiles against the residuals.

## 1.13 Statistic test on assumptions

### Durbin-Watson Test for Assumption 3

We can use the Durbin-Watson test to check for autocorrelation in the residuals. The null hypothesis is that there is no autocorrelation in the residuals.

We construct following auxiliary regression:

$$\hat{\epsilon}_i = a \hat{\epsilon}_{i-1} + w_i, \ i = 2, 3, ..., n,$$

where:

- $\hat{\epsilon}_i$ is the residual for the $i$-th observation,
- $\hat{\epsilon}_{i-1}$ is the residual for the $(i-1)$-th observation,
- {$w_i$} is the white noise error term,

Hypotheses options 1:

$$H_0: a = 0,$$
$$H_1: a \neq 0.$$

Hypotheses options 2:

$$H_0: a = 0,$$
$$H_1: a > 0.$$

Hypotheses options 3:

$$H_0: a = 0,$$
$$H_1: a < 0.$$

We normally use the first two options in finance.

The test statistic is given by:

$$DW = \frac{\sum_{i=2}^{n} (\hat{\epsilon}_i - \hat{\epsilon}_{i-1})^2}{\sum_{i=1}^{n} \hat{\epsilon}_i^2}.$$

The Durbin-Watson statistic ranges from 0 to 4, with a value close to 2 indicating no autocorrelation. We reject the null hypothesis if the Durbin-Watson statistic is significantly different from 2.

Interpretation of the Durbin-Watson statistic:

- $DW < 2$: Positive autocorrelation,
- $DW > 2$: Negative autocorrelation,
- $DW = 2$: No autocorrelation.

Example, for hypothesis option 2:

$$H_0: a = 0,$$
$$H_1: a > 0.$$

If $DW < d_L$, we reject the null hypothesis in favor of the alternative hypothesis, and conclude that there is enough evidence that the error terms are positively autocorrelated in a linear form with lag 1.

### Breusch-Pagan Test for Assumption 5

We can use the Breusch-Pagan test to check for conditional heteroscedasticity in the residuals. The null hypothesis is that there is no conditional heteroscedasticity in the residuals.

We construct the auxiliary regression:

$$\hat{\epsilon}_i^2 = b_0 + b_1x_i, \ i = 1, 2, ..., n,$$

where:

- $\hat{\epsilon}_i^2$ is the squared residual for the $i$-th observation,
- $x_i$ is the independent variable,
- $b_0$ and $b_1$ are the coefficients of the auxiliary regression.

The test statistic is given by:

$$BP_{stat} = nR_{aux}^2 \sim \chi^2(k),$$

where:

- $R_{aux}^2$ is the R-squared of the auxiliary regression,
- $k$ is the number of independent variables in the auxiliary regression, for univariate regression $k = 1$.

The hypotheses are:

$$H_0: b_1 = 0,$$
$$H_1: b_1 \neq 0.$$

We reject the null hypothesis if the Breusch-Pagan test statistic is greater than the critical value of the chi-squared distribution at the desired significance level.

### White Test for Assumption 5

We can use the White test to check for conditional heteroscedasticity in the residuals. The null hypothesis is that there is no conditional heteroscedasticity in the residuals.

We construct the auxiliary regression:

$$\hat{\epsilon}_i^2 = b_0 + b_1x_i + b_2x_i^2, \ i = 1, 2, ..., n,$$

where:

- $\hat{\epsilon}_i^2$ is the squared residual for the $i$-th observation,
- $x_i$ is the independent variable,
- $b_0$, $b_1$, and $b_2$ are the coefficients of the auxiliary regression.

The test statistic is given by:

$$WT_{stat} = nR_{aux}^2 \sim \chi^2(k),$$

where:

- $R_{aux}^2$ is the R-squared of the auxiliary regression,
- $k$ is the number of independent variables in the auxiliary regression, for univariate regression $k = 2$.

The hypotheses are:

$$H_0: b_1 = b_2 = 0,$$
$$H_1: b_1 \neq 0 \text{ or } b_2 \neq 0.$$

We reject the null hypothesis if the White test statistic is greater than the critical value of the chi-squared distribution at the desired significance level.

## Conclusion

Univariate regression is a powerful tool for analyzing the relationship between a single independent variable and a dependent variable. By estimating the slope and intercept using the OLS method, we can construct a regression line that best fits the data. The OLS estimators are unbiased, consistent, and efficient under the Gauss-Markov assumptions. We can test the significance of the slope coefficient using the t-test and F-test, and check the assumptions of the regression model using various diagnostic tests. Univariate regression provides a solid foundation for more complex regression models and is widely used in economics, finance, and other fields.




