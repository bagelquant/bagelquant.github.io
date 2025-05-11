---
title: "Mean-Variance Analysis"
permalink: /mean-variance/
layout: splash
header:
  overlay_image: /assets/images/radio-telescope.png
---

Mean-variance portfolio optimization is the foundation of modern portfolio theory, introduced by Harry Markowitz in 1952. The central idea is to construct an optimal portfolio that either **maximizes expected return for a given level of risk** or **minimizes risk for a given expected return**, using **variance** as the measure of risk.

This framework relies on several key assumptions:

- Investors are rational and risk-averse, preferring higher returns for the same level of risk.  
- Investment decisions are made over a single-period horizon.  
- There are no transaction costs or taxes.  
- Only the **mean** and **variance** of asset returns are considered relevant for portfolio selection.  
(These assumptions will be discussed in detail in the first section below.)

When I first encountered modern portfolio theory in a traditional finance program, it was taught in a rather abstract way. We began by plotting two risky assets in the mean-variance space, constructing a frontier hyperbola, and introducing the concepts of the **efficient frontier** and the **market portfolio**. While this provided a strong conceptual foundation—particularly intuitive for finance students—it lacked mathematical rigor.

I later revisited this topic in **Professor [Yangru Wu](https://www.business.rutgers.edu/faculty/yangru-wu)’s Financial Modeling** course, which significantly deepened my understanding. His approach framed mean-variance analysis from a mathematical perspective, filling in the theoretical gaps and offering a more comprehensive rationale for its application. This section draws upon Professor Wu’s course materials and my own reflections. All accompanying plots are derived from his lectures. I am sincerely grateful to Professor Wu for his insights.


## Topics Covered in This Section

1. [From Optimized Utility to Mean-Variance Analysis](from-optimized-utility-to-mean-variance-analysis.md)  
2. [Solution to the Mean-Variance Optimization Problem](solution-to-the-mean-variance-optimization-problem.md)  
3. [Efficient Frontier without a Risk-Free Asset](efficient-frontier-without-risk-free-asset.md)  
4. [Frontier with a Risk-Free Asset](frontier-with-risk-free-asset.md)  
5. [Market Portfolio and the Security Market Line](market-portfolio-and-security-market-line.md)


This section provides a rigorous and structured understanding of mean-variance portfolio optimization and its foundational role in finance. It also lays the groundwork for deeper discussions of the **Capital Asset Pricing Model (CAPM)** and **Arbitrage Pricing Theory (APT)**—both essential to modern financial theory.

> **Note:** This is a math-focused series, aligned with the quant orientation of this blog. We will explore the detailed mathematical derivations and insights behind mean-variance optimization.

For additional topics on optimization techniques in finance, visit:  

👉 [Optimization Models in Finance](https://bagelquant.com/optimization/)

