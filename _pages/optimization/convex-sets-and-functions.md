---
title: "Convex Sets and Functions"
permalink: /convex-sets-and-functions/
sidebar:
    nav: "optimization"
---

## 2.1 Convex Sets Definition

The notion of convex set is central to optimization theory. A convex set is such that, afor any two of its points, the entire segment joining these points is contained in the set.

**Definition:** A set $X \subset \mathbb{R}^n$ is called convex if for all $x^1, x^2 \in X$, it contains all points:

$$\alpha x^1 + (1-\alpha)x^2, \quad \text{for all} \quad \alpha \in (0,1).$$

## 2.2 Convest Set properties

### Intercept of convex set is still convex

Let $I$ be an arbitrary index set. If the sets $X_i \subset \mathbb{R}^n$, $i \isin I$, are convex, then the set $X = \cap_{i \in I} X_i$ is also convex.

**Proof:** 

If two points $x^1$ $x^2$ are in $X$, then they are in all $X_i$ for $i \in I$. Since $X_i$ are convex, the segment joining $x^1$ and $x^2$ is in $X_i$ for all $i \in I$. Therefore, the segment is in $X$.

### Sum and scalar multiplication of convex sets is still convex

**Minkowski sum Definition**

The Minkowski sum of two sets $X_1, X_2 \subset \mathbb{R}^n$ is defined as:

$$X_1 + X_2 = \{x_1 + x_2 \mid x_1 \in X_1, x_2 \in X_2\}.$$

**Scalar multiplication**

The scalar multiplication of a set $X \subset \mathbb{R}^n$ by a scalar $\alpha \in \mathbb{R}$ is defined as:

$$\alpha X = \{\alpha x \mid x \in X\}.$$

**Theorem:** If $X$, $Y$ are convex, $c$ and $d$ are scalar. Then set set:

$$Z = cX + dY$$

is convex.





