---
title: "Derive CAPM"
permalink: /factor-models/derive-capm/
sidebar:
    nav: "factor-models"
---

The Capital Asset Pricing Model (CAPM) is a foundational model in finance that describes the relationship between an asset's expected return and its risk, as measured by beta:

$$
E(\tilde r_i) = r_f + \beta_i (E(\tilde r_m) - r_f)
$$

where:

- $E(\tilde r_i)$ is the expected return of asset $i$.
- $r_f$ is the risk-free rate.
- $\beta_i$ is the sensitivity of the asset's return to the market return.
- $E(\tilde r_m)$ is the expected return of the market.
- $E(\tilde r_m) - r_f$ is the market risk premium.

> As usual, we use a tilde, as in $\tilde r$, to denote a random variable, and $r$ to denote a deterministic variable. For example, $\tilde r_i$ is the random return of asset $i$, and $r_i$ is the deterministic return of asset $i$.

The CAPM is built on the idea that investors demand higher returns for taking on additional risk. In this section, we derive the CAPM using both the mean-variance analysis framework and an alternative approach.

> [!IMPORTANT]  
> Before reading this section, you should be familiar with [utility theory](https://bagelquant.com/quant-models/utility-theory/) and [mean-variance analysis](https://bagelquant.com/mean-variance/). This section focuses on the derivation of CAPM; you may skip it if you are not interested in the mathematical details.

## Derivation of CAPM from Mean-Variance Analysis

Recall that in mean-variance analysis, if the two-fund separation holds, any desirable portfolio can be expressed as a combination of the risk-free asset and the market portfolio. Thus, any portfolio can be written as:

$$
\begin{align*}
E[\tilde r_j] &= r_f + \beta_{jm} (E[\tilde r_m] - r_f) \\
\beta_{jm} &= \frac{Cov(\tilde r_j, \tilde r_m)}{Var(\tilde r_m)}
\end{align*}
$$

For more details, see the [Market Portfolio and Security Market Line](https://bagelquant.com/mean-variance/market-portfolio-and-security-market-line/) section, and the broader [Mean-Variance Analysis](https://bagelquant.com/mean-variance/) discussion.

With this, we have derived the CAPM from the mean-variance framework. The key assumptions required are:

- Investors are rational and risk-averse (i.e., have increasing, concave utility functions).
- Only mean and variance matter for utility optimization, which holds if:
  - Returns are normally distributed, or
  - Investors have quadratic utility functions.
  - See [From Optimized Utility to Mean-Variance Analysis](https://bagelquant.com/mean-variance/from-optimized-utility-to-mean-variance-analysis/) for more.
- The two-fund separation holds (see [Market Portfolio and Security Market Line](https://bagelquant.com/mean-variance/market-portfolio-and-security-market-line/)).
- The market is in equilibrium.

This is an equilibrium approach: assuming all investors are rational, risk-averse, and have the same information, the market reaches equilibrium, allowing us to derive the CAPM. However, these are strong assumptions!

## Alternative Derivation of CAPM

We can also derive the CAPM directly from utility maximization, without relying on mean-variance analysis. The full utility maximization problem is discussed in [Utility Theory](https://bagelquant.com/quant-models/utility-theory/); here, we briefly outline the process.

Assume:

- $r_f$ is the risk-free rate.
- There are $N$ risky assets with returns $r_1, r_2, \ldots, r_j, \ldots, r_N$, which are jointly normally distributed.
- $\tilde W_i$ is the optimally invested wealth for investor $i$.

The first-order condition (FOC) for utility maximization is:

$$
\begin{align*}
E[u_i^\prime(\tilde W_i)(\tilde r_j - r_f)] = 0, \quad \forall i, j \\
\text{where} \quad \tilde W_i = W_0^i [(1 + r_f) + \sum_{j=1}^N w_{ij}(\tilde r_j - r_f)].
\end{align*}
$$

Using the definition of covariance, the FOC can be rewritten as:

$$
\begin{align*}
E[u_i^\prime(\tilde W_i)(\tilde r_j - r_f)] &= Cov(u_i^\prime(\tilde W_i), \tilde r_j - r_f) + E[u_i^\prime(\tilde W_i)]E[\tilde r_j - r_f] = 0, \\
E[u_i^\prime(\tilde W_i)]E[\tilde r_j - r_f] &= -Cov(u_i^\prime(\tilde W_i), \tilde r_j - r_f) \\
&= -Cov(u_i^\prime(\tilde W_i), \tilde r_j) + Cov(u_i^\prime(\tilde W_i), r_f) \\
&= -Cov(u_i^\prime(\tilde W_i), \tilde r_j) + 0 \\
&= -Cov(u_i^\prime(\tilde W_i), \tilde r_j).
\end{align*}
$$

By Stein's Lemma: If $\tilde x$ and $\tilde y$ are bivariate normal, then $cov[g(\tilde x), \tilde y] = E[g^\prime(\tilde x) \tilde y]$, where $g$ is a differentiable function of $\tilde x$.

Thus:

$$
E[u_i^\prime(\tilde W_i)]E[\tilde r_j - r_f] = -E[u_i^{\prime\prime}(\tilde W_i)]Cov(\tilde W_i, \tilde r_j).
$$

So:

$$
\begin{align*}
Cov(\tilde W_i, \tilde r_j) &= \theta_{i}^{-1} E[\tilde r_j - r_f], \\
\text{where} \quad \theta_{i} &= - \frac{E[u_i^{\prime\prime}(\tilde W_i)]}{E[u_i^{\prime}(\tilde W_i)]}.
\end{align*}
$$

Here, $\theta_{i}$ is the absolute risk aversion of investor $i$, measuring how much risk the investor is willing to take. Higher $\theta_{i}$ means greater risk aversion. See [Absolute and Relative Risk Aversion](https://bagelquant.com/utility-theory/absolute-and-relative-risk-aversion/) for more.

Aggregating across all investors gives the market allocation:

$$
\begin{align*}
Cov(\tilde W, \tilde r_j) = (\sum_{i=1}^N \theta_{i}^{-1}) E[\tilde r_j - r_f], \\
E[\tilde r_j - r_f] = (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Cov(\tilde W, \tilde r_j).
\end{align*}
$$

Meanwhile, world wealth is $\tilde W = W_0 [1 + \lambda \tilde r_m + (1 - \lambda) r_f]$, where $\lambda$ is the weight of risky assets in world wealth. Combining the equations, we get:

$$
\begin{align}
E[\tilde r_j - r_f] = W_0 \lambda (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Cov(\tilde r_m, \tilde r_j).
\end{align}
$$

Setting the market portfolio as portfolio $j$:
$$
\begin{align}
E[\tilde r_m - r_f] = W_0 \lambda (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Cov(\tilde r_m, \tilde r_m) = W_0 \lambda (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Var(\tilde r_m).
\end{align}
$$

Dividing (2) by (1) yields:

$$
E[\tilde r_j - r_f] = \frac{Cov(\tilde r_m, \tilde r_j)}{Var(\tilde r_m)} E[\tilde r_m - r_f].
$$

This is the CAPM! We have derived the CAPM directly from utility maximization, without relying on mean-variance analysis.

Interpretation of terms:

- $(\sum_{i=1}^N \theta_{i}^{-1})^{-1}$ is the market's absolute risk aversion, i.e., the harmonic mean of all investors' absolute risk aversion.
- $W_0 (\sum_{i=1}^N \theta_{i}^{-1})^{-1}$ can be interpreted as the aggregate relative risk aversion of the market.

Summary of assumptions:

- Investors are rational and risk-averse (increasing, concave utility functions).
- Risky assets are jointly normally distributed (required for Stein's Lemma).
