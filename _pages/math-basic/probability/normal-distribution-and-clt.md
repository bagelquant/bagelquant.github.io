---
title: "The Normal Distribution and the Central Limit Phenomenon"
permalink: /probability/normal-distribution-and-clt/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

When you open a risk report for a portfolio, you will often see phrases like "we assume daily returns are normal" or charts that look like smooth, bell-shaped curves. At the same time, everyone in markets knows that crashes and wild days do happen. This tension between a clean mathematical model and a messy reality is exactly where the **normal distribution** and the **Central Limit Theorem (CLT)** live.

The normal distribution shows up in two roles that are both important for quants:

- as a **modeling assumption** (for example in mean–variance portfolio theory, regression residuals, or factor models), and
- as the **limit of many small, independent effects**, formalized by the CLT.

## The Normal Distribution

A random variable $X$ is **normally distributed** with mean $\mu$ and variance $\sigma^2$ if it has density

$$
f_X(x) = \frac{1}{\sqrt{2\pi} \, \sigma} \exp\!\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \quad x \in \mathbb{R}.
$$

We write $X \sim N(\mu, \sigma^2)$.

Key properties:

- The distribution is symmetric around $\mu$.
- $E[X] = \mu$, $\operatorname{Var}(X) = \sigma^2$.
- Any linear transformation $Y = aX + b$ is normal: $Y \sim N(a\mu + b, a^2 \sigma^2)$.
 
**Intuition (how it forms):** the bell shape arises naturally as the limit of standardized sums of many small, independent shocks. If you view $X$ as the sum of many tiny independent pieces, each with small effect, then the CLT suggests the total should be approximately normal.

**Expectation and variance (sketch):**

If $Z \sim N(0,1)$ and $X = \mu + \sigma Z$, then $E[Z]=0$ and $\operatorname{Var}(Z)=1$, so

$$
E[X] = E[\mu + \sigma Z] = \mu + \sigma E[Z] = \mu,
$$

and

$$
\operatorname{Var}(X) = \operatorname{Var}(\mu + \sigma Z) = \sigma^2 \operatorname{Var}(Z) = \sigma^2.
$$

## Standard Normal and the CDF

The **standard normal** random variable $Z \sim N(0, 1)$ has density

$$
f_Z(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}.
$$

Its cumulative distribution function (cdf) is

$$
\Phi(z) = P(Z \le z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-t^2/2} \, dt.
$$

For a general $X \sim N(\mu, \sigma^2)$,

$$
P(X \le x) = \Phi\!\left( \frac{x - \mu}{\sigma} \right).
$$

In practice, normal probabilities are computed via numerical libraries or precomputed tables; you very rarely integrate the density by hand.

## Normality in Finance: Uses and Limitations

The normal distribution is widely used because it is mathematically convenient and often a reasonable approximation for **aggregated** effects:

- Portfolio returns as sums of many small, independent contributions
- Estimation errors in sample means and regression coefficients

However, empirical asset returns exhibit **fat tails** and **skewness**, deviating from normality, especially at high frequencies. Normal models can understate extreme risks, especially for deep out-of-the-money options or severe drawdowns. A practical mindset is: use normality as a **first approximation** and then check where it breaks.

## The Central Limit Theorem (CLT)

The CLT formalizes the idea that sums of many small, independent random variables tend to look normal.

Let $X_1, X_2, \dots$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2 \in (0, \infty)$. Define the standardized sum

$$
Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}}.
$$

Then the **Central Limit Theorem** states that

$$
Z_n \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty.
$$

Here $\xrightarrow{d}$ denotes convergence in distribution.

### Intuition

Each $X_i$ might have a complicated or even ugly distribution, but when we sum many of them, the individual irregularities tend to cancel out, and the aggregate behaves approximately like a normal variable.

This approximation is especially good when:

- no single term dominates the sum,
- tails are not too heavy,
- and $n$ is moderately large.

## CLT in Quantitative Finance

Examples of CLT-style reasoning in finance:

- **Portfolio returns over time:** The sum of daily returns over a month or year may be approximated as normal, even if daily returns are not perfectly normal. This is why annualized volatility is often computed assuming something close to normality.
- **Estimation error:** Sample means of returns are approximately normal, which justifies confidence intervals and $t$-tests in performance analysis and factor models.
- **Risk aggregation:** Aggregating many small independent risk contributions (e.g., in insurance or credit portfolios) yields approximately normal total loss, at least in the central region of the distribution.

In all these cases, the CLT gives you a powerful rule of thumb: sums and averages of many small pieces start to look bell-shaped, so normal tools become usable. The rest of this course will keep coming back to this idea, especially when we mix normality with heavy tails and dependence.

Next Topic: [The Lognormal Distribution and Asset Prices](lognormal-distribution-and-asset-prices.md)
