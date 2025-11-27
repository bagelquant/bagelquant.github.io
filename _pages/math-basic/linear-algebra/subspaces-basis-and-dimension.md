---
title: Subspaces, Basis, and Dimension
permalink: /linear-algebra/subspaces-basis-and-dimension/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## Subspaces

A **subspace** of a vector space $V$ is a subset $W$ of $V$ that is itself a vector space under the same operations of vector addition and scalar multiplication defined on $V$.

For a non-empty subset $W$ to be a subspace of $V$, it must satisfy three conditions:

1.  **Contains the zero vector:** The zero vector of $V$ must be in $W$ ($\mathbf{0} \in W$).
2.  **Closed under vector addition:** For any $\mathbf{u}, \mathbf{v} \in W$, their sum $\mathbf{u} + \mathbf{v}$ must also be in $W$.
3.  **Closed under scalar multiplication:** For any scalar $c$ and any vector $\mathbf{u} \in W$, the scalar multiple $c\mathbf{u}$ must also be in $W$.

**Example:** In $\mathbb{R}^3$, a line passing through the origin is a subspace. A plane passing through the origin is also a subspace. A line or plane not passing through the origin is NOT a subspace because it does not contain the zero vector.

### Subspaces in Quant Finance

*   **Portfolio Diversification:** The set of all possible portfolio allocations that satisfy certain constraints (e.g., sum of weights equals 1, no short selling) might form a subspace or a related geometric structure.
*   **Factor Spaces:** In factor models, the "factor space" is the subspace spanned by the risk factors, and asset returns are projected onto this space.

## Span of a Set of Vectors

Given a set of vectors {$\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$} in a vector space $V$, their **span**, denoted $\text{span}\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\}$, is the set of all possible **linear combinations** of these vectors.

A linear combination is an expression of the form $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$, where $c_1, \ldots, c_k$ are scalars.

The span of any set of vectors is always a subspace. It represents all the vectors that can be "reached" by combining the given vectors.

**Example:** In $\mathbb{R}^3$, the span of two non-collinear vectors is a plane through the origin.

## Linear Independence

A set of vectors {$\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$} is said to be **linearly independent** if the only way to form the zero vector as a linear combination of them is if all the scalar coefficients are zero:

$$ c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \cdots = c_k = 0 $$

If there exists at least one non-zero coefficient that produces the zero vector, then the vectors are **linearly dependent**. This means at least one vector in the set can be expressed as a linear combination of the others, implying redundancy.

### Linear Independence in Quant Finance

*   **Risk Factors:** Ideally, the risk factors in a financial model should be linearly independent; otherwise, they are capturing redundant information.
*   **Asset Returns:** If a set of asset returns are linearly dependent, it implies that some assets' returns can be perfectly replicated by others, which is important for arbitrage theory or identifying redundant instruments.

## Basis of a Vector Space (or Subspace)

A **basis** for a vector space $V$ is a set of vectors $B = \{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n\}$ that satisfies two conditions:

1.  $B$ is **linearly independent**.
2.  $B$ **spans** $V$. (Every vector in $V$ can be written as a linear combination of the vectors in $B$.)

Essentially, a basis is the smallest set of vectors that can generate all vectors in the space, and each vector in the space can be uniquely represented as a linear combination of the basis vectors.

**Example:** For $\mathbb{R}^n$, the standard basis is {$\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n$}, where $\mathbf{e}_i$ is a vector with 1 in the $i$-th position and 0s elsewhere.

## Dimension of a Vector Space

The **dimension** of a vector space $V$, denoted $\dim(V)$, is the number of vectors in any basis for $V$. An important theorem states that all bases for a given vector space have the same number of vectors, so the dimension is well-defined.

**Example:**
*   $\dim(\mathbb{R}^2) = 2$ (e.g., basis {$(1,0), (0,1)$})
*   $\dim(\mathbb{R}^3) = 3$ (e.g., basis {$(1,0,0), (0,1,0), (0,0,1)$})

### Dimension in Quant Finance

*   **Degrees of Freedom:** The dimension of a subspace spanned by financial data can tell us the effective number of independent drivers or factors influencing that data. For instance, in Principal Component Analysis (PCA), we often reduce the dimensionality of financial data by finding the most important dimensions (principal components) that explain most of the variance.
*   **Factor Model Construction:** The number of independent factors in an asset pricing model corresponds to the dimension of the factor space.

Understanding subspaces, span, linear independence, basis, and dimension provides a deep insight into the intrinsic structure and properties of data, which is invaluable for building robust and insightful financial models.

---

Next Topic: [Linear Transformations](linear-transformations.md)

