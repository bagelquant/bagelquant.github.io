---
layout: page
title: "Freeman-Tukey Variance Stabilization"
permalink: /learn/techniques/transformations/freeman-tukey/
lang: en
ref: "learn-techniques-transformations-freeman-tukey"
alternate_lang_url: /zh/learn/techniques/transformations/freeman-tukey/
---

## Key idea

Fisher’s variance stabilization transformation (usually called the Fisher z-transformation) converts a correlation coefficient into a variable whose variance is approximately constant and whose distribution is closer to normal.

It is mainly used for:

- Statistical inference on correlations
- Confidence intervals for correlation
- Hypothesis testing
- Averaging correlations
- Making correlation estimates comparable

The transformation is especially useful because raw correlations have non-constant variance.

## Motivation

Suppose sample correlation is:

$$
r\in[-1,1]
$$

The distribution of $r$ is:

- bounded between $-1$ and $1$
- asymmetric near boundaries
- variance depends on true correlation

This makes inference difficult.

For example:

- $r=0.9$ cannot move upward much
- $r=0.1$ has much larger uncertainty

Fisher's transformation removes much of this issue.

## Definition

Transform correlation $r$ into:

$$
z
=
\frac12
\ln\left(
\frac{1+r}{1-r}
\right)
$$

Equivalent form:

$$
z=\operatorname{arctanh}(r)
$$

where:

- $r$ = sample correlation
- $z$ = transformed variable

## Why it works

If:

$$
r\sim\text{Sample Correlation}
$$

then approximately:

$$
z
\sim
N\left(
\operatorname{arctanh}(\rho),
\frac1{n-3}
\right)
$$

where:

- $\rho$ = true population correlation
- $n$ = sample size

Important result:

$$
\operatorname{Var}(z)
\approx
\frac1{n-3}
$$

Notice:

the variance no longer depends on $\rho$.

This is why it is called a variance stabilization transformation.

## Example

Suppose:

$$
r=0.80
$$

Transform:

$$
z
=
\frac12
\ln\left(
\frac{1+0.8}{1-0.8}
\right)
=
1.099
$$

Now inference becomes easier.

To transform back:

$$
r
=
\tanh(z)
=
\frac{e^{2z}-1}{e^{2z}+1}
$$

## Confidence Interval Example

Observed:

$$
r=0.50,\quad n=100
$$

Step 1:

Transform:

$$
z=0.549
$$

Step 2:

Compute standard error:

$$
SE
=
\frac1{\sqrt{97}}
=
0.102
$$

95% interval:

$$
0.549\pm1.96\times0.102
$$

Result:

$$
[0.349,\ 0.749]
$$

Step 3:

Apply inverse transform:

$$
r\in[0.34,\ 0.63]
$$

## Relationship to Other Variance Stabilization Methods

| Data Type         | Transformation     |
| ----------------- | ------------------ |
| Correlation       | Fisher z           |
| Proportion        | Arcsin square root |
| Count (Poisson)   | Square root        |
| Positive skew     | Box–Cox            |
| General variables | Yeo–Johnson        |

## Usage in Quantitative Finance

Fisher transformation appears frequently in quant research:

### Information coefficient (IC)

Convert daily IC:

$$
IC_t
\rightarrow
z_t
=
\operatorname{arctanh}(IC_t)
$$

before averaging.

### Correlation estimation

Stabilize rolling factor correlations.

### Covariance shrinkage

Work in transformed correlation space.

### Signal research

Compare predictive correlations across periods with different sample sizes.

Typical workflow:

$$
\text{Correlation}
\rightarrow
\text{Fisher z}
\rightarrow
\text{Average / Test}
\rightarrow
\text{Inverse transform}
$$

This is one reason IC statistics are often treated using Fisher transforms rather than averaging raw correlations directly.