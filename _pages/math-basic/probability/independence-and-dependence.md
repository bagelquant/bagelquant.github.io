---
title: "Independence and Common Dependence Structures"
permalink: /probability/independence-and-dependence/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

In textbook problems, it is very common to see phrases like "assume the coin tosses are independent" or "assume the errors are independent." On paper this makes life easier. In markets, it is almost never true in any literal sense.

Stocks crash together. Credit spreads widen across sectors at once. Volatility tends to cluster in time. Even when you build a model that starts with independence, the first thing you usually do is add a dependence structure back in.

It is still useful, though, to understand what true independence would mean and how it contrasts with the messy dependence we see in data.

## Independence of Events

Two events $A$ and $B$ are **independent** if

$$
P(A \cap B) = P(A) P(B).
$$

Equivalently (when probabilities are nonzero):

- $P(A \mid B) = P(A)$
- $P(B \mid A) = P(B)$

In words: learning that $B$ occurred does not change your view on whether $A$ occurred. They are completely unrelated in probabilistic terms.

### Pairwise vs Mutual Independence

For three events $A$, $B$, and $C$, the story becomes more subtle.

- They are **pairwise independent** if each pair is independent: $(A, B)$, $(A, C)$, $(B, C)$.
- They are **mutually independent** if *every* finite intersection factors, e.g.

  $$
  P(A \cap B \cap C) = P(A) P(B) P(C).
  $$

Pairwise independence does **not** imply mutual independence. In portfolio modeling, this distinction matters when dealing with many risk factors.

## Independence of Random Variables

Random variables $X$ and $Y$ are **independent** if

$$
P(X \in A, Y \in B) = P(X \in A) P(Y \in B).
$$

In terms of distributions, this says:

- Discrete: $p_{X,Y}(x, y) = p_X(x) p_Y(y)$ for all $(x, y)$.
- Continuous: $f_{X,Y}(x, y) = f_X(x) f_Y(y)$ for all $(x, y)$.

Independence implies uncorrelatedness (zero covariance), but the converse is not true.

### Uncorrelated vs Independent

Two random variables $X$ and $Y$ are **uncorrelated** if

$$
\operatorname{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0.
$$

- If $X$ and $Y$ are independent, then they are uncorrelated.
- But uncorrelated variables can still have strong nonlinear dependence.

In finance, a portfolio may have zero correlation with a benchmark in quiet times but still exhibit strong dependence in the tails: both drop together in a crisis. Independence is broken, but simple correlation might not scream it loudly.

#### Simple Example: Zero Correlation Without Independence

Let $Z$ be a symmetric random variable that takes values $-1$ and $1$ with probability $1/2$ each. Define

$$
X = Z, \quad Y = Z^2.
$$

Then $Y$ is always equal to 1, regardless of whether $Z$ is $-1$ or $1$.

- $E[X] = 0$ by symmetry.
- $E[Y] = 1$.
- $E[XY] = E[Z \cdot Z^2] = E[Z^3] = 0$ (again by symmetry).

So

$$
\operatorname{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0 - 0\cdot 1 = 0,
$$

yet $X$ and $Y$ are clearly **not** independent: knowing $Y=1$ tells you that $X$ must be either $-1$ or $1$, and in fact $Y$ is a deterministic function of $X$.

This illustrates that zero correlation only rules out *linear* dependence; non-linear dependence can still be very strong. In the special case of jointly normal variables, zero correlation does imply independence, which is why Gaussian models are often analytically convenient.

## Measuring Linear Dependence: Covariance and Correlation

The **covariance** between $X$ and $Y$ is

$$
\operatorname{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])].
$$

The **correlation** is the normalized covariance:

$$
\rho_{X,Y} = \operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X) \, \operatorname{Var}(Y)}}.
$$

- $\rho_{X,Y} \in [-1, 1]$
- $\rho_{X,Y} = 1$ means perfect positive linear relationship.
- $\rho_{X,Y} = -1$ means perfect negative linear relationship.

Correlation is widely used in portfolio theory to measure diversification benefits, but it only captures **linear** dependence.

## Dependence in Financial Returns

Real-world financial data show rich dependence structures that are hard to compress into a single number:

- **Cross-sectional dependence:** equities in the same sector or market move together.
- **Time-series dependence:** returns may be nearly uncorrelated over time, but volatility is persistent (volatility clustering).
- **Tail dependence:** assets that appear weakly correlated in normal times can become highly dependent in crises.

These features motivate models beyond simple independence assumptions, such as factor models and copulas (which we will meet later in the course).

## Common Dependence Structures

Here are some building blocks that show up repeatedly in quant models:

### Factor Models

Returns are often decomposed as

$$
R_i = \alpha_i + \beta_{i1} F_1 + \cdots + \beta_{ik} F_k + \varepsilon_i.
$$

- Common factors $F_j$ drive co-movements across assets.
- Idiosyncratic terms $\varepsilon_i$ are often assumed independent (or weakly dependent).

Dependence arises because many assets share exposure to the same factors. Even if the idiosyncratic pieces $\varepsilon_i$ are modeled as independent, the shared factors $F_j$ ensure that bad news in a factor spills across many names at once.

### Conditional Independence

Sometimes variables are independent **conditional** on some hidden or latent factor $Z$.

- Example: Given the market regime (bull/bear), individual stock returns might be modeled as conditionally independent.

This structure is common in credit risk models (e.g., one-factor Gaussian copulas), where defaults are modeled as independent given an underlying systemic factor, but strongly dependent unconditionally.

### Gaussian Dependence

If a random vector $(X_1, \dots, X_n)$ is multivariate normal, then its dependence is fully described by its covariance matrix $\Sigma$.

- Linear combinations of components are normal.
- Zero covariance implies independence in the Gaussian case.

This is the backbone of classical mean-variance portfolio theory and many risk models, where the entire dependence structure between asset returns is summarized in a single matrix.

Understanding the gap between "independent" in the strict sense and the tangled dependence we actually observe is one of the main challenges in risk modeling. In later articles, we will see more advanced tools—like copulas and multivariate distributions—to describe and simulate that dependence in more realistic ways.

Next Topic: [Discrete Random Variables and Distributions](discrete-random-variables.md)
