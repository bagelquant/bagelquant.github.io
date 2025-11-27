---
title: "Techniques of Integration"
permalink: /calculus/techniques-of-integration/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

While the basic integration rules cover many functions, a large number of integrals require more advanced techniques. This section introduces the most important methods for finding antiderivatives.

## The Substitution Rule

The substitution rule is the reverse of the chain rule for differentiation. It's used when an integral contains a function and its derivative.

**The Rule:** If $u = g(x)$ is a differentiable function, then:
$$
\int f(g(x))g'(x)\,dx = \int f(u)\,du
$$

**Strategy:**
1.  Look for a composite function $f(g(x))$ and the derivative of the "inner" function, $g'(x)$.
2.  Let $u = g(x)$.
3.  Find $du = g'(x)dx$.
4.  Substitute $u$ and $du$ into the integral, which should produce a simpler integral in terms of $u$.
5.  Integrate with respect to $u$.
6.  Substitute back $u = g(x)$ to get the final answer in terms of $x$.

**Example:**
Find $\int 2x \cos(x^2) \,dx$.

1.  Let $u = x^2$.
2.  Then $du = 2x \,dx$.
3.  The integral becomes $\int \cos(u) \,du$.
4.  Integrate: $\sin(u) + C$.
5.  Substitute back: $\sin(x^2) + C$.

## Integration by Parts

Integration by parts is the reverse of the product rule. It's useful for integrating products of functions.

**The Formula:**
$$
\int u \,dv = uv - \int v \,du
$$

**Strategy:**
1.  Identify two parts of the integrand, $u$ and $dv$.
2.  A good choice for $u$ is a function that becomes simpler when you differentiate it (e.g., polynomials, $\ln(x)$).
3.  A good choice for $dv$ is the part of the integrand that you can easily integrate.
4.  Find $du$ (by differentiating $u$) and $v$ (by integrating $dv$).
5.  Apply the formula.

**Mnemonic:** A helpful way to choose $u$ is to follow the **LIATE** priority list:
-   **L**ogarithmic Functions ($\ln x$)
-   **I**nverse Trigonometric Functions ($\arctan x$)
-   **A**lgebraic Functions ($x^2, x^3$)
-   **T**rigonometric Functions ($\sin x, \cos x$)
-   **E**xponential Functions ($e^x$)

**Example:**
Find $\int x \ln(x) \,dx$.

1.  Using LIATE, we choose $u = \ln(x)$ and $dv = x \,dx$.
2.  Then $du = \frac{1}{x} dx$ and $v = \frac{x^2}{2}$.
3.  Apply the formula:
    $$
    \begin{aligned}
    \int x \ln(x) \,dx &= \ln(x) \cdot \frac{x^2}{2} - \int \frac{x^2}{2} \cdot \frac{1}{x} \,dx \\
    &= \frac{x^2 \ln(x)}{2} - \frac{1}{2} \int x \,dx \\
    &= \frac{x^2 \ln(x)}{2} - \frac{1}{2} \cdot \frac{x^2}{2} + C \\
    &= \frac{x^2 \ln(x)}{2} - \frac{x^4}{4} + C
    \end{aligned}
    $$

## Trigonometric Integrals

This involves integrals of powers of sine, cosine, tangent, and secant. The strategy depends on whether the powers are odd or even.

-   **If $\cos(x)$ has an odd power:** Save one $\cos(x)$ factor and use the identity $\cos^2(x) = 1 - \sin^2(x)$. Then use the substitution $u = \sin(x)$.
-   **If $\sin(x)$ has an odd power:** Save one $\sin(x)$ factor and use the identity $\sin^2(x) = 1 - \cos^2(x)$. Then use the substitution $u = \cos(x)$.
-   **If both powers are even:** Use the half-angle identities:
    $$
    \sin^2(x) = \frac{1 - \cos(2x)}{2}, \quad \cos^2(x) = \frac{1 + \cos(2x)}{2}
    $$

## Trigonometric Substitution

This technique is used to evaluate integrals containing expressions like $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$. We substitute $x$ with a trigonometric function to simplify the expression.

| Expression          | Substitution        | Identity Used               |
|---------------------|---------------------|-----------------------------|
| $\sqrt{a^2 - x^2}$  | $x = a \sin(\theta)$ | $1 - \sin^2(\theta) = \cos^2(\theta)$ |
| $\sqrt{a^2 + x^2}$  | $x = a \tan(\theta)$ | $1 + \tan^2(\theta) = \sec^2(\theta)$ |
| $\sqrt{x^2 - a^2}$  | $x = a \sec(\theta)$ | $\sec^2(\theta) - 1 = \tan^2(\theta)$ |

After integrating, you use a right triangle to convert the result back from $\theta$ to $x$.

## Integration by Partial Fractions

This method is for integrating **rational functions** (a ratio of two polynomials), $\frac{P(x)}{Q(x)}$.

**Strategy:**
1.  If the degree of $P(x)$ is greater than or equal to the degree of $Q(x)$, use polynomial long division first.
2.  Factor the denominator $Q(x)$ completely.
3.  Decompose the rational function into a sum of simpler "partial" fractions. The form of the decomposition depends on the factors of the denominator (linear factors, repeated linear factors, irreducible quadratic factors).
4.  Integrate each of the simpler fractions.

**Example:**
Find $\int \frac{x+5}{x^2 + x - 2} \,dx$.

1.  Factor the denominator: $x^2 + x - 2 = (x+2)(x-1)$.
2.  Decompose: $\frac{x+5}{(x+2)(x-1)} = \frac{A}{x+2} + \frac{B}{x-1}$.
3.  Solving for $A$ and $B$ gives $A = -1$ and $B = 2$.
4.  Integrate:
    $$
    \int \left( \frac{-1}{x+2} + \frac{2}{x-1} \right) dx = -\ln|x+2| + 2\ln|x-1| + C
    $$

## Practice Problems

1.  Evaluate $\int x^2 \sqrt{x^3 + 1} \,dx$ using substitution.
2.  Evaluate $\int x \cos(x) \,dx$ using integration by parts.
3.  Evaluate $\int \sin^3(x) \cos^2(x) \,dx$.
4.  Evaluate $\int \frac{1}{x^2 - 4} \,dx$ using partial fractions.

*(Solutions will be provided in a separate section or at the end of the course).*

[View Solutions](/math-basic/calculus/calculus-solutions/)

Mastering these techniques is essential for solving a wide variety of problems in calculus and its applications.

Next, we will explore some of the [Applications of Integration](applications-of-integration.md).
