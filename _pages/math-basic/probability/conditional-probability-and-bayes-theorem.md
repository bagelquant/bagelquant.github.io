---
title: "Conditional Probability and Bayes' Theorem"
permalink: /probability/conditional-probability-and-bayes-theorem/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

In finance, information arrives continuously: economic reports, earnings announcements, order flow, volatility spikes. **Conditional probability** is the math of updating beliefs when we learn something new. **Bayes' theorem** turns this into a systematic rule.

This article formalizes conditional probability and shows how Bayes' theorem underlies many practical tasks: regime detection, credit risk modeling, and Bayesian inference.

## Conditional Probability

Let $A$ and $B$ be events with $P(B) > 0$. The **conditional probability** of $A$ given $B$ is defined as

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}.
$$

Interpretation: we restrict our universe to the event $B$ ("we know $B$ happened") and renormalize the probabilities within $B$.

### Basic Properties

From the definition, we get:

- **Product rule**:
  $$
  P(A \cap B) = P(A \mid B) P(B) = P(B \mid A) P(A).
  $$

- **Chain rule** (for three events):
  $$
  P(A \cap B \cap C) = P(A \mid B, C) P(B \mid C) P(C).
  $$

These rules generalize to longer chains and are crucial for probabilistic models with many variables.

## Law of Total Probability

Suppose $B_1, \dots, B_n$ form a **partition** of the sample space: they are disjoint and their union is $\Omega$, with $P(B_i) > 0$ for all $i$. Then for any event $A$,

$$
P(A) = \sum_{i=1}^n P(A \mid B_i) P(B_i).
$$

Interpretation: the total probability of $A$ is a weighted average of its conditional probabilities under different scenarios $B_i$.

**Finance example (market regimes):**

Let $B_1$ = "bull market", $B_2$ = "bear market", $B_3$ = "sideways market". Let $A$ = "portfolio return exceeds 5% this year". Then

$$
P(A) = P(A \mid B_1) P(B_1) + P(A \mid B_2) P(B_2) + P(A \mid B_3) P(B_3).
$$

This expresses overall performance probability as a mixture over regimes.

## Bayes' Theorem

Bayes' theorem in its basic form states that, for events $A$ and $B$ with $P(B) > 0$,

$$
P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}.
$$

Using the law of total probability, we can generalize to a partition $\{B_i\}$:

$$
P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^n P(A \mid B_i) P(B_i)}.
$$

Here:

- $P(B_j)$ is the **prior** probability of scenario $B_j$.
- $P(A \mid B_j)$ is the **likelihood** of observing $A$ under scenario $B_j$.
- $P(B_j \mid A)$ is the **posterior** probability after observing $A$.

### A Simple Numerical Example

Suppose a credit analyst groups firms into two categories:

- $B_1$ = "healthy" with prior probability $P(B_1) = 0.9$,
- $B_2$ = "distressed" with prior probability $P(B_2) = 0.1$.

Let $A$ be the event "credit spread widens sharply in a week". From past data, the analyst believes

$$
P(A \mid B_1) = 0.05, \quad P(A \mid B_2) = 0.6.
$$

First compute the unconditional probability of $A$ using the law of total probability:

$$
P(A) = P(A \mid B_1)P(B_1) + P(A \mid B_2)P(B_2)
  = 0.05 \cdot 0.9 + 0.6 \cdot 0.1
  = 0.045 + 0.06
  = 0.105.
$$

Now apply Bayes' theorem to update the probability of distress after we observe a spread widening:

$$
P(B_2 \mid A) = \frac{P(A \mid B_2)P(B_2)}{P(A)}
      = \frac{0.6 \cdot 0.1}{0.105}
      \approx 0.571.
$$

So the analyst's view of the firm being distressed jumps from 10% to about 57% after this single, informative signal. This is the kind of update Bayes' theorem formalizes.

### Credit Risk Example

Let $B_1$ = "firm is healthy", $B_2$ = "firm is distressed". Let $A$ = "credit spread widens sharply".

- Prior: $P(B_2)$ = baseline probability that the firm is distressed.
- Likelihood: $P(A \mid B_2)$ = probability of a large spread widening if the firm is distressed.
- Posterior: $P(B_2 \mid A)$ = updated probability of distress after we observe the spread move.

Bayes' theorem tells us how much to revise our view of the firm's health given the new price information.

## Conditional Probability for Random Variables

For random variables, conditioning is expressed using densities or mass functions.

### Discrete Case

If $(X, Y)$ is a pair of discrete random variables with joint pmf $p_{X,Y}(x, y)$ and marginal $p_Y(y)$, then

$$
P(X = x \mid Y = y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}, \quad p_Y(y) = \sum_x p_{X,Y}(x, y).
$$

### Continuous Case

If $(X, Y)$ has joint pdf $f_{X,Y}(x, y)$ and marginal $f_Y(y)$, then (when $f_Y(y) > 0$)

$$
f_{X \mid Y}(x \mid y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}, \quad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx.
$$

This conditional density describes the distribution of $X$ given the information $Y = y$.

## Independence Revisited

Two events $A$ and $B$ are **independent** if

$$
P(A \cap B) = P(A) P(B).
$$

Equivalently, as long as $P(B) > 0$,

$$
P(A \mid B) = P(A).
$$

Knowing that $B$ occurred does not change the probability of $A$.

For random variables $X$ and $Y$, independence means that their joint distribution factors into marginals:

- Discrete: $p_{X,Y}(x, y) = p_X(x) p_Y(y)$.
- Continuous: $f_{X,Y}(x, y) = f_X(x) f_Y(y)$.

In finance, independence is often an unrealistic assumption, but it can be a useful baseline or approximation, especially for first-pass models and intuition.

## Summary

In this article we:

- Defined conditional probability and derived the product rule
- Used the law of total probability to express probabilities over scenario partitions
- Introduced Bayes' theorem and interpreted priors, likelihoods, and posteriors
- Extended conditioning to random variables via conditional pmfs and pdfs
- Reinterpreted independence in terms of conditional probabilities

Conditional probability and Bayes' theorem give us a consistent way to update beliefs as new information arrives—central to both trading and risk management.

Next Topic: [Independence and Common Dependence Structures](independence-and-dependence.md)
