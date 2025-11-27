---
title: "Inequalities and Concentration Bounds"
permalink: /probability/concentration-inequalities/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

Suppose you have only 250 trading days of data and you want to say something like "with high probability, my estimate is within this band of the truth". Asymptotic theorems (LLN, CLT) talk about what happens as $n \to \infty$, but 250 is very much finite.

This is where **concentration inequalities** come in: they provide **finite-sample bounds** on how far random quantities are likely to deviate from their expectations.

These tools are useful in risk management and model validation, where we need guarantees that hold for specific sample sizes.

## Markov's Inequality

Let $X$ be a nonnegative random variable and $a > 0$. Then

$$
P(X \ge a) \le \frac{E[X]}{a}.
$$

This is a very general but often loose bound.

## Chebyshev's Inequality

Let $X$ have mean $\mu$ and variance $\sigma^2$. For any $k > 0$,

$$
P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}.
$$

Chebyshev's inequality requires only a finite variance and gives a bound on large deviations from the mean.

Applied to sample averages, Chebyshev's inequality provides a non-asymptotic version of the LLN.

## Hoeffding and Bernstein Inequalities (Idea Only)

More refined inequalities, such as **Hoeffding's** and **Bernstein's** inequalities, give exponentially decaying bounds for sums of bounded or sub-exponential random variables. These are widely used in machine learning and empirical process theory.

While we will not state them in full detail here, the key message is:

- for sums of independent, bounded random variables, deviations from the mean become extremely unlikely at a rate that decays exponentially in the sample size.

## Applications in Finance

Concentration inequalities help with:

- **Backtesting risk models:** bounding the probability that empirical loss frequencies deviate from model predictions.
- **Model validation:** assessing whether observed deviations between model and data are compatible with sampling variability.
- **Risk limits:** setting conservative thresholds based on probabilistic guarantees.

They complement LLN and CLT by quantifying how quickly randomness "averages out" as we collect more data, not just in the limit but for concrete sample sizes.

Next Topic: [Random Vectors and Multivariate Normal](random-vectors-and-multivariate-normal.md)
