---
title: Eigenvalues and Eigenvectors
permalink: /linear-algebra/eigenvalues-and-eigenvectors/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## Introduction to Eigenvalues and Eigenvectors

**Eigenvalues** and **eigenvectors** are fundamental concepts in linear algebra with profound applications across various fields, especially in areas dealing with dynamics, stability, and transformations, which are all crucial in quantitative finance.

When a linear transformation (represented by a matrix) acts on certain special vectors, it simply scales them without changing their direction. These special vectors are called **eigenvectors**, and the scalar factor by which they are scaled is called the **eigenvalue**.

Formally, for a square matrix $A$, an eigenvector $\mathbf{v}$ is a non-zero vector such that when $A$ is multiplied by $\mathbf{v}$, the result is a scalar multiple of $\mathbf{v}$. This scalar multiple, $\lambda$, is the eigenvalue.

$$ A\mathbf{v} = \lambda\mathbf{v} $$

where:
*   $A$ is an $n \times n$ square matrix.
*   $\mathbf{v}$ is a non-zero $n \times 1$ vector (the eigenvector).
*   $\lambda$ is a scalar (the eigenvalue).

## Finding Eigenvalues and Eigenvectors

To find eigenvalues and eigenvectors, we rearrange the equation $A\mathbf{v} = \lambda\mathbf{v}$:

$$ A\mathbf{v} - \lambda\mathbf{v} = \mathbf{0} \\
A\mathbf{v} - \lambda I\mathbf{v} = \mathbf{0} \\
(A - \lambda I)\mathbf{v} = \mathbf{0} $$

where $I$ is the identity matrix of the same dimension as $A$.

For a non-zero eigenvector $\mathbf{v}$ to exist, the matrix $(A - \lambda I)$ must be singular (not invertible). This means its determinant must be zero:

$$ \det(A - \lambda I) = 0 $$

This equation is called the **characteristic equation** of $A$. Solving this polynomial equation for $\lambda$ gives us the eigenvalues. Once an eigenvalue $\lambda$ is found, we substitute it back into $(A - \lambda I)\mathbf{v} = \mathbf{0}$ and solve for $\mathbf{v}$ to find the corresponding eigenvectors.

**Example (2x2 Matrix):**
Let $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$.

1.  **Find eigenvalues:**
    $\det(A - \lambda I) = \det \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix} = (4-\lambda)(3-\lambda) - (1)(2) = 12 - 4\lambda - 3\lambda + \lambda^2 - 2 = \lambda^2 - 7\lambda + 10 = 0$
    Factoring the quadratic equation: $(\lambda - 2)(\lambda - 5) = 0$.
    So, the eigenvalues are $\lambda_1 = 2$ and $\lambda_2 = 5$.

2.  **Find eigenvectors for $\lambda_1 = 2$:**
    $(A - 2I)\mathbf{v} = \begin{pmatrix} 4-2 & 1 \\ 2 & 3-2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
    This gives the equation $2v_1 + v_2 = 0$. So, $v_2 = -2v_1$.
    A possible eigenvector is $\mathbf{v}_1 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$ (or any non-zero scalar multiple of it).

3.  **Find eigenvectors for $\lambda_2 = 5$:**
    $(A - 5I)\mathbf{v} = \begin{pmatrix} 4-5 & 1 \\ 2 & 3-5 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
    This gives the equation $-v_1 + v_2 = 0$, so $v_1 = v_2$.
    A possible eigenvector is $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ (or any non-zero scalar multiple of it).

## Diagonalization

A square matrix $A$ is **diagonalizable** if there exists an invertible matrix $P$ and a diagonal matrix $D$ such that $A = PDP^{-1}$. The columns of $P$ are the eigenvectors of $A$, and the diagonal entries of $D$ are the corresponding eigenvalues.

Diagonalization is powerful because it simplifies matrix powers ($A^k = PD^kP^{-1}$) and other matrix functions. Not all matrices are diagonalizable, but many important ones (especially symmetric matrices, common in finance) are.

## Eigenvalues and Eigenvectors in Quant Finance

Eigenvalues and eigenvectors provide insights into the structure and dynamics of financial systems:

1.  **Principal Component Analysis (PCA):** In PCA (which we'll cover in detail later), the eigenvectors of a covariance matrix represent the principal components – orthogonal directions of maximum variance in the data. The corresponding eigenvalues indicate the amount of variance explained by each principal component. This is crucial for dimensionality reduction and identifying independent sources of risk in asset returns.
2.  **Portfolio Risk Decomposition:** Eigenvalues and eigenvectors of the portfolio covariance matrix can help decompose portfolio risk into contributions from different risk factors, aiding in risk management.
3.  **Stability Analysis:** In dynamic financial models, eigenvalues can determine the stability of a system. For example, in econometric models, eigenvalues of transition matrices can indicate whether a system converges to a steady state or diverges.
4.  **Factor Models:** Some factor models derive factors directly from the eigenvalues and eigenvectors of observed return data, aiming to capture the underlying market dynamics.
5.  **Markov Chains:** In Markov chain models (used for credit risk modeling, state transitions), the dominant eigenvalue (often 1) and its corresponding eigenvector represent the long-run steady-state probabilities.

Eigenvalues and eigenvectors allow us to break down complex linear transformations into simpler, independent scaling actions along specific directions. This decomposition reveals the intrinsic properties and behavior of matrices, making them invaluable tools for financial analysis and modeling.

---

Next Topic: [Inner Product Spaces and Orthogonality](inner-product-spaces-and-orthogonality.md)

