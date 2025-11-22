---
title: "Convex Sets and Functions"
layout: page
permalink: /optimization/convex-sets-and-functions/

nav: "optimization"
---

## 2.1 Definition of Convex Sets

The concept of a convex set is fundamental in optimization theory. A set is convex if, for any two points within the set, the entire line segment connecting them also lies within the set.

**Definition:** A set $X \subset \mathbb{R}^n$ is convex if for all $x^1, x^2 \in X$, it contains every point of the form:

$$
\alpha x^1 + (1-\alpha)x^2, \quad \text{for all} \quad \alpha \in (0,1).
$$

## 2.2 Properties of Convex Sets

### Intersection of Convex Sets

Let $I$ be an arbitrary index set. If each $X_i \subset \mathbb{R}^n$, $i \in I$, is convex, then the intersection $X = \cap_{i \in I} X_i$ is also convex.

**Proof:**

If $x^1$ and $x^2$ are in $X$, then they are in every $X_i$ for $i \in I$. Since each $X_i$ is convex, the segment joining $x^1$ and $x^2$ is in every $X_i$, and thus in $X$.

### Sum and Scalar Multiplication of Convex Sets

**Minkowski Sum:**

The Minkowski sum of two sets $X_1, X_2 \subset \mathbb{R}^n$ is defined as:

$$
X_1 + X_2 = \{x_1 + x_2 \mid x_1 \in X_1, x_2 \in X_2\}.
$$

**Scalar Multiplication:**

The scalar multiplication of a set $X \subset \mathbb{R}^n$ by $\alpha \in \mathbb{R}$ is:

$$
\alpha X = \{\alpha x \mid x \in X\}.
$$

**Theorem:** If $X$ and $Y$ are convex, and $c, d$ are scalars, then the set

$$
Z = cX + dY
$$

is convex.

### Convex Combination

A point $x$ is a convex combination of points $x^1, x^2, ..., x^k$ if there exist $\alpha_1, \alpha_2, ..., \alpha_k$ such that:

$$
x = \alpha_1 x^1 + \alpha_2 x^2 + ... + \alpha_k x^k, \quad \text{where} \quad \alpha_i \geq 0, \quad \sum_{i=1}^{k} \alpha_i = 1.
$$

### Convex Hull

The convex hull of a set $X \subset \mathbb{R}^n$ is the set of all convex combinations of points in $X$:

$$
\text{conv}(X) = \left\{\sum_{i=1}^{k} \alpha_i x^i \mid x^i \in X, \alpha_i \geq 0, \sum_{i=1}^{k} \alpha_i = 1\right\}.
$$

> **Note:** The relationship between convex combinations and the convex hull leads to the following lemma.

**Lemma:** The set $\text{conv}(X)$ consists of all convex combinations of points in $X$.

### Carathéodory's Lemma

**Lemma:** If $X \subset \mathbb{R}^n$, then every point in $\text{conv}(X)$ can be represented as a convex combination of at most $n+1$ points from $X$.

## 2.3 Projection

**Definition:** The projection of a point $x \in \mathbb{R}^n$ onto a set $X \subset \mathbb{R}^n$ is the point in $X$ closest to $x$.
