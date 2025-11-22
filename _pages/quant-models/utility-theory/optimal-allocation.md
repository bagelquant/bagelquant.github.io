---
title: "Optimal Allocation"
layout: page
permalink: /utility-theory/optimal-allocation/

nav: "utility-theory"
---

With the utility function in hand, we can now discuss optimal decision-making. Utility can be linked to various choices, such as asset allocation or investment strategies. The goal is to maximize the expected utility of the decision. Clearly, decision-making affects wealth (wealth is a function of the decision process), and wealth, in turn, determines utility (utility is a function of wealth). Thus:

$$
u(W) = u(W(x)),$$

where:

- $u(W)$ is the utility function
- $W(x)$ is the wealth function, which depends on the decision variable $x$

For a risk-averse individual, the utility function is increasing and concave. This means the highest utility is achieved at the first-order condition (FOC), where the first derivative of the utility function with respect to the decision variable is zero.

## Optimal Portfolio Allocation Problem

Consider a specific wealth function:

$$
\tilde W = (W_0 - \sum_{j=1}^{n} a_j) (1 + r_f) + \sum_{j=1}^{n} a_j (1 + \tilde r_j)
$$

where:

- $W_0$ is initial wealth
- $a_j$ is the amount invested in asset $j$
- $W_0 - \sum_{j=1}^{n} a_j$ is the amount invested in the risk-free asset
- $r_f$ is the risk-free rate
- $\tilde r_j$ is the random return of asset $j$
- $n$ is the number of risky assets
- $\tilde W$ is the random wealth after investment

We can rewrite the wealth function as:

$$
\tilde W = W_0 (1 + r_f) + \sum_{j=1}^{n} a_j (\tilde r_j - r_f)
$$

The individual's objective is to maximize the expected utility of wealth (not just maximize wealth itself!):

$$
\max_{\{a_j\}} E[u(W)] = E[u(W_0 (1 + r_f) + \sum_{j=1}^{n} a_j (\tilde r_j - r_f))]
$$

The first-order condition (FOC) is:

$$
\frac{\partial E[u(W)]}{\partial a_j} = 0 \\
E[u'(W) \cdot (\tilde r_j - r_f)] = 0, \quad \text{for } j = 1, 2, ..., n
$$

This condition determines the optimal allocation for each asset $j$.

## Intuition 1: Risk Premium $\tilde r_j - r_f$

The term $\tilde r_j - r_f$ is called the **risk premium** of asset $j$. It is the excess return an investor expects for taking on the additional risk of a risky asset compared to the risk-free asset.

From the FOC, $E[u'(W) \cdot (\tilde r_j - r_f)] = 0$. Since $u'(W)$ is always positive, $\tilde r_j - r_f$ must sometimes be positive and sometimes negative for the expectation to be zero.

> If an asset always has a strictly positive risk premium, the FOC cannot be zero, and the optimal allocation would be infinite (subject to borrowing constraints, the investor would allocate all wealth to that asset).

## Intuition 2: Risk Aversion

**Claim:**

A risk-averse individual (with an increasing, concave utility function) will invest in risky assets if and only if the expected risk premium is positive for at least one asset.

> An individual will invest in risky assets if and only if at least one $j$ has $E[\tilde r_j - r_f] > 0$.

**Proof:**

For an individual to invest zero (or even short sell) in risky asset $j$, it must be that:

1. The optimal allocation for asset $j$ is zero or negative, $a_j \leq 0$.
2. The maximum utility is achieved at $a_j = 0$ or less.
3. Therefore, when $a_j = 0$, the slope should be less than or equal to zero:

$$
E[u'(W) \cdot (\tilde r_j - r_f)] \leq 0
$$

Since $u'(W) > 0$, this implies:

$$
E[\tilde r_j - r_f] \leq 0, \quad \forall j = 1, 2, ..., n
$$

Therefore, an individual will not invest in risky assets if and only if all expected risk premia are less than or equal to zero. If at least one asset has a positive expected risk premium, the individual will invest in risky assets.

Next up: [Absolute and Relative Risk Aversion](absolute-and-relative-risk-aversion.md)
