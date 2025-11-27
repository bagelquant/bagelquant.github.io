---
title: Singular Value Decomposition (SVD)
permalink: /linear-algebra/singular-value-decomposition/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

## What is Singular Value Decomposition (SVD)?

The **Singular Value Decomposition (SVD)** is one of the most powerful and widely used matrix factorization techniques in linear algebra. It decomposes any $m \times n$ matrix $A$ into three simpler matrices:

$$ 
A = U \Sigma V^T
$$ 

where:
*   $U$ is an $m \times m$ **orthogonal matrix** (its columns are orthonormal eigenvectors of $AA^T$).
*   $\Sigma$ (Sigma) is an $m \times n$ **diagonal matrix** containing the **singular values** of $A$. The singular values are the square roots of the non-zero eigenvalues of $A^TA$ (and $AA^T$), arranged in descending order.
*   $V^T$ is the transpose of an $n \times n$ **orthogonal matrix** $V$ (its columns are orthonormal eigenvectors of $A^TA$).

Unlike eigenvalue decomposition, which only applies to square matrices, SVD can be applied to *any* matrix, making it incredibly versatile.

## Singular Values

The diagonal entries of $\Sigma$, denoted $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$, are the **singular values** of $A$. The number $r$ is the rank of the matrix $A$. The singular values measure the "strength" or "importance" of the corresponding singular vectors. Large singular values indicate directions along which the matrix transforms vectors with high gain.

## Geometric Interpretation

SVD has a beautiful geometric interpretation: any linear transformation (matrix $A$) can be broken down into a sequence of three simpler transformations:

1.  A **rotation** or reflection ($V^T$).
2.  A **scaling** along coordinate axes ($\Sigma$).
3.  Another **rotation** or reflection ($U$).

This means that a matrix $A$ transforms the unit sphere in $\mathbb{R}^n$ into an ellipsoid in $\mathbb{R}^m$. The singular values are the lengths of the semi-axes of this ellipsoid, and the columns of $U$ and $V$ provide the directions of these axes.

## Key Properties and Applications

### 1. Low-Rank Approximation

One of the most important applications of SVD is constructing **low-rank approximations** of a matrix. If we take only the $k$ largest singular values and their corresponding singular vectors, we can approximate the original matrix $A$ with a matrix $A_k$ of rank $k$, where $A_k$ is the "best" rank-$k$ approximation of $A$ in terms of minimizing the Frobenius norm of the difference $(A - A_k)$.

$$ 
A_k = U_k \Sigma_k V_k^T
$$ 

where $U_k$ contains the first $k$ columns of $U$, $\Sigma_k$ contains the top-left $k \times k$ block of $\Sigma$, and $V_k^T$ contains the first $k$ rows of $V^T$.

This property is crucial for **dimensionality reduction** and **noise reduction**, as smaller singular values often correspond to noise or less significant components of the data.

### 2. Solving Linear Systems and Pseudo-Inverse

SVD provides a stable way to compute the **pseudo-inverse** (or Moore-Penrose inverse) of any matrix, even non-square or singular matrices. The pseudo-inverse $A^+$ allows us to find least-squares solutions to $A\mathbf{x} = \mathbf{b}$ even when $A$ is not invertible.

### 3. Image Compression and Noise Reduction

By using low-rank approximations, SVD can significantly compress images (representing them as matrices) or remove noise.

## SVD in Quant Finance

SVD is an incredibly versatile tool in quantitative finance for tasks ranging from data analysis to model building:

*   **Principal Component Analysis (PCA):** SVD is the computational backbone of PCA. Performing SVD on a centered data matrix (or its covariance matrix) directly yields the principal components (columns of $V$) and the variance explained by each (related to singular values). This helps identify dominant risk factors, reduce dimensionality, and denoise financial time series.
*   **Factor Models:** In quantitative finance, factor models aim to explain asset returns using a set of common factors. SVD can extract these underlying factors from a matrix of historical asset returns, providing insights into systematic risks.
*   **Denoising Financial Data:** By keeping only the largest singular values and reconstructing the data, SVD can filter out noise from high-dimensional financial datasets (e.g., historical price data, implied volatility surfaces).
*   **Risk Management:** SVD can help decompose portfolio risk by identifying key risk dimensions. It can also be used to identify nearly singular covariance matrices, which can arise from highly correlated assets and pose problems for portfolio optimization.
*   **Term Structure Modeling:** In fixed income, SVD can be applied to a matrix of yield curve movements to identify the dominant "shocks" (e.g., level, slope, curvature) that drive the term structure.
*   **Quantitative Trading Strategies:** SVD can be used to identify robust statistical arbitrage opportunities or develop mean-reversion strategies by identifying cointegrated relationships between assets.

SVD's ability to reveal the intrinsic structure of data, approximate it with lower-rank representations, and handle any matrix makes it an indispensable tool for any quant.

---

Next Topic: [PCA and Applications in Finance](pca-and-applications-in-finance.md)

