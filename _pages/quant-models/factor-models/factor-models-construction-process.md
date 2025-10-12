---
title: "Factor Models Construction Process"
permalink: /factor-models/factor-models-construction-process/
sidebar:
    nav: "factor-models"
---

Factor models are widely used in finance to explain the variation in asset returns through a set of underlying factors. Their popularity, especially in portfolio and risk management, stems from their ability to differentiate cross-sectional return variation rather than attempting to predict the future with precision.

By understanding these variations, we can construct trades—buying assets with high expected returns and shorting those with low expected returns. Profits arise from differences in factor exposures. Factor models also help estimate portfolio risk, identify which factors contribute most to risk, and quantify overall risk exposure.

However, the factor models used in industry differ significantly from those in academia. Academic models require factors to be interpretable, robust, long-term, and stable, with minimal correlation between them. The goal is to find a reasonable model that explains the market. Academic models typically use only 3-5 factors, such as in the Fama-French 3-factor model (market, size, value). Any other variable that explains return variation is considered an **anomaly**.

In contrast, industry models are often black boxes. The focus is on profitability, not interpretability. All variables—whether considered factors or anomalies in academia—are treated as factors in industry. Models may include hundreds of factors and are not necessarily linear; machine learning techniques are frequently used both to discover and to combine factors in nonlinear ways.

The table below summarizes the key differences between academic and industry factor models:

| Aspect                | Academic Factor Models                          | Industry Factor Models                        |
|-----------------------|-------------------------------------------------|-----------------------------------------------|
| Purpose               | Explain market                                  | Make money                                    |
| Factors               | 3-5 interpretable factors                       | Hundreds of factors                           |
| Model Complexity      | Linear models                                   | Non-linear models, often machine learning     |
| Focus                 | Stability, robustness, interpretability         | Profitability, adaptability                   |
| Anomalies             | Treated as anomalies                            | Treated as factors                            |

A typical process for constructing industry factor models includes:

1. **Data Collection**: Gather a broad range of financial data, such as stock prices, trading volumes, and fundamental metrics (e.g., earnings, book value).
2. **Feature Engineering**: Generate a large set of potential factors, including both traditional factors (like size and value) and anomalies (like momentum and low volatility).
3. **Factor Selection**: Test individual factors to assess their usefulness.
4. **Model Training**: Combine selected factors using linear or nonlinear methods.
5. **Model Evaluation**: Assess performance using out-of-sample testing and cross-validation to ensure generalizability.
6. **Risk Management**: Analyze the model's risk exposures and ensure alignment with the desired risk profile.
7. **Deployment**: Implement the model in live trading, continuously monitoring and adjusting as needed.

In the next two sections, we will discuss steps 3 and 4 in detail, focusing on the academic approach. For factor selection, we will cover single-factor testing—a common method for evaluating factor usefulness. For model training, we will use a linear model to empirically test the factor model.

Next up: [Single Factor Test](single-factor-test.md)
