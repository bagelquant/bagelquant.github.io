---
layout: page
title: "Multivariable Integration and Change of Variables"
permalink: /calculus/multivariable-integration-and-change-of-variables/

nav: "calculus"
header:
  overlay_image: assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

In quantitative finance, many quantities depend on multiple continuous variables — asset prices, interest rates, and volatility states.  
Multivariable integration generalizes one-dimensional integration to compute accumulated effects over multidimensional domains, such as joint probability distributions and multi-asset payoffs.

## Double and Multiple Integrals

For a function $f(x,y)$ defined on a rectangular region $R = [a,b]\times[c,d]$, the **double integral** is defined as

$$
\iint_R f(x,y)\,dx\,dy =
\lim_{m,n\to\infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(x_i^*, y_j^*)\,\Delta x\,\Delta y,
$$

provided the limit exists and is finite.

This represents the *volume under the surface* $z=f(x,y)$ over region $R$.

Similarly, a triple integral
$$
\iiint_V f(x,y,z)\,dx\,dy\,dz
$$
computes the *hyper-volume* over a 3D region $V$.

## Iterated Integrals and Fubini’s Theorem

If $f$ is continuous on $R$, then the double integral equals the iterated integral:

$$
\iint_R f(x,y)\,dx\,dy = \int_c^d \int_a^b f(x,y)\,dx\,dy = \int_a^b \int_c^d f(x,y)\,dy\,dx.
$$

**Example:**
$$
\iint_{[0,1]^2} (x+y)\,dx\,dy
= \int_0^1 \left[\frac{x^2}{2} + xy\right]_0^1 dy
= \int_0^1 \left(\frac{1}{2} + y\right) dy
= \frac{1}{2} + \frac{1}{2} = 1.
$$

**Application:**  
In finance, this structure appears in **joint expectations** where two or more random variables interact (e.g., multi-asset options, correlation products).

## Integration Over Non-Rectangular Regions

When the domain $R$ is bounded by curves or surfaces, limits of integration depend on $x$ or $y$.

**Example:**  
Region bounded by $y=0$, $y=x$, and $x=1$:
$$
\iint_R y\,dx\,dy = \int_0^1 \int_0^x y\,dy\,dx = \int_0^1 \frac{x^2}{2}\,dx = \frac{1}{6}.
$$

## Change of Variables and Jacobians

Often it is convenient to transform variables $(x,y)$ to new variables $(u,v)$ for simpler integration.  
If $(x,y)$ are smooth functions of $(u,v)$:

$$
x = x(u,v), \quad y = y(u,v),
$$

then

$$
dx\,dy = \left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,du\,dv,
$$

where the **Jacobian determinant** is

$$
\frac{\partial(x,y)}{\partial(u,v)} =
\begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{vmatrix}.
$$

**Example (Polar Coordinates):**

Let $x = r\cos\theta$, $y = r\sin\theta$.  
Then
$$
\frac{\partial(x,y)}{\partial(r,\theta)} =
\begin{vmatrix}
\cos\theta & -r\sin\theta \\
\sin\theta & r\cos\theta
\end{vmatrix} = r.
$$

Thus $dx\,dy = r\,dr\,d\theta$.

**Illustration:**
$$
\iint_R f(x,y)\,dx\,dy = \int_{\theta_1}^{\theta_2} \int_{r_1}^{r_2} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta.
$$

This formula is used extensively when integrating over circular or elliptical regions, such as correlation ellipses or bivariate normal densities.

## Integration of Joint Probability Densities

If $(X,Y)$ has joint pdf $p(x,y)$, the probability over region $A$ is

$$
P((X,Y)\in A) = \iint_A p(x,y)\,dx\,dy.
$$

Marginal densities are obtained by integrating out the other variable:

$$
p_X(x) = \int_{-\infty}^\infty p(x,y)\,dy, \quad
p_Y(y) = \int_{-\infty}^\infty p(x,y)\,dx.
$$

**Example:**  
If $(X,Y)$ are jointly normal with correlation $\rho$,
$$
p(x,y)=\frac{1}{2\pi\sqrt{1-\rho^2}}
\exp\!\left(-\frac{x^2 - 2\rho xy + y^2}{2(1-\rho^2)}\right).
$$
Then
$$
p_X(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}, \quad p_Y(y)=\frac{1}{\sqrt{2\pi}}e^{-y^2/2}.
$$

**In Finance:**  
This is the basis for pricing **basket options**, **spread options**, and **correlation derivatives**.

## Expectation and Covariance via Multivariable Integrals

Expected value of a function $g(X,Y)$ is
$$
E[g(X,Y)] = \iint_{\mathbb{R}^2} g(x,y)p(x,y)\,dx\,dy.
$$

Covariance is computed as
$$
Cov(X,Y) = \iint_{\mathbb{R}^2} (x - E[X])(y - E[Y])p(x,y)\,dx\,dy.
$$

**Example:**  
For jointly normal $(X,Y)$, $Cov(X,Y) = \rho$.

## Application: Bivariate Normal Transformation

Let $(U,V)\sim N(0,I)$ be independent.  
Define correlated variables:
$$
X = U, \quad Y = \rho U + \sqrt{1-\rho^2}\,V.
$$

Then $(X,Y)$ has joint pdf with correlation $\rho$.  
The Jacobian determinant of the linear transformation is 1, hence densities transform directly.

**This change of variables is essential in Monte Carlo simulation** of correlated random variables for portfolio or VaR modeling.

## Multivariate Integration in Pricing

A European option on two assets with payoff $f(S_1,S_2)$ has risk-neutral price:

$$
V_0 = e^{-rT}\iint_0^\infty f(S_1,S_2)p(S_1,S_2)\,dS_1\,dS_2.
$$

**Example:**  
Basket call with weights $w_1, w_2$ and strike $K$:

$$
f(S_1,S_2) = \max(w_1S_1 + w_2S_2 - K, 0).
$$

Analytic solutions are rare; Monte Carlo integration is used to approximate this double integral.

## Monte Carlo and Numerical Multivariate Integration

For $n$-dimensional integrals, direct quadrature becomes impractical as $n$ grows.  
Monte Carlo replaces the integral by an expectation estimated through random sampling:

$$
\int_{\mathbb{R}^n} f(\mathbf{x})p(\mathbf{x})\,d\mathbf{x}
\approx \frac{1}{N}\sum_{i=1}^N f(\mathbf{x}_i), \quad \mathbf{x}_i\sim p(\mathbf{x}).
$$

**Properties:**

- Error $\mathcal{O}(1/\sqrt{N})$, independent of dimension.  
- Applicable for any distribution shape.  
- Used in pricing, risk aggregation, and exposure simulation.

## Change of Variables in Probability Integrals

If $Y=g(X)$ and $X$ has pdf $p_X(x)$, then
$$
p_Y(y) = p_X(x)\left|\frac{dx}{dy}\right|.
$$

**Example:**  
If $X$ is uniform on $[0,1]$ and $Y=-\ln X$,  
then $p_Y(y)=e^{-y}$ for $y>0$, i.e., an exponential distribution.

This concept generalizes to multivariate transformations through the absolute Jacobian determinant.

**In Finance:**  
Used for transforming between return spaces (log vs. arithmetic), yield–discount mappings, or volatility parameterizations.

## Summary

- Multiple integrals extend one-dimensional area to multidimensional volume.  
- The Jacobian corrects for distortion under variable transformations.  
- In probability, integration computes expectations, covariances, and prices.  
- Monte Carlo integration generalizes to high-dimensional financial problems.  
- These tools underpin simulation, copula modeling, and multi-asset derivative pricing.

Next, [Series Expansion and Taylor Approximation](series-expansion-and-taylor-approximation.md).
