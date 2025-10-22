---
title: "Quant Interview FAQ — Linear Regression & Statistical Modeling"
permalink: /quant-interview-faq-linear-regression/
excerpt: "A cheat sheet of common linear regression and statistical modeling concepts for quant interviews."
tags:
    - linear-regression
    - statistical-modeling
    - interview
header:
  overlay_image: /assets/images/headers/linear-regression-faq-header.png
  overlay_filter: 0.8
---

Linear regression is one of the most fundamental yet widely tested topics in quantitative interviews. It forms the backbone of econometrics, risk modeling, and machine learning pipelines. Below are frequently asked questions that test both conceptual understanding and practical implementation.

> Full topic regarding **econometrics** can be found in [Econometrics](https://bagelquant.com/econometrics/) page.

### 🧠 1. What is linear regression and when is it appropriate?

**Short Answer:**  
Linear regression models a dependent variable $y$ as a linear function of one or more independent variables $x_i$, assuming the relationship is approximately linear and residuals are random.

**Example:**  
Predicting stock returns based on beta, size, and value exposures:

$$
R_i = \alpha + \beta_1 \text{MKT} + \beta_2 \text{SMB} + \beta_3 \text{HML} + \epsilon_i
$$

**Detailed Explanation:**  
The model estimates coefficients $\beta$ by minimizing the sum of squared residuals:

$$
\min_{\beta} \sum_{i=1}^n (y_i - X_i'\beta)^2
$$
It’s appropriate when the underlying relationship is roughly linear, variables are continuous, and residuals satisfy classical OLS assumptions (linearity, independence, homoskedasticity, no perfect multicollinearity, and normally distributed errors for inference).

### 🧩 2. What are the assumptions of OLS and why do they matter?

1 **Linearity:** Model is linear in parameters.    
2 **Random Sampling:** Each observation $(x_i, y_i)$ is iid.  
3 **No Perfect Multicollinearity:** No independent variable is a perfect linear combination of others.  
4 **Zero Conditional Mean:**: eusures unbiasedness.

$$
E[\epsilon | X]=0
$$


5 **Homoskedasticity:** 

$$
Var(\epsilon | X)=\sigma^2
$$

6 **Normality (optional):** Needed for valid t and F tests.

**Why it matters:**  

Violation of these assumptions affects unbiasedness, efficiency, and inference validity. For example, heteroskedasticity invalidates standard errors, and multicollinearity inflates variance of coefficient estimates.

### 📈 3. How do you interpret $R^2$ and Adjusted $R^2$?

- **$R^2$:** Fraction of variance in $y$ explained by the model.  
$$R^2 = 1 - \frac{\text{SSR}}{\text{SST}}$$
- **Adjusted $R^2$:** Penalizes model complexity to prevent overfitting.
$$R^2_{adj} = 1 - (1 - R^2)\frac{n-1}{n-k-1}$$

**Interview Tip:** Adding more variables always increases $R^2$, but not necessarily predictive power — adjusted $R^2$ is more robust for model comparison.

### ⚖️ 4. What is multicollinearity and how can you detect it?

**Definition:** When two or more independent variables are highly correlated, leading to unstable coefficient estimates.

**Detection:**  

- High correlation matrix entries  
- Variance Inflation Factor (VIF): $VIF_i = 1/(1 - R_i^2)$  
- Large standard errors or sign flips in coefficients  

**Remedies:** Drop redundant variables, use regularization (Ridge/Lasso), or principal component regression.

### 📊 5. What is heteroskedasticity and how do you handle it?

**Definition:** When the variance of residuals depends on $X$ (non-constant error variance).

**Consequences:**  

- OLS estimates remain unbiased but inefficient.  
- Standard errors are biased → invalid t-tests.

**Tests and Fixes:**  

- **Breusch–Pagan / White Test** for detection.  
- **Robust Standard Errors (Huber–White)** or **Weighted Least Squares (WLS)** for correction.

### 🔍 6. What’s the difference between OLS, GLS, and MLE?

| Method | Core Idea | When Used |
|:--|:--|:--|
| OLS | Minimize squared residuals | Homoskedastic, uncorrelated errors |
| GLS | Weight residuals by covariance matrix | Heteroskedastic or correlated errors |
| MLE | Maximize likelihood under distributional assumptions | When error distribution known or in probabilistic models |

### 🧮 7. How do you evaluate regression models?

1. **In-sample fit:** $R^2$, Adjusted $R^2$, RMSE  
2. **Out-of-sample performance:** Cross-validation, rolling regression  
3. **Statistical tests:** t-test (individual significance), F-test (joint significance)  
4. **Economic sense:** Coefficient signs and magnitudes consistent with theory  

**Quant Tip:** In asset pricing, we often test factor significance by **cross-sectional regression t-stats** and **Gibbons–Ross–Shanken (GRS) tests**.

### 💡 8. What is regularization and why is it useful?

**Purpose:** Reduce overfitting and handle multicollinearity by adding penalty terms to the loss function.

- **Ridge:** L2 penalty, shrinks coefficients continuously.  

$$
\min_\beta \sum (y_i - X_i'\beta)^2 + \lambda \sum \beta_j^2
$$  
- **Lasso:** L1 penalty, induces sparsity.  

$$
\min_\beta \sum (y_i - X_i'\beta)^2 + \lambda \sum |\beta_j|
$$  
- **Elastic Net:** Combination of both.

**Application:** In quant research, used for factor selection or constructing parsimonious alpha models.

### 🧭 9. What are residual diagnostics and why are they important?

Residuals help detect model misspecification.  
Plotting residuals vs. fitted values should show no patterns.  
Key diagnostics include:

- Normality test (Jarque–Bera)  
- Autocorrelation (Durbin–Watson, Ljung–Box)  
- Leverage & influence (Cook’s distance)  

In time-series regression, persistent autocorrelation indicates you may need ARIMA or HAC standard errors.

### 🚀 10. What are common extensions of linear regression?

| Model | Description | Quant Application |
|:--|:--|:--|
| Time-Series Regression | Accounts for autocorrelated errors | Predicting returns over time |
| Panel Regression | Combines cross-section and time | Factor exposure studies |
| Logistic / Probit | Models binary outcomes | Credit risk, default prediction |
| Quantile Regression | Models conditional quantiles | Risk (VaR, tail behavior) |
| Bayesian Regression | Incorporates priors | Hierarchical or shrinkage models |

### 🧾 Summary

Linear regression underpins nearly all quantitative modeling frameworks — from estimating betas to calibrating risk models and ML pipelines. A deep understanding of its assumptions, diagnostics, and extensions is key to explaining not just *what* a model predicts, but *why* it behaves that way.
