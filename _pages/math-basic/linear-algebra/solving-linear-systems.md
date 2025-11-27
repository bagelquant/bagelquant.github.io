---
title: Solving Linear Systems
permalink: /linear-algebra/solving-linear-systems/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## Introduction to Linear Systems

A **system of linear equations** is a set of equations where each equation is linear. In two variables, a linear equation represents a straight line. In higher dimensions, it represents a hyperplane. The solution to a system of linear equations is the set of values for the variables that satisfy all equations simultaneously.

Consider a system of $m$ linear equations in $n$ variables:

$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m
\end{align*}
$$

This system can be written in a compact matrix form: $A\mathbf{x} = \mathbf{b}$, where:

*   $A$ is the $m \times n$ **coefficient matrix**.
*   $\mathbf{x}$ is the $n \times 1$ **vector of variables**.
*   $\mathbf{b}$ is the $m \times 1$ **vector of constants**.

$$
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
b_2 \\
\vdots \\
b_m
\end{pmatrix}
$$

### Linear Systems in Quant Finance

Systems of linear equations are fundamental in quantitative finance:

*   **Portfolio Allocation:** Determining the optimal weights for a portfolio often involves solving linear systems that represent budget constraints and desired risk/return profiles.
*   **Arbitrage Opportunities:** Identifying arbitrage involves solving systems where some combinations of assets yield a risk-free profit.
*   **Curve Fitting:** In fixed income, constructing a yield curve from observed bond prices often requires solving linear systems.
*   **Factor Exposures:** Calculating the exposure of a portfolio or asset to various risk factors can be formulated as a linear system.

## Methods for Solving Linear Systems

### 1. Gaussian Elimination (Row Reduction)

Gaussian elimination is a systematic procedure for transforming a system of linear equations into an equivalent system that is easier to solve. This is done by applying a sequence of **elementary row operations** to the augmented matrix $[A \| \mathbf{b}]$:

1.  Swapping two rows.
2.  Multiplying a row by a non-zero scalar.
3.  Adding a multiple of one row to another row.

The goal is to transform the augmented matrix into **row echelon form** (or **reduced row echelon form**), from which the solution can be found by back-substitution.

**Example (Financial Context):** Imagine you have three assets, and you want to find a combination that yields specific total returns under different market scenarios. This could be set up as a system of linear equations and solved using Gaussian elimination.

### 2. Matrix Inversion

If the coefficient matrix $A$ is square ($m=n$) and **invertible** (meaning its determinant is non-zero, a concept we'll explore in the next article), then we can find its inverse, denoted $A^{-1}$.

If $A\mathbf{x} = \mathbf{b}$, and $A^{-1}$ exists, we can multiply both sides by $A^{-1}$:

$$
A^{-1}(A\mathbf{x}) = A^{-1}\mathbf{b} \\
(A^{-1}A)\mathbf{x} = A^{-1}\mathbf{b} \\
I\mathbf{x} = A^{-1}\mathbf{b} \\
\mathbf{x} = A^{-1}\mathbf{b}
$$

This method provides a direct solution for $\mathbf{x}$. However, computing $A^{-1}$ can be computationally expensive for large matrices and is numerically unstable for ill-conditioned matrices. For practical applications with large systems, Gaussian elimination (or LU decomposition, a related technique) is often preferred.

**Example (Financial Context):** If $A$ represents the sensitivities of a portfolio to different risk factors, and $\mathbf{b}$ represents desired factor exposures, then $A^{-1}\mathbf{b}$ could give the required changes in portfolio positions to achieve those exposures.

## Existence and Uniqueness of Solutions

For a system $A\mathbf{x} = \mathbf{b}$, there are three possibilities for solutions:

1.  **Unique Solution:** The system has exactly one solution. This typically occurs when $A$ is square and invertible. Geometrically, the hyperplanes intersect at a single point.
2.  **No Solution:** The system is **inconsistent**. This happens when the equations contradict each other. Geometrically, the hyperplanes are parallel or do not intersect at a common point.
3.  **Infinitely Many Solutions:** The system has an infinite number of solutions. This typically occurs when some equations are redundant (linearly dependent). Geometrically, the hyperplanes intersect along a line or a higher-dimensional space.

The number of solutions can be determined by analyzing the row echelon form of the augmented matrix and the ranks of $A$ and $[A \| \mathbf{b}]$. This will be further elaborated when we discuss rank and null space.

Understanding how to solve linear systems is a cornerstone for many quantitative finance problems, from optimizing portfolios to calibrating models. The ability to structure a problem as $A\mathbf{x} = \mathbf{b}$ and apply the appropriate solution method is a valuable skill.

---

Next Topic: [Determinants and Their Properties](determinants-and-their-properties.md)

