---
title: "Absolute and Relative Risk Aversion"
permalink: /utility-theory/absolute-and-relative-risk-aversion/
sidebar:
    nav: "utility-theory"
---

We established the a risk-averse individual should have increasing and concave utility function. With the discussion of certainty equivalent and risk premium, obviously, the individual with more "concave" utility function should be more risk averse. We could quantify the risk aversion with the following two measures:

- **Absolute Risk Aversion (ARA)**:

$$
R_A = -\frac{u''(W)}{u'(W)}.
$$

- **Relative Risk Aversion (RRA)**:

$$
R_R = -\frac{ u''(W)}{u'(W)} W_0.
$$

We will discuss the two measures in detail in the following sections.

## Derive the ARA and RRA by Taylor Expansion

Consider an individual to invest all his wealth in a risky asset with random return $\tilde r$, the following equation holds:

$$
E[u'[W_0 (1 + \tilde r)](\tilde r - r_f)] \ge 0,
$$

> Invest all wealth in risky -> means optimal allocation $a_j \ge W_0$.

We could use Taylor expansion of $u'(.)$around $r_f$ to approximate the utility function:

$$
u'[W_0 (1 + \tilde r)] = u'[W_0 (1 + r_f)] + u''[W_0 (1 + r_f)] (\tilde r - r_f) W_0 + \frac{u'''[W_0 (1 + r_f)]}{2} (\tilde r - r_f)^2 + \cdots
$$

if we ignore the higher order terms, the approximation of the utility function is:

$$
u'[W_0 (1 + \tilde r)] \approx u'[W_0 (1 + r_f)] + u''[W_0 (1 + r_f)] (\tilde r - r_f)]W_0.
$$

Then we could mutiply both sides with $(\tilde r - r_f)$ and take expectation:

$$
E[u'[W_0 (1 + \tilde r)](\tilde r - r_f)] \approx u'[W_0 (1 + r_f)] E[\tilde r - r_f] + u''[W_0 (1 + r_f)] E[(\tilde r - r_f)^2] W_0.
$$

Rearranging the equation, we have:

$$
E[\tilde r - r_f] = -\frac{u''[W_0 (1 + r_f)]}{u'[W_0 (1 + r_f)]} W_0 E[(\tilde r - r_f)^2] + E[u'[W_0 (1 + r_f)](\tilde r - r_f)].
$$

Since $E[u'[W_0 (1 + r_f)](\tilde r - r_f)] \ge 0$, we have:

$$
E[\tilde r - r_f] \ge -\frac{u''[W_0 (1 + r_f)]}{u'[W_0 (1 + r_f)]} W_0 E[(\tilde r - r_f)^2] \\
\equiv R_A \cdot W_0 E[(\tilde r - r_f)^2] \\
\equiv R_r \cdot E[(\tilde r - r_f)^2].
$$

Intuitively, the ARA and RRA are the coefficients of the Taylor expansion of the utility function. A risk-averse individual will invest all wealth in risky assets when the expected risk premium is greater than the risk aversion coefficient multiplied by the second moment of the risk premium. This is called minimum risk premium.

And RRA is just a scaled version of ARA, which is the ARA multiplied by the initial wealth $W_0$.

With ARA and RRA, we have a quantitative measure of risk aversion. Then we could further discuss the change of the ARA and RRA with the change of wealth $\frac{dR_A(z)}{dz}$ and $\frac{dR_R(z)}{dz}$.

## Constant, Decreasing and Increasing ARA

We define:

$$
\frac{dR_A(z)}{dz} > 0 \text{ (increasing absolute risk aversion IARA) } \\
\frac{dR_A(z)}{dz} = 0 \text{ (constant absolute risk aversion CARA) } \\
\frac{dR_A(z)}{dz} < 0 \text{ (decreasing absolute risk aversion DARA) } \\
$$


Claim:

$$
\frac{dR_A(z)}{dz} 
\begin{cases}
> 0, \ \forall z \\
= 0, \ \forall z \\
< 0, \ \forall z
\end{cases}
\Rightarrow
\frac{da}{dW_0}
\begin{cases}
< 0, \ \forall W_0 \\
= 0, \ \forall W_0 \\
> 0, \ \forall W_0
\end{cases}
$$

Increasing ARA -> initial wealth increases, will invest less amount in risky assets. And vice versa.

> Proof omitted for brevity

## Constant, Decreasing and Increasing RRA

We define:

$$
\frac{dR_R(z)}{dz} > 0 \text{ (increasing relative risk aversion IRRA) } \\
\frac{dR_R(z)}{dz} = 0 \text{ (constant relative risk aversion CRRA) } \\
\frac{dR_R(z)}{dz} < 0 \text{ (decreasing relative risk aversion DRRA) } \\
$$

Claim:

$$
\frac{dR_R(z)}{dz}
\begin{cases}
> 0, \ \forall z \\
= 0, \ \forall z \\
< 0, \ \forall z
\end{cases}
\Rightarrow
\eta\equiv
\frac{da/a}{dW_0/W_0}
\begin{cases}
< 1, \ \forall W_0 \\
= 1, \ \forall W_0 \\
> 1, \ \forall W_0
\end{cases}
$$

Increasing RRA -> initial wealth increases, will invest less in risky assets in proportion. And vice versa.

