---
title: "Volatility Surface and Smile"
permalink: /derivatives/volatility-surface-and-smile
sidebar:
  nav: "derivatives"
---

**Implied volatility (IV)** is the volatility input that, when used in the Black–Scholes–Merton (BSM) formula, reproduces a market option price.  
Across strikes and maturities, markets quote a *surface* of IVs rather than a single number. Understanding, cleaning, and modeling this **volatility surface** is central to pricing, risk, and hedging.

## 1) From Prices to Implied Volatility

Given a mid market price $C^{mkt}(K,T)$ (or $P^{mkt}$), implied volatility $\sigma_{\text{iv}}(K,T)$ solves
$$
C^{BSM}\!\big(S_0,K,T;r,q,\sigma_{\text{iv}}\big)=C^{mkt}(K,T).
$$
Inversion is typically done by **Newton–Raphson** with the derivative (Vega):
$$
\sigma_{n+1}=\sigma_n-\frac{C^{BSM}(\sigma_n)-C^{mkt}}{\text{Vega}(\sigma_n)},\qquad
\text{Vega}=S_0 e^{-qT}\phi(d_1)\sqrt{T}.
$$
Good seeds: *Brenner–Subrahmanyam* for near-ATM, or bracket searches for deep OTM/ITM.

**Quoting conventions.** Equity & rates often use strike $K$ or **log-moneyness** $k=\ln(K/F)$ with $F=S_0e^{(r-q)T}$; FX often quotes by **delta** (25-risk-reversal, 25-butterfly, ATM).

## 2) Smile, Skew, and Term Structure (Intuition)

- **Equities:** Typically **downward skew** (OTM puts rich) due to leverage effect, crash risk, and demand for downside protection.
- **FX:** More **smile-like**; asymmetry reflects macro skew (e.g., risk-reversals).
- **Commodities:** Smiles vary; inventory/risk premia can produce positive skew.
- **Term structure:** Short maturities exhibit stronger skew/kurtosis; long maturities tend to be smoother with lower level and curvature.

## 3) No-Arbitrage Anatomy of a Surface

For **undiscounted** call price $C(K,T)$:

- **Butterfly (static) arbitrage free** in strike $\Rightarrow$ convexity:
  $$
  \frac{\partial^2 C}{\partial K^2}(K,T)\ \ge\ 0\quad\Longleftrightarrow\quad\text{non-negative density.}
  $$
- **Calendar arbitrage free** in maturity:
  $$
  \frac{\partial C}{\partial T}(K,T)\ \ge\ 0\quad\text{(holding $K$ fixed)}.
  $$
- **Vertical spread bounds:** $0 \le \frac{\partial C}{\partial K} \le e^{-rT}$.
- **Lee’s moment bounds (wings):** the slope of **total variance** $w(k,T)=\sigma_{\text{iv}}^2(k,T)\,T$ must obey constraints as $|k|\to\infty$; helpful for robust extrapolation.

**Practical check (discrete quotes).** Ensure convexity across strikes (finite-difference second derivative $\ge 0$) and monotonicity in $T$ for each strike bucket.

## 4) Building a Production-Quality Surface (Workflow)

1. **Data cleaning**
   - Use mid quotes; drop stale/outliers; enforce put–call parity to harmonize calls & puts.
   - Map to a consistent **forward** $F(T)$ and discount factor $D(T)=e^{-rT}$ using your curves.

2. **Transform to stable coordinates**
   - Work in **log-moneyness** $k=\ln(K/F)$ or **delta** for FX.
   - Interpolate **total variance** $w(k,T)=\sigma_{\text{iv}}^2(k,T)\,T$ rather than $\sigma$—it behaves more linearly in $T$.

3. **Parametrize cross-sections (smiles)**
   - **SVI (Stochastic Volatility Inspired)** per maturity:
     $$
     w(k)=a + b\Big(\rho (k-m)+\sqrt{(k-m)^2+\sigma^2}\Big),
     $$
     with constraints on $(a,b,\rho,m,\sigma)$ to avoid static arbitrage.
   - Alternatives: quadratic in $k$ near ATM with wing constraints; **Spline-in-$k$** on $w$ with convexity enforcement.

4. **Interpolate in maturity**
   - Interpolate **forward variance** $w(k,T_2)-w(k,T_1)$ linearly in $T$ (or use monotone splines) to preserve calendar monotonicity.

5. **Wing extrapolation**
   - Anchor tails using Lee’s bounds or product-specific heuristics (e.g., FX risk-reversal/Butterfly extrapolation).

6. **Sanity & arbitrage checks**
   - Numerically verify $\partial_{KK} C\!\ge\!0$ and $\partial_T C\!\ge\!0$ on a dense $(k,T)$ grid.

## 5) Local and Stochastic Volatility Links

### Dupire Local Volatility

From the (arbitrage-free) surface, the **local volatility** $\sigma_{\text{loc}}(t,S)$ satisfies
$$
\sigma_{\text{loc}}^2(t,K)=
\frac{\partial_T C(K,T)+q\,C(K,T)-r\,K\,\partial_K C(K,T)}
{\tfrac12\,K^2\,\partial_{KK} C(K,T)}\Bigg|_{T=t}.
$$
This yields a diffusion $dS_t=(r-q)S_t\,dt+\sigma_{\text{loc}}(t,S_t)S_t\,dW_t$ reproducing *all* vanilla prices by construction.

### SABR (log-normal β=1 summary)

SABR dynamics (for forward $F_t$):
$$
\begin{aligned}
dF_t &= \alpha_t F_t\, dW_t^{(1)},\\
d\alpha_t &= \nu \alpha_t\, dW_t^{(2)},\qquad d\langle W^{(1)},W^{(2)}\rangle_t=\rho\,dt.
\end{aligned}
$$
Hagan’s approximation provides a closed-form **implied vol** $\sigma_{\text{iv}}(K,T)$ matching smiles for rates/FX; parameters $(\alpha_0,\nu,\rho)$ control level, skew, and convexity.

> **When to use what?**  
> Local vol exactly matches today’s surface but can mis-represent dynamics (too “sticky-strike”).  
> Stochastic vol (Heston/SABR) captures **smile dynamics** and term structures more realistically but won’t fit surfaces exactly without extra freedom.

## 6) Surface Dynamics for Hedging

- **Sticky-strike:** keep $\sigma_{\text{iv}}(K,T)$ fixed as $S$ moves.  
- **Sticky-delta:** keep $\sigma_{\text{iv}}(\Delta,T)$ fixed (common in FX).  
- **Sticky-moneyness/log-moneyness:** partial adjustment with $S$.

Your choice impacts **P&L attribution** and hedge performance (delta/vega rebalancing, vanna/vomma effects). Backtest under the desk’s house convention.

## 7) Implementation Notes (desk-ready)

- **Numerics:** Use robust IV inversion (bounded Newton + vega floor).  
- **Grids:** Work on $(k,T)$ lattices; store $w=\sigma^2T$ for stability.  
- **Calibration:** Fit each maturity slice (SVI), then smooth through time.  
- **Risk:** Compute **surface Greeks** ($\partial \sigma/\partial K$, $\partial \sigma/\partial T$) for vanna/vomma management and slippage analysis.  
- **Auditability:** Persist raw quotes, cleaning flags, and fitted parameters for replay.

## 8) Quick Example (SVI slice)

Suppose for $T=1$ year you fit an SVI smile with parameters  
$a=0.02,\ b=0.15,\ \rho=-0.4,\ m=0.0,\ \sigma=0.25$.  
At $k=\ln(K/F)=-0.1$,
$$
w(k)=0.02+0.15\Big(-0.4(-0.1)+\sqrt{0.1^2+0.25^2}\Big)=0.02+0.15(0.04+0.269)=0.02+0.046=0.066.
$$
So $\sigma_{\text{iv}}(K,T)=\sqrt{w/T}\approx \sqrt{0.066}=25.7\%$.

## 9) Takeaways

- The **volatility surface** encodes the market’s risk-neutral beliefs and risk premia.  
- Building a **clean, arbitrage-free** surface requires careful coordinates (log-moneyness), **total variance** interpolation, and **SVI/other parametric** fits.  
- **Local vol** reproduces the surface; **stochastic vol** reproduces *smile dynamics*; practitioners often blend both (e.g., local-stochastic vol).

Next up: [Exotic Options](exotic-options.md)
