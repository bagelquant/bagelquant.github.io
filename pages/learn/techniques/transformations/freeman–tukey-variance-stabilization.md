---
layout: page
permalink: /learn/techniques/transformations/freeman–tukey-variance-stabilization/
lang: en
ref: "learn-techniques-transformations-freeman-tukey-variance-stabilization"
alternate_lang_url: /zh/learn/techniques/transformations/freeman-tukey-variance-stabilization/
---
# Freeman–Tukey Variance Stabilization

## Key idea

Freeman–Tukey variance stabilization transformation is a transformation designed for count and proportion data, especially when observations follow a Poisson or Binomial distribution.

Its goal is the same as other variance stabilization methods:

- Reduce dependence between mean and variance
- Make distributions more Gaussian
- Improve statistical inference
- Improve averaging and regression

Compared with Anscombe, Freeman–Tukey is another square-root-based correction with better finite-sample behavior in some settings.

## Motivation

For count data:

$$
X\sim\text{Poisson}(\lambda)
$$

we have:

$$
E[X]=\lambda
$$

and

$$
\operatorname{Var}(X)=\lambda
$$

Large values naturally have larger noise.

Example:

| Count | Standard deviation |
| ----- | ------------------ |
| 1     | 1                  |
| 100   | 10                 |

This changing variance makes modeling unstable.

Variance stabilization tries to produce:

$$
\operatorname{Var}(Y)\approx\text{constant}
$$

after transformation.

## Definition (Poisson Version)

For count variable:

$$
X\sim\text{Poisson}(\lambda)
$$

Freeman–Tukey transform:

$$
Y
=
\sqrt X
+
\sqrt{X+1}
$$

where:

- $X$ = original count
- $Y$ = transformed variable

For large counts:

$$
Y
\approx
2\sqrt X
$$

which resembles Anscombe.

## Interpretation

Compare several transforms:

| Method | Formula |
|---|---|
| Square root | $\sqrt X$ |
| Anscombe | $2\sqrt{X+\frac38}$ |
| Freeman–Tukey | $\sqrt X+\sqrt{X+1}$ |

All are approximations to the same variance stabilization objective.

Freeman–Tukey often behaves slightly better near:

$$
X\approx0
$$

because of the extra correction term.

## Example

Original counts:

$$
X=[0,1,4,9,25]
$$

Transform:

$$
Y=
[
1.00,
2.41,
4.24,
6.16,
10.10
]
$$

Notice:

the spacing becomes more uniform.

## Why it works

Using the delta method:

Suppose:

$$
Y=g(X)
$$

then:

$$
\operatorname{Var}(Y)
\approx
(g'(\lambda))^2
\operatorname{Var}(X)
$$

For Poisson:

$$
\operatorname{Var}(X)=\lambda
$$

To obtain constant variance:

$$
g'(\lambda)
\propto
\frac1{\sqrt\lambda}
$$

Integrating gives:

$$
g(\lambda)\propto\sqrt\lambda
$$

Freeman–Tukey adds a finite-sample correction.

Result:

$$
\operatorname{Var}(Y)\approx1
$$

approximately independent of $\lambda$.

## Freeman–Tukey for Proportions

For Binomial proportion:

Observed:

$$
p=\frac{x}{n}
$$

Freeman–Tukey double-arcsine transform:

$$
Y
=
\arcsin\sqrt{\frac{x}{n+1}}
+
\arcsin\sqrt{\frac{x+1}{n+1}}
$$

This is widely used in:

- meta-analysis
- proportion aggregation
- rare event estimation

because it handles:

$$
p=0,\quad p=1
$$

more gracefully.

## Relationship to Other Variance Stabilization Methods

| Data Type | Transformation |
|---|---|
| Correlation | Fisher z |
| Poisson | Freeman–Tukey |
| Poisson | Anscombe |
| Proportion | Arcsin / Freeman–Tukey |
| Positive skew | Box–Cox |

## Anscombe vs Freeman–Tukey

| Property | Anscombe | Freeman–Tukey |
|---|---|---|
| Formula | $2\sqrt{X+\frac38}$ | $\sqrt X+\sqrt{X+1}$ |
| Poisson | Yes | Yes |
| Small count behavior | Very good | Very good |
| Simplicity | Slightly cleaner | Symmetric correction |

For moderate and large counts they become nearly identical.

## Usage in Quantitative Finance

Direct use is uncommon, but the idea appears for event-count features:

Examples:

- Trade count
- News count
- Analyst revision count
- Order arrival count
- Alternative data event intensity

Typical preprocessing:

$$
\text{Count}
\rightarrow
\text{Freeman–Tukey}
\rightarrow
\text{Z-score}
\rightarrow
\text{Factor}
$$

The underlying principle:

> If signal magnitude increases measurement noise, transform before estimating relationships.ggG
