---
title: "Moment Generating Functions and Characteristic Functions"
permalink: /probability/mgf-and-characteristic-functions/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

When you move deeper into probability theory, you start to see distributions not just as densities or cdfs, but as objects that can be transformed and combined. **Moment generating functions (mgfs)** and **characteristic functions** are like fingerprints of distributions: compact representations that make algebra on random variables much easier.

They compactly encode the distributions of random variables and are powerful tools for analyzing sums of random variables and deriving limit theorems.

## Moment Generating Function (mgf)

For a random variable $X$, the **moment generating function** (when it exists in a neighborhood of 0) is

$$
M_X(t) = E[e^{tX}].
$$

If $M_X(t)$ exists in an interval around $t = 0$, it uniquely determines the distribution of $X$.

The name comes from the fact that derivatives at 0 yield moments:

$$
M_X^{(k)}(0) = E[X^k].
$$

## Characteristic Function

The **characteristic function** of $X$ is

$$
\varphi_X(t) = E[e^{itX}], \quad t \in \mathbb{R},
$$

where $i$ is the imaginary unit.

Characteristic functions always exist (they are bounded by 1) and uniquely determine the distribution of $X$.

## Sums of Independent Random Variables

If $X$ and $Y$ are independent, then

$$
M_{X+Y}(t) = M_X(t) M_Y(t),
$$

and similarly for characteristic functions:

$$
\varphi_{X+Y}(t) = \varphi_X(t) \varphi_Y(t).
$$

This multiplicative property makes mgfs and characteristic functions especially useful for analyzing sums and proving limit theorems like the CLT.

## Example: Normal Distribution

If $X \sim N(\mu, \sigma^2)$, its mgf is

$$
M_X(t) = \exp\!\left( \mu t + \frac{1}{2} \sigma^2 t^2 \right).
$$

From this, we can derive $E[X] = \mu$ and $\operatorname{Var}(X) = \sigma^2$. In more advanced models (e.g., Lévy processes, stochastic volatility), characteristic functions often have simple closed forms even when densities do not.

## Applications in Finance

In quantitative finance, mgfs and characteristic functions are used to:

- derive closed-form pricing formulas in models where the characteristic function is known (e.g., via Fourier transform methods),
- analyze sums of log-returns and compute distributions of aggregated returns,
- and prove theoretical results about convergence and approximations.

This concludes our introductory probability course for quants. The tools developed here—distributions, expectation, convergence, multivariate models, and measure changes—are the probabilistic foundation for stochastic calculus, econometrics, and modern asset-pricing theory.
