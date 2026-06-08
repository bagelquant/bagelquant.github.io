---
layout: page
permalink: /learn/techniques/transformations/anscombe-variance-stabilization/
lang: en
ref: "learn-techniques-transformations-anscombe-variance-stabilization"
alternate_lang_url: /zh/learn/techniques/transformations/anscombe-variance-stabilization/
---
# Anscombe Variance Stabilization

## Key idea

Anscombe variance stabilization transformation is a transformation designed primarily for Poisson-distributed count data.

Its goal is to convert data whose variance depends on the mean into a variable with approximately constant variance.

For Poisson data:

$$
X\sim\text{Poisson}(\lambda)
$$

the variance equals the mean:

$$
\operatorname{Var}(X)=\lambda
$$

This causes heteroscedasticity.

Anscombe transformation makes the transformed variable approximately Gaussian with nearly constant variance.

## Motivation

Suppose we observe counts:

$$
[1,4,9,25,100]
$$

For Poisson processes:

| Mean | Variance |
| ---- | -------- |
| 1    | 1        |
| 10   | 10       |
| 100  | 100      |

Large observations naturally have larger noise.

Direct modeling becomes difficult.

Variance stabilization attempts to make:

$$
\operatorname{Var}(Y)\approx\text{constant}
$$

after transformation.

## Definition

For Poisson variable:

$$
X\sim\text{Poisson}(\lambda)
$$

Anscombe transform:

$$
Y
=
2\sqrt{X+\frac38}
$$

where:

- $X$ = original count
- $Y$ = transformed value

After transformation:

$$
Y
\approx
N(2\sqrt{\lambda},1)
$$

approximately.

Important result:

$$
\operatorname{Var}(Y)\approx1
$$

independent of $\lambda$.

This is the variance stabilization property.

## Why not just square root?

A simple variance stabilization for Poisson is:

$$
Y=\sqrt X
$$

Using the delta method:

$$
\operatorname{Var}(\sqrt X)
\approx
\frac14
$$

Anscombe improves small-sample behavior by adding:

$$
\frac38
$$

inside the square root.

Comparison:

| Method      | Transformation      |
| ----------- | ------------------- |
| Simple sqrt | $\sqrt X$           |
| Anscombe    | $2\sqrt{X+\frac38}$ |

Anscombe is more accurate for small counts.

## Example

Original counts:

$$
X=[0,1,4,9,25]
$$

Transform:

$$
Y
=
[
1.225,
2.345,
4.183,
6.124,
10.075
]
$$

Notice:

relative variability becomes more uniform.

## Inverse Transformation

Approximate inverse:

$$
X
\approx
\left(
\frac Y2
\right)^2
-\frac38
$$

More accurate inverse formulas exist for low-count settings.

## Derivation (Delta Method Intuition)

Suppose:

$$
Y=g(X)
$$

Variance propagation:

$$
\operatorname{Var}(Y)
\approx
(g'(\lambda))^2
\operatorname{Var}(X)
$$

Since:

$$
\operatorname{Var}(X)=\lambda
$$

choose:

$$
g'(\lambda)
\propto
\frac1{\sqrt\lambda}
$$

Integrating:

$$
g(\lambda)
\propto
\sqrt\lambda
$$

which leads to the square-root family.

Anscombe adds the correction term.

## Relationship to Other Variance Stabilization Transformations

| Data Type | Transformation |
|---|---|
| Poisson count | Anscombe |
| Correlation | Fisher z |
| Proportion | Arcsin square root |
| Positive skew | Box–Cox |
| General numeric | Yeo–Johnson |

## Usage in Quantitative Finance

Anscombe itself is uncommon in equity alpha research but the idea appears often.

Applications with count-like variables:

- News arrival counts
- Number of analyst revisions
- Trade counts
- Event frequencies
- Alternative data event streams

Example:

$$
\text{Trade Count}
\rightarrow
\text{Anscombe}
\rightarrow
\text{Z-score}
\rightarrow
\text{Factor}
$$

The broader principle is more important than the exact formula:

> When variance grows with signal strength, transform before modeling.
