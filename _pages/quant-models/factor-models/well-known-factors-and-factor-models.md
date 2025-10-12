---
title: "Well-Known Factors and Factor Models"
permalink: /factor-models/well-known-factors-and-factor-models/
sidebar:
    nav: "factor-models"
---

## Well-Known Factors

In quantitative finance, several well-established factors have been identified that help explain the cross-sectional variation in asset returns. These factors are widely used in factor models to assess the risk and return characteristics of assets. Below are some of the most recognized factors:

- **Market Risk (Beta):**
  Measures an asset's sensitivity to overall market returns, typically estimated using the Capital Asset Pricing Model (CAPM).

- **Size:**
  The size effect suggests that smaller companies tend to outperform larger ones on a risk-adjusted basis, often measured by market capitalization.

- **Value:**
  The value factor reflects the tendency for undervalued stocks (with low price-to-earnings or price-to-book ratios) to outperform overvalued stocks. Common value metrics include:
  - **Book-to-Market Ratio (BM):** Book value divided by market value.
  - **Earnings-to-Price Ratio (E/P):** Earnings divided by stock price.

- **Momentum:**
  Captures the tendency for assets that have performed well in the past to continue performing well, and vice versa for underperformers. Typically measured using past returns over periods such as 3 to 12 months.
  > Eugene Fama famously opposed the momentum factor, arguing it is not a true risk factor but a result of behavioral biases. Nevertheless, momentum is observed across many asset classes, including stocks, bonds, and commodities.

- **Profitability:**
  Firms with higher profitability (measured by metrics like return on equity or operating income) tend to outperform less profitable firms. Common metrics include:
  - **Return on Equity (ROE):** Net income divided by shareholders' equity.
  - **Return on Assets (ROA):** Net income divided by total assets.
  - **Return on Invested Capital (ROIC):** Net operating profit after tax divided by invested capital.
  - **Return on Tangible Assets (ROTA):** Net income divided by tangible assets.
  - **Operating Profitability:** Operating income divided by total assets.

- **Investment:**
  Firms that invest conservatively (low asset growth) tend to outperform those that invest aggressively (high asset growth). This is often measured by asset growth or capital expenditures.

> [!NOTE]
> The factors above are not exhaustive. Many other factors have been proposed in the literature, and their significance can vary across asset classes and market conditions.

In practice, hundreds or even thousands of factors (including so-called anomalies) are used in quantitative finance. Factors can be constructed using feature engineering, combining multiple features, or applying machine learning to identify patterns. However, the factors listed above remain the most widely recognized and studied.

## Well-Known Factor Models

The table below summarizes some of the most influential factor models in the literature:

| Factor Model                  | Factors                                 | Year |
|-------------------------------|-----------------------------------------|------|
| Fama-French 3-Factor Model    | Market, Size, Value                     | 1993 |
| Carhart 4-Factor Model        | Market, Size, Value, Momentum           | 1997 |
| Novy-Marx 5-Factor Model      | Market, Size, Value, Profitability, Investment | 2013 |
| Fama-French 5-Factor Model    | Market, Size, Value, Profitability, Investment | 2015 |
| Hou-Xue-Zhang 4-Factor Model  | Market, Size, Value, Profitability      | 2015 |
| Stambaugh-Yuan 4-Factor Model | Market, Size, Value, Profitability      | 2017 |
| Hou-Xue-Zhang 5-Factor Model  | Market, Size, Value, Profitability, Investment | 2017 |

Although each new factor model aims to improve upon its predecessors, debate continues over which model is best. The choice of factor model often depends on the specific context, asset class, and research question at hand.

## Literature Review

- [Factor Models in Asset Pricing: A Comprehensive Literature Review(Up to 2024)](https://bagelquant.com/literature-review-factor-models/)
- [Evolution of Alpha Signals in Asset Pricing: A Literature Review](https://bagelquant.com/literature-review-alphas/)
