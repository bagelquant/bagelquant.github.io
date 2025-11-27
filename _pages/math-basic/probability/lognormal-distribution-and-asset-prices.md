---
title: "The Lognormal Distribution and Asset Prices"
permalink: /probability/lognormal-distribution-and-asset-prices/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

Imagine explaining to a non-quant colleague why a stock price chart never goes below zero, yet log-returns in your model are treated as roughly normal. The bridge between these two views is the **lognormal distribution**: prices themselves are positive and skewed, but their logarithms behave in a more symmetric, Gaussian way.

In many models of asset prices, such as **Geometric Brownian Motion (GBM)**, prices are assumed to be **lognormally distributed**. This reflects two key features that traders care about:

1. Prices are strictly positive (you cannot have a negative share price).
2. Returns over fixed horizons (log-returns) are often modeled as approximately normally distributed.

## The Lognormal Distribution

A positive random variable $S$ is **lognormally distributed** if $\log S$ is normally distributed. That is,

$$
\log S \sim N(\mu, \sigma^2).
$$

We then write $S \sim \operatorname{Lognormal}(\mu, \sigma^2)$.

The pdf of $S$ is

$$
f_S(s) = \frac{1}{s \, \sigma \sqrt{2\pi}} \exp\!\left( -\frac{(\log s - \mu)^2}{2\sigma^2} \right), \quad s > 0.
$$

Key properties:

- $S > 0$ almost surely.
- $\log S$ is symmetric around $\mu$, but $S$ is positively skewed. On a linear price chart, you see a long right tail: very large prices are rare, but more common than under a symmetric normal model.

**Intuition (how it forms):** start from a normal variable $Y = \log S$ and exponentiate. This is natural when you think in terms of **multiplicative** changes and log-returns. Positivity and right skew automatically appear after exponentiation.

**Deriving the pdf:** if $Y = \log S \sim N(\mu,\sigma^2)$ with density $f_Y(y)$, then for $s>0$,

$$
P(S \le s) = P(\log S \le \log s) = P(Y \le \log s).
$$

Differentiating with respect to $s$ and using the change-of-variables formula gives

$$
f_S(s) = f_Y(\log s) \cdot \frac{1}{s}
 = \frac{1}{s \, \sigma \sqrt{2\pi}} \exp\!\left( -\frac{(\log s - \mu)^2}{2\sigma^2} \right).
$$

## Moments of the Lognormal

If $S \sim \operatorname{Lognormal}(\mu, \sigma^2)$, then:

- Mean:
  $$
  E[S] = e^{\mu + \frac{1}{2} \sigma^2}.
  $$

- Variance:
  $$
  \operatorname{Var}(S) = \big(e^{\sigma^2} - 1\big) e^{2\mu + \sigma^2}.
  $$

These formulas follow from the moment-generating function of the normal distribution applied to $\log S$. In practice, they tell you that volatility in log-space (the $\sigma$ in the exponent) translates into both higher average price and larger dispersion in actual prices.

## Asset Prices in Geometric Brownian Motion

In the Black–Scholes model, the price process $S_t$ satisfies the stochastic differential equation

$$
\frac{dS_t}{S_t} = \mu \, dt + \sigma \, dW_t,
$$

where $W_t$ is a standard Brownian motion. The solution is

$$
S_T = S_0 \exp\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)T + \sigma \sqrt{T} \, Z\right), \quad Z \sim N(0, 1).
$$

Thus,

$$
\log S_T \sim N\left(\log S_0 + \left(\mu - \tfrac{1}{2}\sigma^2\right)T, \, \sigma^2 T\right),
$$

which means $S_T$ is lognormal. The randomness lives in the normal variable $Z$; the exponential converts that symmetric noise into a positive, skewed price.

Under the risk-neutral measure (used for pricing derivatives), $\mu$ is replaced by the risk-free rate $r$, but the lognormal structure remains.

## Implications for Option Pricing

In Black–Scholes theory, the lognormal distribution of $S_T$ is crucial:

- The payoff of a European call option at maturity is $(S_T - K)^+ = \max(S_T - K, 0)$.
- The option price is the discounted expected payoff under the risk-neutral measure:

  $$
  C_0 = e^{-rT} E^Q[(S_T - K)^+].
  $$

Since $S_T$ is lognormal under $Q$, this expectation can be computed in closed form, yielding the Black–Scholes formula. When you see the $d_1$ and $d_2$ terms in Black–Scholes, they are simply normal quantiles coming from this lognormal structure.

## When Lognormality Breaks Down

While lognormal models capture positivity and some aspects of return behavior, real asset prices can deviate significantly:

- **Jumps and crashes** (discontinuities) cannot be captured by pure lognormal diffusion.
- **Volatility clustering** and time-varying volatility require extensions like stochastic volatility models.
- **Fat tails** in returns lead to more extreme price moves than lognormal would predict.

These limitations motivate more advanced models (jump-diffusion, stochastic volatility, etc.), but lognormality remains a fundamental starting point. Even when you move to richer models, you will still think in terms of "lognormal plus corrections".

Next Topic: [Bernoulli, Binomial, and Poisson Models](bernoulli-binomial-poisson.md)
