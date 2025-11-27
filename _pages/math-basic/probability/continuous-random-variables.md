---
title: "Continuous Random Variables and Densities"
permalink: /probability/continuous-random-variables/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

When you zoom out on a price chart, the jagged tick-by-tick movements blur into a smooth curve. Returns look like they can take "any" value in some range, not just a few discrete points. This is where **continuous random variables** enter the story.

Many key quantities in finance—returns, log-prices, interest rates, volatility—are modeled as continuous. Mathematically, that means they can, in principle, take any value in an interval of real numbers.

In this setting, we stop counting probabilities over individual points and start integrating over ranges.

## Definition of a Continuous Random Variable

A random variable $X$ is **continuous** if its distribution can be described by a **probability density function (pdf)** $f_X$ such that for any interval $[a, b]$,

$$
P(a \le X \le b) = \int_a^b f_X(x) \, dx.
$$

The pdf must satisfy:

- $f_X(x) \ge 0$ for all $x$,
- $$\int_{-\infty}^{\infty} f_X(x) \, dx = 1.$$

Unlike in the discrete case, for a truly continuous variable,

$$
P(X = x) = 0 \quad \text{for any fixed } x.
$$

Probabilities are associated with **intervals**, not points. If this feels strange at first, it may help to think of the pdf as a kind of "density" of probability spread along the real line.

## Cumulative Distribution Function (cdf)

The **cumulative distribution function** of $X$ is

$$
F_X(x) = P(X \le x) = \int_{-\infty}^{x} f_X(t) \, dt.
$$

Properties:

- $F_X$ is non-decreasing,
- $\lim_{x \to -\infty} F_X(x) = 0$, $\lim_{x \to \infty} F_X(x) = 1$,
- $F_X$ is right-continuous.

When $f_X$ is continuous, we have

$$
f_X(x) = F_X'(x),
$$

so the pdf is the derivative of the cdf.

## Expectation and Variance

The **expectation** (mean) of a continuous random variable $X$ with pdf $f_X$ is

$$
E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx.
$$

For any function $g$, we define

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx.
$$

The **variance** of $X$ is

$$
\operatorname{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2.
$$

These formulas parallel the discrete case, with integrals replacing sums. Conceptually, you can think of the integral as adding up infinitely many tiny pieces, each with probability proportional to $f_X(x) \, dx$.

## Common Continuous Distributions in Finance (Preview)

We will study these in detail later, but here are some important examples:

- **Normal distribution** (Gaussian): central in risk modeling and the central limit theorem.
- **Lognormal distribution**: commonly used for asset prices in geometric Brownian motion.
- **Exponential and Gamma distributions**: used for waiting times in Poisson processes.

Each is specified by a pdf and parameters (mean, variance, etc.), and each has characteristic shapes and tail behaviors. Once you learn to read and sketch these shapes, you start to see them hidden inside many models.

## Joint Continuous Distributions

For a pair of continuous random variables $(X, Y)$, the **joint pdf** $f_{X,Y}(x, y)$ satisfies

- $f_{X,Y}(x, y) \ge 0$,
- $$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx \, dy = 1.$$ 

Probabilities of regions $C \subset \mathbb{R}^2$ are given by

$$
P\big((X, Y) \in C\big) = \iint_C f_{X,Y}(x, y) \, dx \, dy.
$$

The **marginal** densities are obtained by integrating out the other variable:

- $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy,$$
- $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx.$$

$X$ and $Y$ are independent if $f_{X,Y}(x, y) = f_X(x) f_Y(y)$ for all $(x, y)$.

## Change of Variables (Simple Case)

If $Y = g(X)$ is a monotone differentiable function and $X$ has pdf $f_X$, then the pdf of $Y$ is given by the **change-of-variables formula**.

- For $Y = g(X)$ with strictly increasing $g$,

  $$
  f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|.
  $$

This is used frequently in finance, e.g., when going from log-returns to prices or vice versa.

**Example:** If $R$ is a continuously distributed log-return and $S_T = S_0 e^R$ is the terminal price, we can derive the pdf of $S_T$ from the pdf of $R$ using this formula. This is exactly what lies behind the lognormal models of asset prices.

Continuous random variables are the backbone of modern asset-pricing and risk models. Once you are comfortable with densities, cdfs, and simple change-of-variable tricks, you have most of the calculus you need to navigate distributional assumptions in quant papers.

Next Topic: [Expectation, Variance, and Moments](expectation-variance-and-moments.md)
