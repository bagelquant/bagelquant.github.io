---
title: "Absolute and Relative Risk Aversion"
layout: page
permalink: /utility-theory/absolute-and-relative-risk-aversion/

nav: "utility-theory"
---

We have established that a risk-averse individual should have an increasing and concave utility function. Building on the concepts of certainty equivalent and risk premium, it is clear that the more "concave" the utility function, the more risk averse the individual. We can quantify risk aversion using two key measures:

- **Absolute Risk Aversion (ARA):**

$$
R_A = -\frac{u''(W)}{u'(W)}
$$

- **Relative Risk Aversion (RRA):**

$$
R_R = -\frac{u''(W)}{u'(W)} W_0
$$

We will discuss these two measures in detail below.

## Deriving ARA and RRA via Taylor Expansion

Consider an individual investing all their wealth in a risky asset with random return $\tilde r$. The following condition must hold:

$$
E[u'[W_0 (1 + \tilde r)](\tilde r - r_f)] \ge 0
$$

> Investing all wealth in risky assets means the optimal allocation $a_j \ge W_0$.

We can use a Taylor expansion of $u'(\cdot)$ around $r_f$ to approximate the utility function:

$$
u'[W_0 (1 + \tilde r)] = u'[W_0 (1 + r_f)] + u''[W_0 (1 + r_f)] (\tilde r - r_f) W_0 + \frac{u'''[W_0 (1 + r_f)]}{2} (\tilde r - r_f)^2 + \cdots$$

Ignoring higher-order terms, we approximate:

$$
u'[W_0 (1 + \tilde r)] \approx u'[W_0 (1 + r_f)] + u''[W_0 (1 + r_f)] (\tilde r - r_f) W_0$$

Multiplying both sides by $(\tilde r - r_f)$ and taking expectations:

$$
E[u'[W_0 (1 + \tilde r)](\tilde r - r_f)] \approx u'[W_0 (1 + r_f)] E[\tilde r - r_f] + u''[W_0 (1 + r_f)] E[(\tilde r - r_f)^2] W_0
$$

Rearranging gives:

$$
E[\tilde r - r_f] = -\frac{u''[W_0 (1 + r_f)]}{u'[W_0 (1 + r_f)]} W_0 E[(\tilde r - r_f)^2] + E[u'[W_0 (1 + r_f)](\tilde r - r_f)]
$$

Since $E[u'[W_0 (1 + r_f)](\tilde r - r_f)] \ge 0$:

$$
E[\tilde r - r_f] \ge -\frac{u''[W_0 (1 + r_f)]}{u'[W_0 (1 + r_f)]} W_0 E[(\tilde r - r_f)^2] \\
\equiv R_A \cdot W_0 E[(\tilde r - r_f)^2] \\
\equiv R_R \cdot E[(\tilde r - r_f)^2]
$$

Intuitively, ARA and RRA are coefficients from the Taylor expansion of the utility function. A risk-averse individual will invest all wealth in risky assets only if the expected risk premium exceeds the risk aversion coefficient times the second moment of the risk premium. This is the minimum risk premium required.

RRA is simply ARA scaled by initial wealth $W_0$.

With ARA and RRA, we have quantitative measures of risk aversion. We can also examine how ARA and RRA change with wealth, i.e., $\frac{dR_A(z)}{dz}$ and $\frac{dR_R(z)}{dz}$.

## Constant, Decreasing, and Increasing ARA

We define:

$$
\frac{dR_A(z)}{dz} > 0 \text{ (increasing absolute risk aversion, IARA) } \\
\frac{dR_A(z)}{dz} = 0 \text{ (constant absolute risk aversion, CARA) } \\
\frac{dR_A(z)}{dz} < 0 \text{ (decreasing absolute risk aversion, DARA) }
$$

**Claim:**

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

Increasing ARA means that as initial wealth increases, the individual invests less in risky assets, and vice versa.

> Proof omitted for brevity.

## Constant, Decreasing, and Increasing RRA

We define:

$$
\frac{dR_R(z)}{dz} > 0 \text{ (increasing relative risk aversion, IRRA) } \\
\frac{dR_R(z)}{dz} = 0 \text{ (constant relative risk aversion, CRRA) } \\
\frac{dR_R(z)}{dz} < 0 \text{ (decreasing relative risk aversion, DRRA) }
$$

**Claim:**

$$
\frac{dR_R(z)}{dz}
\begin{cases}
> 0, \ \forall z \\
= 0, \ \forall z \\
< 0, \ \forall z
\end{cases}
\Rightarrow
\eta \equiv \frac{da/a}{dW_0/W_0}
\begin{cases}
< 1, \ \forall W_0 \\
= 1, \ \forall W_0 \\
> 1, \ \forall W_0
\end{cases}
$$

Increasing RRA means that as initial wealth increases, the individual invests a smaller proportion in risky assets, and vice versa.
