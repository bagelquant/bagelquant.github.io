---
title: "Optimal Allocation"
permalink: /utility-theory/optimal-allocation/
sidebar:
    nav: "utility-theory"
---

With the utility function, we can now discuss the optimal decision-making. We could link utilty with certain decision-making activities, such as asset allocation or investment strategies. The goal is to maximize the expected utility of the decision. Obviously, the decision-making effects the wealth(Wealth is a function of certain decision-making process), wealth effects the utility(Utility is a function of wealth), therefore:

$$
u(W)] = u(W(x)),
$$

where:

- $u(W)$ is the utility function
- $W(x)$ is the wealth function, which is a function of the decision variable $x$.


For a risk-averse individual, the utility function is increasing and concave. This means the highest utility is achieved under First-order condition(FOC) (the first derivative of the utility function is zero).

## Optimal Portfolio Allocation Problem

Now consider a specific wealth function:

$$
\tilde W = (W_0 - \sum_{j=1}^{n} a_j) (1 + r_f) + \sum_{j=1}^{n} a_j (1 + \tilde r_j) \\,
$$

where:

- $W_0$ is the initial wealth
- $a_j$ is the amount invested in asset $j$
- $W_0 - \sum_{j=1}^{n} a_j$ is the amount invested in the risk-free asset
- $r_f$ is the risk-free rate
- $\tilde r_j$ is the random return of asset $j$
- $n$ is the number of risky assets
- $\tilde W$ is the random wealth after the investment

We could rewrite the wealth function as:

$$
\tilde W = W_0 (1 + r_f) + \sum_{j=1}^{n} a_j (\tilde r_j - r_f).
$$

The individual's goal is to maximize the expected utility of the wealth function (not maximize the wealth function itself !!!):

$$
\max_{\{a_j\}} E[u(W)] = E[u(W_0 (1 + r_f) + \sum_{j=1}^{n} a_j (\tilde r_j - r_f))].
$$

First-order condition (FOC):

$$
\frac{\partial E[u(W)]}{\partial a_j} = 0, \\
\frac{\partial E[u(W_0 (1 + r_f) + \sum_{j=1}^{n} a_j (\tilde r_j - r_f))]}{\partial a_j} = 0,\\
E[u'(W) \cdot \frac{\partial W}{\partial a_j}] = 0. \\
$$

Therefore, for each asset $j$, we have:

$$
E[u'(W) \cdot \frac{\partial W}{\partial a_j}] = E[u'(W) \cdot ( \tilde r_j - r_f)] = 0, \text{ for } j = 1, 2, ..., n.
$$

Under this condition, we could find the optimal allocation of each asset $j$.

## Intuition one: risk premium $\tilde r_j-r_f$

We call the term $\tilde r_j - r_f$ the **risk premium** of asset $j$. The risk premium is the excess return that an investor expects to receive for taking on the additional risk associated with investing in a risky asset compared to a risk-free asset.

From the FOC, we can see that $E[u'(W) \cdot ( \tilde r_j - r_f)] = 0$, since $u'(W)$ is always positive, we have:

> Stock $j$'s risk premium ($\tilde r_j - r_f$) is a random variable could be positive or negative. That's the only way to result FOC to be zero.

In other words, if we have a asset strictly with positive risk premium (always better than risk-free asset), the FOC could not be zero, therefore, the optimal allocation of this asset is not possible, the individual will invest infinite amount of wealth in this asset. With the limitation of borrowing, the individual will invest all wealth in this asset.

## Intuition two: risk aversion

Claim: 

An individual with a increasing and concave utility function will undertake risky investment if and only if the expected risk premium is positive for at least one risky asset. 

> Individual will invest in risky asset if and only if at least one $j$ has $\tilde r_j - r_f > 0$, j=1,2,...,n

Proof:

For an individual to invest $0 in or even short sell the risky asset j, it is necessary that:

1. The optimal allocation of asset j is zero or negative, $a_j \leq 0$,
2. The highest point is less or equal to zero,
3. Therefore, when $a_j = 0$, the slope should be less or equal to zero:

$$
E[u'(W) \cdot ( \tilde r_j - r_f)] \leq 0, \\
u'(W) \cdot E[\tilde r_j - r_f] \leq 0, \forall j = 1, 2, ..., n.
$$

Since $u'(W)$ is always positive, we have:

$$
E[\tilde r_j - r_f] \leq 0, \forall j = 1, 2, ..., n.
$$

Therefore, we don't invest in risky asset if and only if all expected risk premium is less than or equal to zero. In other words, if we have at least one asset with positive expected risk premium, we will invest in risky asset.

