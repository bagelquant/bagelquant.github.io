---
title: "Efficient Frontier without Risk-Free Asset"
permalink: /mean-variance/efficient-frontier-without-risk-free-asset/
sidebar:
    nav: "mean-variance"
---

Now we have the solution to the mean-variance optimization problem, for every target expected return $E[\tilde r_p]$, we could find the optimal weights $\boldsymbol W^*$, and the corresponding variance $\sigma^2_p$ and expected return $E[\tilde r_p]$. We could explore:

- The weight vector $\boldsymbol W^*$ for different target expected returns $E[\tilde r_p]$. (Two Fund Theorem)
- The relationship between the expected return $E[\tilde r_p]$ and the variance $\sigma^2_p$. (Efficient Frontier)
- Covariance (covariance with minimum variance portfolio (MVP), zero covariance portfolio, etc.)

These three are the core features of the mean-variance optimization. We will explore them one by one.

## Two Fund Theorem

From previous section, we have the optimal weight vector $\boldsymbol W^*$ for a given target expected return $E[\tilde r_p]$:

$$
\boldsymbol W^* = \boldsymbol g + \boldsymbol h \cdot E[\tilde r_p],
$$

where:

- $\boldsymbol g = \frac{1}{D} \left( B \cdot \boldsymbol V^{-1} \boldsymbol 1 - A \cdot \boldsymbol V^{-1} \boldsymbol \mu \right)$, $N \times 1$ vector
- $\boldsymbol h = \frac{1}{D} \left( C \cdot \boldsymbol V^{-1} \boldsymbol \mu - A \cdot \boldsymbol V^{-1} \boldsymbol 1 \right)$, $N \times 1$ vector

Clearly, all the optimal weights are a linear function of the target expected return $E[\tilde r_p]$. With a different target expected return, we could find a different optimal weight vector. All the optimal portfolios weights are on the same line in the $\mathbb{R}^N$ weight space . Since they are on a straight line, we could use any two optimal portfolios to construct the other optimal portfolios. This is the ***Two Fund Theorem***.

**Claim:**

For any two optimal portfolios, the linear combination of them is also an optimal portfolio:

$$
\boldsymbol W^* = \alpha \boldsymbol W^*_1 + (1 - \alpha) \boldsymbol W^*_2, \quad \forall \alpha \in [0, 1]
$$

**Proof:**

Since they are optimal portfolios, we could write them as:

$$
\begin{align*}
\boldsymbol W^*_1 = \boldsymbol g_1 + \boldsymbol h_1 \cdot E[\tilde r_1], \\
\boldsymbol W^*_2 = \boldsymbol g_2 + \boldsymbol h_2 \cdot E[\tilde r_2],
\end{align*}
$$

where $\boldsymbol g_1, \boldsymbol h_1$ are the optimal weights for portfolio 1, and $\boldsymbol g_2, \boldsymbol h_2$ are the optimal weights for portfolio 2. We could rewrite the linear combination of them as:

$$
\begin{align*}
\boldsymbol W^* &= \alpha \boldsymbol W^*_1 + (1 - \alpha) \boldsymbol W^*_2 \\
&= \alpha (\boldsymbol g_1 + \boldsymbol h_1 \cdot E[\tilde r_1]) + (1 - \alpha) (\boldsymbol g_2 + \boldsymbol h_2 \cdot E[\tilde r_2]) \\
&= \alpha \boldsymbol g_1 + (1 - \alpha) \boldsymbol g_2 + \alpha \boldsymbol h_1 \cdot E[\tilde r_1] + (1 - \alpha) \boldsymbol h_2 \cdot E[\tilde r_2] \\
&= \boldsymbol g + \boldsymbol h \cdot E[\tilde r_p]
\end{align*}
$$

where:

- $\boldsymbol g = \alpha \boldsymbol g_1 + (1 - \alpha) \boldsymbol g_2$
- $\boldsymbol h = \alpha \boldsymbol h_1 + (1 - \alpha) \boldsymbol h_2$
- $E[\tilde r_p] = \alpha E[\tilde r_1] + (1 - \alpha) E[\tilde r_2]$
- $\boldsymbol W^*$ is the optimal portfolio for target expected return $E[\tilde r_p]$.

Thus, we have proved that the linear combination of any two optimal portfolios is also an optimal portfolio. This is the ***Two Fund Theorem***.

> Note: The optimal portfolios are also called ***frontier portfolios***, see below Efficient Frontier section.

## Frontier without Risk-Free Asset

Now we know weights $\boldsymbol W^*$ are a straight line in the weight space $\mathbb{R}^N$. 

How about in the mean-variance space ($\mu, \sigma^2$)? or mean-standard deviation space ($\mu, \sigma$)? 

We know that the optimal weights $\boldsymbol W^*$ are a linear function of the target expected return $E[\tilde r_p]$, the variance of portfolio $\sigma^2_p$ is a function of the weights ($\sigma^2_p = W^T_p V W_p$), where V is the covariance matrix of the asset returns. Clearly, we could find the relationship between the expected return $E[\tilde r_p]$ and the variance $\sigma^2_p$.

The variance of the portfolio is given by:

$$
\begin{align*}
\sigma^2_p &= \boldsymbol W^T \boldsymbol V \boldsymbol W \\
&= \left( \boldsymbol g + \boldsymbol h \cdot E[\tilde r_p] \right)^T \boldsymbol V \left( \boldsymbol g + \boldsymbol h \cdot E[\tilde r_p] \right) \\
&= \frac{C}{D} [E(\tilde r_p)] - \frac{A}{C}]^2 + \frac{1}{C} \\
\end{align*}
$$

The variance ($\sigma^2_p$) is a quadratic function of the expected return ($E[\tilde r_p]$), if we plot the expected return and variance on a 2D graph, we could find the relationship between them is a parabola. The minimum variance portfolio (MVP) is the point on the parabola with the minimum variance. 

![Mean-Variance Frontier](attachments/mean-variance-frontier.png)

### Minimum Variance Portfolio (MVP)

The minimum variance portfolio (mvp) is the point on the parabola with the minimum variance. Clearly, it has the expected return $E[\tilde r_{mvp}] = \frac{A}{C}$ and variance $\sigma^2_{mvp} = \frac{1}{C}$. 

### Efficient Frontier

Recall the utility theory, if we assume only the mean and variance of the wealth are relevant for decision-making, any rational investor would choose the portfolio with highest expected return at given level of variance. (Top left corner of the mean-variance space). Therefore, the lower half of the parabola is not desirable, and the upper half of the parabola is the ***efficient frontier***. In summary:

- **Frontier Portfolios**
    - All parabolas are frontier portfolios
    - All frontier portfolios is the lowest variance portfolio for a given expected return
    - The frontier is the edge of all feasible portfolios
    - Any two frontier portfolios could be combined to form another frontier portfolio
- **Minimum Variance Portfolio (MVP)**
    - The pivot point of the parabola
    - The MVP is the lowest variance portfolio of all portfolios
- **Efficient Frontier**
    - The upper half of the parabola
    - Higher than the MVP ($E(\tilde r_p > E(\tilde r_{mvp}) = \frac{A}{C}$)
- **Inefficient Portfolios**
    - The lower half of the parabola
    - Higher than the MVP ($E(\tilde r_p < E(\tilde r_{mvp}) = \frac{A}{C}$)
    - Not desirable

### Mean-Standard Deviation space

![Mean-Standard Deviation Frontier](attachments/mean-std-frontier.png)


Asymptotes:

$$
E[\tilde r_p] = \frac{A}{C} + \sqrt{\frac{D}{C}} \cdot \sigma_p
$$

## Explore Covariance

### Covariance

The covariance between any portfolios could be calculated using the covariance matrix $V$:

$$
Cov(\tilde r_p, \tilde r_q) = \boldsymbol W^T_p \boldsymbol V \boldsymbol W_q
$$

where $\boldsymbol W_p$ and $\boldsymbol W_q$ are the weight vectors of the two portfolios.

### Covariance of Frontier Portfolios

Recall the variance of the frontier portfolio is given by:

$$
\sigma^2_p = \frac{C}{D} [E(\tilde r_p)] - \frac{A}{C}]^2 + \frac{1}{C} \\
$$

With the same logic, we could find the covariance between any two frontier portfolios is given by:

$$
Cov(\tilde r_p, \tilde r_q) = \frac{C}{D} [E(\tilde r_p)] - \frac{A}{C}] \cdot [E(\tilde r_q)] - \frac{A}{C}] + \frac{1}{C} \\
$$

### Covariance with Minimum Variance Portfolio (MVP)

**Claim:**

The covariance between any portfolio (not necessarily frontier portfolio) and the minimum variance portfolio (MVP) is equal to variance of the minimum variance portfolio (MVP):

$$
Cov(\tilde r_p, \tilde r_{mvp}) = \sigma^2_{mvp}
$$

**Proof:**

Consider the following portfolio: $\alpha \tilde r_p + (1 - \alpha) \tilde r_{mvp}$, where $\alpha$ is a constant. The variance of this portfolio is given by:

$$
\begin{align*}
Var(\alpha \tilde r_p + (1 - \alpha) \tilde r_{mvp}) &= \alpha^2 Var(\tilde r_p) + (1 - \alpha)^2 Var(\tilde r_{mvp}) + 2\alpha(1 - \alpha) Cov(\tilde r_p, \tilde r_{mvp}) \\
&= \alpha^2 \sigma^2_p + (1 - \alpha)^2 \sigma^2_{mvp} + 2\alpha(1 - \alpha) Cov(\tilde r_p, \tilde r_{mvp}) \\
&= \alpha^2 \sigma^2_p + (1 - \alpha)^2 \sigma^2_{mvp} + 2\alpha(1 - \alpha) \sigma^2_{mvp} \\
\end{align*}
$$

The solution of: 

$$
\min_{\alpha} Var(\alpha \tilde r_p + (1 - \alpha) \tilde r_{mvp}),
$$ 

should be $\alpha = 0$, since the mvp is the lowest variance portfolio. The First Order Condition (FOC) is given by:

$$
\begin{align*}
\frac{\partial Var(\alpha \tilde r_p + (1 - \alpha) \tilde r_{mvp})}{\partial \alpha} &= 2\alpha \sigma^2_p + 2(1 - \alpha) \sigma^2_{mvp} + 2\alpha Cov(\tilde r_p, \tilde r_{mvp}) - 2(1 - \alpha) Cov(\tilde r_p, \tilde r_{mvp}) = 0 \\
\end{align*}
$$

plugging in $\alpha = 0$, we have:

$$
\begin{align*}
2(1 - 0) \sigma^2_{mvp} + 2(0) Cov(\tilde r_p, \tilde r_{mvp}) - 2(1 - 0) Cov(\tilde r_p, \tilde r_{mvp}) &= 0 \\
Cov(\tilde r_p, \tilde r_{mvp}) &= \sigma^2_{mvp} \\
\end{align*}
$$

Thus, we have proved that the covariance between any portfolio (not necessarily frontier portfolio) and the minimum variance portfolio (MVP) is equal to variance of the minimum variance portfolio (MVP).

### Zero Covariance Portfolio

**Claim:**

For any frontier portfolio $p$, except for the minimum variance portfolio (MVP), there exists a unique frontier portfolio $zc(p)$ such that the covariance between $p$ and $zc(p)$ is zero.

**Proof:**

We set 

$$
\begin{align*}
Cov(\tilde r_p, \tilde r_q) &= W^T_p \boldsymbol V W_q \\
&= (\lambda \boldsymbol V^{-1} \boldsymbol \mu + \gamma \boldsymbol V^{-1} \boldsymbol 1)^T \boldsymbol V W_q \\
&= \lambda \mu^T V^{-1} V W_q + \gamma \boldsymbol 1^T V^{-1}V W_q \\
&= \lambda \mu^T W_q + \gamma \boldsymbol 1^T W_q \\
&= \lambda E[\tilde r_q] + \gamma.
\end{align*}
$$

Using the definition of $\lambda$ and $\gamma$:

$$
\begin{align*}
\lambda &= \frac{C \cdot E[\tilde r_p] - A}{D}, \\
\gamma &= \frac{B - A \cdot E[\tilde r_p]}{D},
\end{align*}
$$

we could obtain:

$$
\begin{align*}
E[\tilde r_q] &= E[\tilde r_{zc(p)}] + \frac{cov(\tilde r_p, \tilde r_q)}{\sigma^2_{p}} \cdot \{E[\tilde r_p] - E[\tilde r_{zc(p)}]\} \\
&= E[\tilde r_{zc(p)}] + \beta_{qp} \cdot \{E[\tilde r_p] - E[\tilde r_{zc(p)}]\}.
\end{align*}
$$

Where $\beta_{qp} = \frac{cov(\tilde r_p, \tilde r_q)}{\sigma^2_{p}}$ is the beta of portfolio $q$ with respect to portfolio $p$.

**Interpretation:**

Any portfolio $q$ that is not the minimum variance portfolio (MVP) could be **expressed** or **explained** or **constructed** by the a frontier portfolio $p$ and its zero covariance portfolio $zc(p)$.

This give us a new perspective of how to explain the expected return of a portfolio. In the mean-variance setup, we explain the expected return by the variance (measure the relationship between the mean and variance). Now we could explain the expected return by the $\beta_{qp}$, higher the beta, higher the expected return. 

Later, we will introduce the **Market Portfolio**, which is a special case of the equation above, substituting the market portfolio for $p$ will give us the a line called **Security Market Line** (SML). And it will further lead us to the **Capital Asset Pricing Model** (CAPM). We will discuss this in the next section.

## Conclusion

Key takeaways from this section:

- The optimal weights $\boldsymbol W^*$ are a linear function of the target expected return $E[\tilde r_p]$.
- The variance of the portfolio $\sigma^2_p$ is a quadratic function of the target expected return $E[\tilde r_p]$.
- The minimum variance portfolio (MVP) is the point on the parabola with the minimum variance.
- The efficient frontier is the upper half of the parabola, and the lower half is the inefficient portfolios.
- The covariance between any portfolio (not necessarily frontier portfolio) and the minimum variance portfolio (MVP) is equal to variance of the minimum variance portfolio (MVP).
- The covariance between any two frontier portfolios is given by the covariance matrix $V$.
- For any frontier portfolio $p$, except for the minimum variance portfolio (MVP), there exists a unique frontier portfolio $zc(p)$ such that the covariance between $p$ and $zc(p)$ is zero.
- Any portfolio $q$ that is not the minimum variance portfolio (MVP) could be expressed or explained or constructed by the a frontier portfolio $p$ and its zero covariance portfolio $zc(p)$.

