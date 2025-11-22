---
title: "Introduction to Calculus"
permalink: /calculus/introduction-to-calculus/
header:
  overlay_image: assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

Calculus is the mathematical foundation of continuous change.  
In quantitative finance, it underpins derivative pricing, risk management, and dynamic optimization — from computing sensitivities (Greeks) to modeling stochastic processes in continuous time.

## 1. The Concept of Limit

Let $f: \mathbb{R} \to \mathbb{R}$.  
We say that $f(x)$ approaches $L$ as $x$ approaches $a$ if, for every $\epsilon > 0$, there exists $\delta > 0$ such that

$$
0 < |x - a| < \delta \implies |f(x) - L| < \epsilon.
$$

This formal $\epsilon$–$\delta$ definition allows calculus to treat continuous motion precisely.

**Example:**  
For $f(x) = 3x + 2$,  
$$
\lim_{x \to 1} f(x) = 5.
$$

**Remark:**  
Limits describe continuity, differentiability, and integral accumulation — all subsequent operations are built upon this notion.

## 2. Continuity

A function $f(x)$ is *continuous* at $x=a$ if:

1. $f(a)$ is defined,  
2. $\lim_{x \to a} f(x)$ exists, and  
3. $\lim_{x \to a} f(x) = f(a)$.

Equivalently, small perturbations in $x$ produce small changes in $f(x)$.

**Example:**  
Polynomial and exponential functions are continuous everywhere; step or piecewise functions may not be.

**In Finance:**  
Continuity allows infinitesimal modeling — asset prices $S_t$ are modeled as continuous semimartingales, even though real prices move discretely.

## 3. The Derivative

The **derivative** of $f$ at point $x=a$ is defined by the limit:

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}.
$$

It measures the *instantaneous rate of change* or the slope of the tangent line to $f$ at $x=a$.

**Existence:**  
If the above limit exists (finite), $f$ is *differentiable* at $a$.

**Example:**  
$f(x) = x^2 \Rightarrow f'(x) = 2x.$

## 4. Higher-Order Derivatives

Repeated differentiation yields higher-order derivatives:

$$
f^{(n)}(x) = \frac{d^n f(x)}{dx^n}.
$$

These measure curvature and higher-order sensitivities — analogous to Gamma, Vomma, and higher Greeks in option pricing.

**Example:**  
For $f(x) = e^{ax}$,  
$$
f^{(n)}(x) = a^n e^{ax}.
$$

## 5. Differentiation Rules

Let $u(x)$ and $v(x)$ be differentiable functions.

1. **Linearity:** $(au + bv)' = au' + bv'$  
2. **Product Rule:** $(uv)' = u'v + uv'$  
3. **Quotient Rule:** $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$  
4. **Chain Rule:** $\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$

**Example (Chain Rule):**  
If $f(x) = e^{3x^2}$,  
then $f'(x) = e^{3x^2} \cdot 6x.$

## 6. Differentiability and Continuity

Every differentiable function is continuous,  
but continuity does not imply differentiability.

**Counterexample:**  
$f(x) = |x|$ is continuous at $x=0$ but not differentiable there:
$$
\lim_{h\to 0^+}\frac{|h|-0}{h}=1,\quad
\lim_{h\to 0^-}\frac{|h|-0}{h}=-1.
$$

## 7. The Mean Value Theorem (MVT)

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$,  
then there exists $c \in (a,b)$ such that

$$
f'(c) = \frac{f(b) - f(a)}{b - a}.
$$

**Interpretation:**  
There exists a point where the instantaneous slope equals the average rate of change.

**In Finance:**  
The theorem underlies linear approximations like Delta hedging — local linearization of payoff with respect to the underlying.

## 8. The Integral — The Inverse of Differentiation

Given $f(x)$ continuous on $[a,b]$,  
the **definite integral** is the limit of Riemann sums:

$$
\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x_i.
$$

It represents the *accumulated area* under $f(x)$ from $a$ to $b$.

**Fundamental Theorem of Calculus:**

If $F'(x) = f(x)$, then
$$
\int_a^b f(x)\,dx = F(b) - F(a).
$$

Thus differentiation and integration are inverse operations.

## 9. Applications in Quantitative Finance

1. **Instantaneous returns:**  
   $r_t = \frac{dS_t}{S_t\,dt}$ → continuous compounding.  
2. **Sensitivity analysis:**  
   Greeks = partial derivatives of option price $V(S, \sigma, t, \dots)$.  
3. **Optimization:**  
   Portfolio weights solved via derivative-based first-order conditions.  
4. **Continuous-time models:**  
   Ito calculus extends these limits to stochastic processes.

## 10. Key Takeaways

- Limits formalize continuity and smoothness.  
- Derivatives quantify infinitesimal changes.  
- Integrals accumulate effects over continuous domains.  
- The interplay between the two forms the foundation of continuous-time finance.

This groundwork supports more advanced topics such as **partial differentiation**, **multivariable integration**, and **stochastic calculus**.

Next, [Differentiation and Rates of Change](differentiation-and-rates-of-change.md).

---

Some differentiation formulas for reference:

| Function                | Derivative                     |
|-------------------------|--------------------------------|
| $c$ (constant)          | $0$                            |
| $x^n$                   | $nx^{n-1}$                     |
| $e^{x}$                 | $e^{x}$                        |
| $e^{cx}$                | $ce^{cx}$                      |
| $\ln(x)$                | $\frac{1}{x}$                  |
| $\sin(x)$               | $\cos(x)$                      |
| $\cos(x)$               | $-\sin(x)$                     |
| $\tan(x)$               | $\sec^2(x)$                    |
| $u(x)v(x)$             | $u'(x)v(x) + u(x)v'(x)$       |
| $\frac{u(x)}{v(x)}$    | $\frac{u'(x)v(x) - u(x)v'(x)}{v^2(x)}$ |
| $f(g(x))$              | $f'(g(x)) \cdot g'(x)$         |
| $f^{(n)}(x)$            | $\frac{d^n f(x)}{dx^n}$         |

Derivative Rules Summary:

|Derivatives Rule         | Description                    |
|-------------------------|--------------------------------|
|Sum                      | $\frac{d}{dx}[u + v] = \frac{du}{dx} + \frac{dv}{dx}$ |
|Product                 | $\frac{d}{dx}[uv] = u\frac{dv}{dx} + v\frac{du}{dx}$ |
|Quotient                | $\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}$ |
|Chain                    | $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$ |
|Power                   | $\frac{d}{dx}[u^n] = nu^{n-1}\frac{du}{dx}$ |
|Inverse                  | $\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}$ |
