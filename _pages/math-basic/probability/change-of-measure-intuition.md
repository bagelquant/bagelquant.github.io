---
title: "Change of Measure and Radon–Nikodym Intuition"
permalink: /probability/change-of-measure-intuition/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

If you read a derivatives book, you quickly encounter two different "worlds": the **real-world measure** $P$, where you think about actual probabilities of events and calibrate to historical data, and the **risk-neutral measure** $Q$, where discounted prices are martingales and option pricing formulas live.

In mathematical finance, we frequently change from one probability measure to another—most notably from $P$ to $Q$.

This article gives an intuitive overview of **change of measure** and the **Radon–Nikodym derivative**, without going deep into measure theory.

## Why Change Measures?

Under the real-world measure $P$:

- Probabilities reflect actual frequencies or beliefs about future outcomes.

Under the risk-neutral measure $Q$:

- Discounted asset prices are martingales.
- Expected discounted payoffs equal current prices.

We use $Q$ for **pricing** and $P$ for **risk measurement and forecasting**. In a typical workflow, you might price instruments under $Q$ but run stress tests and scenario analyses under $P$.

## Radon–Nikodym Derivative (Intuition)

Suppose $Q$ is "absolutely continuous" with respect to $P$ (roughly, $Q$ does not assign positive probability to events that are impossible under $P$).

Then there exists a nonnegative random variable $Z$ such that for any event $A$,

$$
Q(A) = E_P[Z \, 1_A].
$$

This $Z$ is the **Radon–Nikodym derivative** of $Q$ with respect to $P$, denoted

$$
Z = \frac{dQ}{dP}.
$$

Intuitively, $Z$ reweights probabilities from $P$ to $Q$.

## Expectation Under the New Measure

For any integrable random variable $X$,

$$
E_Q[X] = E_P[X Z].
$$

That is, expectations under $Q$ can be computed as weighted expectations under $P$ using the Radon–Nikodym derivative. You can think of $Z$ as a pricing kernel or **state-price density** that tells you how much each scenario is "worth" in present-value terms.

This is the probabilistic core of many pricing formulas and Girsanov's theorem in continuous-time models.

## Example: Risk-Neutral Pricing (High Level)

In a simple discrete-time model, suppose we know the real-world probabilities and the market prices of traded assets. We can solve for a risk-neutral measure $Q$ such that discounted prices are martingales and then express option prices as

$$
\text{Price}_0 = E_Q[\text{Discounted Payoff}].
$$

The change of measure from $P$ to $Q$ is encoded in the Radon–Nikodym derivative $\frac{dQ}{dP}$. In continuous-time models, these ideas become Girsanov's theorem and stochastic exponentials; here we are just building the probabilistic intuition.

Next Topic: [Moment Generating Functions and Characteristic Functions](mgf-and-characteristic-functions.md)
