---
title: "Convergence Concepts in Probability"
permalink: /probability/convergence-of-random-variables/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

When you run a backtest or a Monte Carlo simulation, you are implicitly trusting that "if I take enough samples, my averages will get close to the truth" or that a fine discrete-time model will behave like its continuous-time limit. All of this is language about **sequences of random variables getting closer** to some target.

To make that idea precise, probability theory gives us several modes of **convergence of random variables**. They sound abstract at first, but they are exactly what justifies many everyday approximations in quant work.

## Types of Convergence

Let $X_1, X_2, \dots$ be a sequence of random variables and $X$ another random variable.

### Convergence in Probability

We say that $X_n$ **converges in probability** to $X$ if for every $\varepsilon > 0$,

$$
P\big(|X_n - X| > \varepsilon\big) \xrightarrow[n \to \infty]{} 0.
$$

Notation: $X_n \xrightarrow{P} X$.

Informally: the probability that $X_n$ is far from $X$ becomes negligible as $n$ grows.

### Almost Sure (a.s.) Convergence

We say that $X_n$ **converges almost surely** (or with probability 1) to $X$ if

$$
P\big(\{\omega : X_n(\omega) \to X(\omega) \text{ as } n \to \infty\}\big) = 1.
$$

Notation: $X_n \xrightarrow{\text{a.s.}} X$.

Almost sure convergence is stronger than convergence in probability.

### Convergence in Distribution

We say that $X_n$ **converges in distribution** (or in law) to $X$ if

$$
F_{X_n}(x) \xrightarrow[n \to \infty]{} F_X(x)
$$

for all continuity points $x$ of the cdf $F_X$.

Notation: $X_n \xrightarrow{d} X$.

This is the weakest of the three notions and is used in the Central Limit Theorem.

## Relationships Between Modes of Convergence

In general:

- Almost sure convergence $\implies$ convergence in probability.
- Convergence in probability $\implies$ convergence in distribution.

The converses do **not** hold in general.

You can think of these as different strengths of promises about how the sequence $X_n$ behaves. For many applications in finance, convergence in probability or in distribution is sufficient to justify approximations; almost sure convergence is reassuring but often more than you strictly need.

## Convergence and the Law of Large Numbers

The **Law of Large Numbers (LLN)** is a fundamental result about averages of i.i.d. random variables, which we discuss in detail in the next article. It states that sample averages converge to the true mean in some mode of convergence (probability or almost surely).

This provides the theoretical foundation for:

- estimating expected returns from historical data,
- and using long-run frequency interpretations of probability ("in the long run, the fraction of heads converges to $p$").

## Convergence in Distribution and the CLT

The **Central Limit Theorem (CLT)** is a statement about convergence in distribution:

$$
\frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}} \xrightarrow{d} N(0, 1).
$$

It tells us that standardized sums of i.i.d. variables become approximately normal as $n$ increases, which underpins many normal approximations in statistics and risk modeling. Whenever you say "for large $n$, this looks Gaussian", you are relying on a convergence-in-distribution statement like this.

Next Topic: [The Law of Large Numbers](law-of-large-numbers.md)
