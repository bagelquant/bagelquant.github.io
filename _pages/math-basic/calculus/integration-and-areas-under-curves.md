---
title: "Integration and Areas Under Curves"
permalink: /calculus/integration-and-areas-under-curves/
sidebar:
  nav: "calculus"
header:
  overlay_image: assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

Integration is the inverse operation of differentiation.  
Where differentiation measures instantaneous change, integration measures total accumulation.  
In finance, integration underlies pricing by expectation, continuous compounding, and risk aggregation — computing areas, totals, or probabilities over continuous domains.

## 1. The Concept of Integral

Given a continuous function $f:[a,b]\to\mathbb{R}$, the **definite integral** of $f$ over $[a,b]$ is the limit of Riemann sums:

$$
\int_a^b f(x)\,dx =
\lim_{n \to \infty}\sum_{i=1}^{n} f(x_i^*) \,\Delta x_i,
$$

where $\Delta x_i = \frac{b-a}{n}$ and $x_i^* \in [x_{i-1},x_i]$.

This represents the **area under the curve** $y=f(x)$ from $x=a$ to $x=b$.

If the limit exists and is finite, $f$ is **Riemann integrable** on $[a,b]$.

**Geometric interpretation:**  

- For $f(x)\ge0$, the integral is the exact area under $f$.  
- For $f(x)$ of mixed sign, areas below the axis subtract from the total.

## 2. Indefinite Integral and Antiderivative

The **indefinite integral** (antiderivative) of $f$ is any function $F$ such that $F'(x)=f(x)$:

$$
\int f(x)\,dx = F(x) + C,
$$

where $C$ is an arbitrary constant.

**Example:**  
$\int 3x^2\,dx = x^3 + C$.

**Fundamental Theorem of Calculus:**  
If $f$ is continuous on $[a,b]$ and $F'(x)=f(x)$, then
$$
\int_a^b f(x)\,dx = F(b) - F(a).
$$

Differentiation and integration are inverse processes.

## 3. Linearity and Basic Rules

For integrable functions $f,g$ and constant $c$:

1. $\int (f + g)\,dx = \int f\,dx + \int g\,dx$
2. $\int c f\,dx = c \int f\,dx$
3. $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$
4. If $a<b<c$, $\int_a^c f(x)\,dx = \int_a^b f(x)\,dx + \int_b^c f(x)\,dx$

**Example:**
$$
\int_0^2 (3x^2 - 2x)\,dx = [x^3 - x^2]_0^2 = 8 - 4 = 4.
$$

## 4. Standard Integrals

| Function | $\displaystyle \int f(x)\,dx$ |
|-----------|-------------------------------|
| $x^n$, $n\neq -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |
| $1/x$ | $\ln\|x\|+C$ |
| $e^x$ | $e^x+C$ |
| $a^x$ | $\dfrac{a^x}{\ln a}+C$ |
| $\sin x$ | $-\cos x+C$ |
| $\cos x$ | $\sin x+C$ |
| $\sec^2 x$ | $\tan x+C$ |
| $\frac{1}{1+x^2}$ | $\tan^{-1}x+C$ |

These form the building blocks for analytic integration.

## 5. Integration Techniques

### 5.1 Substitution (Change of Variable)

If $u=g(x)$, then
$$
\int f(g(x))g'(x)\,dx = \int f(u)\,du.
$$

**Example:**
$$
\int e^{3x}\,dx = \frac{1}{3}e^{3x}+C.
$$

### 5.2 Integration by Parts

If $u=u(x)$ and $v=v(x)$ are differentiable,
$$
\int u\,dv = uv - \int v\,du.
$$

**Example:**
$$
\int x e^x dx = x e^x - \int e^x dx = e^x(x - 1) + C.
$$

### 5.3 Partial Fractions

For rational functions, decompose into simpler fractions and integrate term by term.

**Example:**
$$
\int \frac{1}{x(x+1)} dx = \int \left( \frac{1}{x} - \frac{1}{x+1} \right) dx = \ln\left|\frac{x}{x+1}\right| + C.
$$

### 5.4 Improper Integrals

When limits are infinite or integrand has singularity, use limit definition:

$$
\int_a^\infty f(x)\,dx = \lim_{b\to\infty} \int_a^b f(x)\,dx.
$$

**Example:**
$$
\int_1^\infty \frac{1}{x^2}dx = \left[-\frac{1}{x}\right]_1^\infty = 1.
$$

## 6. Applications in Finance

### 6.1 Continuous Compounding

The continuously compounded value of principal $P_0$ at rate $r$ over $[0,T]$ is
$$
P_T = P_0 e^{\int_0^T r(t)\,dt}.
$$

If $r(t)$ is constant, $\int_0^T r\,dt = rT$, giving $P_T = P_0 e^{rT}$.

### 6.2 Expected Value and Pricing

If $X$ is a continuous random variable with pdf $p(x)$, then
$$
E[X] = \int_{-\infty}^{\infty} x p(x)\,dx.
$$

In risk-neutral pricing:
$$
V_0 = e^{-rT}\int_0^\infty f(S_T)p(S_T)\,dS_T.
$$

Thus, valuation becomes integration of discounted payoff weighted by probability density.

### 6.3 Continuous Portfolio Returns

Instantaneous return rate:
$$
r_t = \frac{dS_t}{S_t dt} \quad \Rightarrow \quad \ln\frac{S_T}{S_0} = \int_0^T r_t\,dt.
$$

### 6.4 Total Risk (Variance Integration)

Variance of a continuous variable:
$$
Var(X) = \int_{-\infty}^\infty (x - E[X])^2 p(x)\,dx.
$$

This integration measures dispersion around the mean — core to risk quantification.

## 7. Connection to Differentiation

If $F(x)=\int_a^x f(t)\,dt$, then by the fundamental theorem,
$$
\frac{dF}{dx}=f(x).
$$

Conversely, $\int f'(x)\,dx = f(x) + C$.

Differentiation decomposes accumulation; integration reconstructs it.

## 8. Numerical Integration

When analytic evaluation is impossible, approximate via discrete summation.

**Riemann approximation:**
$$
\int_a^b f(x)\,dx \approx \sum_{i=1}^n f(x_i)\Delta x.
$$

**Trapezoidal rule:**
$$
\int_a^b f(x)\,dx \approx \frac{\Delta x}{2}\left(f(a)+2\sum_{i=1}^{n-1}f(x_i)+f(b)\right).
$$

**Monte Carlo integration:**
$$
\int_a^b f(x)\,dx \approx (b-a)\frac{1}{N}\sum_{i=1}^N f(U_i), \quad U_i \sim \text{Uniform}(a,b).
$$

In finance, Monte Carlo integration generalizes to expectation over high-dimensional stochastic spaces.

## 9. Improper and Infinite Domain Integrals in Probability

For densities $p(x)$ defined over $\mathbb{R}$, we require:
$$
\int_{-\infty}^\infty p(x)\,dx = 1.
$$

**Example:**  
For the standard normal density
$$
p(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2},
$$
we have
$$
\int_{-\infty}^\infty p(x)\,dx = 1.
$$

Many pricing integrals (e.g., Black–Scholes expectation) are Gaussian-weighted improper integrals.

## 10. Summary

- Integration accumulates infinitesimal contributions.  
- The definite integral computes total change or area; the indefinite integral reverses differentiation.  
- Financial applications include continuous compounding, expected values, and risk aggregation.  
- In probabilistic pricing, every valuation integral is an area under a probability density.  
- Numerical integration (trapezoidal, Monte Carlo) bridges analytic calculus with computational finance.

Next, [Multivariable Integration and Change of Variables](multivariable-integration-and-change-of-variables.md).
