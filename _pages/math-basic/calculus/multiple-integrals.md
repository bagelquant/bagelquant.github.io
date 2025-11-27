---
title: "Multiple Integrals"
permalink: /calculus/multiple-integrals/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

Just as we extended the concept of a derivative to functions of multiple variables, we can also extend the concept of an integral. **Multiple integrals** allow us to compute the "volume under a surface" or to integrate over two- and three-dimensional regions.

## Double Integrals over Rectangles

Let's start with a function $f(x, y)$ of two variables defined on a rectangular region $R = [a, b] \times [c, d]$.

Just as we approximated area with Riemann sums, we can approximate the volume under the surface $z = f(x, y)$ by dividing the rectangle $R$ into a grid of smaller sub-rectangles, each with area $\Delta A = \Delta x \Delta y$.

The **double integral** is the limit of these double Riemann sums as the number of sub-rectangles goes to infinity:
$$
\iint_R f(x,y)\,dA = \lim_{m,n\to\infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(x_{ij}^*, y_{ij}^*)\,\Delta A
$$

### Iterated Integrals and Fubini's Theorem

Calculating double integrals from the definition is impractical. **Fubini's Theorem** states that if $f$ is continuous on the rectangle $R$, we can calculate the double integral as an **iterated integral**, where we integrate with respect to one variable at a time, holding the other constant.

$$
\iint_R f(x,y)\,dA = \int_c^d \left[ \int_a^b f(x,y)\,dx \right] dy = \int_a^b \left[ \int_c^d f(x,y)\,dy \right] dx
$$

The order of integration does not matter for rectangular regions.

**Example:**
Evaluate $\iint_R (xy^2) \,dA$ over the rectangle $R = \{(x, y) | 0 \le x \le 2, 1 \le y \le 3 \}$.

$$
\begin{aligned}
\int_1^3 \int_0^2 xy^2 \,dx\,dy &= \int_1^3 \left[ \frac{x^2}{2}y^2 \right]_{x=0}^{x=2} dy \\
&= \int_1^3 \left( \frac{2^2}{2}y^2 - 0 \right) dy = \int_1^3 2y^2 \,dy \\
&= \left[ \frac{2}{3}y^3 \right]_1^3 = \frac{2}{3}(3^3 - 1^3) = \frac{2}{3}(26) = \frac{52}{3}
\end{aligned}
$$

## Double Integrals over General Regions

We often need to integrate over non-rectangular regions.
-   **Type I Region:** A region bounded by $x=a$, $x=b$, $y=g_1(x)$, and $y=g_2(x)$.
    $$
    \iint_D f(x,y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx
    $$
-   **Type II Region:** A region bounded by $y=c$, $y=d$, $x=h_1(y)$, and $x=h_2(y)$.
    $$
    \iint_D f(x,y)\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy
    $$

**Strategy:**
1.  Sketch the region of integration.
2.  Decide whether to integrate with respect to $x$ or $y$ first. One order may be much simpler than the other.
3.  Set up the limits of integration based on the sketch.
4.  Evaluate the iterated integral.

## Change of Variables: The Jacobian

Sometimes, changing the coordinate system can dramatically simplify an integral. The most common change is from Cartesian coordinates $(x, y)$ to **polar coordinates** $(r, \theta)$.

The relationship is:
$$ x = r\cos\theta, \quad y = r\sin\theta $$

When we change variables, the infinitesimal area element $dA$ also changes. The conversion factor is the absolute value of the **Jacobian determinant**:
$$ 
  dA = dx\,dy = \left| \frac{\partial(x,y)}{\partial(r,\theta)} \right| dr\,d\theta
$$ 
The Jacobian is the determinant of the matrix of partial derivatives:
$$ 
  \frac{\partial(x,y)}{\partial(r,\theta)} = \begin{vmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{vmatrix} = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta - (-r\sin^2\theta) = r
$$ 
So, for polar coordinates, the area element is $dA = r\,dr\,d\theta$.

This is crucial for integrating over circular or annular regions.

## Triple Integrals

The concept extends naturally to three dimensions. A **triple integral** is used to integrate a function $f(x, y, z)$ over a 3D region $E$.
$$ 
  \iiint_E f(x,y,z)\,dV
$$ 
This can be used to calculate mass (if $f$ is a density function) or hyper-volume. If $f(x,y,z)=1$, the integral simply gives the volume of the region $E$.

Triple integrals are also evaluated as iterated integrals, and changes of variables to **cylindrical** or **spherical coordinates** are common for regions with symmetry.

## Financial Application: Pricing Multi-Asset Options

Multiple integrals are the cornerstone of pricing derivatives that depend on more than one underlying asset.

Consider a **basket option**, whose payoff depends on a weighted average of two stocks, $S_1$ and $S_2$. The payoff at expiration is $f(S_1, S_2) = \max(w_1 S_1 + w_2 S_2 - K, 0)$.

The price of this option is the discounted expected payoff, which requires integrating over the joint probability distribution of the two stocks:
$$ 
  V_0 = e^{-rT} \iint_{\mathbb{R}^2} f(s_1, s_2) p(s_1, s_2) \,ds_1 ds_2 
$$ 
where $p(s_1, s_2)$ is the joint probability density function. While these integrals are rarely solved by hand, their structure is fundamental to the pricing models, and they are evaluated numerically, often using **Monte Carlo methods**.

## Practice Problems

1.  Evaluate the iterated integral $\int_0^1 \int_0^x (x+2y) \,dy\,dx$.
2.  Find the volume of the solid that lies under the plane $3x + 2y + z = 12$ and above the rectangle $R = [0, 1] \times [0, 2]$.
3.  Evaluate $\iint_D (x^2+y^2) \,dA$ where $D$ is the disk with center the origin and radius 2, by converting to polar coordinates.

*(Solutions will be provided in a separate section or at the end of the course).*

[View Solutions](/math-basic/calculus/calculus-solutions/)

Next, we will explore the final topic of our calculus series: [Vector Calculus](vector-calculus.md).
