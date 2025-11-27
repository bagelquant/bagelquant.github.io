---
title: Linear Algebra
permalink: /linear-algebra/
header:
  overlay_image: /assets/images/headers/linear-algebra.png
  overlay_opacity: 0.8
nav: "linear-algebra"
---

Welcome to the Linear Algebra series! This collection of articles is designed to provide a rigorous yet accessible introduction to linear algebra, with a particular focus on its applications and relevance in quantitative finance. Whether you're building models, analyzing financial data, or understanding complex algorithms, linear algebra provides the essential mathematical framework.

The linear algebra is a cornerstone of many quantitative techniques used in finance, since it naturally handles multi-dimensional data and relationships. Concepts such as vectors, matrices, describe financial data relly well, a finance data set usually have two identifiers: time and asset id, and all the "features" are just different dimensions. For example, Apple's stock price could represent in a table like this:


| Date       | Asset ID | Price | Volume | Market Cap |
|------------|----------|-------|--------|------------|
| 2023-01-01 | AAPL     | 150   | 10000  | 2T         |
| 2023-01-02 | AAPL     | 152   | 12000  | 2.1T       |

Linear algebra allows us to efficiently manipulate and analyze such multi-dimensional data, enabling some core tasks in quantitative finance, including:

- Portfolio Optimization: Techniques like mean-variance optimization rely heavily on matrix operations to determine optimal asset allocations that balance risk and return.
- Risk Management: Covariance matrices are used to model the relationships between asset returns, helping to assess and manage portfolio risk.
- Factor Models: Linear algebra is used to decompose asset returns into factors, aiding in understanding
- Machine Learning: Many machine learning algorithms, such as linear regression, principal component analysis (PCA), and neural networks, are built upon linear algebra concepts.

We will start with the fundamental concepts of vectors and matrices, progressively moving towards more advanced topics such as eigenvalues, eigenvectors, and singular value decomposition. Each topic will be presented with clear definitions, illustrative examples, and insights into how these concepts are applied in the world of finance.

*   [Introduction to Linear Algebra](introduction-to-linear-algebra.md)
*   [Vectors and Vector Spaces](vectors-and-vector-spaces.md)
*   [Matrices and Matrix Operations](matrices-and-matrix-operations.md)
*   [Solving Linear Systems](solving-linear-systems.md)
*   [Determinants and Their Properties](determinants-and-their-properties.md)
*   [Subspaces, Basis, and Dimension](subspaces-basis-and-dimension.md)
*   [Linear Transformations](linear-transformations.md)
*   [Eigenvalues and Eigenvectors](eigenvalues-and-eigenvectors.md)
*   [Inner Product Spaces and Orthogonality](inner-product-spaces-and-orthogonality.md)
*   [Singular Value Decomposition](singular-value-decomposition.md)
*   [PCA and Applications in Finance](pca-and-applications-in-finance.md)
*   [Least Squares and Regression](least-squares-and-regression.md)

Next Topic: [Introduction to Linear Algebra](introduction-to-linear-algebra.md)

