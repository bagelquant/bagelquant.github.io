---
title: "Calculus Practice Problems: Solutions"
layout: page
---

Here you'll find the solutions to the practice problems from the main calculus articles.

### Solutions for "The Derivative"

**1. Find the derivative of $f(x) = 5x^4 - \frac{1}{x^2} + \sqrt{x}$.**

First, rewrite the function with power notation:
$f(x) = 5x^4 - x^{-2} + x^{1/2}$

Now, apply the power rule for differentiation, $(x^n)' = nx^{n-1}$:
$f'(x) = 5(4x^3) - (-2x^{-3}) + \frac{1}{2}x^{-1/2}$
$f'(x) = 20x^3 + 2x^{-3} + \frac{1}{2}x^{-1/2}$
$f'(x) = 20x^3 + \frac{2}{x^3} + \frac{1}{2\sqrt{x}}$

**2. Differentiate $g(x) = x^3 e^x$ using the product rule.**

The product rule is $(uv)' = u'v + uv'$.
Let $u = x^3$ and $v = e^x$.
Then $u' = 3x^2$ and $v' = e^x$.

$g'(x) = (3x^2)(e^x) + (x^3)(e^x) = e^x(3x^2 + x^3)$

**3. Differentiate $h(x) = \frac{\ln(x)}{x}$ using the quotient rule.**

The quotient rule is $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$.
Let $u = \ln(x)$ and $v = x$.
Then $u' = \frac{1}{x}$ and $v' = 1$.

$h'(x) = \frac{(\frac{1}{x})(x) - (\ln(x))(1)}{x^2} = \frac{1 - \ln(x)}{x^2}$

**4. Differentiate $k(x) = \sin(x^2 + 3x)$ using the chain rule.**

The chain rule is $(f(g(x)))' = f'(g(x))g'(x)$.
Let $f(u) = \sin(u)$ and $g(x) = x^2 + 3x$.
Then $f'(u) = \cos(u)$ and $g'(x) = 2x + 3$.

$k'(x) = \cos(x^2 + 3x) \cdot (2x + 3) = (2x+3)\cos(x^2 + 3x)$

**5. Find the second derivative of $f(x) = x \ln(x)$. Is it concave or convex at $x=1$?**

First derivative (using product rule):
$f'(x) = (1)(\ln(x)) + (x)(\frac{1}{x}) = \ln(x) + 1$

Second derivative:
$f''(x) = \frac{1}{x}$

At $x=1$, $f''(1) = \frac{1}{1} = 1$.
Since $f''(1) > 0$, the function is **convex** at $x=1$.

---
### Solutions for "The Integral"

**1. Find the indefinite integral of $f(x) = 6x^2 - 2x + 5$.**

Using the power rule for integration, $\int x^n dx = \frac{x^{n+1}}{n+1}$:
$\int (6x^2 - 2x + 5) dx = 6\frac{x^3}{3} - 2\frac{x^2}{2} + 5x + C$
$= 2x^3 - x^2 + 5x + C$

**2. Find the indefinite integral of $g(x) = e^x + \sin(x)$.**

$\int (e^x + \sin(x)) dx = e^x - \cos(x) + C$

**3. Evaluate the definite integral $\int_1^e \frac{1}{x} \,dx$.**

$\int_1^e \frac{1}{x} dx = [\ln|x|]_1^e = \ln(e) - \ln(1) = 1 - 0 = 1$

**4. Find the area under the curve of $y = \sqrt{x}$ from $x=0$ to $x=4$.**

Area $= \int_0^4 \sqrt{x} dx = \int_0^4 x^{1/2} dx$
$= [\frac{x^{3/2}}{3/2}]_0^4 = [\frac{2}{3}x^{3/2}]_0^4$
$= \frac{2}{3}(4^{3/2}) - \frac{2}{3}(0^{3/2}) = \frac{2}{3}(8) - 0 = \frac{16}{3}$

---
### Solutions for "Applications of Integration"

**1. Find the area of the region bounded by $y = x$ and $y = x^2$.**

Intersection points: $x = x^2 \implies x^2 - x = 0 \implies x(x-1) = 0$. So, $x=0$ and $x=1$.
In $[0, 1]$, $y=x$ is the top function.
Area $= \int_0^1 (x - x^2) dx = [\frac{x^2}{2} - \frac{x^3}{3}]_0^1$
$= (\frac{1}{2} - \frac{1}{3}) - (0) = \frac{1}{6}$

**2. The region under $y = \sqrt{x}$ from $x=0$ to $x=4$ is revolved around the x-axis. Find the volume.**

Using the disk method, $V = \int_a^b \pi [f(x)]^2 dx$.
$V = \int_0^4 \pi (\sqrt{x})^2 dx = \int_0^4 \pi x dx$
$= \pi [\frac{x^2}{2}]_0^4 = \pi (\frac{16}{2} - 0) = 8\pi$

**3. Set up the integral for the arc length of $y = x^2$ from $x=0$ to $x=1$.**

Arc length $L = \int_a^b \sqrt{1 + [f'(x)]^2} dx$.
$f(x) = x^2 \implies f'(x) = 2x$.
$L = \int_0^1 \sqrt{1 + (2x)^2} dx = \int_0^1 \sqrt{1 + 4x^2} dx$

---
### Solutions for "Techniques of Integration"

**1. Evaluate $\int x^2 \sqrt{x^3 + 1} \,dx$ using substitution.**

Let $u = x^3 + 1$, so $du = 3x^2 dx \implies x^2 dx = \frac{1}{3}du$.
$\int \sqrt{u} \frac{1}{3}du = \frac{1}{3} \int u^{1/2} du$
$= \frac{1}{3} \frac{u^{3/2}}{3/2} + C = \frac{2}{9}(x^3 + 1)^{3/2} + C$

**2. Evaluate $\int x \cos(x) \,dx$ using integration by parts.**

Let $u = x$ and $dv = \cos(x) dx$.
Then $du = dx$ and $v = \sin(x)$.
$\int u dv = uv - \int v du$
$\int x \cos(x) dx = x \sin(x) - \int \sin(x) dx$
$= x \sin(x) - (-\cos(x)) + C = x \sin(x) + \cos(x) + C$

**3. Evaluate $\int \sin^3(x) \cos^2(x) \,dx$.**

Rewrite as $\int \sin(x) \sin^2(x) \cos^2(x) dx = \int \sin(x) (1-\cos^2(x)) \cos^2(x) dx$.
Let $u = \cos(x)$, so $du = -\sin(x) dx$.
$-\int (1-u^2)u^2 du = -\int (u^2 - u^4) du$
$= -(\frac{u^3}{3} - \frac{u^5}{5}) + C = \frac{\cos^5(x)}{5} - \frac{\cos^3(x)}{3} + C$

**4. Evaluate $\int \frac{1}{x^2 - 4} \,dx$ using partial fractions.**

$\frac{1}{(x-2)(x+2)} = \frac{A}{x-2} + \frac{B}{x+2}$.
$1 = A(x+2) + B(x-2)$.
If $x=2$, $1 = 4A \implies A = 1/4$.
If $x=-2$, $1 = -4B \implies B = -1/4$.
$\int (\frac{1/4}{x-2} - \frac{1/4}{x+2}) dx = \frac{1}{4}(\ln|x-2| - \ln|x+2|) + C = \frac{1}{4}\ln|\frac{x-2}{x+2}| + C$

---
### Solutions for "Partial Derivatives"

Let $f(x, y) = x e^{xy}$.

**1. Find $f_x$ and $f_y$.**

$f_x = 1 \cdot e^{xy} + x \cdot (y e^{xy}) = e^{xy}(1 + xy)$
$f_y = x \cdot (x e^{xy}) = x^2 e^{xy}$

**2. Find $\nabla f$ at $(1, 0)$.**

$\nabla f(1, 0) = \langle e^{0}(1+0), 1^2 e^{0} \rangle = \langle 1, 1 \rangle$

**3. Find the directional derivative of $f$ at $(1, 0)$ in the direction of $\mathbf{v} = \langle 3, 4 \rangle$.**

Unit vector $\mathbf{u} = \frac{\mathbf{v}}{|\mathbf{v}|} = \frac{\langle 3, 4 \rangle}{\sqrt{9+16}} = \langle \frac{3}{5}, \frac{4}{5} \rangle$.
$D_{\mathbf{u}}f(1, 0) = \nabla f(1, 0) \cdot \mathbf{u} = \langle 1, 1 \rangle \cdot \langle \frac{3}{5}, \frac{4}{5} \rangle = \frac{3}{5} + \frac{4}{5} = \frac{7}{5}$

**4. Find all second-order partial derivatives and verify $f_{xy} = f_{yx}$.**

$f_{xx} = y e^{xy}(1+xy) + e^{xy}(y) = ye^{xy}(2+xy)$
$f_{yy} = x^2 (x e^{xy}) = x^3 e^{xy}$
$f_{xy} = \frac{\partial}{\partial y}(e^{xy}(1+xy)) = x e^{xy}(1+xy) + e^{xy}(x) = xe^{xy}(2+xy)$
$f_{yx} = \frac{\partial}{\partial x}(x^2 e^{xy}) = 2x e^{xy} + x^2 (y e^{xy}) = xe^{xy}(2+xy)$
They are equal.

---
### Solutions for "Power and Taylor Series"

**1. Find the first three non-zero terms of the Maclaurin series for $f(x) = e^{-x^2}$.**

Start with $e^u = 1 + u + \frac{u^2}{2!} + \dots$
Let $u = -x^2$.
$e^{-x^2} = 1 + (-x^2) + \frac{(-x^2)^2}{2!} + \dots = 1 - x^2 + \frac{x^4}{2}$

**2. Find the second-degree Taylor polynomial for $f(x) = \sqrt{x}$ at $a=4$.**

$f(x) = x^{1/2} \implies f(4) = 2$
$f'(x) = \frac{1}{2}x^{-1/2} \implies f'(4) = \frac{1}{4}$
$f''(x) = -\frac{1}{4}x^{-3/2} \implies f''(4) = -\frac{1}{32}$
$T_2(x) = f(4) + f'(4)(x-4) + \frac{f''(4)}{2!}(x-4)^2$
$T_2(x) = 2 + \frac{1}{4}(x-4) - \frac{1}{64}(x-4)^2$

**3. Use the linear approximation of $f(x) = \ln(x)$ at $a=1$ to estimate $\ln(1.1)$.**

$f(x) = \ln(x) \implies f(1) = 0$
$f'(x) = \frac{1}{x} \implies f'(1) = 1$
$L(x) = f(1) + f'(1)(x-1) = 0 + 1(x-1) = x-1$.
$\ln(1.1) \approx L(1.1) = 1.1 - 1 = 0.1$

---
### Solutions for "Multiple Integrals"

**1. Evaluate $\int_0^1 \int_0^x (x+2y) \,dy\,dx$.**

Inner integral: $\int_0^x (x+2y) dy = [xy + y^2]_0^x = x^2 + x^2 = 2x^2$.
Outer integral: $\int_0^1 2x^2 dx = [\frac{2x^3}{3}]_0^1 = \frac{2}{3}$

**2. Find the volume under the plane $3x + 2y + z = 12$ and above the rectangle $R = [0, 1] \times [0, 2]$.**

Volume $= \int_0^1 \int_0^2 (12 - 3x - 2y) dy dx$.
Inner: $[12y - 3xy - y^2]_0^2 = 24 - 6x - 4 = 20 - 6x$.
Outer: $\int_0^1 (20 - 6x) dx = [20x - 3x^2]_0^1 = 20 - 3 = 17$.

**3. Evaluate $\iint_D (x^2+y^2) \,dA$ where $D$ is the disk with center the origin and radius 2, using polar coordinates.**

$x^2+y^2=r^2$, $dA=rdrd\theta$.
Region D: $0 \le r \le 2$, $0 \le \theta \le 2\pi$.
$\int_0^{2\pi} \int_0^2 (r^2) r dr d\theta = \int_0^{2\pi} [\frac{r^4}{4}]_0^2 d\theta$
$= \int_0^{2\pi} 4 d\theta = [4\theta]_0^{2\pi} = 8\pi$
