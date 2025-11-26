---
title: "Quant Interview FAQ — Volatility Modeling"
layout: post
header:
  overlay_image: /assets/images/headers/volatility-modeling-dark.png
  overlay_filter: 0.4
excerpt: "A technical overview of volatility modeling, including historical volatility, GARCH, implied volatility, stochastic volatility models, and the foundations of modern vol surface modeling."
---

Volatility is central to options pricing, risk management, and systematic trading.  
Most quant interviews include questions about historical volatility, GARCH models, implied volatility, and stochastic volatility frameworks such as the Heston model.  
This guide covers the core concepts and modeling techniques.

## What is volatility and why does it matter?

Volatility measures the variability of returns. It is critical for:

- Derivatives pricing (vol is a direct input to option valuation)
- Portfolio risk management Scenario analysis and stress testing
- Forecasting tail risk
- High-frequency market-making

In Black–Scholes, volatility is the only free parameter, making it the core object that traders model and quote.

## Historical volatility

Historical volatility estimates the standard deviation of asset returns over a past window.

For log returns $r_t = \ln(S_t/S_{t-1})$:

$$
\sigma_{hist} = \sqrt{252} \cdot \text{Std}(r_t)
$$

Variants:

- Close-to-close volatility  
- Parkinson volatility (uses high-low range)  
- Garman–Klass  
- Rogers–Satchell  
- Hodges-Tompkins adjustment  

Historical vol is simple and model-free but backward-looking.

## What is GARCH and why is it used?

GARCH models capture volatility clustering, one of the most important stylized facts in financial returns.

### GARCH(1,1)

$$
\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2
$$

Interpretation:

- $\alpha$: reaction to recent shocks  
- $\beta$: persistence  
- $\alpha + \beta$: volatility persistence (often near 1)

Why it's used:

- Captures mean-reverting volatility  
- Good for forecasting short-term vol  
- Easy to estimate via maximum likelihood  

Extensions:

- EGARCH (asymmetry)
- GJR-GARCH (leverage effect)
- FIGARCH (long memory)

## Implied volatility

Implied volatility is the volatility that, when plugged into Black–Scholes, matches the observed market option price.

It reflects:

- Market expectations of future risk  
- Supply and demand dynamics  
- Volatility risk premium  

Implied volatility is forward-looking and reacts quickly to new information.

## Volatility smile and surface

Options with different strikes or maturities exhibit different implied volatilities:

- **Smile**: symmetric curve common in FX  
- **Skew**: equity markets show downside skew  
- **Term structure**: short-term vol spikes around events  

The collection of strike–maturity volatilities forms the **volatility surface**.

Key interview question:  

Why does equity implied volatility skew downward?  

Because of crash risk, leverage effects, and demand for downside protection.

## Local volatility models

A local volatility model assumes volatility depends on price and time:

$$
dS_t = S_t \sigma(S_t, t) dW_t
$$

The Dupire formula recovers local vol directly from market option prices.

Pros:

- Perfectly fits all European option prices at a point in time  

Cons:

- No stochastic component → underestimates forward uncertainty  
- Unrealistic dynamics for hedging  

Common in risk-neutral calibration and scenario analysis.

## Stochastic volatility models

These models assume volatility itself follows a stochastic process.

### Heston Model

Price:

$$
dS_t = \mu S_t dt + \sqrt{v_t} S_t dW_t^S
$$

Variance:

$$
dv_t = \kappa(\theta - v_t)dt + \sigma_v \sqrt{v_t} dW_t^v
$$

Correlation:

$$
dW_t^S dW_t^v = \rho dt
$$

Important properties:

- Volatility mean-reverts  
- Nonzero correlation produces skew  
- Allows negative skew typical in equities  

Used widely in trading because it generates realistic implied vol surfaces and has semi-closed-form solutions for European options.

## Comparing volatility modeling approaches

| Model | Pros | Cons | Typical Use |
|------|------|------|--------------|
| Historical Vol | Simple, fast | Backward-looking | Baseline risk estimates |
| GARCH | Captures clustering | No skew or smile | Short-term vol forecasting |
| Local Vol | Fits option prices exactly | Unrealistic dynamics | Risk-neutral calibration |
| Heston (SV) | Captures skew, dynamics | Harder to calibrate | Derivatives pricing |
| SABR | Good for rates, skew | No dynamics of vol | Interest-rate options |

## Volatility forecasting vs. volatility pricing

Two different tasks:

### Pricing  

Requires **risk-neutral volatility**, extracted from option prices.  
Implied vol surfaces, stochastic volatility models, and local vol models are used.

### Forecasting  

Requires **realized volatility**, reflecting the true distribution of returns.  
GARCH, HAR-RV, realized kernels, and intraday data are common tools.

Interviews often test whether candidates understand this distinction.
