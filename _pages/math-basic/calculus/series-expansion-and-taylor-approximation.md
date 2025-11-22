---
title: "Series Expansion and Taylor Approximation"
permalink: /calculus/series-expansion-and-taylor-approximation/

nav: "calculus"
---

Series expansions allow us to approximate complex nonlinear functions with polynomial terms around a known point.  
In quantitative finance, Taylor expansions are used for **risk approximation**, **Greeks computation**, and **convexity adjustments** — expressing prices and sensitivities in powers of small perturbations.

## Power Series and Analytic Functions

A **power series** centered at $a$ is a sum of the form:

$$
\sum_{n=0}^\infty c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots
$$

If the series converges for $|x-a|<R$, where $R$ is the **radius of convergence**, the function defined by this series is said to be *analytic* at $a$.

**Example:**  
The exponential function has the representation:
$$
e^x = \sum_{n=0}^\infty \frac{x^n}{n!}.
$$

The sine and cosine functions similarly:
$$
\sin x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{(2n+1)!}, \quad
\cos x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}.
$$

## Taylor Series

If $f(x)$ is infinitely differentiable near $a$, its **Taylor series** expansion around $a$ is:

$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots
$$

Or compactly,
$$
f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n.
$$

The **remainder term** after truncating at order $n$ (Taylor’s theorem) is:
$$
R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}, \quad \text{for some } \xi \text{ between } a \text{ and } x.
$$

**Example:**  
Expanding $e^x$ around $a=0$:
$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
$$

## Maclaurin Series

A special case with $a=0$:
$$
f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots
$$

**Examples:**

- $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$, $|x|<1$
- $(1+x)^r = 1 + rx + \frac{r(r-1)}{2!}x^2 + \frac{r(r-1)(r-2)}{3!}x^3 + \cdots$

The binomial series extends to non-integer $r$, crucial in continuous compounding and yield approximations.

## First and Second Order Approximations

Truncating the series gives **linear** and **quadratic** approximations:

**First order (linearization):**
$$
f(x) \approx f(a) + f'(a)(x-a).
$$

**Second order (quadratic):**
$$
f(x) \approx f(a) + f'(a)(x-a) + \frac{1}{2}f''(a)(x-a)^2.
$$

These approximations capture the slope and curvature near $a$.  
They form the foundation for **Greeks expansion** and **hedging analysis**.

**Example (Option Price Sensitivity):**
$$
dV \approx \Delta\,dS + \frac{1}{2}\Gamma\,(dS)^2.
$$
Here, $\Delta = \frac{\partial V}{\partial S}$ and $\Gamma = \frac{\partial^2 V}{\partial S^2}$ are the first and second derivatives with respect to $S$.

## Taylor Expansion in Several Variables

For $f(x_1,\ldots,x_n)$, the first- and second-order Taylor expansion around $\mathbf{a}$ is:

$$
f(\mathbf{x}) \approx f(\mathbf{a})
+ \nabla f(\mathbf{a})^\top (\mathbf{x}-\mathbf{a})
+ \frac{1}{2} (\mathbf{x}-\mathbf{a})^\top H(f)(\mathbf{a}) (\mathbf{x}-\mathbf{a}),
$$

where $\nabla f$ is the gradient and $H(f)$ is the Hessian matrix.

**In Finance:**

- $\nabla f$: vector of sensitivities (Greeks)
- $H(f)$: curvature matrix of cross-Greeks
- The expansion provides the **second-order P&L approximation** used in risk aggregation.

## Error and Convergence

The accuracy of a truncated Taylor expansion depends on the remainder $R_n(x)$ and the behavior of higher derivatives.

If $\lim_{n\to\infty} R_n(x)=0$ for $|x-a|<R$, then the Taylor series converges to $f(x)$ in that interval.

However, convergence does not always guarantee equality — some functions are infinitely differentiable but not equal to their Taylor series outside the convergence domain.

**Example:**  
$f(x) = e^{-1/x^2}$ for $x\neq 0$ and $f(0)=0$ has all derivatives zero at 0, but $f(x)\neq 0$ for $x\neq 0$.

## Applications in Quantitative Finance

### Option Pricing Approximations

Small perturbations in inputs allow for local approximations:
$$
V(S+\Delta S) \approx V(S) + \Delta\,\Delta S + \tfrac{1}{2}\Gamma (\Delta S)^2.
$$
This expansion isolates linear (delta) and quadratic (gamma) risk components, forming the backbone of **delta-gamma hedging**.

### Convexity Adjustment

In interest rate products, the expectation of a nonlinear function of rates can be expanded:
$$
E[f(r)] \approx f(E[r]) + \tfrac{1}{2}f''(E[r])Var(r).
$$
The correction term is the **convexity adjustment**, arising from Jensen’s inequality for convex functions.

### Volatility Expansion

For implied volatility $\sigma = \sigma_0 + \epsilon$, one can expand price $V(\sigma)$:
$$
V(\sigma) \approx V(\sigma_0) + \nu (\sigma - \sigma_0) + \tfrac{1}{2}\text{Vomma}(\sigma - \sigma_0)^2,
$$
capturing vega and higher-order vol sensitivities.

### Duration and Convexity of Bonds

Bond price as function of yield $y$:
$$
P(y) \approx P(y_0) - D\,P(y_0)(y - y_0) + \tfrac{1}{2}C\,P(y_0)(y - y_0)^2.
$$
This gives the **duration-convexity** decomposition for yield curve risk management.

## Asymptotic Expansions

Taylor series often provide local approximations; for extreme values or limits, **asymptotic expansions** are used:

$$
f(x) \sim a_0 + \frac{a_1}{x} + \frac{a_2}{x^2} + \cdots, \quad x \to \infty.
$$

Used in:

- Approximation of option tails (e.g., far OTM Black–Scholes prices)
- Large deviation theory
- Laplace and saddlepoint methods in risk analytics

## Logarithmic and Exponential Approximations

Frequently used first-order expansions:

| Function | Approximation near 0 |
|-----------|---------------------|
| $\ln(1+x)$ | $x - \tfrac{x^2}{2} + \tfrac{x^3}{3}$ |
| $e^x$ | $1 + x + \tfrac{x^2}{2}$ |
| $(1+x)^r$ | $1 + rx + \tfrac{r(r-1)}{2}x^2$ |

**In Finance:**

- $\ln(1+r) \approx r$ for small $r$ → link between discrete and continuous returns.
- $(1+y/m)^{mT} \approx e^{yT}$ → continuous compounding approximation.

## Summary

- Series expansions approximate smooth functions via polynomial terms.  
- Taylor’s theorem provides systematic local approximations and error control.  
- In finance, expansions linearize and quadratize models for analytical intuition.  
- Key applications: delta-gamma hedging, convexity corrections, volatility perturbations, and yield curve risk.  
- Understanding truncation errors ensures correct interpretation of sensitivities and risk exposure.
