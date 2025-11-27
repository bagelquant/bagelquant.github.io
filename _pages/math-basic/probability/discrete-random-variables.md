---
title: "Discrete Random Variables and Distributions"
permalink: /probability/discrete-random-variables/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

When you sketch a simple risk model in a notebook, you are often not thinking in terms of smooth curves and densities. Instead, you imagine a small menu of scenarios: "market up 2%", "flat", "down 3%", and you assign rough probabilities to each. That mental picture is the world of **discrete** random variables.

A **random variable** assigns a numerical value to each outcome of an experiment. We call it **discrete** when it can only take values in a finite or countable set.

Discrete models are a natural fit for many quant problems: number of trades, counts of defaults, states in a binomial tree, or a handful of stress-test scenarios.

## Definition of a Discrete Random Variable

Let $(\Omega, \mathcal{F}, P)$ be a probability space. A **random variable** $X$ is a function

$$
X : \Omega \to \mathbb{R}.
$$

$X$ is **discrete** if the set of possible values $\{x_1, x_2, \dots\}$ is finite or countable, and

$$
P(X = x_i) > 0 \quad \text{for each } i, \quad \sum_i P(X = x_i) = 1.
$$

The function $p(x_i) = P(X = x_i)$ is called the **probability mass function (pmf)** of $X$.

## Probability Mass Function (pmf)

For a discrete $X$ with support $S = \{x_1, x_2, \dots\}$, the pmf satisfies:

- $p(x) \ge 0$ for all $x$,
- $\sum_{x \in S} p(x) = 1$,
- $P(X \in A) = \sum_{x \in A} p(x)$ for any subset $A$ of $S$.

**Example (Number of Defaults in a Portfolio):**

Let $X$ = number of defaults among $n$ independent obligors, each defaulting with probability $p$ in a given year. Then $X$ is a **binomial** random variable with parameters $(n, p)$ and pmf

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \dots, n.
$$

We will study binomial and other key discrete distributions in detail in a later article.

## Cumulative Distribution Function (cdf)

The **cumulative distribution function (cdf)** of $X$ is

$$
F_X(x) = P(X \le x).
$$

For a discrete variable, $F_X$ is a right-continuous step function: flat between support points and jumping at each $x_i$. The size of the jump at $x_i$ is exactly $P(X = x_i)$.

## Expectation and Variance of Discrete Random Variables

The **expectation** (mean) of a discrete random variable $X$ is

$$
E[X] = \sum_{x} x \, p(x).
$$

For any function $g$, we define

$$
E[g(X)] = \sum_{x} g(x) \, p(x).
$$

The **variance** of $X$ is

$$
\operatorname{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2.
$$

These definitions will be reused in later articles for continuous variables (with sums replaced by integrals).

## Transformations of Discrete Random Variables

If $Y = g(X)$ for some function $g$, and $X$ is discrete, then $Y$ is also discrete. Its pmf can be computed in a very concrete way:

1. Identify the possible values of $Y$.
2. For each $y$, sum the probabilities of all $x$ such that $g(x) = y$:

   $$
   P(Y = y) = \sum_{x: g(x) = y} P(X = x).
   $$

**Finance example:**

Let $X$ = number of defaults in a portfolio and define $Y = \min(X, 1)$ (indicator of at least one default). Then

- $P(Y = 0) = P(X = 0)$
- $P(Y = 1) = P(X \ge 1) = 1 - P(X = 0)$

This kind of "collapse" from a count to a 0/1 indicator shows up in tranche payoffs and credit derivatives: you often care not about *how many* names defaulted, but whether you have crossed a certain attachment point.

## Joint Distributions for Discrete Variables

For a pair of discrete random variables $(X, Y)$, the **joint pmf** is

$$
P(X = x, Y = y) = p_{X,Y}(x, y).
$$

From the joint pmf we obtain the **marginals** by summing:

- $p_X(x) = \sum_y p_{X,Y}(x, y)$
- $p_Y(y) = \sum_x p_{X,Y}(x, y)$

We say $X$ and $Y$ are independent if $p_{X,Y}(x, y) = p_X(x) p_Y(y)$ for all $x, y$.

Discrete random variables provide a clean and intuitive starting point for probability theory and many simplified quant models. Once you are comfortable thinking in terms of supports and mass functions, it becomes much easier to generalize to the continuous case.

Next Topic: [Continuous Random Variables and Densities](continuous-random-variables.md)
