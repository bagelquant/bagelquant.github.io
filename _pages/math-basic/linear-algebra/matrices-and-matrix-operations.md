---
title: Matrices and Matrix Operations
permalink: /linear-algebra/matrices-and-matrix-operations/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## What is a Matrix?

A **matrix** is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. It's a powerful tool for organizing and manipulating data, especially when dealing with multiple variables or systems of equations.

A matrix with $m$ rows and $n$ columns is called an $m \times n$ matrix. We denote a matrix by an uppercase letter (e.g., $A$) and its elements by lowercase letters with subscripts indicating their position (e.g., $a_{ij}$ for the element in the $i$-th row and $j$-th column).

$$ 
A = \begin{pmatrix}
 a_{11} & a_{12} & \cdots & a_{1n} \\
 a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & \ddots & \vdots \\
 a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$$

### Matrices in Quant Finance

Matrices are central to almost every quantitative finance model:

*   **Covariance Matrices:** A symmetric matrix where elements $C_{ij}$ represent the covariance between asset $i$ and asset $j$. The diagonal elements $C_{ii}$ are the variances. This is fundamental for portfolio risk calculation.
*   **Return Data:** A matrix could store daily returns for multiple assets over several days, where rows are days and columns are assets.
*   **Factor Loadings:** In factor models, a matrix can represent the sensitivity of various assets to different economic or market factors.

## Types of Matrices

*   **Square Matrix:** A matrix where the number of rows equals the number of columns ($m=n$).
*   **Identity Matrix ($I$):** A square matrix with ones on the main diagonal and zeros elsewhere. It acts like the number '1' in matrix multiplication ($AI = IA = A$).
    $$ 
    I = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    $$ 
*   **Zero Matrix ($0$):** A matrix where all elements are zero. It acts like the number '0' ($A+0 = A$).
*   **Diagonal Matrix:** A square matrix where all non-diagonal elements are zero.
*   **Symmetric Matrix:** A square matrix $A$ such that $A = A^T$ (where $A^T$ is the transpose of $A$). Covariance matrices are always symmetric.
*   **Transpose ($A^T$):** The matrix obtained by interchanging the rows and columns of $A$. If $A$ is $m \times n$, then $A^T$ is $n \times m$.

## Basic Matrix Operations

### 1. Matrix Addition and Subtraction

Matrices of the same dimensions can be added or subtracted by adding or subtracting their corresponding elements.

If $A$ and $B$ are $m \times n$ matrices, then $C = A+B$ where $c_{ij} = a_{ij} + b_{ij}$.

**Example:** If $A$ represents a portfolio's current asset holdings and $B$ represents additional purchases, $A+B$ would be the new holdings.

### 2. Scalar Multiplication

Multiplying a matrix by a scalar involves multiplying every element in the matrix by that scalar.

If $A$ is an $m \times n$ matrix and $c$ is a scalar, then $C = cA$ where $c_{ij} = ca_{ij}$.

**Example:** If $A$ is a matrix of stock prices, $0.9A$ could represent a 10% price drop across all stocks.

### 3. Matrix Multiplication

This is the most crucial and often misunderstood matrix operation. For the product $AB$ to be defined, the number of columns in matrix $A$ must equal the number of rows in matrix $B$.

If $A$ is an $m \times p$ matrix and $B$ is a $p \times n$ matrix, their product $C = AB$ is an $m \times n$ matrix where the element $c_{ij}$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$:

$$ 
c_{ij} = \sum_{k=1}^{p} a_{ik}b_{kj}
$$ 

**Example:** Let's say $A$ is a matrix of factor loadings (assets as rows, factors as columns) and $B$ is a vector (a $p \times 1$ matrix) of factor returns. Then $AB$ would give a vector of asset returns explained by the factors.

$$ 
\begin{pmatrix}
 a_{11} & a_{12} \\
 a_{21} & a_{22} \\
 a_{31} & a_{32}
\end{pmatrix}
\begin{pmatrix}
 b_1 \\
 b_2
\end{pmatrix}
= 
\begin{pmatrix}
 a_{11}b_1 + a_{12}b_2 \\
 a_{21}b_1 + a_{22}b_2 \\
 a_{31}b_1 + a_{32}b_2
\end{pmatrix}
$$ 

Matrix multiplication is **not commutative** ($AB \neq BA$ in general) but it is **associative** ($(AB)C = A(BC)$) and **distributive** ($A(B+C) = AB+AC$).

## Matrix-Vector Product

A special case of matrix multiplication is the product of a matrix and a vector. If $A$ is an $m \times n$ matrix and $\mathbf{x}$ is an $n \times 1$ column vector, then $A\mathbf{x}$ is an $m \times 1$ column vector. This operation is fundamental for solving systems of linear equations and for linear transformations.

$$ 
A\mathbf{x} = \begin{pmatrix}
 a_{11} & \cdots & a_{1n} \\
 \vdots & \ddots & \vdots \\
 a_{m1} & \cdots & a_{mn}
\end{pmatrix}
\begin{pmatrix}
 x_1 \\
 \vdots \\
 x_n
\end{pmatrix}
= 
\begin{pmatrix}
 a_{11}x_1 + \cdots + a_{1n}x_n \\
 \vdots \\
 a_{m1}x_1 + \cdots + a_{mn}x_n
\end{pmatrix}
$$ 

Understanding these fundamental operations is the cornerstone of effectively applying linear algebra to complex financial problems. In the next article, we will see how these operations come into play when solving systems of linear equations.

---

Next Topic: [Solving Linear Systems](solving-linear-systems.md)

