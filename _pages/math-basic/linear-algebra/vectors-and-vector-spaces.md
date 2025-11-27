---
title: Vectors and Vector Spaces
permalink: /linear-algebra/vectors-and-vector-spaces/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## What is a Vector?

In physics, a vector is often described as a quantity with both magnitude and direction, like velocity or force. In linear algebra, we adopt a more abstract and generalized definition. A **vector** is an ordered list of numbers. These numbers are called the components or entries of the vector.

We typically represent vectors as columns:

$$ 
\mathbf{v} = \begin{pmatrix} v_1 \ v_2 \ \vdots \ v_n 
\end{pmatrix} 
$$ 

Here, $\mathbf{v}$ is an $n$-dimensional vector, and $v_1, v_2, \ldots, v_n$ are its components.

### Vectors in Quant Finance

In quantitative finance, vectors are ubiquitous. For example:

*   **Asset Returns:** A vector could represent the daily returns of $n$ different stocks: $\mathbf{r} = (r_1, r_2, \ldots, r_n)^T$.
*   **Portfolio Weights:** The proportion of capital allocated to each asset in a portfolio: $\mathbf{w} = (w_1, w_2, \ldots, w_n)^T$.
*   **Economic Indicators:** A collection of macroeconomic variables at a certain point in time: $\mathbf{e} = (\text{GDP}, \text{Inflation}, \text{Interest Rate})^T$.

## Basic Vector Operations

Vectors can be manipulated in several fundamental ways:

### 1. Vector Addition

If $\mathbf{u}$ and $\mathbf{v}$ are two vectors of the same dimension $n$, their sum $\mathbf{u} + \mathbf{v}$ is obtained by adding their corresponding components:

$$ 
\mathbf{u} + \mathbf{v} = \begin{pmatrix} u_1 \ u_2 \ \vdots \ u_n 
\end{pmatrix} + \begin{pmatrix} v_1 \ v_2 \ \vdots \ v_n 
\end{pmatrix} = \begin{pmatrix} u_1+v_1 \ u_2+v_2 \ \vdots \ u_n+v_n 
\end{pmatrix} 
$$ 

**Example:** If $\mathbf{r}_1$ represents today's stock returns and $\mathbf{r}_2$ represents tomorrow's expected returns, then $\mathbf{r}_1 + \mathbf{r}_2$ could represent the combined two-day returns for each stock.

### 2. Scalar Multiplication

If $c$ is a scalar (a real number) and $\mathbf{v}$ is a vector, their product $c\mathbf{v}$ is obtained by multiplying each component of $\mathbf{v}$ by $c$:

$$ 
c\mathbf{v} = c \begin{pmatrix} v_1 \ v_2 \ \vdots \ v_n 
\end{pmatrix} = \begin{pmatrix} cv_1 \ cv_2 \ \vdots \ cv_n 
\end{pmatrix} 
$$ 

**Example:** If $\mathbf{r}$ is a vector of asset returns, then $2\mathbf{r}$ would represent doubling the returns of each asset. If $\mathbf{w}$ is a vector of portfolio weights, then $0.5\mathbf{w}$ represents halving the capital allocated to each asset.

### 3. Dot Product (Inner Product)

The dot product of two $n$-dimensional vectors $\mathbf{u}$ and $\mathbf{v}$ (also known as the Euclidean inner product) results in a scalar:

$$ 
\mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + \cdots + u_nv_n = \sum_{i=1}^{n} u_iv_i 
$$ 

**Example:** In finance, if $\mathbf{r}$ is a vector of asset returns and $\mathbf{w}$ is a vector of portfolio weights, then $\mathbf{w} \cdot \mathbf{r}$ (assuming weights sum to 1) represents the total return of the portfolio.

## Vector Spaces

A **vector space** (or linear space) is a collection of vectors that satisfies certain properties under vector addition and scalar multiplication. These properties ensure that the standard operations behave as expected, allowing for a rich mathematical structure.

Formally, a vector space $V$ over a field of scalars $F$ (usually $\mathbb{R}$ for real numbers in finance) is a set $V$ together with two operations:

1.  **Vector Addition:** For any $\mathbf{u}, \mathbf{v} \in V$, $\mathbf{u} + \mathbf{v} \in V$.
2.  **Scalar Multiplication:** For any $c \in F$ and $\mathbf{v} \in V$, $c\mathbf{v} \in V$.

These operations must satisfy eight axioms (associativity, commutativity, existence of zero vector, existence of additive inverse, distributive properties, and identity for scalar multiplication). The most common vector space we deal with is $\mathbb{R}^n$, the set of all $n$-dimensional vectors with real components.

### Why are Vector Spaces Important?

Understanding vector spaces allows us to think about data and models in a structured way. For instance:

*   **Financial Data as Points in Space:** A series of asset prices over time can be seen as a path in an $n$-dimensional space.
*   **Portfolio Choice:** The set of all possible portfolios forms a vector space, allowing us to analyze their properties using linear algebraic tools.
*   **Basis and Dimension:** These concepts (which we'll cover in a later article) help us understand the intrinsic "degrees of freedom" or the minimum number of independent variables needed to describe a financial system.

By understanding vectors and the spaces they inhabit, we lay the groundwork for understanding more complex linear algebraic concepts and their powerful applications in quantitative finance.

---

Next Topic: [Matrices and Matrix Operations](matrices-and-matrix-operations.md)

