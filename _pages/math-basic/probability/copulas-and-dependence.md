---
title: "Copulas and Modeling Dependence"
permalink: /probability/copulas-and-dependence/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

When quants talk about "correlation breaking" in a crisis, they usually mean that assets start moving together in the tails in a way that simple Gaussian correlation cannot capture. One way to handle this is to separate **what each asset looks like on its own** from **how they move together**.

Traditional multivariate models (like the multivariate normal) tie together **marginal distributions** and **dependence structure** in a single object. **Copulas** allow us to separate these two aspects: we can model each marginal distribution flexibly and then choose a copula to specify dependence.

This separation is useful in finance, where marginals (e.g., fat-tailed returns) and dependence (e.g., tail dependence) both matter.

## Sklar's Theorem (Idea)

Sklar's theorem states that any multivariate distribution function can be decomposed into its marginals and a copula that captures dependence.

For a 2D case: let $(X, Y)$ have joint cdf $F_{X,Y}(x, y)$ and marginal cdfs $F_X(x)$ and $F_Y(y)$. Then there exists a copula $C$ such that

$$
F_{X,Y}(x, y) = C(F_X(x), F_Y(y)).
$$

Conversely, given marginals and a copula, we can construct a joint distribution.

## What Is a Copula?

A **copula** is a multivariate distribution function on the unit cube $[0, 1]^n$ with uniform marginals. It captures the dependence structure between variables, independent of their marginals.

In practice:

- Model marginals: choose appropriate distributions for each asset or factor (e.g., heavy-tailed).
- Choose a copula: Gaussian, t-copula, or others to specify dependence.
- Combine them to obtain a full joint model.

## Copulas in Finance

Copulas are used to model:

- **Credit portfolios:** joint default events, especially clustering and tail dependence.
- **Multi-asset derivatives:** dependence between underlyings in basket options or CDO tranches.
- **Risk aggregation:** combining different types of risks (market, credit, operational).

The **Gaussian copula** became widely known (and criticized) for its role in pre-crisis CDO pricing, where it was used to model dependence between default times. The lesson is not that copulas are bad, but that you must choose and calibrate them carefully, especially in the tails.

Next Topic: [Generating Random Variables and Monte Carlo Basics](monte-carlo-and-random-number-generation.md)
