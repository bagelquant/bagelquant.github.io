---
title: "Sequences and Series: The Path to Infinity"
permalink: /calculus/sequences-and-series/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

So far, we have dealt with functions on continuous intervals. Now, we shift our focus to an ordered list of numbers, called a **sequence**, and the process of summing them up, which leads to a **series**. Understanding how to handle these infinite sums is crucial for the powerful approximation techniques we'll see in the next section.

## Sequences

A **sequence** is simply an ordered list of numbers:
$$ a_1, a_2, a_3, \ldots, a_n, \ldots $$
We can also think of a sequence as a function whose domain is the set of positive integers. We often write it as ${a_n}_{n=1}^{\infty}$.

**Example:** The sequence ${ \frac{n}{n+1} }_{n=1}^{\infty}$ starts with the terms:
$$ \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \ldots $$

### Limit of a Sequence

We are often interested in the long-term behavior of a sequence. The **limit** of a sequence is the value that its terms approach as $n$ becomes very large.

We say that $\lim_{n \to \infty} a_n = L$ if the terms $a_n$ can be made arbitrarily close to $L$ by taking $n$ sufficiently large.

-   If the limit $L$ exists and is a finite number, the sequence **converges**.
-   Otherwise, the sequence **diverges**.

**Example:** For the sequence { \frac{n}{n+1} }, as $n$ gets very large, the terms get closer and closer to 1. So, $\lim_{n \to \infty} \frac{n}{n+1} = 1$. This sequence converges.

## Series

A **series** is the sum of the terms of a sequence. An **infinite series** is what we get when we try to add up an infinite number of terms:
$$ \sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots $$

But how can we add up infinitely many numbers? We do it by looking at the sequence of **partial sums**.

The $n$-th partial sum, $s_n$, is the sum of the first $n$ terms:
$$ s_n = \sum_{i=1}^n a_i = a_1 + a_2 + \cdots + a_n $$
This creates a new sequence of partial sums: {s_n}_{n=1}^{\infty}.

If this sequence of partial sums converges to a finite limit $S$, then we say that the series **converges**, and its sum is $S$.
$$ \sum_{n=1}^{\infty} a_n = \lim_{n \to \infty} s_n = S $$
If the sequence of partial sums diverges, then the series **diverges**.

### The Geometric Series

A geometric series is one where each term is obtained by multiplying the previous one by a constant ratio, $r$.
$$ \sum_{n=1}^{\infty} ar^{n-1} = a + ar + ar^2 + \cdots $$
This is one of the few series where we can easily find the sum.

The geometric series **converges** if $|r| < 1$, and its sum is:
$$ S = \frac{a}{1-r} $$
If $|r| \ge 1$, the series **diverges**.

**Financial Application:** The formula for the present value of a perpetuity (a stream of equal payments that goes on forever) is an application of the geometric series.

## Tests for Convergence

For most series, finding the exact sum is difficult or impossible. The more important question is often just to determine *if* the series converges. We have several tests for this.

**The Divergence Test:**
If $\lim_{n \to \infty} a_n \neq 0$ or the limit does not exist, then the series $\sum a_n$ **diverges**.
**Warning:** If the limit *is* 0, this test tells us nothing! The series might converge or diverge. (e.g., the harmonic series $\sum \frac{1}{n}$).

**The Integral Test:**
Suppose $f(x)$ is a continuous, positive, decreasing function on $[1, \infty)$ and let $a_n = f(n)$.
-   If $\int_1^{\infty} f(x) \,dx$ is convergent, then $\sum_{n=1}^{\infty} a_n$ is convergent.
-   If $\int_1^{\infty} f(x) \,dx$ is divergent, then $\sum_{n=1}^{\infty} a_n$ is divergent.

This test is the basis for the **p-series test**: the series $\sum \frac{1}{n^p}$ converges if $p > 1$ and diverges if $p \le 1$.

**The Comparison Test:**
Suppose we have two series with positive terms, $\sum a_n$ and $\sum b_n$.
-   If $\sum b_n$ is convergent and $a_n \le b_n$ for all $n$, then $\sum a_n$ is also convergent.
-   If $\sum b_n$ is divergent and $a_n \ge b_n$ for all $n$, then $\sum a_n$ is also divergent.

**The Ratio Test:**
This is a very powerful test, especially for series involving factorials or $n$-th powers. Let $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L$.
-   If $L < 1$, the series is absolutely convergent.
-   If $L > 1$, the series is divergent.
-   If $L = 1$, the test is inconclusive.

## Summary

-   A **sequence** is an ordered list of numbers. We are interested in its limit as the number of terms goes to infinity.
-   A **series** is the sum of the terms of a sequence. We analyze its convergence by looking at the limit of its partial sums.
-   Various **tests** (Divergence, Integral, Comparison, Ratio) help us determine whether a series converges or diverges, which is crucial for the next step.

With this foundation in infinite series, we are now ready to explore a special and incredibly useful type of series.

Next, we will look at [Power and Taylor Series](power-and-taylor-series.md).

---

[View Problems and Solutions for Sequences And Series](/math-basic/calculus/problems/sequences-and-series-problems/)
