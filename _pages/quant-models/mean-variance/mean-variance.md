---
title: "Mean-Variance Optimization"
layout: topic
permalink: /mean-variance/

nav: "mean-variance"
---

Mean-variance portfolio optimization, introduced by Harry Markowitz in 1952, is the cornerstone of modern portfolio theory. The core idea is to construct an optimal portfolio that either **maximizes expected return for a given level of risk** or **minimizes risk for a given expected return**, with **variance** serving as the measure of risk.

This framework is built on several key assumptions:

- Investors are rational and risk-averse, preferring higher returns for the same level of risk.
- Investment decisions are made over a single-period horizon.
- There are no transaction costs or taxes.
- Only the **mean** and **variance** of asset returns are relevant for portfolio selection.
  (These assumptions are discussed in detail in the first section below.)

When I first encountered modern portfolio theory in a traditional finance program, it was presented in a rather abstract way. We started by plotting two risky assets in mean-variance space, constructing the frontier hyperbola, and introducing the concepts of the **efficient frontier** and the **market portfolio**. While this provided a strong conceptual foundation—especially for finance students—it often lacked mathematical rigor.

My understanding deepened significantly in **Professor [Yangru Wu](https://www.business.rutgers.edu/faculty/yangru-wu)’s Financial Modeling** course. His approach framed mean-variance analysis from a mathematical perspective, filling in theoretical gaps and providing a more comprehensive rationale for its application. This section draws on Professor Wu’s course materials and my own reflections. All accompanying plots are derived from his lectures. I am sincerely grateful to Professor Wu for his insights.

For the calculations in these sections, I created a simple Python package called [bagel-mean-variance](https://github.com/bagelquant/bagel-mean-variance). It is designed to calculate optimal portfolio weights using the methods discussed here. The package is implemented with pure matrix operations, avoiding optimization libraries. It is simple, efficient, and flexible—ideal for financial analysis and portfolio management tasks.

This section provides a rigorous and structured understanding of mean-variance portfolio optimization and its foundational role in finance. It also lays the groundwork for deeper discussions of the **Capital Asset Pricing Model (CAPM)** and **Arbitrage Pricing Theory (APT)**—both essential to modern financial theory.

> **Note:** This is a math-focused series, aligned with the quant orientation of this blog. We will explore the detailed mathematical derivations and insights behind mean-variance optimization.

## Topics

- [From Optimized Utility to Mean-Variance Analysis](from-optimized-utility-to-mean-variance-analysis.md)
- [Solution to the Mean-Variance Optimization Problem](solution-to-the-mean-variance-optimization-problem.md)
- [Efficient Frontier without Risk-Free Asset](efficient-frontier-without-risk-free-asset.md)
- [Frontier with Risk-Free Asset](frontier-with-risk-free-asset.md)
- [Market Portfolio and Security Market Line](market-portfolio-and-security-market-line.md)

> You could navigate all topics at left sidebar.

For additional topics on optimization techniques in finance, visit:

👉 [Optimization Models in Finance](https://bagelquant.com/optimization/)
