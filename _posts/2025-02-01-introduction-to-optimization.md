---
title: "Introduction to Optimization"
permalink: /optimization/introduction-to-optimization/
sidebar:
    nav: "optimization"
---

## 1.1 General Optimization Problem

We have certain set $X$, and a function $f$ which assigns every element of $X$ to a real number.

The problem is to find a point $\hat{x} \in X$ such that 

$$\begin{equation}
f(\hat{x}) \leq f(x) \text{ for all } x \in X,
\end{equation}
$$

where:

- $X$ is the feasible set,
- $f \to \mathbb{R}$ is the objective function,
- $x \in X$ is the element of the feasible set,
- $\hat{x}$ is the optimal solution.

At this level of generality, the problem is too broad, very little can be said about it. Therefore, we will focus on $X$ is a subset of a finite-dimensional Euclidean space $\mathbb{R}^n$.

## 1.2 Common Optimization Problem

- **Unconstraint Optimization**: The feasible set $X$ is the whole space $\mathbb{R}^n$.
- **Constraint Optimization**: The feasible set $X$ is a strict subset of $\mathbb{R}^n$.
- **Linear Programming**: The objective function $f$ is linear and the feasible set $X$ is defined by linear equalities and inequalities.
- **Nonlinear Programming**: The objective function $f$ is nonlinear or some of equations or inequalities defining $X$ are nonlinear.

## 1.3 Global minimum and Local minimum

- **Global minimum**: A point $\hat{x}$ satisfying the relation $(1)$ is called a global minimum.
- **Local minimum**: If a point $\tilde{x}$ satisfies for some $\epsilon > 0$ that 

$$f(\tilde{x}) \leq f(x) \text{ for all } x \in X \text{ such that } ||x - \tilde{x}|| < \epsilon,$$

then $\tilde{x}$ is called a local minimum.

> Every global minimum is a local minimum, but not other way around.

## 1.4 The Main Purpose of Optimization Theory

The main purpose of optimization theory is to develop methods for finding the optimal solution $\hat{x}$ ***without having to examine every point*** in the feasible set $X$. 

Obviously, full enumaration is impossible with infinite feasible set, and even with finite feasible set, it is impractical and time-consuming.

Later chapters, we will be able to check whether a given point is optimal or not without checking every point in the feasible set.


