---
layout: page
title: "Kelly Criterion"
permalink: /learn/techniques/portfolio/kelly-criterion/
lang: en
ref: "learn-techniques-portfolio-kelly-criterion"
alternate_lang_url: /zh/learn/techniques/portfolio/kelly-criterion/
---

## Key idea

Kelly Criterion is a position sizing framework that determines the fraction of capital to allocate in order to maximize long-run geometric wealth growth.

Unlike mean–variance optimization, Kelly directly optimizes compound growth.

Core question:

> Given an edge and uncertainty, how much capital should I bet?

The result is the theoretically optimal leverage under repeated independent opportunities.

## Definition

For a binary bet:

- Probability of winning: $p$
- Probability of losing: $q=1-p$
- Net payoff ratio: $b$

Optimal fraction of wealth to invest:

$$
f^=\frac{bp-q}{b}
$$

where:

- $f^$ = fraction of total wealth to allocate
- $b$ = profit per unit risked
- $p$ = win probability
- $q$ = loss probability

Special case: even odds ($b=1$)

$$
f^=2p-1
$$

Examples:

- $p=0.60\rightarrow f=0.2$ 
- $p=0.55\rightarrow f=0.1$
- $p=0.50\rightarrow f=0$

No edge → no bet.

## Derivation

Assume repeated investment.

Wealth evolves as:

$$
W_T
=
W_0
\prod_t(1+fR_t)
$$

Kelly maximizes expected log wealth:

$$
\max_f E[\log(1+fR)]
$$

The logarithm captures compound growth.

Equivalent objective:

$$
\max_f
\lim_{T\to\infty}
\frac1T\log\left(\frac{W_T}{W_0}\right)
$$

## Continuous Return Version

For continuous returns:

Assume:

$$
R\sim(\mu,\sigma^2)
$$

Approximate Kelly leverage:

$$
f^
=
\frac{\mu}{\sigma^2}
$$

where:

- $\mu$ = expected excess return
- $\sigma^2$ = variance

Interpretation:

- Higher alpha → larger position
- Higher uncertainty → smaller position

This formula appears frequently in quantitative finance.

## Example

Strategy:

- Annual alpha: $8%$
- Volatility: $20%$

Then:

$$
f^*
=
\frac{0.08}{0.2^2}
=
2
$$

Kelly recommends:

$$
200%
$$

gross exposure.

Meaning:

- $100%$ capital
- borrow another $100%$

## Fractional Kelly

Full Kelly is often too aggressive.

Common practice:

$$
f=\lambda f^*
$$

with:

$$
\lambda\in[0.25,0.50]
$$

Typical choices:

- Quarter Kelly
- Half Kelly

Reasons:

- estimation error
- nonstationarity
- drawdown control
- transaction cost

## Relationship to Portfolio Theory

Kelly and mean–variance are closely connected.

Under Gaussian assumptions:

$$
w^*
\propto
\Sigma^{-1}\mu
$$

which resembles:

- maximum Sharpe ratio portfolio
- unconstrained mean–variance optimization

Difference:

| Method        | Objective                 |
| ------------- | ------------------------- |
| Mean–Variance | maximize utility          |
| Sharpe        | maximize return/risk      |
| Kelly         | maximize geometric growth |

## Usage in Quantitative Equity

Kelly ideas appear in:

- portfolio leverage
- alpha weighting
- capital allocation
- strategy scaling
- risk budgeting

One practical implementation:

$$
w_i
\propto
\frac{\alpha_i}{\sigma_i^2}
$$

subject to:

- turnover constraints
- exposure limits
- liquidity controls
- drawdown constraints

Pure Kelly is rarely deployed directly in production.