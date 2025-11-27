---
title: "Power and Taylor Series: Approximating Functions"
permalink: /calculus/power-and-taylor-series/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

One of the most profound ideas in calculus is that we can represent complex, non-linear functions as an **infinite polynomial**, known as a **power series**. This allows us to approximate functions, which is an incredibly powerful tool in both theory and practice.

## Power Series

A **power series** is a type of infinite series of the form:
$$
\sum_{n=0}^{\infty} c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots
$$
Here, $a$ is a constant called the **center** of the series. For a given power series, there are three possibilities for convergence:
1.  The series converges only at its center, $x=a$.
2.  The series converges for all $x$.
3.  There is a positive number $R$ such that the series converges if $\|x-a\| < R$ and diverges if $\|x-a\| > R$. $R$ is called the **radius of convergence**.

## Taylor Series: The Ultimate Approximation

The key question is: if we have a function $f(x)$, can we find a power series that represents it? The answer is yes, if the function is "nice" enough (infinitely differentiable).

The **Taylor series** of a function $f(x)$ centered at $a$ is the power series:
$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots $$
where $f^{(n)}(a)$ is the $n$-th derivative of $f$ evaluated at the point $a$.

**The Idea:** The Taylor series constructs a polynomial whose derivatives at the point $a$ match the derivatives of the function $f(x)$ at that same point. The first term matches the function's value, the second term matches the slope, the third term matches the concavity, and so on.

When the center is $a=0$, the series is called a **Maclaurin series**.

### Important Maclaurin Series

Here are some of the most useful Maclaurin series to know:

| Function | Maclaurin Series | Interval of Convergence |
|----------|------------------|-------------------------|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=0}^{\infty} \frac{x^n}{n!}$ | $(-\infty, \infty)$ |
| $\sin(x)$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}$ | $(-\infty, \infty)$ |
| $\cos(x)$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}$ | $(-\infty, \infty)$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n}$ | $(-1, 1]$ |
| $(1+x)^k$ | $1 + kx + \frac{k(k-1)}{2!}x^2 + \cdots = \sum_{n=0}^{\infty} \binom{k}{n} x^n$ | $\|x\| < 1$ |

## Taylor Polynomials: The Approximation in Practice

In practice, we can't sum an infinite number of terms. Instead, we use a finite number of terms to create a **Taylor polynomial**, which serves as an approximation of the function.

The **n-th degree Taylor polynomial** of $f$ at $a$ is:
$$ T_n(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!}(x-a)^i $$

-   $T_1(x) = f(a) + f'(a)(x-a)$ is the **linear approximation** (the tangent line).
-   $T_2(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2$ is the **quadratic approximation**.

The more terms we include, the better the approximation becomes near the center point $a$.

<img src="/assets/images/calculus/taylor-approximation.png" alt="Taylor polynomial approximations of sin(x)" style="width: 600px; max-width: 100%; margin: 1rem auto; display: block;">
*(Image: Approximations of sin(x) by Taylor polynomials of degree 1, 3, 5, and 7)*

## Taylor's Theorem and the Remainder

How good is the approximation? **Taylor's Theorem** gives us control over the error, or **remainder**, $R_n(x) = f(x) - T_n(x)$.

The most common form of the remainder is:
$$ R_n(x) = \frac{f^{(n+1)}(z)}{(n+1)!}(x-a)^{n+1} $$
for some number $z$ between $x$ and $a$. This tells us that the error is related to the size of the next derivative in the series.

## Financial Application: Delta-Gamma Hedging

Taylor series are the mathematical foundation of risk approximation in finance. Consider the price of an option, $V$, as a function of the underlying stock price, $S$. The change in the option's value for a small change in the stock price, $\Delta S$, can be approximated by a Taylor expansion:

$$ \Delta V \approx \frac{\partial V}{\partial S} \Delta S + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} (\Delta S)^2 $$

In financial terms, this is:
$$ \text{Change in Option Value} \approx (\text{Delta} \times \text{Change in Stock Price}) + \frac{1}{2} (\text{Gamma} \times (\text{Change in Stock Price})^2) $$

This is the famous **Delta-Gamma approximation**. It tells a trader that their risk is not just linear (Delta), but also has a curvature component (Gamma). Hedging strategies are often designed to neutralize both of these risks.

## Practice Problems

1.  Find the first three non-zero terms of the Maclaurin series for $f(x) = e^{-x^2}$.
2.  Find the second-degree Taylor polynomial for $f(x) = \sqrt{x}$ centered at $a=4$.
3.  Use the linear approximation of $f(x) = \ln(x)$ at $a=1$ to estimate the value of $\ln(1.1)$.

*(Solutions will be provided in a separate section or at the end of the course).*

This concludes our journey through the core concepts of single-variable calculus. We are now equipped to tackle problems involving multiple variables.

Next, we will begin Part 3 of our series with [Vectors and the Geometry of Space](vectors-and-geometry-of-space.md).

---

[View Problems and Solutions for Power And Taylor Series](/math-basic/calculus/problems/power-and-taylor-series-problems/)
