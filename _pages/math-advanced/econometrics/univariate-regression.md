---
title: "Univariate Regression"
layout: page
permalink: /econometrics/univariate-regression/

nav: "econometrics"
---

Univariate regression is a foundational econometric technique that models the relationship between a single independent variable and a dependent variable. It forms the basis for more advanced models, such as multivariable and logistic regression. By analyzing the linear association between variables, univariate regression reveals how changes in the independent variable affect the dependent variable.

For random variables $x$ and $y$, the univariate regression model is:

$$y = \beta_0 + \beta_1x + \epsilon,$$

where:

- $y$: dependent variable
- $x$: independent variable
- $\beta_0$: intercept
- $\beta_1$: slope
- $\epsilon$: error term

This model describes a linear relationship between $x$ and $y$, but the true values of $\beta_0$ and $\beta_1$ are unknown. Our objective is to estimate these parameters from sample data and construct the best-fitting regression line.

## 1.1 How to Find $\beta_0$ and $\beta_1$

**First attempt:**

We might try minimizing the sum of residuals: $\sum_{i=1}^{n} \epsilon_i$. However, this is ineffective because positive and negative residuals can offset each other.

**Second attempt:**

To avoid cancellation, we could minimize the sum of absolute residuals: $\sum_{i=1}^{n} |\epsilon_i|$. Yet, this approach leads to a non-differentiable function, complicating optimization.

**Best approach:**

The standard method is to minimize the sum of squared residuals, known as Ordinary Least Squares (OLS):

$$\sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

> The hats on $\hat\beta_0$ and $\hat\beta_1$ indicate they are estimators, not the true parameters. Similarly, $\hat{\epsilon}_i$ is the residual for observation $i$, not the true error term.

## 1.2 OLS Estimation

$\hat{\beta}_0$ and $\hat{\beta}_1$ are the OLS estimators of $\beta_0$ and $\beta_1$, found by minimizing the sum of squared residuals:

$$\min S(\beta_0, \beta_1) = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

The solutions are:

$$\begin{cases}
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x} \\
\hat{\beta}_1 = \frac{\bar{x}\bar{y} - \overline{xy}}{\bar{x}^2 - \overline{x^2}} = \frac{cov(x, y)}{var(x)}
\end{cases}$$

where:

- $\bar{x}$: mean of $x$
- $\bar{y}$: mean of $y$
- $\overline{xy}$: mean of $xy$
- $\overline{x^2}$: mean of $x^2$
- $cov(x, y)$: covariance of $x$ and $y$
- $var(x)$: variance of $x$

> OLS estimators $\hat{\beta}_0$ and $\hat{\beta}_1$ are unbiased and consistent estimators of the true parameters.

### Proof of OLS Estimators

To solve for $\hat{\beta}_0$ and $\hat{\beta}_1$, minimize the sum of squared residuals:

$$\min \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

Take partial derivatives with respect to $\beta_0$ and $\beta_1$:

$$
\begin{cases}
\frac{\partial S}{\partial \beta_0} = -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i) = 0 \\
\frac{\partial S}{\partial \beta_1} = -2 \sum_{i=1}^{n} x_i(y_i - \beta_0 - \beta_1x_i) = 0
\end{cases}
$$

$$
\begin{cases}
n\bar{y} - n\beta_0 - \bar{x} \beta_1 = 0 \\
n\overline{xy} - n\beta_0\bar{x} - n\overline{x^2}\beta_1 = 0
\end{cases}
$$

Solving yields:

$$
\begin{cases}
\beta_0 = \bar{y} - \beta_1\bar{x} \\
\beta_1 = \frac{\overline{xy} - \bar{x}\bar{y}}{\overline{x^2} - \bar{x}^2}
\end{cases}
$$

### Properties of OLS Estimators

- **Unbiasedness**: $E(\hat{\beta}_0) = \beta_0$, $E(\hat{\beta}_1) = \beta_1$
- **Consistency**: $\hat{\beta}_0 \xrightarrow{p} \beta_0$, $\hat{\beta}_1 \xrightarrow{p} \beta_1$
- **Efficiency**: $var(\hat{\beta}_0) \leq var(\tilde{\beta}_0)$, $var(\hat{\beta}_1) \leq var(\tilde{\beta}_1)$
- **Normality**: $\hat{\beta}_0 \sim N(\beta_0, \sigma^2_{\beta_0})$, $\hat{\beta}_1 \sim N(\beta_1, \sigma^2_{\beta_1})$

Other key results:

- $\sum_{i=1}^{n} \hat{\epsilon}_i = 0$
- $\sum_{i=1}^{n} x_i\hat{\epsilon}_i = 0$

## 1.3 Gauss-Markov Assumptions

The Gauss-Markov theorem specifies when the OLS estimator is the Best Linear Unbiased Estimator (BLUE). The assumptions are:

1. **Linearity**: The relationship between $y$ and $x$ is linear.
2. **Variability in $x$**: The independent variable $x$ has non-zero variance.
3. **Independence and randomness of errors**.
4. **Zero conditional mean**: $E(\epsilon_i \mid x_i) = 0$
5. **Homoscedasticity**: $var(\epsilon_i \mid x_i) = \sigma^2$
6. **Normality**: $\epsilon_i \sim N(0, \sigma^2)$

If these hold, OLS is BLUE: unbiased, minimum variance among linear unbiased estimators, and normally distributed.

## 1.4 MLE Approach

OLS estimators can also be derived via Maximum Likelihood Estimation (MLE). The likelihood function is:

$$L(\beta_0, \beta_1) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y_i - \beta_0 - \beta_1x_i)^2}{2\sigma^2}\right).$$

> By assumption 3, errors $\epsilon_i$ are i.i.d., so the likelihood is a product of individual likelihoods.

The log-likelihood is:

$$\ln L(\beta_0, \beta_1) = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1x_i)^2.$$

Maximizing the log-likelihood with respect to $\beta_0$ and $\beta_1$ is equivalent to minimizing the sum of squared residuals, yielding the OLS estimators.

> The last term matches the OLS objective, so MLE and OLS estimators coincide.

## 1.5 Variability in Data: SST, SSE, SSR

> Notation follows the lecture; it may differ in other sources.

- **Total Sum of Squares (SST)**: Total variability in $y$:

$$SST = \sum_{i=1}^{n} (y_i - \bar{y})^2.$$

- **Sum of Squares Explained (SSE)**: Variability explained by the model:

$$SSE = \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2.$$

- **Sum of Squared Residuals (SSR)**: Unexplained variability:

$$SSR = \sum_{i=1}^{n} \hat{\epsilon}_i^2 = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2.$$

These satisfy:

$$SST = SSE + SSR.$$

### Coefficient of Determination $R^2$

$R^2$ measures the proportion of total variability in $y$ explained by the model:

$$R^2 = \frac{SSE}{SST} = 1 - \frac{SSR}{SST}.$$

### Proof: $SST = SSE + SSR$

$$SST = \sum_{i=1}^{n} (y_i - \bar{y})^2 = \sum_{i=1}^{n} (y_i - \hat{y}_i + \hat{y}_i - \bar{y})^2.$$

Expanding:

$$SST = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + 2\sum_{i=1}^{n} (y_i - \hat{y}_i)(\hat{y}_i - \bar{y}) + \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2.$$

The middle term is zero because:

$$\sum_{i=1}^{n} (y_i - \hat{y}_i)(\hat{y}_i - \bar{y}) = \sum_{i=1}^{n} \epsilon_i(\hat{\beta}_0 + \hat{\beta}_1x_i - \bar{y}) = 0.$$

> Recall $\sum_{i=1}^{n} \epsilon_i = 0$ and $\sum_{i=1}^{n} x_i\epsilon_i = 0$.

Thus:

$$SST = SSR + SSE.$$

## 1.6 Bias in SST

*To be added later.*

## 1.7 Hypothesis Testing on $\beta_1$

Recall the t-distribution:

$$ T = \frac{Z}{\sqrt{Y/D}} ,$$

where $Z \sim N(0, 1)$, $Y \sim \chi^2(D)$, and $Z$, $Y$ are independent. As $D \to \infty$, the t-distribution approaches the standard normal.

A t-test assesses the significance of $\beta_1$:

$$H_0: \beta_1 = 0$$
$$H_1: \beta_1 \neq 0$$

Test statistic:

$$t = \frac{\hat{\beta}_1 - \beta_1}{SE(\hat{\beta}_1)} \sim t(n-k-1),$$

where:

- $\hat{\beta}_1$: estimated slope
- $\beta_1$: hypothesized value (usually 0)
- $SE(\hat{\beta}_1)$: standard error of $\hat{\beta}_1$
- $n$: sample size
- $k$: number of independent variables ($k=1$ for univariate)

Reject $H_0$ if $|t|$ exceeds the critical value at the chosen significance level.

## 1.8 F-test

Define:

- **MSE** (Mean Squared Explained):

$$MSE = \frac{SSE}{k}, \text{ where } k = 1.$$

- **MSR** (Mean Squared Residual):

$$MSR = \frac{SSR}{n-k-1}.$$

> Notation may differ in other sources (e.g., in machine learning, $MSE = \frac{SSR}{n}$).

For the F-test:

$$H_0: \beta_1 = 0$$
$$H_1: \beta_1 \neq 0$$

Test statistic:

$$F = \frac{MSE}{MSR} = \frac{SSE/k}{SSR/(n-k-1)} \sim F(k, n-k-1),$$

where $k$ is the number of independent variables ($k=1$), $n$ is the sample size. Reject $H_0$ if $F$ exceeds the critical value.

## 1.9 Test Based on Correlation Coefficient

The correlation coefficient $\rho$:

$$\rho = \frac{cov(x, y)}{\sqrt{var(x)var(y)}} = \frac{E[(x - E(x))(y - E(y))]}{\sqrt{E[(x - E(x))^2]E[(y - E(y))^2]}}$$

$$= \frac{E[(x - E(x))(\beta_0 + \beta_1x - E(\beta_0 + \beta_1x ))]}{\sqrt{E[(x - E(x))^2]E[(\beta_0 + \beta_1x - E(\beta_0 + \beta_1x ))^2]}}$$

$$= \frac{E[(x - E(x))(\beta_1x - \beta_1E(x))]}{\sqrt{E[(x - E(x))^2]E[(\beta_1x - \beta_1E(x))^2]}}$$

$$= \frac{\beta_1E[(x - E(x))^2]}{\sqrt{\beta_1^2E[(x - E(x))^2]E[(x - E(x))^2]}}$$

$$= \frac{\beta_1}{|\beta_1|}.$$

Therefore,
$$\rho = \begin{cases} 1, & \text{if } \beta_1 > 0, \\ -1, & \text{if } \beta_1 < 0. \end{cases}$$

Sample correlation coefficient $R$:

$$R_{x, y} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}.$$

Test statistic:

$$t = \frac{R_{x,y}\sqrt{n-k-1}}{\sqrt{1 - R_{x,y}^2}} \sim t(n-k-1).$$

Hypotheses:

$$H_0: R_{x,y} = 0$$
$$H_1: R_{x,y} \neq 0$$

> This test is equivalent to the t-test on $\beta_1$; both yield the same statistic.

## 1.10 Interval Estimator of $\beta_1$

$\hat{\beta}_1$ is a point estimator. The interval estimator is:

$$(\hat{\beta}_1 - t_{\alpha/2}(n-2)SE(\hat{\beta}_1), \ \hat{\beta}_1 + t_{\alpha/2}(n-2)SE(\hat{\beta}_1)),$$

where:

- $t_{\alpha/2}(n-2)$: critical value of the t-distribution at significance level $\alpha/2$ with $n-2$ degrees of freedom
- $SE(\hat{\beta}_1)$: standard error of $\hat{\beta}_1$

## 1.11 t-test on $\beta_0$

The t-test for the intercept $\beta_0$ mirrors that for $\beta_1$:

$$H_0: \beta_0 = 0$$
$$H_1: \beta_0 \neq 0$$

Interval estimator:

$$(\hat{\beta}_0 - t_{\alpha/2}(n-2)SE(\hat{\beta}_0), \ \hat{\beta}_0 + t_{\alpha/2}(n-2)SE(\hat{\beta}_0)),$$

where $t_{\alpha/2}(n-2)$ is the critical value and $SE(\hat{\beta}_0)$ is the standard error of the intercept.

## 1.12 Subjective Check of Assumptions

1. **Linearity**: Plot $y$ vs. $x$ to visually assess linearity.
2. **Variability in $x$**: Ensure $x$ has non-zero variance; otherwise, it cannot explain $y$.
3. **Independence of Errors**: Plot residuals vs. $x$ to check for patterns; trends indicate violation.
4. **Zero Conditional Mean**: OLS ensures zero mean of residuals by construction.
5. **Homoscedasticity**: Plot residuals vs. fitted values to check for constant variance.
6. **Normality of Errors**: Use a Q-Q plot of residuals; points on a straight line indicate normality.

To construct a Q-Q plot:

1. Sort residuals: $e_{(1)} \leq ... \leq e_{(n)}$
2. Compute theoretical probabilities: $(i - 0.5)/n$
3. Theoretical quantile: $z_{(i)} = \Phi^{-1}((i - 0.5)/n)$
4. Plot theoretical quantiles vs. residuals

## 1.13 Statistical Tests on Assumptions

### Durbin-Watson Test (Assumption 3)

The Durbin-Watson test detects autocorrelation in residuals. The null hypothesis is no autocorrelation.

Auxiliary regression:

$$\hat{\epsilon}_i = a \hat{\epsilon}_{i-1} + w_i, \ i = 2, ..., n$$

where $w_i$ is white noise.

Hypotheses (option 1):

$$H_0: a = 0$$
$$H_1: a \neq 0$$

Test statistic:

$$DW = \frac{\sum_{i=2}^{n} (\hat{\epsilon}_i - \hat{\epsilon}_{i-1})^2}{\sum_{i=1}^{n} \hat{\epsilon}_i^2}.$$

Interpretation:

- $DW < 2$: Positive autocorrelation
- $DW > 2$: Negative autocorrelation
- $DW = 2$: No autocorrelation

If $DW < d_L$, reject $H_0$ in favor of positive autocorrelation.

### Breusch-Pagan Test (Assumption 5)

The Breusch-Pagan test checks for conditional heteroscedasticity. The null hypothesis is homoscedasticity.

Auxiliary regression:

$$\hat{\epsilon}_i^2 = b_0 + b_1x_i$$

Test statistic:

$$BP_{stat} = nR_{aux}^2 \sim \chi^2(k)$$

where $R_{aux}^2$ is the R-squared from the auxiliary regression, $k=1$.

Hypotheses:

$$H_0: b_1 = 0$$
$$H_1: b_1 \neq 0$$

Reject $H_0$ if $BP_{stat}$ exceeds the critical value.

### White Test (Assumption 5)

The White test also checks for heteroscedasticity.

Auxiliary regression:

$$\hat{\epsilon}_i^2 = b_0 + b_1x_i + b_2x_i^2$$

Test statistic:

$$WT_{stat} = nR_{aux}^2 \sim \chi^2(k)$$

where $k=2$.

Hypotheses:

$$H_0: b_1 = b_2 = 0$$
$$H_1: b_1 \neq 0 \text{ or } b_2 \neq 0$$

Reject $H_0$ if $WT_{stat}$ exceeds the critical value.

## Conclusion

Univariate regression is a powerful tool for analyzing the relationship between a single independent and dependent variable. By estimating the slope and intercept using OLS, we obtain a regression line that best fits the data. Under the Gauss-Markov assumptions, OLS estimators are unbiased, consistent, and efficient. We can test the significance of coefficients using t- and F-tests, and check model assumptions with diagnostic tests. Univariate regression provides a solid foundation for more advanced econometric models and is widely used in economics, finance, and beyond.

Next up: [multivariable regression](multivariable-regression.md)
