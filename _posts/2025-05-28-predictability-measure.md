---
title: "Predictability Measure - IC, ICIR"
tags:
    - factor
---

For a factor model, we can measure the predictability of a factor by calculating the Information Coefficient (IC) and the Information Coefficient Information Ratio (ICIR).

## Information Coefficient (IC)

**Information Coefficient (IC)** measures the cross-sectional correlation between factor scores at time *t* and realized returns at time *t+1*:

$$
IC_t = \text{corr}(f_t, r_{t+1})
$$

where:

- $f_t$ is the factor score(factor loading) at time *t*.
- $r_{t+1}$ is the realized return at time *t+1*.

Interpretation:

- IC > 0.15: strong predictive power
- IC ≈ 0: no predictive power
- IC < 0: inverse predictor (potentially shortable)

### Spearman rank IC and Pearson IC

IC can be calculated using either Spearman rank correlation or Pearson correlation:

## Pearson vs Spearman Information Coefficient (IC)

| Feature                     | Pearson IC                              | Spearman IC                              |
|----------------------------|------------------------------------------|------------------------------------------|
| Definition                 | Correlation of **raw values**            | Correlation of **ranked values**         |
| Measures                   | **Linear relationship**                  | **Monotonic relationship**               |
| Sensitivity to outliers    | High (can be distorted by outliers)      | Low (robust to extreme values)           |
| Suitable when              | Factor scores and returns are linearly related | Factor and returns follow any consistent ordering |
| Common in finance?         | Sometimes used, but less robust          | Widely used in quant research            |
| Interpretation             | Can be misleading if extreme values dominate | Better reflects **true rank predictability** |
| Preferred for factor IC?   | No (unless assumptions clearly hold)     | Yes (default choice in empirical analysis) |

## Information Coefficient Information Ratio (ICIR)

The **Information Coefficient Information Ratio (ICIR)** measures the consistency and stability of the IC across time periods:

$$
ICIR = \frac{\text{mean}(IC)}{\text{std}(IC)}
$$

**Interpretation:**

- ICIR > 0.5: Indicates good consistency in the factor's predictive power.
- ICIR > 1.0: Indicates a very strong and stable factor.

These metrics are standard tools in quantitative finance for evaluating the quality and reliability of predictive factors.
