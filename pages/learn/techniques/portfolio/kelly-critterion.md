---
layout: page
permalink: /learn/techniques/portfolio/position-sizing/
lang: en
ref: "learn-techniques-portfolio-position-sizing"
alternate_lang_url: /zh/learn/techniques/portfolio/position-sizing/
---

# Position Sizing

## Key idea

Position sizing determines how much capital to allocate to each investment opportunity.

A good signal alone is insufficient.

Portfolio performance depends jointly on:

- signal quality
- capital allocation
- diversification
- risk control

Core question:

> Given multiple opportunities, how much should each position contribute?

Position sizing transforms forecasts into deployable portfolios.

## Definition

Given:

- signal vector: $\alpha$
- portfolio weights: $w$

Position sizing defines:

$$
w=f(\alpha)
$$

subject to:

$$
\sum_i |w_i|\le L
$$

where:

- $w_i$ = portfolio weight
- $\alpha_i$ = expected return signal
- $L$ = leverage limit

Different sizing rules imply different portfolio behaviors.

## Equal Weight

Simplest allocation:

$$
w_i=\frac1N
$$

Properties:

- maximum simplicity
- diversification by count
- ignores conviction

Useful as a benchmark.

## Score-Based Sizing

Allocate proportionally to signal strength:

$$
w_i
=
\frac{\alpha_i}
{\sum_j|\alpha_j|}
$$

Interpretation:

- stronger alpha → larger position
- weak alpha → smaller position

Common in factor investing.

## Volatility-Adjusted Sizing

Scale positions by risk.

$$
w_i
\propto
\frac{\alpha_i}{\sigma_i}
$$

where:

- $\sigma_i$ = asset volatility

Interpretation:

- equalize risk contribution
- reduce concentration

Widely used in quantitative portfolios.

## Kelly-Based Sizing

Kelly allocation:

$$
w_i
\propto
\frac{\alpha_i}{\sigma_i^2}
$$

Interpretation:

- expected return scales allocation
- variance penalizes leverage

This maximizes long-run growth under ideal assumptions.

See also:

→ Kelly Criterion

## Position Constraints

Production portfolios usually enforce:

$$
w_i\in[w_{\min},w_{\max}]
$$

Additional controls:

- leverage limits
- sector neutrality
- turnover constraints
- liquidity constraints
- drawdown limits

Position sizing therefore becomes an optimization problem.

## Relationship to Portfolio Construction

Position sizing sits between:

$$
\text{Signal}
\rightarrow
\text{Sizing}
\rightarrow
\text{Portfolio}
\rightarrow
\text{Execution}
$$

Examples:

| Method | Weight Driver |
|---------|---------------|
| Equal Weight | count |
| Score Weight | alpha |
| Vol Scaling | alpha/risk |
| Kelly | alpha/variance |
| Optimization | objective + constraints |

## Usage in Quantitative Equity

Position sizing appears in:

- factor portfolios
- alpha combination
- portfolio optimization
- execution scheduling
- leverage control

Sizing often contributes as much performance improvement as signal generation.