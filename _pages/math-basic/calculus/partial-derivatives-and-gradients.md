---
title: "Partial Derivatives and Gradients"
permalink: /calculus/partial-derivatives-and-gradients

nav: "calculus"
header:
  overlay_image: assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

Many financial quantities depend on several variables — for example, an option’s value depends on price, volatility, time, and rates.  
To measure how such a multivariable function changes with respect to each variable independently, we use **partial derivatives**.  
Their collection, the **gradient**, describes the direction and magnitude of the steepest change.

## Functions of Several Variables

Let $f: \mathbb{R}^n \to \mathbb{R}$ and $\mathbf{x} = (x_1, x_2, \ldots, x_n)$.  
The function $f$ assigns a scalar output to multiple inputs.

**Examples in finance:**

- $V(S, \sigma, t)$ — option value as a function of price, volatility, and time.
- $P(y_1, y_2, \ldots, y_n)$ — bond portfolio value as a function of key interest rates.
- $L(w_1, w_2, \ldots, w_n)$ — portfolio loss as a function of factor exposures.

## Definition of a Partial Derivative

The **partial derivative** of $f$ with respect to $x_i$ is

$$
\frac{\partial f}{\partial x_i}(\mathbf{x}) =
\lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}.
$$

It measures the instantaneous rate of change in $f$ when only $x_i$ varies, all other variables held fixed.

**Example:**  
For $f(x,y) = x^2 y + 3xy^2$,  
$$
\frac{\partial f}{\partial x} = 2xy + 3y^2, \quad
\frac{\partial f}{\partial y} = x^2 + 6xy.
$$

**Interpretation:**  
Each partial derivative isolates the sensitivity of $f$ to one variable — similar to computing the “Greeks” in finance.

## Notation and Terminology

- $\frac{\partial f}{\partial x}$ : partial derivative with respect to $x$.  
- $\nabla f$ : gradient vector (all partial derivatives).  
- $D_i f$ : alternative notation for $\frac{\partial f}{\partial x_i}$.

If $f$ is differentiable in all arguments, the total differential is
$$
df = \sum_{i=1}^n \frac{\partial f}{\partial x_i} dx_i.
$$

This gives the **first-order approximation** of a small change in $f$.

**Example:**  
If $V(S, \sigma, t)$ is differentiable,  
$$
dV \approx \frac{\partial V}{\partial S} dS + \frac{\partial V}{\partial \sigma} d\sigma + \frac{\partial V}{\partial t} dt.
$$
In finance, this is the infinitesimal P&L approximation.

## The Gradient Vector

For $f: \mathbb{R}^n \to \mathbb{R}$, the gradient is defined as

$$
\nabla f(\mathbf{x}) =
\left(
\frac{\partial f}{\partial x_1},
\frac{\partial f}{\partial x_2},
\ldots,
\frac{\partial f}{\partial x_n}
\right).
$$

**Properties:**

- Points in the direction of steepest ascent of $f$.  
- Magnitude $|\nabla f|$ is the rate of maximal increase.  
- Orthogonal to level curves (or level surfaces) of $f$.

**Geometric Analogy:**  

In two variables $f(x,y)$, contours of equal $f$ form curves in $(x,y)$-space.  
$\nabla f$ is perpendicular to each contour.

**Financial Analogy:**  

$\nabla V = (\Delta, \nu, \Theta, \rho, \dots)$ — vector of Greeks describing sensitivities along each input dimension.

## Second-Order Partial Derivatives and Hessian Matrix

If all second-order derivatives exist and are continuous,  
the matrix of second derivatives is the **Hessian**:

$$
H(f) =
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}.
$$

**Clairaut’s Theorem:**  
If mixed partials are continuous,  
$$
\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}.
$$

**Interpretation:**  
The Hessian captures curvature and interaction effects — in finance, this reflects how risk factors jointly affect nonlinear portfolios.

**Example:**  
For $f(x,y)=x^2y+y^3$,  
$$
H(f)=
\begin{bmatrix}
2y & 2x \\
2x & 6y
\end{bmatrix}.
$$

Positive definiteness of $H$ implies local convexity (e.g., convex payoffs like calls).

## Total Differential and Sensitivity Approximation

The total differential gives a local linear approximation:

$$
df \approx \sum_{i=1}^n \frac{\partial f}{\partial x_i} \, dx_i = \nabla f^\top \, d\mathbf{x}.
$$

**Example (Option P&L):**
$$
dV \approx \Delta \, dS + \nu \, d\sigma + \Theta \, dt.
$$

This approximation forms the foundation of *delta-hedging* and *risk attribution*.  
Higher-order terms (e.g., $\frac{1}{2}\Gamma (dS)^2$) appear in second-order Taylor expansions.

## Chain Rule for Multivariable Functions

If $z = f(x,y)$ and $x = g(t)$, $y = h(t)$, then

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}.
$$

**Example:**  
If $f(x,y)=x^2y$, $x(t)=e^t$, $y(t)=t$,  
$$
\frac{dz}{dt} = 2xy\frac{dx}{dt} + x^2\frac{dy}{dt}
= 2e^t t e^t + e^{2t} = e^{2t}(2t+1).
$$

**Use in Finance:**  
When risk factors depend on common drivers (e.g., correlated market variables), total exposure to a driver is obtained via multivariate chain rule.

## Gradient in Optimization

The gradient vanishes at critical points:
$$
\nabla f(\mathbf{x}^*) = 0.
$$

To determine type:

- $H(f)$ positive definite → local minimum.  
- $H(f)$ negative definite → local maximum.  
- Indefinite → saddle point.

**Applications:**

- Portfolio optimization: $\nabla L(w) = 0$ gives optimal weights.  
- Calibration: gradients used in gradient-descent or quasi-Newton algorithms for parameter fitting.  
- Lagrange multipliers: enforce equality constraints $\nabla f = \lambda \nabla g$.

## Mixed Sensitivities in Finance

Consider a derivative portfolio value $V(S,\sigma,t)$.  
Second-order sensitivities (cross-partials):

$$
\frac{\partial^2 V}{\partial S \partial \sigma} = \text{Vanna}, \qquad
\frac{\partial^2 V}{\partial \sigma^2} = \text{Vomma}.
$$

These appear in the Taylor expansion:
$$
dV \approx \Delta \, dS + \nu \, d\sigma + \tfrac{1}{2}\Gamma (dS)^2 + \tfrac{1}{2}\text{Vomma} (d\sigma)^2 + \text{Vanna} \, dS \, d\sigma.
$$

Such interactions are crucial for hedging multi-risk portfolios.

## Directional Derivatives

For a unit vector $\mathbf{u}$,  
the **directional derivative** of $f$ at $\mathbf{x}$ in the direction of $\mathbf{u}$ is

$$
D_{\mathbf{u}} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}.
$$

It measures the instantaneous rate of change of $f$ in direction $\mathbf{u}$.

**Example:**  
If $\nabla f(1,2) = (3,4)$ and $\mathbf{u} = (1/\sqrt{2},1/\sqrt{2})$,  
then $D_{\mathbf{u}}f = 3/\sqrt{2} + 4/\sqrt{2} = 7/\sqrt{2}$.

**Interpretation:**  
In portfolio space, $\mathbf{u}$ may represent a normalized portfolio change; $D_{\mathbf{u}} f$ is the marginal change in portfolio value along that direction.

## Summary

- Partial derivatives isolate sensitivities to individual variables.  
- The gradient aggregates these sensitivities and points in the direction of steepest ascent.  
- The Hessian encodes curvature and cross-effects, essential for risk decomposition and optimization.  
- In finance, these tools form the mathematical language of multi-factor risk analysis, portfolio optimization, and option Greeks.

Next, [Integration and Areas Under Curves](integration-and-areas-under-curves.md).
