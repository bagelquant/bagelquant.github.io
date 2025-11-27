---
title: "Partial Derivatives and Gradients"
permalink: /calculus/partial-derivatives/
nav: "calculus"
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

In single-variable calculus, the derivative measures the rate of change of a function. But what about functions of multiple variables, like the value of an option which depends on stock price, time, and volatility? To understand how such a function changes, we introduce the **partial derivative**.

## Functions of Several Variables

A function of two variables, $f(x, y)$, maps each ordered pair $(x, y)$ in a domain $D \subset \mathbb{R}^2$ to a unique real number $z = f(x, y)$. The graph of such a function is a **surface** in three-dimensional space.

**Financial Example:** A simple portfolio's value $V$ might depend on the price of two stocks, $S_1$ and $S_2$. We could write this as a function $V(S_1, S_2)$.

## Partial Derivatives

The **partial derivative** of $f(x, y)$ with respect to $x$ is found by treating $y$ as a constant and differentiating with respect to $x$. It is denoted by $\frac{\partial f}{\partial x}$ or $f_x$.

$$ 
\frac{\partial f}{\partial x}(x,y) = \lim_{h \to 0} \frac{f(x+h, y) - f(x,y)}{h} 
$$

Similarly, the partial derivative with respect to $y$ is found by treating $x$ as a constant:

$$ 
\frac{\partial f}{\partial y}(x,y) = \lim_{h \to 0} \frac{f(x, y+h) - f(x,y)}{h} 
$$

**Geometric Interpretation:**
-   $\frac{\partial f}{\partial x}$ is the slope of the surface in the direction of the x-axis.
-   $\frac{\partial f}{\partial y}$ is the slope of the surface in the direction of the y-axis.

**Example:**
Find the partial derivatives of $f(x, y) = x^3 + x^2y^3 - 2y^2$.
-   To find $f_x$, treat $y$ as a constant:
    $$ f_x(x,y) = 3x^2 + 2xy^3 - 0 = 3x^2 + 2xy^3 $$ 
-   To find $f_y$, treat $x$ as a constant:
    $$ f_y(x,y) = 0 + x^2(3y^2) - 4y = 3x^2y^2 - 4y $$ 

## The Gradient Vector

The **gradient** of a function $f(x, y)$, denoted $\nabla f$, is the vector of its partial derivatives:

$$ 
\nabla f(x,y) = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle = f_x(x,y)\mathbf{i} + f_y(x,y)\mathbf{j} 
$$ 

The gradient is incredibly important for two reasons:
1.  It points in the direction of the **steepest ascent** of the function at that point.
2.  Its magnitude, $\|\nabla f\|$, is the maximum rate of change.

## The Directional Derivative

The partial derivatives tell us the rate of change in the x and y directions. But what about other directions?

The **directional derivative** of $f$ in the direction of a unit vector $\mathbf{u} = \langle a, b \rangle$ is given by the dot product of the gradient and the direction vector:

$$ 
D_{\mathbf{u}}f(x,y) = \nabla f(x,y) \cdot \mathbf{u} = \frac{\partial f}{\partial x}a + \frac{\partial f}{\partial y}b 
$$ 

This tells you the slope of the surface if you were to walk in the direction of **u**.

## Higher-Order Partial Derivatives

We can take partial derivatives of partial derivatives. For a function $f(x, y)$, there are four second-order partial derivatives:

1.  $f_{xx} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial x^2}$
2.  $f_{yy} = \frac{\partial}{\partial y} \left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial y^2}$
3.  $f_{xy} = \frac{\partial}{\partial y} \left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial y \partial x}$ (Differentiate w.r.t. x, then y)
4.  $f_{yx} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial x \partial y}$ (Differentiate w.r.t. y, then x)

**Clairaut's Theorem:** If the second partial derivatives are continuous, then the order of differentiation does not matter: $f_{xy} = f_{yx}$.

## Tangent Planes and Linear Approximations

Just as we used a tangent line to approximate a single-variable function, we can use a **tangent plane** to approximate a multivariable function near a point $(x_0, y_0)$.

The equation of the tangent plane to the surface $z = f(x, y)$ at the point $(x_0, y_0, z_0)$ is:
$$ 
z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) 
$$ 
This leads to the **linear approximation** of $f$ at $(x_0, y_0)$:
$$ 
f(x, y) \approx f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) 
$$ 

## Financial Application: The Greeks

The partial derivatives of an option's price are so important they are given Greek letter names. For an option price $V(S, t, \sigma, r, K)$:

-   **Delta ($\Delta$):** $\frac{\partial V}{\partial S}$ - Rate of change with respect to the stock price.
-   **Theta ($\Theta$):** $\frac{\partial V}{\partial t}$ - Rate of change with respect to time (time decay).
-   **Vega ($\nu$):** $\frac{\partial V}{\partial \sigma}$ - Rate of change with respect to volatility.
-   **Rho ($\rho$):** $\frac{\partial V}{\partial r}$ - Rate of change with respect to the interest rate.
-   **Gamma ($\\Gamma$):** $\frac{\partial^2 V}{\partial S^2}$ - The second partial derivative with respect to stock price, measuring the curvature of the option's value.

Using the linear approximation (also called a Taylor expansion), the change in an option's value can be approximated as:
$$ 
\Delta V \approx \Delta \cdot \Delta S + \Theta \cdot \Delta t + \nu \cdot \Delta \sigma + \rho \cdot \Delta r 
$$ 
This is the fundamental formula used for hedging and risk management of derivative portfolios.

## Practice Problems

Let $f(x, y) = x e^{xy}$.
1.  Find the partial derivatives $f_x$ and $f_y$.
2.  Find the gradient vector $\nabla f$ at the point $(1, 0)$.
3.  Find the directional derivative of $f$ at $(1, 0)$ in the direction of the vector $\mathbf{v} = \langle 3, 4 \rangle$. (Remember to use a unit vector for the direction!).
4.  Find all second-order partial derivatives ($f_{xx}, f_{yy}, f_{xy}, f_{yx}$) and verify that $f_{xy} = f_{yx}$.

*(Solutions will be provided in a separate section or at the end of the course).*

Next, we will use these concepts to solve optimization problems in multiple dimensions in [Applications of Partial Derivatives](applications-of-partial-derivatives.md).

---

[View Problems and Solutions for Partial Derivatives](/math-basic/calculus/problems/partial-derivatives-problems/)
