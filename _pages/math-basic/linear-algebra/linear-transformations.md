---
title: Linear Transformations
permalink: linear-algebra/linear-transformations/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## What is a Linear Transformation?

A **linear transformation** (also known as a linear mapping or linear function) is a function $T: V \to W$ between two vector spaces $V$ and $W$ (over the same field of scalars) that preserves the operations of vector addition and scalar multiplication.

Formally, a transformation $T$ is linear if for all vectors $\mathbf{u}, \mathbf{v}$ in $V$ and all scalars $c$:

1.  **Additivity:** $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2.  **Homogeneity (Scalar Multiplication):** $T(c\mathbf{u}) = cT(\mathbf{u})$

These two properties can be combined into a single condition: $T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})$.

### Examples of Linear Transformations

*   **Scaling:** $T(\mathbf{x}) = c\mathbf{x}$ for a scalar $c$. (e.g., adjusting all asset prices by a factor)
*   **Rotation:** Rotating a vector in $\mathbb{R}^2$ or $\mathbb{R}^3$.
*   **Projection:** Projecting a vector onto a line or a plane. (e.g., projecting a high-dimensional data point onto a lower-dimensional factor space)
*   **Zero Transformation:** $T(\mathbf{x}) = \mathbf{0}$ for all $\mathbf{x}$.
*   **Identity Transformation:** $T(\mathbf{x}) = \mathbf{x}$ for all $\mathbf{x}$.

### Non-Examples of Linear Transformations

*   **Translation:** $T(\mathbf{x}) = \mathbf{x} + \mathbf{b}$ (if $\mathbf{b} \neq \mathbf{0}$) is generally not linear because $T(\mathbf{0}) \neq \mathbf{0}$. A linear transformation *must* map the zero vector to the zero vector: $T(\mathbf{0}) = T(0\mathbf{v}) = 0T(\mathbf{v}) = \mathbf{0}$.
*   **Non-linear functions:** $T(x) = x^2$ or $T(x) = \sin(x)$ are not linear.

## Matrix Representation of Linear Transformations

One of the most profound insights of linear algebra is that every linear transformation between finite-dimensional vector spaces can be represented by a **matrix**. Conversely, every matrix defines a linear transformation.

If $T: \mathbb{R}^n \to \mathbb{R}^m$ is a linear transformation, then there exists a unique $m \times n$ matrix $A$ such that $T(\mathbf{x}) = A\mathbf{x}$ for all $\mathbf{x} \in \mathbb{R}^n$. This matrix $A$ is called the **standard matrix** of the linear transformation $T$.

The columns of the standard matrix $A$ are the images of the standard basis vectors of $\mathbb{R}^n$ under the transformation $T$:

$$
A = [T(\mathbf{e}_1) \quad T(\mathbf{e}_2) \quad \cdots \quad T(\mathbf{e}_n)]
$$

where $\mathbf{e}_j$ is the vector with 1 in the $j$-th position and 0s elsewhere.

**Example (Rotation in $\mathbb{R}^2$):**
A counter-clockwise rotation by an angle $\theta$ in $\mathbb{R}^2$ is a linear transformation.
$T(\mathbf{e}_1) = T\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}$
$T(\mathbf{e}_2) = T\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}$
So, the standard matrix for this rotation is $A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

## Kernel and Range of a Linear Transformation

Just as functions have domains and ranges, linear transformations have special subspaces associated with them:

### Kernel (Null Space)

The **kernel** of a linear transformation $T: V \to W$, denoted $\ker(T)$ or $N(T)$, is the set of all vectors in $V$ that are mapped to the zero vector in $W$:

$$$
\ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}
$$$

The kernel is always a subspace of $V$. For a matrix $A$, the kernel of the transformation $T(\mathbf{x}) = A\mathbf{x}$ is the **null space** of $A$, $N(A)$, which is the set of all solutions to $A\mathbf{x} = \mathbf{0}$.

### Range (Image)

The **range** of a linear transformation $T: V \to W$, denoted $\text{range}(T)$ or $R(T)$, is the set of all vectors in $W$ that are images of at least one vector in $V$:

$$$
\text{range}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}
$$$

The range is always a subspace of $W$. For a matrix $A$, the range of the transformation $T(\mathbf{x}) = A\mathbf{x}$ is the **column space** of $A$, $Col(A)$, which is the span of the columns of $A$.

### Rank-Nullity Theorem

A fundamental theorem connecting the dimensions of the kernel and range is the **Rank-Nullity Theorem**:

$$$
\dim(\ker(T)) + \dim(\text{range}(T)) = \dim(V)
$$$

Or, for a matrix $A$:

$$$
\text{nullity}(A) + \text{rank}(A) = n \quad (\text{number of columns of } A)
$$$

where $\text{nullity}(A)$ is the dimension of the null space, and $\text{rank}(A)$ is the dimension of the column space (which also equals the dimension of the row space).

## Linear Transformations in Quant Finance

*   **Change of Basis:** Converting financial data from one representation (e.g., absolute prices) to another (e.g., log returns) can be viewed as a linear transformation.
*   **Factor Models and PCA:** In factor models, a linear transformation maps high-dimensional asset returns to a lower-dimensional space of risk factors. Principal Component Analysis (PCA), which we will discuss later, uses linear transformations to project data onto principal components.
*   **Derivatives Hedging:** A hedge strategy can be thought of as a linear transformation that aims to minimize the risk exposure of a portfolio.
*   **Risk Transformation:** Transforming individual asset risks into portfolio risk involves linear operations.

Linear transformations provide a powerful framework for understanding how operations reshape vector spaces and thus how data is processed and interpreted in quantitative finance. They are the backbone of many dimensionality reduction techniques and portfolio management strategies.

---

Next Topic: [Eigenvalues and Eigenvectors](eigenvalues-and-eigenvectors.md)

