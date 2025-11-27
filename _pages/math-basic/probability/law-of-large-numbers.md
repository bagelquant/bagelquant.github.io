---
title: "The Law of Large Numbers"
permalink: /probability/law-of-large-numbers/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

If you flip a biased coin many times and track the running average of heads, you will see the proportion slowly stabilizing near its true probability $p$. The same thing happens when you estimate an expected return from more and more data: the average stops jumping around so much.

The **Law of Large Numbers (LLN)** is the theorem behind this stabilization. It justifies interpreting probabilities as long-run frequencies and supports the use of sample averages as estimators of expected values.

In finance, it underlies the estimation of expected returns, default rates, and other average quantities from historical data.

## Setup

Let $X_1, X_2, \dots$ be i.i.d. random variables with mean $\mu = E[X_1]$ and finite variance $\sigma^2 = \operatorname{Var}(X_1) < \infty$.

Define the sample average

$$
\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i.
$$

## Weak Law of Large Numbers (WLLN)

The **Weak Law of Large Numbers** states that

$$
\bar{X}_n \xrightarrow{P} \mu \quad \text{as } n \to \infty.
$$

That is, for every $\varepsilon > 0$,

$$
P\big(|\bar{X}_n - \mu| > \varepsilon\big) \xrightarrow[n \to \infty]{} 0.
$$

Intuitively: the probability that the sample average deviates significantly from the true mean goes to zero as the sample size grows. As you add more observations, large deviations become rarer and rarer.

## Strong Law of Large Numbers (SLLN)

The **Strong Law of Large Numbers** strengthens this to almost sure convergence:

$$
\bar{X}_n \xrightarrow{\text{a.s.}} \mu \quad \text{as } n \to \infty.
$$

This means that with probability 1, the sequence of sample averages converges to $\mu$ for almost every outcome.

## Finance Applications

Examples where LLN intuition is used in quant work:

- **Estimating expected returns:** The average historical return of a stock over many periods is used as an estimator for its expected return.
- **Default rate estimation:** The observed default frequency in a large portfolio approximates the underlying default probability.
- **Risk metrics:** Averages of loss or P&L across many Monte Carlo scenarios estimate expected loss or expected shortfall.

In all cases, the LLN provides a theoretical justification for why averages stabilize as the number of observations grows. It tells you that, under reasonable assumptions, "more data" really does mean "more reliability" for averages.

Next Topic: [The Central Limit Theorem in Depth](central-limit-theorem.md)
