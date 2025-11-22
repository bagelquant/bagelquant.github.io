---
title: "Introduction to Optimization"
layout: page
permalink: /optimization/introduction-to-optimization/

nav: "optimization"
---

## 1.1 General Optimization Problem

Suppose we have a set $X$ and a function $f$ that assigns a real number to each element of $X$.

The goal is to find a point $\hat{x} \in X$ such that

$$
f(\hat{x}) \leq f(x) \quad \text{for all } x \in X,
$$

where:

- $X$ is the feasible set,
- $f: X \to \mathbb{R}$ is the objective function,
- $x \in X$ is an element of the feasible set,
- $\hat{x}$ is the optimal solution.

At this level of generality, the problem is too broad to analyze effectively. Therefore, we typically focus on cases where $X$ is a subset of a finite-dimensional Euclidean space $\mathbb{R}^n$.

## 1.2 Common Types of Optimization Problems

- **Unconstrained Optimization**: The feasible set $X$ is the entire space $\mathbb{R}^n$.
- **Constrained Optimization**: The feasible set $X$ is a strict subset of $\mathbb{R}^n$.
- **Linear Programming**: The objective function $f$ is linear, and $X$ is defined by linear equalities and inequalities.
- **Nonlinear Programming**: The objective function $f$ is nonlinear, or some of the constraints defining $X$ are nonlinear.

## 1.3 Global Minimum and Local Minimum

- **Global minimum**: A point $\hat{x}$ that satisfies the relation above is called a global minimum.
- **Local minimum**: A point $\tilde{x}$ is a local minimum if there exists $\epsilon > 0$ such that

$$
f(\tilde{x}) \leq f(x) \quad \text{for all } x \in X \text{ with } ||x - \tilde{x}|| < \epsilon.
$$

> Every global minimum is a local minimum, but not every local minimum is global.

## 1.4 The Main Purpose of Optimization Theory

The main purpose of optimization theory is to develop methods for finding the optimal solution $\hat{x}$ ***without having to examine every point*** in the feasible set $X$.

Exhaustive enumeration is impossible for infinite sets and impractical even for large finite sets.

In later chapters, we will learn how to determine whether a given point is optimal without checking every point in the feasible set.

Next up: [Conves Sets and Functions](convex-sets-and-functions.md)
