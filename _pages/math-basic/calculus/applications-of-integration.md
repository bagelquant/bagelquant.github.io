---
title: "Applications of Integration"
permalink: /calculus/applications-of-integration/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

The definite integral was born from the problem of finding the area under a curve. This concept of summing up infinitesimal pieces can be extended to solve a wide variety of geometric and real-world problems.

## Area Between Two Curves

The area of the region bounded by the curves $y = f(x)$ and $y = g(x)$ and the lines $x=a$ and $x=b$, where $f(x) \geq g(x)$ for all $x$ in $[a, b]$, is:

$$ A = \int_a^b [f(x) - g(x)] \,dx $$

**Strategy:**
1.  Sketch the curves to determine which function is on top ($f(x)$) and which is on the bottom ($g(x)$).
2.  Find the points of intersection of the curves to determine the limits of integration ($a$ and $b$), if they are not given.
3.  Set up and evaluate the integral of (top function - bottom function).

**Example:**
Find the area of the region enclosed by the parabolas $y = x^2$ and $y = 2x - x^2$.

1.  The line $y = 2x - x^2$ is the "top" function.
2.  Find intersection points: $x^2 = 2x - x^2 \implies 2x^2 - 2x = 0 \implies 2x(x-1) = 0$. They intersect at $x=0$ and $x=1$.
3.  Set up the integral:
    $$ A = \int_0^1 [(2x - x^2) - x^2] \,dx = \int_0^1 (2x - 2x^2) \,dx = \left[x^2 - \frac{2}{3}x^3\right]_0^1 = 1 - \frac{2}{3} = \frac{1}{3} $$

## Volumes of Solids of Revolution

A solid of revolution is a 3D shape obtained by rotating a 2D region around an axis. We can find its volume by integrating the area of its cross-sections.

### The Disk Method

If we revolve a region under a curve $y = f(x)$ from $x=a$ to $x=b$ around the x-axis, the cross-sections are disks (circles) with radius $R = f(x)$. The area of each disk is $A(x) = \pi [f(x)]^2$.

The volume is the integral of these disk areas:

$$ V = \int_a^b \pi [f(x)]^2 \,dx $$

<img src="/assets/images/calculus/disk-method.png" alt="Disk Method for Volume" style="width: 500px; max-width: 100%; margin: 1rem auto; display: block;">

### The Washer Method

If we revolve the region between two curves, $y=f(x)$ and $y=g(x)$, the cross-sections are washers (rings). The area of each washer is the area of the outer disk minus the area of the inner disk: $A(x) = \pi (\text{Outer Radius})^2 - \pi (\text{Inner Radius})^2$.

$$ V = \int_a^b \pi \left( [f(x)]^2 - [g(x)]^2 \right) \,dx $$

## Arc Length

To find the length of a curve $y=f(x)$ from $x=a$ to $x=b$, we can use an integral. We approximate the curve with a series of small line segments, each of length $ds$. Using the Pythagorean theorem, we find that an infinitesimal segment of arc length is:

$$ ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \,dx $$

Integrating this from $a$ to $b$ gives the total arc length:

$$ L = \int_a^b \sqrt{1 + [f'(x)]^2} \,dx $$

## Probability and Expected Value

In probability, integration is essential for working with **continuous random variables**. If a variable $X$ has a **probability density function (PDF)** $p(x)$, then:

-   The probability that $X$ falls between $a$ and $b$ is the area under the PDF curve:
    $$ P(a \le X \le b) = \int_a^b p(x) \,dx $$
-   The **expected value** (or mean) of the variable is:
    $$ E[X] = \int_{-\infty}^{\infty} x \cdot p(x) \,dx $$
    This is a weighted average of all possible values, where the weighting is the probability density.

**Financial Application:**
In risk-neutral pricing, the price of a derivative is the discounted expected value of its future payoff. For a European call option with payoff $f(S_T) = \max(S_T - K, 0)$, the price is:

$$ V_0 = e^{-rT} E[f(S_T)] = e^{-rT} \int_0^\infty \max(S_T - K, 0) \cdot p(S_T) \,dS_T $$

where $p(S_T)$ is the risk-neutral probability density of the final stock price.

## Practice Problems

1.  Find the area of the region bounded by $y = x$ and $y = x^2$.
2.  The region under the curve $y = \sqrt{x}$ from $x=0$ to $x=4$ is revolved around the x-axis. Find the volume of the resulting solid.
3.  Set up, but do not evaluate, the integral for the arc length of the curve $y = x^2$ from $x=0$ to $x=1$.

*(Solutions will be provided in a separate section or at the end of the course).*

[View Solutions](calculus-solutions.md)

This is just a sample of the many applications of integration. It is a versatile tool for summing up continuous quantities in geometry, physics, probability, and finance.

Next, we will move on to the study of [Sequences and Series](sequences-and-series.md).
