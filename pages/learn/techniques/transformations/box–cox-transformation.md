---
layout: page
permalink: /learn/techniques/transformations/box–cox-transformation/
lang: en
ref: "learn-techniques-transformations-box-cox-transformation"
alternate_lang_url: /zh/learn/techniques/transformations/box–cox-transformation/
---
# Box–Cox Transformation

## Key idea

Box–Cox transformation is a family of power transformations used to transform a variable into a more model-friendly form.

Its main goals are:

- Reduce skewness
- Stabilize variance
- Improve normality
- Improve linear relationships
- Make statistical assumptions easier to satisfy

It is commonly used before regression, statistical modeling, and occasionally factor preprocessing.

## Definition

For a positive variable $y>0$:

$$
y^{(\lambda)}=
\begin{cases}
\frac{y^\lambda-1}{\lambda}, & \lambda\neq0\
\ln(y), & \lambda=0
\end{cases}
$$

where:

- $y$ = original value
- $\lambda$ = transformation parameter

## Interpretation of $\lambda$

Common values:

| $\lambda$ | Transformation    |
| --------- | ----------------- |
| $1$       | No transformation |
| $0.5$     | Square root       |
| $0$       | Log transform     |
| $-1$      | Reciprocal        |

As $\lambda$ decreases, large observations are compressed more aggressively.

## Example

Original data:

$$
[1,2,4,8,16]
$$

If $\lambda=0$:

$$
[0,0.69,1.39,2.08,2.77]
$$

(log transform)

If $\lambda=0.5$:

$$
[1,1.41,2,2.83,4]
$$

(square-root transform)

Large values become less dominant.

## Selecting $\lambda$

Typically choose $\lambda$ using Maximum Likelihood Estimation (MLE):

$$
\lambda^*
=
\arg\max_\lambda
L(\lambda)
$$

The objective is to find the transformation that makes the transformed data as close to Gaussian as possible.

Example:

python from scipy.stats import boxcox  x_transformed, lam = boxcox(x) print(lam) 

## Limitations

Box–Cox requires:

$$
y>0
$$

If data contains zero or negative values:

- Shift the variable:

python x = x - x.min() + 1 

- Or use Yeo–Johnson transformation

## Relationship with Other Transformations

| Method | Supports Negative Values | Parameterized |
|---|---|---|
| Log | No | No |
| Box–Cox | No | Yes |
| Yeo–Johnson | Yes | Yes |
| Rank Gaussianization | Yes | No |

## Usage in Quantitative Finance

Box–Cox is less common than rank normalization and z-score normalization in cross-sectional equity models.

Typical applications:

- Market capitalization
- Trading volume
- Turnover
- Accounting variables
- Highly skewed alternative data

Example preprocessing pipeline:

$$
\text{Raw Factor}
\rightarrow
\text{Winsorize}
\rightarrow
\text{Box–Cox}
\rightarrow
\text{Z-score}
\rightarrow
\text{Neutralize}
$$

In cross-sectional factor research, Box–Cox is usually estimated independently for each date rather than globally across time.
