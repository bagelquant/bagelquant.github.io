---
title: "Derive CAPM"
permalink: /factor-models/derive-capm/
sidebar:
    nav: "factor-models"
---

The Capital Asset Pricing Model (CAPM) is a widely used model in finance that describes the relationship between the expected return of an asset and its risk, as measured by beta:

$$
E(\tilde r_i) = r_f + \beta_i (E(\tilde r_m) - r_f)
$$

where:

- $E(\tilde r_i)$ is the expected return of asset $i$.
- $r_f$ is the risk-free rate.
- $\beta_i$ is the sensitivity of the asset's return to the market return.
- $E(\tilde r_m)$ is the expected return of the market.
- $E(\tilde r_m) - r_f$ is the market risk premium.

> As usual, we will use the notation tilde like $\tilde r$ to denote a random variable, and $r$ to denote a deterministic variable. For example, $\tilde r_i$ is the random return of asset $i$, and $r_i$ is the deterministic return of asset $i$.

The CAPM is based on the idea that investors require a higher return for taking on additional risk. In this section, we will derive the CAPM using the mean-variance analysis framework and an alternative approach.

> [!IMPORTANT]  
> You need to understand the concepts in [utility theory](https://bagelquant.com/quant-models/utility-theory/) and [mean-variance analysis](https://bagelquant.com/mean-variance/) before reading this section. This section is only about how to derive the CAPM, you could skip this part if you are not interested in the derivation process.

## Derivation of CAPM From Mean-Variance Analysis

Recall that in the mean-variance analysis, if the two-fund separation holds, we can express any desirable portfolio as a combination of the risk-free asset and the market portfolio, then we could express any portfolio using market portfolio and risk free asset as follows:

$$
\begin{align*}
E[\tilde r_j] &= r_f + \beta_{jm} (E[\tilde r_m] - r_f) \\
\beta_{jm} &= \frac{Cov(\tilde r_j, \tilde r_m)}{Var(\tilde r_m)}
\end{align*}
$$

The details is discussed in the [Market Portfolio and Security Market Line](https://bagelquant.com/mean-variance/market-portfolio-and-security-market-line/) section. And whole mean-variance analysis is discussed in the [Mean-Variance Analysis](https://bagelquant.com/mean-variance/) section.

That is done! we obtained the CAPM from the mean-variance analysis framework. All we need to do is make sure the assumptions of mean-variance analysis hold, that is:

- The investors are rational and risk-averse. (Increasing concave utility function)
- Only mean and variance are relevant of optimizing utility, that is:
    - Normal distribution of returns.
    - Or, the investors have quadratic utility function.
    - See [From Optimized Utility to Mean-Variance Analysis](https://bagelquant.com/mean-variance/from-optimized-utility-to-mean-variance-analysis/) section for more details.
- The two-fund separation holds:
    - see [Market Portfolio and Security Market Line](https://bagelquant.com/mean-variance/market-portfolio-and-security-market-line/) section for more details.
- Market at equilibrium

We could clearly see that this is an equilibrium approach, we assume every investor is rational and risk-averse, and they all have the same information and act in their own best interest, then the market will achieve certain equilibrium, and we could derive the CAPM from it. However, we have lots of strong assumptions!

## Alternative Derivation of CAPM

We could also derive the CAPM directly from utility maximization, without the mean-variance analysis framework. The full utility maximization problem is discussed in the [Utility Theory](https://bagelquant.com/quant-models/utility-theory/) section. Here we will just briefly introduce the utility maximization problem and derive the CAPM from it.

Assume that:

- $r_f$ is the risk-free rate.
- We have $N$ risky assets with returns $r_1, r_2, \ldots, r_j, \ldots, r_N$, which are multivariate normal distributed.
- Let $\tilde W_i$ be the optimally invested wealth for investor $i$.

Then the first-order condition of the utility maximization problem is:

$$
\begin{align*}
E[u_i^\prime(\tilde W_i)(\tilde r_j - r_f)] = 0, \quad \forall i, j \\
where \quad \tilde W_i = W_0^i [(1 + rf) + \sum_{j=1}^N w_{ij}(\tilde r_j - r_f)].

\end{align*}
$$

Using definition of covariance, the FOC could be rewritten as:

$$
\begin{align*}
E[u_i^\prime(\tilde W_i)(\tilde r_j - r_f)] &= Cov(u_i^\prime(\tilde W_i), \tilde r_j - r_f) + E[u_i^\prime(\tilde W_i)]E[\tilde r_j - r_f] = 0, \\
E[u_i^\prime(\tilde W_i)]E[\tilde r_j - r_f] &= -Cov(u_i^\prime(\tilde W_i), \tilde r_j - r_f) \\
&= -Cov(u_i^\prime(\tilde W_i), \tilde r_j) + Cov(u_i^\prime(\tilde W_i), r_f) \\
&= -Cov(u_i^\prime(\tilde W_i), \tilde r_j) + 0 \\
&= -Cov(u_i^\prime(\tilde W_i), \tilde r_j). \\
\end{align*}
$$

Using the Stein's Lemma: If $\tilde x$ and $\tilde y$ are bi-variate normal, the $cov[g(\tilde x), \tilde y] = E[g^\prime(\tilde x) \tilde y]$, where $g$ is a differentiable function of $\tilde x$.

We obtain:

$$
E[u_i^\prime(\tilde W_i)]E[\tilde r_j - r_f] = -E[u_i^{\prime\prime}(\tilde W_i)]Cov(\tilde W_i, \tilde r_j).
$$

That is:

$$
\begin{align*}
Cov(\tilde W_i, \tilde r_j) &= \theta_{i}^{-1} E[\tilde r_j - r_f], \\
where \quad \theta_{i} &= - \frac{E[u_i^{\prime\prime}(\tilde W_i)]}{E[u_i^{\prime}(\tilde W_i)]}.
\end{align*}
$$

The $\theta_{i}$ is the absolute risk aversion of investor $i$, it is a measure of how much risk the investor is willing to take. The higher the $\theta_{i}$, the more risk-averse the investor is. See [Absolute and Relative Risk Aversion](https://bagelquant.com/utility-theory/absolute-and-relative-risk-aversion/) section for more details.

Add all investors together, we have the market allocation: 

$$
\begin{align*}
Cov(\tilde W, \tilde r_j) = (\sum_{i=1}^N \theta_{i}^{-1}) E[\tilde r_j - r_f], \\
E[\tilde r_j - r_f] = (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Cov(\tilde W, \tilde r_j).
\end{align*}
$$

In the mean time, we have world wealth $\tilde W = W_0 [1 + \lambda \tilde r_m + (1 - \lambda) r_f]$, where $\lambda$ is the weight of risky asset in the world wealth. Combine the two equations, we have:

$$
\begin{align}
E[\tilde r_j - r_f] = W_0 \lambda (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Cov(\tilde r_m, \tilde r_j).
\end{align}
$$

Set market portfolio as the portfolio $j$, we have:
$$
\begin{align}
E[\tilde r_m - r_f] = W_0 \lambda (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Cov(\tilde r_m, \tilde r_m) = W_0 \lambda (\sum_{i=1}^N \theta_{i}^{-1})^{-1} Var(\tilde r_m).
\end{align}
$$

(2)/(1) gives us:

$$
E[\tilde r_j - r_f] = \frac{Cov(\tilde r_m, \tilde r_j)}{Var(\tilde r_m)} E[\tilde r_m - r_f].
$$

This is the CAPM! We have derived the CAPM from utility maximization directly, without the mean-variance analysis framework.

Note, Interpretation of terms:

- $(sum_{i=1}^N \theta_{i}^{-1})^{-1}$ is the market absolute risk aversion, is the harmonic mean of all investors' absoulte risk aversion.
- $W_0 (sum_{i=1}^N \theta_{i}^{-1})^{-1}$ can be interpreted as the aggregate relative risk aversion of the market.

Summarize of the assumptions:

- The investors are rational and risk-averse. (Increasing concave utility function)
- The risky assets are multivariate normal distributed. (Used in the Stein's Lemma)

