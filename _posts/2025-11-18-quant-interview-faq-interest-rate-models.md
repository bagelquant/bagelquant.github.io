---
title: "Quant Interview FAQ — Interest Rate Models"
tags: [vasicek, CIR, hull-white, short-rate-model, fixed-income, term-structure]
header:
  overlay_image: /assets/images/headers/interest-rate-models-dark.png
  overlay_filter: 0.4
excerpt: "A technical overview of short-rate interest rate models commonly used in quantitative finance, including Vasicek, CIR, and Hull–White. Covers model intuition, equations, calibration, and typical interview topics."
---

Short-rate models are fundamental tools in interest rate quant roles. They describe the evolution of the instantaneous short rate, allowing quants to price bonds, swaps, swaptions, and construct arbitrage-free term structures. Vasicek, CIR, and Hull–White are among the most common models tested in interviews because of their tractability and closed-form solutions.

## 1. What is a short-rate model?

A short-rate model specifies the stochastic process followed by the instantaneous short rate $r_t$. It defines the drift, volatility, and randomness of interest rate movements.

General form:

$$
dr_t = \mu(t,r_t)dt + \sigma(t,r_t)dW_t.
$$

Given $r_t$, the time-$t$ price of a zero-coupon bond maturing at $T$ is:

$$
P(t,T) = \mathbb{E}_t \left[ e^{-\int_t^T r_s ds} \right].
$$

Short-rate models allow closed-form bond pricing under certain assumptions, making them widely used for fixed-income derivatives.

## 2. Vasicek Model

SDE:
$$
dr_t = a(b - r_t) dt + \sigma dW_t
$$

Parameters:  
- $a$: speed of mean reversion  
- $b$: long-term mean  
- $\sigma$: constant volatility  

Key properties:
- Rates revert to $b$ at speed $a$.  
- Gaussian distribution → negative rates possible.  
- Closed-form bond price.

Bond price:
$$
P(t,T) = \exp\left(A(t,T) - B(t,T) r_t\right)
$$

Where:
$$
B(t,T) = \frac{1 - e^{-a(T-t)}}{a}
$$
$$
A(t,T) = \left(b - \frac{\sigma^2}{2a^2}\right)(B(t,T) - (T-t)) - \frac{\sigma^2}{4a}B(t,T)^2
$$

Pros: analytically simple, widely used for intuition and pedagogy.  
Cons: allows negative rates; cannot match the initial yield curve exactly.

## 3. CIR Model (Cox–Ingersoll–Ross)

SDE:
$$
dr_t = a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

Differences from Vasicek:
- Volatility increases with the level of rates $\sqrt{r_t}$.
- Rates remain non-negative if the Feller condition holds:
  $$
  2ab \ge \sigma^2
  $$

Bond pricing is also available in closed form:
$$
P(t,T)=A(t,T)\exp(-B(t,T)r_t)
$$

Pros:
- Ensures positive rates (unlike Vasicek).  
- Captures level-dependent volatility.

Cons:
- Less flexible; cannot match the initial yield curve exactly.  
- Still a one-factor model.

Common in credit risk and Monte Carlo simulation of short rates.

## 4. Hull–White One-Factor Model (Extended Vasicek)

SDE:
$$
dr_t = a(\theta(t) - r_t)\,dt + \sigma\,dW_t
$$

Here, $\theta(t)$ is a time-dependent function chosen so that the model fits the current market yield curve exactly.

This is the key distinction:
- Vasicek and CIR do not fit today's term structure.  
- Hull–White does, by construction.

Bond price remains affine:
$$
P(t,T) = A(t,T)\exp(-B(t,T)r_t),
$$
but with $A(t,T)$ computed from the observed yield curve and \(\theta(t)\).

Pros:
- Accurately fits today’s yield curve.  
- Closed-form pricing for swaps and vanilla IR derivatives.  
- Used widely in practice.

Cons:
- Gaussian → negative rates possible.  
- Still one-factor → cannot capture slope/twist of the curve.

## 5. Model Comparison

| Model | Mean Reversion | Volatility | Rates Always Positive | Fits Initial Curve | Typical Use |
|-------|----------------|------------|------------------------|---------------------|-------------|
| Vasicek | Yes | Constant | No | No | Intro modeling, analytical pricing |
| CIR | Yes | $\sigma\sqrt{r}$ | Yes (Feller) | No | Credit risk, simulation |
| Hull–White | Yes | Constant | No | Yes | Curve calibration, swaption pricing |

## 6. Calibration Approaches

Vasicek / CIR:
- Estimate $a, b, \sigma$ from historical short rates using MLE or GMM.  
- Fit to bond prices using least-squares.

Hull–White:
- Calibrate $\theta(t)$ directly from the yield curve.  
- Calibrate $(a, \sigma)$ to swaption or cap/floor vol surfaces.

Common interview question:  
“Explain how to calibrate the Hull–White one-factor model to the market.”

Answer:  
Fit $\theta(t)$ to match the initial term structure, and fit $a$ and $\sigma$ to match market swaption/cap volatilities.

## 7. When to use each model

- Use **Vasicek** when you need tractability and simple closed-form intuition.  
- Use **CIR** when positivity of rates is required or when rate-level-dependent volatility is important.  
- Use **Hull–White** when you need an arbitrage-free model that fits the current yield curve exactly.

For more complex curve dynamics, two-factor extensions such as G2++ or multi-factor Hull–White models are used.

## 8. Limitations of One-Factor Short-Rate Models

- Cannot capture multi-factor yield curve movements (twist, butterfly).  
- Gaussian models can produce negative rates.  
- Limited flexibility in matching volatility surfaces.  
- Oversimplify correlation structures across maturities.

Modern desks often use HJM models or the Libor Market Model (LMM), but Vasicek, CIR, and Hull–White remain core interview topics.

## Summary

Short-rate models describe the stochastic evolution of interest rates and provide analytical pricing tools for fixed-income securities.  

Vasicek provides simplicity, CIR enforces positivity, and Hull–White ensures exact calibration to the observed yield curve. A clear understanding of their dynamics, calibration methods, and use cases is essential for fixed-income quantitative roles.

