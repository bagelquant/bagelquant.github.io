---
title: "Differentiation and Rates of Change"
permalink: /calculus/differentiation-and-rates-of-change/
sidebar:
  nav: calculus
header:
  overlay_image: assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

Differentiation is the central tool of calculus — it formalizes how quantities vary with respect to each other.  
In quantitative finance, differentiation measures *sensitivity*: how a small change in one variable (price, rate, volatility) affects another (portfolio value, risk, or return).

## 1. Definition

Let $f:\mathbb{R}\to\mathbb{R}$.  
The **derivative** of $f$ at $x=a$ is

$$
f'(a) = \lim_{h\to 0} \frac{f(a+h) - f(a)}{h},
$$

if this limit exists. The derivative represents the *instantaneous rate of change* of $f$ at $x=a$.

If $f'(a)$ exists for every $a$ in an interval, then $f$ is **differentiable** on that interval.

**Geometric interpretation:**  
The derivative equals the slope of the tangent line to $f(x)$ at $x=a$.

**Economic interpretation:**  
The derivative is the marginal change of output per unit change in input — e.g., marginal profit, marginal cost, marginal return.

## 2. Basic Differentiation Rules

Let $u(x)$ and $v(x)$ be differentiable functions and $c$ a constant.

1. **Constant Rule:** $(c)' = 0$  
2. **Power Rule:** $\frac{d}{dx} x^n = n x^{n-1}$ for all $n \in \mathbb{R}$  
3. **Exponential Rule:** $\frac{d}{dx} e^{x} = e^{x}$, and $\frac{d}{dx} e^{a x} = a e^{a x}$  
4. **Logarithmic Rule:** $\frac{d}{dx} \ln(x) = \frac{1}{x}$  
5. **Constant Multiple Rule:** $(c u)' = c u'$  
6. **Sum Rule:** $(u+v)' = u' + v'$  
7. **Product Rule:** $(uv)' = u'v + uv'$  
8. **Quotient Rule:** $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$  
9. **Chain Rule:** $\frac{d}{dx} f(g(x)) = f'(g(x)) \, g'(x)$

**Example:**  
For $f(x) = e^{3x^2}$,
$$
f'(x) = e^{3x^2} \cdot 6x.
$$

## 3. Derivatives of Common Functions

| Function $f(x)$ | Derivative $f'(x)$ |
|-----------------|--------------------|
| $x^n$ | $n x^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $1/x$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $a^x$ | $a^x \ln a$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |

**Verification Example:**  
If $f(x) = x^3 + 2x^2 - 5x + 4$, then
$$
f'(x) = 3x^2 + 4x - 5.
$$

## 4. The Chain Rule — Composition of Functions

Suppose $y=f(u)$ and $u=g(x)$, then
$$
\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx} = f'(g(x))g'(x).
$$

**Example:**  
Let $f(x)=\ln(3x^2+2)$. Then
$$
f'(x)=\frac{1}{3x^2+2}\cdot6x=\frac{6x}{3x^2+2}.
$$

In finance, this principle governs *propagation of sensitivities* — e.g., the delta of an option whose underlying itself depends on other factors.

## 5. Higher-Order Derivatives

The second derivative is
$$
f''(x) = \frac{d}{dx}\left(f'(x)\right).
$$

It measures curvature — the rate at which slope itself changes.

If $f''(x) > 0$, the function is *convex*; if $f''(x) < 0$, it is *concave*.

**Example:**  
$f(x)=x^3 \Rightarrow f''(x)=6x$ — positive for $x>0$, negative for $x<0$.

**Applications:**

- Convex payoff functions (options) have positive second derivative (Gamma).
- Portfolio curvature: second derivative of value wrt price or rate measures nonlinearity of exposure.

## 6. Implicit Differentiation

When $y$ is defined implicitly by $F(x,y)=0$, differentiation uses the chain rule:

$$
\frac{dF}{dx} = F_x + F_y \frac{dy}{dx} = 0 \Rightarrow \frac{dy}{dx} = -\frac{F_x}{F_y}.
$$

**Example:**  
For $x^2 + y^2 = 25$,  
$2x + 2y\frac{dy}{dx} = 0 \Rightarrow \frac{dy}{dx} = -\frac{x}{y}.$

**In Finance:**  
Used in sensitivities derived from equilibrium or constraint conditions, e.g. yield-curve bootstrapping where yields depend implicitly on discount factors.

## 7. Logarithmic Differentiation

When differentiating products or powers efficiently:

Take logs on both sides of $y = f(x)$, then differentiate:

$$
\ln y = \ln f(x) \quad \Rightarrow \quad \frac{1}{y} \frac{dy}{dx} = \frac{f'(x)}{f(x)}.
$$

**Example:**  
$y = x^x \Rightarrow \ln y = x \ln x \Rightarrow \frac{1}{y}\frac{dy}{dx} = \ln x + 1 \Rightarrow \frac{dy}{dx} = x^x(\ln x + 1).$

## 8. Differentiation in Financial Contexts

### 8.1 Instantaneous Rate of Return

For a continuously compounded return process:
$$
r_t = \frac{dS_t}{S_t \, dt}.
$$
The derivative here measures instantaneous proportional growth.

### 8.2 Yield Curve Slope

If $y(T)$ is the zero-coupon yield for maturity $T$,  
the slope $\frac{dy}{dT}$ measures how yields change with maturity (key rate sensitivity).

### 8.3 Option Greeks

The option price $V(S, \sigma, t)$ yields:
$$
\Delta = \frac{\partial V}{\partial S}, \quad
\Gamma = \frac{\partial^2 V}{\partial S^2}, \quad
\nu = \frac{\partial V}{\partial \sigma}.
$$
All are applications of partial differentiation and rates of change.

### 8.4 Duration and Convexity

For bond price $P(y)$ as a function of yield $y$:
$$
D = -\frac{1}{P}\frac{dP}{dy}, \quad C = \frac{1}{P}\frac{d^2 P}{dy^2}.
$$
Duration and convexity describe first- and second-order sensitivities to rate changes.

## 9. Differentiability vs Smoothness

- Differentiable ⇒ continuous  
- $C^1$ ⇒ continuously differentiable (no kinks)  
- $C^\infty$ ⇒ infinitely differentiable (smooth)

Smoothness is essential in models requiring Ito’s lemma or Taylor expansions.

**Example:**  
$|x|$ is not differentiable at 0 (kink), but $x^2$ is $C^\infty$.

## 10. Summary

- Differentiation formalizes infinitesimal rates of change.  
- Fundamental rules (chain, product, quotient) allow decomposition of complex relationships.  
- Second and higher derivatives reveal curvature and nonlinear effects.  
- In finance, derivatives quantify risk sensitivities — yield slopes, option Greeks, and exposure curvature.

Next, [Partial Derivatives and Gradients](partial-derivatives-and-gradients.md).
