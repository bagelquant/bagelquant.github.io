---
title: "Applications of Partial Derivatives"
permalink: /calculus/applications-of-partial-derivatives/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

Partial derivatives are the key to finding maximum and minimum values for functions of several variables. This process, known as **multivariable optimization**, is fundamental to solving problems in fields from engineering to economics and finance.

## Maxima and Minima

Just like in single-variable calculus, we have local and absolute extrema.
-   A function $f(x, y)$ has a **local maximum** at $(a, b)$ if $f(x, y) \le f(a, b)$ for all points $(x, y)$ in a disk centered at $(a, b)$.
-   A function $f(x, y)$ has a **local minimum** at $(a, b)$ if $f(x, y) \ge f(a, b)$ for all points $(x, y)$ in a disk centered at $(a, b)$.

**Key Insight:** At a local maximum or minimum, the tangent plane to the surface is horizontal. This means the slopes in all directions are zero. Therefore, all partial derivatives must be zero.

### Critical Points

A point $(a, b)$ is a **critical point** of $f$ if:
1.  $\frac{\partial f}{\partial x}(a, b) = 0$ and $\frac{\partial f}{\partial y}(a, b) = 0$ (i.e., $\nabla f(a, b) = \mathbf{0}$), or
2.  One of the partial derivatives does not exist.

Local extrema can only occur at critical points.

### The Second Derivatives Test

To classify a critical point, we use the **Second Derivatives Test**, which involves the **discriminant** $D$, calculated from the Hessian matrix.

Let
$$ D(a, b) = f_{xx}(a, b) f_{yy}(a, b) - [f_{xy}(a, b)]^2 $$

1.  If $D > 0$ and $f_{xx}(a, b) > 0$, then $f(a, b)$ is a **local minimum**.
2.  If $D > 0$ and $f_{xx}(a, b) < 0$, then $f(a, b)$ is a **local maximum**.
3.  If $D < 0$, then $f(a, b)$ is a **saddle point** (neither a max nor a min).
4.  If $D = 0$, the test is inconclusive.

**Example:**
Find and classify the critical points of $f(x, y) = x^2 + y^2 + x^2y + 4$.

1.  **Find partial derivatives:**
    $f_x = 2x + 2xy = 2x(1+y)$
    $f_y = 2y + x^2$
2.  **Find critical points (set partials to 0):**
    From $f_x = 0$, we get $x=0$ or $y=-1$.
    -   If $x=0$, then from $f_y=0$, we get $2y + 0 = 0 \implies y=0$. So, **(0, 0)** is a critical point.
    -   If $y=-1$, then from $f_y=0$, we get $2(-1) + x^2 = 0 \implies x^2 = 2 \implies x = \pm\sqrt{2}$. So, **($\sqrt{2}$, -1)** and **(-$\sqrt{2}$, -1)** are critical points.
3.  **Find second derivatives:**
    $f_{xx} = 2 + 2y$
    $f_{yy} = 2$
    $f_{xy} = 2x$
4.  **Apply the Second Derivatives Test:**
    -   At **(0, 0):**
        $f_{xx}(0,0) = 2$, $D = (2)(2) - 0^2 = 4 > 0$. Since $f_{xx} > 0$, this is a **local minimum**.
    -   At **($\sqrt{2}$, -1):**
        $D = (2 + 2(-1))(2) - (2\sqrt{2})^2 = 0 - 8 = -8 < 0$. This is a **saddle point**.
    -   At **(-$\sqrt{2}$, -1):**
        $D = (2 + 2(-1))(2) - (-2\sqrt{2})^2 = 0 - 8 = -8 < 0$. This is a **saddle point**.

## Constrained Optimization: Lagrange Multipliers

Often, we need to find the maximum or minimum of a function subject to a **constraint**. For example, maximizing profit subject to a budget. The method of **Lagrange multipliers** is a powerful technique for this.

**The Problem:** Maximize or minimize a function $f(x, y)$ subject to the constraint $g(x, y) = k$.

**The Method:**
Geometrically, at an extremum, the gradient of the function $f$ must be parallel to the gradient of the constraint function $g$. This is because if they were not parallel, you could move along the constraint curve and increase the value of $f$.

Two vectors are parallel if one is a scalar multiple of the other. So, we must have:
$$ \nabla f(x, y) = \lambda \nabla g(x, y) $$
where $\lambda$ (lambda) is a constant called the **Lagrange multiplier**.

This vector equation, along with the original constraint, gives us a system of equations to solve for $x$, $y$, and $\lambda$:
1.  $f_x = \lambda g_x$
2.  $f_y = \lambda g_y$
3.  $g(x, y) = k$

**Financial Application: Utility Maximization**
A common problem in economics is to maximize an investor's utility function $U(x, y)$ (where $x$ and $y$ are quantities of two assets) subject to a budget constraint $p_x x + p_y y = B$. Using Lagrange multipliers, we find the optimal allocation where the marginal utility per dollar spent is equal for both assets.

## Summary

-   Partial derivatives are used to find **critical points** of multivariable functions, which are candidates for maxima or minima.
-   The **Second Derivatives Test** helps classify these critical points as local maxima, minima, or saddle points.
-   The method of **Lagrange multipliers** is a powerful tool for finding the extrema of a function subject to a constraint.
-   These optimization techniques are central to solving problems in finance, such as finding optimal portfolio allocations or calibrating model parameters.

Next, we will extend our study of integration to multiple dimensions with [Multiple Integrals](multiple-integrals.md).
