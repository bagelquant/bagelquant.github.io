---
title: "The Derivative: Measuring Instantaneous Change"
permalink: /calculus/derivatives/

nav: calculus
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

Now that we have a solid understanding of limits, we can introduce the first major concept of calculus: the **derivative**. The derivative is a tool that allows us to find the **instantaneous rate of change** of a function.

## From Average Rate of Change to Instantaneous Rate of Change

Imagine a car traveling between two points. The **average speed** is easy to calculate:

$$
\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}
$$

This is the slope of the **secant line** connecting the two points on a distance-time graph.

<img src="/assets/images/calculus/secant-line.png" alt="Secant line between two points" style="width: 500px; max-width: 100%; margin: 1rem auto; display: block;">

But what about the car's speed at a single moment in time? This is the **instantaneous speed**. To find this, we need to make the interval between our two points infinitesimally small.

This is exactly what a limit does. The **derivative** of a function $f$ at a point $x=a$ is the limit of the average rate of change as the interval around $a$ shrinks to zero.

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

This gives us the slope of the **tangent line** at that single point.

<img src="/assets/images/calculus/tangent-line.png" alt="Tangent line at a single point" style="width: 500px; max-width: 100%; margin: 1rem auto; display: block;">

If this limit exists, we say that the function $f$ is **differentiable** at $a$. The process of finding the derivative is called **differentiation**.

**Example: Finding a Derivative from the Definition**

Let's find the derivative of $f(x) = x^2$ at $x=3$.

$$
\begin{aligned}
f'(3) &= \lim_{h \to 0} \frac{f(3+h) - f(3)}{h} \\
&= \lim_{h \to 0} \frac{(3+h)^2 - 3^2}{h} \\
&= \lim_{h \to 0} \frac{(9 + 6h + h^2) - 9}{h} \\
&= \lim_{h \to 0} \frac{6h + h^2}{h} \\
&= \lim_{h \to 0} (6 + h) \\
&= 6
\end{aligned}
$$

So, the slope of the tangent line to the parabola $y=x^2$ at the point $(3, 9)$ is exactly 6.

## The Derivative as a Function

We can generalize this process to find the derivative at any point $x$. The result, $f'(x)$, is a new function that gives us the slope of $f(x)$ at any given $x$.

For $f(x) = x^2$, the derivative function is $f'(x) = 2x$. (You can prove this using the limit definition). This means at $x=3$, the slope is $2(3)=6$, and at $x=-1$, the slope is $2(-1)=-2$.

## Basic Differentiation Rules

Using the limit definition for every function would be incredibly tedious. Fortunately, we have a set of rules that make finding derivatives much easier.

Let $u(x)$ and $v(x)$ be differentiable functions and $c$ be a constant.

1.  **Constant Rule:** If $f(x) = c$, then $f'(x) = 0$. (The slope of a horizontal line is zero).
2.  **Power Rule:** If $f(x) = x^n$, then $f'(x) = n x^{n-1}$.
    *   *Example:* $\frac{d}{dx} x^5 = 5x^4$
3.  **Constant Multiple Rule:** $(c \cdot u)' = c \cdot u'$.
    *   *Example:* $\frac{d}{dx} (4x^5) = 4 \cdot (5x^4) = 20x^4$
4.  **Sum/Difference Rule:** $(u \pm v)' = u' \pm v'$.
    *   *Example:* For $f(x) = x^3 + 2x^2 - 5x + 4$, $f'(x) = 3x^2 + 4x - 5$.
5.  **Product Rule:** $(uv)' = u'v + uv'$.
    *   *Example:* For $f(x) = x^2 \sin(x)$, $f'(x) = (2x)\sin(x) + x^2\cos(x)$.
6.  **Quotient Rule:** $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$.
    *   *Example:* For $f(x) = \frac{x^2}{x+1}$, $f'(x) = \frac{2x(x+1) - x^2(1)}{(x+1)^2} = \frac{x^2+2x}{(x+1)^2}$.
7.  **Chain Rule:** If $y=f(g(x))$, then $\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$. This is for differentiating composite functions (a function inside another function).
    *   *Example:* For $f(x) = (x^2+1)^3$, let $u = x^2+1$. Then $f(u) = u^3$. $f'(x) = (3u^2) \cdot (2x) = 3(x^2+1)^2(2x) = 6x(x^2+1)^2$.

## Derivatives of Common Functions

| Function $f(x)$ | Derivative $f'(x)$ |
|-----------------|--------------------|
| $e^x$           | $e^x$              |
| $\ln(x)$        | $1/x$              |
| $\sin(x)$       | $\cos(x)$          |
| $\cos(x)$       | $-\sin(x)$         |
| $\tan(x)$       | $\sec^2(x)$        |

## Higher-Order Derivatives

The **second derivative**, denoted $f''(x)$, is the derivative of the first derivative. It measures the rate of change of the slope, also known as **concavity**.

-   If $f''(x) > 0$, the function is **convex** (concave up, like a cup). The slope is increasing.
-   If $f''(x) < 0$, the function is **concave** (concave down, like a frown). The slope is decreasing.

**Financial Application:** The second derivative of an option's price with respect to the underlying stock price is called **Gamma**. A positive gamma means the option's delta (its directional exposure) increases as the stock price rises, a key feature of long option positions.

## Practice Problems

1.  Find the derivative of $f(x) = 5x^4 - \frac{1}{x^2} + \sqrt{x}$.
2.  Using the product rule, differentiate $g(x) = x^3 e^x$.
3.  Using the quotient rule, differentiate $h(x) = \frac{\ln(x)}{x}$.
4.  Using the chain rule, differentiate $k(x) = \sin(x^2 + 3x)$.
5.  Find the second derivative of $f(x) = x \ln(x)$. Is the function concave or convex at $x=1$?

*(Solutions will be provided in a separate section or at the end of the course).*

[View Solutions](/math-basic/calculus/calculus-solutions/)

With these rules, we can differentiate a wide variety of functions. This ability to precisely measure rates of change is the first major step in applying calculus to real-world problems.

Next, we will explore the applications of differentiation, including how to find the maximum or minimum values of a function.

[Next: Applications of Derivatives](applications-of-differentiation.md)
