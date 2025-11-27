---
title: "The Integral: Accumulating Change"
permalink: /calculus/integrals/
nav: "calculus"
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
---

Welcome to the second major pillar of calculus: **integration**. If differentiation is about finding instantaneous rates of change, integration is about the opposite: **accumulating quantities** and finding the total.

## The Problem of Area

Imagine you want to find the area of a shape with curved sides. Simple geometric formulas for rectangles and triangles won't work. This is the classic problem that leads to the concept of the **definite integral**.

The strategy is to approximate the area by slicing it into a large number of thin vertical rectangles, each with a width of $\Delta x$.

<img src="/assets/images/calculus/riemann-sum.png" alt="Approximating area with Riemann Sums" style="width: 600px; max-width: 100%; margin: 1rem auto; display: block;">

The area of each rectangle is its height, $f(x_i^*)$, times its width, $\Delta x$. By summing the areas of all these rectangles, we get an approximation of the total area:

$$ 
\text{Area} \approx \sum_{i=1}^n f(x_i^*) \Delta x 
$$ 

This is called a **Riemann Sum**.

To get the *exact* area, we take the limit as the number of rectangles goes to infinity, and the width of each rectangle shrinks to zero. This limit is the **definite integral**.

$$ 
\int_a^b f(x)\,dx = 
\lim_{n \to \infty}\sum_{i=1}^{n} f(x_i^*) \,\Delta x 
$$ 

## The Fundamental Theorem of Calculus

Calculating integrals from the limit definition is even more difficult than for derivatives. Fortunately, the **Fundamental Theorem of Calculus (FTC)** provides a miraculous shortcut.

The FTC comes in two parts and connects differentiation and integration as inverse processes.

### Part 1: The Derivative of an Integral

If we define a function $g(x)$ as the accumulated area under the curve of $f$ from a constant $a$ to a variable $x$:
$$ g(x) = \int_a^x f(t)\,dt 
$$ 
Then the rate at which this area-so-far function changes is simply the original function:
$$ g'(x) = f(x) 
$$ 

### Part 2: Evaluating a Definite Integral

This is the part of the theorem that we use most often for calculations. It states that if $F$ is any **antiderivative** of $f$ (meaning $F'(x) = f(x)$), then:

$$ 
\int_a^b f(x)\,dx = F(b) - F(a) 
$$ 

This is a phenomenal result. It means that to find the exact area under a curve, we just need to find its antiderivative and plug in the endpoints.

## The Indefinite Integral

An **antiderivative** is the function whose derivative is our original function. For example, an antiderivative of $f(x) = 2x$ is $F(x) = x^2$, because the derivative of $x^2$ is $2x$.

However, $x^2 + 5$ and $x^2 - 100$ are also antiderivatives of $2x$. Since the derivative of a constant is zero, any function of the form $x^2 + C$ (where $C$ is any constant) is an antiderivative.

The family of all antiderivatives of a function $f$ is called the **indefinite integral** and is denoted by:

$$ 
\int f(x)\,dx = F(x) + C 
$$ 

## Basic Integration Rules

Integration rules are essentially the reverse of differentiation rules.

1.  **Power Rule:** $\int x^n \,dx = \frac{x^{n+1}}{n+1} + C$ (for $n \neq -1$)
    *   *Example:* $\int x^3 \,dx = \frac{x^4}{4} + C$
2.  **Special Case, n=-1:** $\int \frac{1}{x} \,dx = \ln\|x\| + C$
3.  **Exponential Rule:** $\int e^x \,dx = e^x + C$
4.  **Constant Multiple Rule:** $\int c \cdot f(x) \,dx = c \cdot \int f(x) \,dx$
5.  **Sum/Difference Rule:** $\int [f(x) \pm g(x)] \,dx = \int f(x) \,dx \pm \int g(x) \,dx$

**Example: Evaluating a Definite Integral**
Calculate the area under the curve of $f(x) = 3x^2 + 4$ from $x=0$ to $x=2$.

$$ 
\begin{aligned}
\int_0^2 (3x^2 + 4)\,dx &= \left[ 3 \cdot \frac{x^3}{3} + 4x \right]_0^2 \\
&= [x^3 + 4x]_0^2 \\
&= (2^3 + 4(2)) - (0^3 + 4(0)) \\
&= (8 + 8) - 0 = 16
\end{aligned}
$$ 

## Financial Application: Total Return from Instantaneous Returns

If you have a model for the instantaneous rate of return, $r(t)$, of an asset, the total log-return from time $t=0$ to $t=T$ is the integral of this rate:

$$ 
\text{Total Log-Return} = \ln\left(\frac{P_T}{P_0}\right) = \int_0^T r(t)\,dt 
$$ 

Integration allows us to move from an instantaneous rate to a total accumulated change over a period.

## Practice Problems

1.  Find the indefinite integral of $f(x) = 6x^2 - 2x + 5$.
2.  Find the indefinite integral of $g(x) = e^x + \sin(x)$.
3.  Evaluate the definite integral $\int_1^e \frac{1}{x} \,dx$.
4.  Find the area under the curve of $y = \sqrt{x}$ from $x=0$ to $x=4$.

*(Solutions will be provided in a separate section or at the end of the course).*

[View Solutions](/math-basic/calculus/calculus-solutions/)

While these basic rules are powerful, many functions are not so simple to integrate.

Next, we will explore more advanced [Techniques of Integration](techniques-of-integration.md).
