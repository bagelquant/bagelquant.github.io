---
title: "Limits and Continuity: The Foundation of Calculus"
permalink: /calculus/limits-and-continuity/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

The concept of a **limit** is the fundamental building block of calculus. Without it, we cannot define derivatives or integrals. A limit allows us to talk about what happens to a function's output as its input gets *arbitrarily close* to a certain value.

## Intuitive Definition of a Limit

Imagine you are walking along the graph of a function, say, $f(x) = x^2$. As you get closer and closer to the point where $x=2$, what value does $f(x)$ approach?

- If you approach from the left (e.g., $x = 1.9, 1.99, 1.999, \ldots$), $f(x)$ gets closer to 4.
- If you approach from the right (e.g., $x = 2.1, 2.01, 2.001, \ldots$), $f(x)$ also gets closer to 4.

Since the function approaches the same value from both sides, we say that the **limit of $f(x)$ as $x$ approaches 2 is 4**. We write this as:

$$
\lim_{x \to 2} x^2 = 4
$$

**Crucially, the limit does not care about the value of the function *at* the point.** It only cares about what happens in the immediate neighborhood around it.

## The Formal (Epsilon-Delta) Definition

The intuitive idea is made precise with the epsilon-delta ($\epsilon$-$\delta$) definition.

We say that $\lim_{x \to a} f(x) = L$ if for every number $\epsilon > 0$, there exists a corresponding number $\delta > 0$ such that:

$$ 
\text{if } 0 < |x - a| < \delta \text{, then } |f(x) - L| < \epsilon 
$$ 

Let's break this down:
-   **For every $\epsilon > 0$**: No matter how small a vertical "tolerance window" ($\pm\epsilon$) you set around the limit $L$...
-   **there exists a $\delta > 0$**: ...we can always find a horizontal "tolerance window" ($\pm\delta$) around $a$...
-   **such that...**: ...if our input $x$ is inside the $\delta$-window (but not exactly at $a$), then the output $f(x)$ is guaranteed to be inside the $\epsilon$-window.

<img src="/assets/images/calculus/epsilon-delta.png" alt="Epsilon-Delta Definition of a Limit" style="width: 600px; max-width: 100%; margin: 1rem auto; display: block;">

This definition is the rigorous bedrock that allows us to prove all the important theorems of calculus.

## When Do Limits Not Exist?

A limit fails to exist at a point if:
1.  **The function approaches different values from the left and right.** (A "jump discontinuity").
2.  **The function increases or decreases without bound.** (A "vertical asymptote").
3.  **The function oscillates infinitely.** (e.g., $\lim_{x \to 0} \sin(1/x)$).

## Limit Laws

Calculating limits from the $\epsilon$-$\delta$ definition is tedious. Thankfully, we can use a set of laws to simplify the process. Suppose that $c$ is a constant and the limits $\lim_{x \to a} f(x)$ and $\lim_{x \to a} g(x)$ exist. Then:

1.  **Sum/Difference Rule:** $\lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)$
2.  **Constant Multiple Rule:** $\lim_{x \to a} [c \cdot f(x)] = c \cdot \lim_{x \to a} f(x)$
3.  **Product Rule:** $\lim_{x \to a} [f(x)g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$
4.  **Quotient Rule:** $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$ (if $\lim_{x \to a} g(x) \neq 0$)
5.  **Power Rule:** $\lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n$

## Continuity

Now we can give a precise definition of continuity. A function $f$ is **continuous** at a number $a$ if:

$$ 
\lim_{x \to a} f(x) = f(a) 
$$ 

This simple equation implies three things:
1.  $f(a)$ must be defined (you can't have a hole at $a$).
2.  $\lim_{x \to a} f(x)$ must exist (it can't be a jump or asymptote).
3.  The limit value must be the same as the function's value at that point.

Visually, a continuous function is one whose graph can be drawn without lifting your pen from the paper. Polynomials, exponentials, and trigonometric functions are continuous on their domains.

### The Intermediate Value Theorem (IVT)

One of the most important consequences of continuity is the IVT. It states:

> Suppose that $f$ is continuous on the closed interval $[a, b]$. Let $N$ be any number between $f(a)$ and $f(b)$. Then there exists a number $c$ in $(a, b)$ such that $f(c) = N$.

In simple terms, a continuous function must take on every value between any two of its points. This theorem is crucial for proving the existence of roots of equations.

**Financial Application:** If a continuous pricing model tells you an option is worth $1 today and $3 tomorrow, the IVT guarantees that at some point in between, it must have been worth $2.

With the concepts of limits and continuity firmly established, we are now ready to tackle the first major pillar of calculus.

Next, we will explore the [Derivative](derivatives.md).

---

[View Problems and Solutions for Limits And Continuity](/math-basic/calculus/problems/limits-and-continuity-problems/)
