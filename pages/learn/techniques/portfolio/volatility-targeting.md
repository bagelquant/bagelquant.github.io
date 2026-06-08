---
layout: page
permalink: /learn/techniques/portfolio/volatility-targeting/
lang: en
ref: "learn-techniques-portfolio-volatility-targeting"
alternate_lang_url: /zh/learn/techniques/portfolio/volatility-targeting/
---

# Volatility Targeting

## Key idea

Volatility Targeting dynamically adjusts portfolio exposure to maintain a desired volatility level.

Instead of forecasting return:

it stabilizes risk.

Core question:

> If market risk changes, how should leverage change?

## Definition

Target volatility:

$$
\sigma^*
$$

Observed portfolio volatility:

$$
\hat\sigma_t
$$

Scaling factor:

$$
k_t
=
\frac{\sigma^}{\hat\sigma_t}
$$

Adjusted weights:

$$
w_t
=
k_tw_0
$$

Interpretation:

- realized volatility rises → reduce exposure
- realized volatility falls → increase exposure

## Example

Portfolio:

- target vol: $10%$
- current vol: $20%$

Then:

$$
k=\frac{10}{20}=0.5
$$

New exposure:

$$
50%
$$

If current volatility drops to $5%$:

$$
k=2
$$

Exposure doubles.

## Estimating Volatility

Common estimators:

Rolling estimate:

$$
\hat\sigma_t
=
\sqrt{
252
\cdot
\operatorname{Var}(r)
}
$$

EWMA:

$$
\sigma_t^2
=
\lambda\sigma_{t-1}^2
+
(1-\lambda)r_t^2
$$

Typical:

$$
\lambda=0.94\sim0.99
$$

## Relationship to Kelly

Continuous Kelly:

$$
f^
=
\frac{\mu}{\sigma^2}
$$

Vol targeting implicitly stabilizes:

$$
f\sigma
\approx
\text{constant}
$$

Kelly determines optimal leverage.

Vol targeting determines realized leverage.

## Benefits

Advantages:

- smoother risk profile
- drawdown reduction
- leverage normalization

Potential drawbacks:

- delayed response
- whipsaw
- turnover increase

## Usage in Quantitative Equity

Volatility targeting appears in:

- portfolio overlays
- market timing
- risk budgeting
- factor allocation
- CTA and multi-asset systems

A common production pipeline:

$$
\text{Signal}
\rightarrow
\text{Portfolio}
\rightarrow
\text{Vol Target}
\rightarrow
\text{Execution}
$$

Volatility targeting is one of the most widely deployed risk-control mechanisms.