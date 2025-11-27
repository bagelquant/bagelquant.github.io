---
title: "Generating Random Variables and Monte Carlo Basics"
permalink: /probability/monte-carlo-and-random-number-generation/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

If you have ever set up a pricing engine or a risk engine, you have probably written a Monte Carlo loop: simulate scenarios, compute payoffs, average. It is one of the few places where probability theory turns directly into code.

Monte Carlo methods are a workhorse of quantitative finance. They approximate expectations and probabilities by **simulating random variables** and averaging outcomes.

This article introduces the basics of random number generation and Monte Carlo estimation.

## Pseudo-Random Number Generation

Computers generate **pseudo-random** numbers: deterministic sequences that mimic randomness.

Most libraries provide functions to generate i.i.d. $U(0, 1)$ variables (uniform on $(0, 1)$). From these, we can construct other distributions.

## Transforming Uniforms into Other Distributions

Given $U \sim U(0, 1)$ and a target distribution with cdf $F$, we can use the **inverse transform method**:

1. Generate $U \sim U(0, 1)$.
2. Set $X = F^{-1}(U)$.

Then $X$ has cdf $F$.

This works when $F^{-1}$ is available in closed form or can be computed numerically.

For the normal distribution, specialized methods (e.g., Box–Muller, Ziggurat algorithm) are often used instead of direct inversion. In practice, you rarely implement these yourself; you rely on well-tested library implementations.

## Monte Carlo Estimation of Expectations

Suppose we want to compute

$$
E[g(X)]
$$

for some random variable $X$ and function $g$ (e.g., an option payoff). If we can simulate i.i.d. samples $X^{(1)}, \dots, X^{(N)}$, we estimate

$$
\hat{\mu}_N = \frac{1}{N} \sum_{i=1}^N g\big(X^{(i)}\big).
$$

By the Law of Large Numbers,

$$
\hat{\mu}_N \xrightarrow{P} E[g(X)] \quad \text{as } N \to \infty.
$$

By the Central Limit Theorem,

$$
\sqrt{N} \left( \hat{\mu}_N - E[g(X)] \right) \approx N(0, \sigma^2)
$$

for large $N$, where $\sigma^2 = \operatorname{Var}(g(X))$.

This allows us to construct confidence intervals for Monte Carlo estimates: the standard error shrinks like $1/\sqrt{N}$, so quadrupling the number of paths halves the Monte Carlo noise.

## Monte Carlo in Finance

Monte Carlo methods are widely used to:

- Price path-dependent derivatives (barrier options, Asian options)
- Estimate risk measures (VaR, Expected Shortfall) from simulated loss distributions
- Evaluate portfolio P&L under complex, nonlinear payoffs

The key idea: simulate many scenarios, compute the payoff or loss in each, and average. Everything else (path generation, variance reduction, parallelization) is about doing this more efficiently and accurately.

## Variance Reduction (Brief Mention)

To improve accuracy for a given computational budget, variance-reduction techniques are used:

- Antithetic variates
- Control variates
- Importance sampling

These techniques aim to reduce $\operatorname{Var}(g(X))$ or make simulation more efficient. Well-designed variance reduction can give you much tighter estimates for the same number of paths.

Next Topic: [Change of Measure and Radon–Nikodym Intuition](change-of-measure-intuition.md)
