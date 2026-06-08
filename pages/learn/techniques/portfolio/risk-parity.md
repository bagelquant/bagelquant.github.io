---
layout: page
permalink: /learn/techniques/portfolio/risk-parity/
lang: en
ref: "learn-techniques-portfolio-risk-parity"
alternate_lang_url: /zh/learn/techniques/portfolio/risk-parity/
---

# Risk Parity

## Key idea

Risk Parity allocates capital so that each asset contributes equal risk rather than equal capital.

Traditional portfolios allocate dollars.

Risk parity allocates volatility.

Core question:

> How should capital be distributed so no asset dominates portfolio risk?

## Definition

Portfolio volatility:

$$
\sigma_p
=
\sqrt{w^\top\Sigma w}
$$

Risk contribution of asset $i$:

$$
RC_i
=
w_i
\frac{(\Sigma w)_i}
{\sigma_p}
$$

Risk parity requires:

$$
RC_1
=
RC_2
=
\cdots
=
RC_N
$$

Each asset contributes equally.

## Equal Volatility Approximation

If correlations are ignored:

$$
w_i
\propto
\frac1{\sigma_i}
$$

Interpretation:

- lower volatility → larger weight
- higher volatility → smaller weight

This approximation is commonly deployed.

## Example

Two assets:

| Asset | Volatility |
|--------|------------|
| Equity | 20% |
| Bond | 10% |

Risk parity gives:

$$
w
\propto
(5,10)
$$

Normalized:

$$
(33%,67%)
$$

Capital is tilted toward lower-risk assets.

## Leverage

Risk parity often requires leverage.

Example:

- bond allocation increases
- expected return decreases

Leverage restores target return.

This differs from traditional 60/40 portfolios.

## Relationship to Mean–Variance

Risk parity ignores expected return.

Mean–variance includes:

$$
\max
w^\top\mu
-
\lambda w^\top\Sigma w
$$

Comparison:

| Method | Objective |
|---------|-----------|
| Equal Weight | equal capital |
| Mean–Variance | utility |
| Risk Parity | equal risk |

## Usage in Quantitative Equity

Risk parity ideas appear in:

- multi-asset portfolios
- factor allocation
- risk budgeting
- strategy blending
- volatility management

Practical implementations usually include:

- covariance shrinkage
- turnover constraints
- exposure controls
- leverage limits

Pure equal-risk solutions are rarely used directly.
