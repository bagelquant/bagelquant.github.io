---
title: "Bernoulli, Binomial, and Poisson Models"
permalink: /probability/bernoulli-binomial-poisson/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

Think about a day in a credit portfolio desk: did a given issuer default today or not? How many trades did your strategy execute in the last hour? How many orders arrived on the bid side of a limit order book this second? These are all **yes/no events** and **counts of events**.

The **Bernoulli**, **binomial**, and **Poisson** distributions form the basic toolkit for this discrete world. They are simple, but they show up everywhere in models of defaults, trades, and arrivals.

## Bernoulli Distribution

A **Bernoulli** random variable $X$ takes values in $\{0, 1\}$ with

$$
P(X = 1) = p, \quad P(X = 0) = 1 - p.
$$

Here $p$ is the probability of "success" (e.g., default occurs, trade happens, event triggers).
This is the atomic building block: a single yes/no outcome.

**Intuition (how it forms):** we encode "event happens" as 1 and "does not happen" as 0. One probability parameter $p$ completely specifies the model.

**pmf and cdf:**

$$
P(X = 1) = p,\quad P(X = 0) = 1 - p.
$$

The cumulative distribution function is

$$
F_X(x) =
\begin{cases}
0, & x < 0, \\
1-p, & 0 \le x < 1, \\
1, & x \ge 1.
\end{cases}
$$

**Expectation and variance (derivation):**

$$
E[X] = 0\cdot(1-p) + 1\cdot p = p.
$$

Since $X^2 = X$ for $X \in \{0,1\}$,

$$
E[X^2] = E[X] = p,
$$

so

$$
\operatorname{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p).
$$

Bernoulli variables are building blocks for more complex count models.

## Binomial Distribution

Let $X_1, \dots, X_n$ be independent Bernoulli($p$) variables, and define

$$
S_n = X_1 + \cdots + X_n.
$$

Then $S_n$ has a **binomial** distribution with parameters $(n, p)$, written $S_n \sim \operatorname{Binomial}(n, p)$, and pmf

$$
P(S_n = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \dots, n.
$$

The combinatorial factor $\binom{n}{k}$ counts how many sequences of $n$ Bernoulli trials contain exactly $k$ successes.

**Intuition (how it forms):** you are repeating the same Bernoulli experiment $n$ times independently and counting how many times you see a 1.

**cdf:**

$$
F_{S_n}(k) = P(S_n \le k) = \sum_{j=0}^{\lfloor k \rfloor} \binom{n}{j} p^j (1-p)^{n-j}.
$$

**Expectation and variance (derivation):** write $S_n = X_1 + \cdots + X_n$ with each $X_i \sim \text{Bernoulli}(p)$.

By linearity of expectation,

$$
E[S_n] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n p = np.
$$

Using independence,

$$
\operatorname{Var}(S_n) = \sum_{i=1}^n \operatorname{Var}(X_i)
 = n p(1-p).
$$

**Finance example:** Number of defaults in a portfolio of $n$ independent obligors, each with default probability $p$ over a fixed horizon. Here $np$ is the expected number of defaults; risk managers compare that to worst-case scenarios or regulatory stress tests.

## Poisson Distribution

The **Poisson** distribution models the number of events occurring in a fixed interval of time (or space) when events happen independently at a constant average rate.

A random variable $N$ has a Poisson distribution with parameter $\lambda > 0$, written $N \sim \operatorname{Poisson}(\lambda)$, if

$$
P(N = k) = e^{-\lambda} \frac{\lambda^k}{k!}, \quad k = 0, 1, 2, \dots.
$$
This formula can be obtained as the limit of the binomial pmf when $n \to \infty$, $p \to 0$ in such a way that $np \to \lambda$.

**Intuition (how it forms):** imagine many tiny independent opportunities for an event to occur, each with very small probability, but with a constant average rate $\lambda$ per unit time. The total count of events in one interval then follows approximately a Poisson distribution.

**cdf:**

$$
F_N(k) = P(N \le k) = \sum_{j=0}^{\lfloor k \rfloor} e^{-\lambda} \frac{\lambda^j}{j!}.
$$

**Expectation and variance (sketch of derivation):**

Using the series representation,

$$
E[N] = \sum_{k=0}^\infty k\, e^{-\lambda} \frac{\lambda^k}{k!}
 = \lambda.
$$

Similarly, computing $E[N^2]$ or using the moment generating function $M_N(t) = \exp(\lambda(e^t-1))$ gives

$$
\operatorname{Var}(N) = \lambda.
$$

**Connection to binomial:** If $n$ is large and $p$ is small, with $np = \lambda$ held fixed, then

$$
\operatorname{Binomial}(n, p) \approx \operatorname{Poisson}(\lambda).
$$

This is useful for approximating rare-event counts, such as the number of defaults in a large, diversified portfolio over a short horizon, or the number of trades in a very liquid instrument in a short time window.

## Poisson Processes (Preview)

In continuous time, a **Poisson process** with rate $\lambda$ is a counting process $(N_t)_{t \ge 0}$ such that

- $N_0 = 0$.
- Increments are independent.
- Increments over length-$t$ intervals are Poisson($\lambda t$).

Poisson processes are used to model:

- Arrival of orders in a limit order book
- Trade counts in high-frequency data
- Default counts in credit risk (with modifications)

We will return to these processes when discussing stochastic models and continuous-time probability. For now, it is enough to see how Bernoulli, binomial, and Poisson fit together as a ladder: from one event, to many independent events, to events in continuous time.

Next Topic: [Heavy-Tailed Distributions and Financial Returns](heavy-tailed-distributions-and-returns.md)
