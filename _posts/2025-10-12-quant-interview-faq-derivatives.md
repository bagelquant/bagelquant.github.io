---
title: "Quant Interview FAQ — Derivatives"
permalink: /quant-interview-faq-derivatives/
tags: 
    - derivatives
    - interview
sidebar:
    nav: derivatives
---

Each question below includes a **Short Answer**, a concrete **Example**, and a **Detailed Explanation** with quant-level depth, including formulas, edge cases, and practical caveats.

> Full topic regarding derivatives is covered in the [Derivatives](https://bagelquant.com/derivatives/) section.

## 1) Forward vs. Futures

**Short Answer**  
Forward = OTC, single settlement at $T$, bilateral credit risk; Futures = exchange-traded, standardized, daily mark-to-market with margin and clearing.

**Example**  
Crude oil June forward struck at $K$ vs. NYMEX CL June futures: same notionally, but futures P&L is realized daily; the forward’s P&L is realized once at expiry.

**Detailed Explanation**  

- **Pricing:** With deterministic rates, $F_0^{fut} = F_0^{fwd} = S_0 e^{(r-q)T}$. With stochastic rates and $\mathrm{corr}(S,r)\neq 0$, daily settlement creates a **convexity bias**: $\mathbb{E}[F^{fut}] \gtrless F^{fwd}$ depending on sign of correlation.  
- **Credit & Funding:** Forwards embed bilateral CVA/DVA, CSA terms (thresholds, MTA, collateral rate), and potentially different **discounting curves** (OIS vs. legacy IBOR). Futures replace bilateral credit risk with CCP exposure and margin liquidity risk.  
- **Operations:** Futures require intraday margin; forwards require CSA collateral management and closeout mechanics (ISDA).  
- **Hedging Impact:** Futures P&L realized early changes effective reinvestment rate and can create basis vs a forward hedge.

## 2) No-Arbitrage Pricing

**Short Answer**  
Portfolios with identical future cash flows must have the same price today.

**Example**  
Equity forward parity: $F_0=S_0 e^{(r-q)T}$. If market quotes $F_0^\star > S_0 e^{(r-q)T}$, do **cash-and-carry** (borrow cash, buy spot, short forward) to lock risk-free profit.

**Detailed Explanation**  

- **Cash-and-carry:** Profit at $T$ equals $F_0^\star - S_0 e^{(r-q)T}$.  
- **Reverse carry:** If $F_0^\star < S_0 e^{(r-q)T}$, short spot, invest proceeds, long forward; profit $= S_0 e^{(r-q)T}-F_0^\star$.  
- **Carry components:** $q$ can be dividends (equity), foreign rate (FX: $r_d-r_f$), or convenience yield vs storage (commodities).  
- **Real-world frictions:** Bid–ask, short-borrow fees, taxes, discrete dividends, and collateral rates shrink or flip apparent arbitrages.

## 3) Risk-Neutral Valuation

**Short Answer**  
Under $\mathbb{Q}$, discounted prices are martingales; price = discounted expectation of payoff under $\mathbb{Q}$.

**Example**  
European option: $V_0=e^{-rT}\mathbb{E}^{\mathbb{Q}}[f(S_T)]$, with $dS_t=(r-q)S_t\,dt+\sigma S_t\,dW_t^{\mathbb{Q}}$.

**Detailed Explanation**  

- **Change of Measure:** Girsanov transforms drift $\mu\to r-q$ to remove risk premia from pricing; risk is handled via replication.  
- **Completeness:** If the market is complete (e.g., BSM), replication is unique ⇒ a unique $\mathbb{Q}$. In incomplete markets (jumps, stoch-vol), additional criteria (e.g., minimal martingale measure) pick a $\mathbb{Q}$.  
- **Numeraire:** Pricing invariance across numeraires (bank account, $T$-bond, annuity) leads to forward measures simplifying some products (e.g., caplets).

## 4) BSM PDE (Derivation)

**Short Answer**  
Delta-hedge $V(S,t)$ to eliminate diffusion; the residual riskless portfolio must earn $r$ ⇒
$$
V_t+\tfrac12\sigma^2 S^2 V_{SS}+rS V_S-rV=0.
$$

**Example**  
For a call with $V(T,S)=\max(S-K,0)$, solving the PDE yields the Black–Scholes formula.

**Detailed Explanation**  

- **Itô’s Lemma:** $dV=V_t dt+V_S dS+\tfrac12 V_{SS}(dS)^2$. With $dS=\mu S dt+\sigma S dW$.  
- **Hedge:** Take $\Delta=V_S$, portfolio $\Pi=V-\Delta S$ eliminates $dW$.  
- **No-arb:** $d\Pi=r\Pi dt$ ⇒ PDE above with appropriate boundary (terminal payoff), and conditions at $S\to 0,\infty$.  
- **Dividends:** With continuous yield $q$, PDE becomes $V_t+\tfrac12\sigma^2 S^2 V_{SS}+(r-q)S V_S-rV=0$.

## 5) Meaning of $N(d_1)$ and $N(d_2)$

**Short Answer**  
$N(d_2)$ ≈ risk-neutral probability of finishing ITM; $N(d_1)$ relates to delta/expected exercise under $\mathbb{Q}$.

**Example**  
Call: $C=S_0 e^{-qT}N(d_1)-K e^{-rT}N(d_2)$. If $N(d_2)=0.60$, there’s a 60% $\mathbb{Q}$-chance of $S_T>K$.

**Detailed Explanation**  

- **Term 1:** $S_0 e^{-qT}N(d_1)$ = PV of expected asset delivered at exercise (adjusted for $q$).  
- **Term 2:** $K e^{-rT}N(d_2)$ = PV of exercise price paid, weighted by exercise probability.  
- **Delta:** $\Delta_{call}=e^{-qT}N(d_1)$, connecting $N(d_1)$ to hedging ratio.

## 6) Volatility’s Impact

**Short Answer**  
Higher $\sigma$ raises option value due to convexity (Jensen’s inequality).

**Example**  
ATM call $S_0=K=100$, $T=1$, $r=q=0$: $C(\sigma=10\%)\approx 3.99$ vs $C(\sigma=30\%)\approx 11.92$ (BSM).

**Detailed Explanation**  

- **Convex Payoff:** Upside unbounded, downside floored at 0 ⇒ dispersion benefits long options.  
- **Vega:** $\nu=S_0 e^{-qT}\phi(d_1)\sqrt{T}>0$. Peaks near ATM and for longer $T$.  
- **Skews:** Market smiles imply state-dependent effective volatility, making sensitivity path-dependent in practice.

## 7) Delta Hedging

**Short Answer**  
Hold $\Delta=\partial V/\partial S$ shares against an option to neutralize small $S$ moves.

**Example**  
Short 100 calls with $\Delta=0.55$ ⇒ buy 55 shares to be delta-neutral initially; rebalance as $\Delta$ changes.

**Detailed Explanation**  

- **Gamma–Theta:** Frequent rebalancing needed if $\Gamma$ large; long gamma gains from realized variance but pays theta (time decay).  
- **Discrete Hedging Error:** Hedging discretely produces residual P&L $\approx \tfrac12\Gamma (\Delta S)^2-\Theta \Delta t$ plus transaction costs.  
- **Smile Dynamics:** “Sticky-delta” vs “sticky-strike” conventions materially affect hedge slippage.

## 8) Put–Call Parity

**Short Answer**  
$C-P=S_0 e^{-qT}-K e^{-rT}$ for European options with same $(K,T)$.

**Example**  
$S_0=100$, $r=5\%$, $q=2\%$, $T=1$. If $C=9.0$, parity implies $P=9.0-100e^{-0.02}+100e^{-0.05}\approx 6.4$.

**Detailed Explanation**  

- **Replication:** Long call + short put = synthetic forward $S_T-K$.  
- **Uses:** Build synthetics (e.g., covered call ↔ short put), detect data inconsistencies, infer missing quotes.  
- **Edge Cases:** Early-exercise (American) parity becomes an inequality; discrete dividends must be PV-adjusted.

## 9) Volatility Smile/Skew

**Short Answer**  
Implied vol varies with strike/maturity due to non-Gaussian returns and supply/demand.

**Example**  
Equities: OTM puts rich (downward skew); FX: more symmetric smiles with risk-reversal asymmetry.

**Detailed Explanation**  

- **Drivers:** Leverage effect ($\rho_{S,\sigma}<0$), crash risk premia, hedging pressure, jumps/stoch-vol.  
- **Modeling:** SVI per maturity, SABR/Heston dynamics, local vol for exact fit vs. dynamics realism trade-off.  
- **Arb-free:** Enforce butterfly (convexity in $K$) and calendar (monotonic in $T$) constraints.

## 10) Vega

**Short Answer**  
Sensitivity to volatility: $\nu=S_0 e^{-qT}\phi(d_1)\sqrt{T}$.

**Example**  
$S_0=K=100$, $T=1$, $r=q=0$, $\sigma=20\%$ ⇒ $\nu\approx 39.9$ per unit vol (i.e., 0.399 per 1% vol point).

**Detailed Explanation**  

- **Term Structure:** Per-maturity vega buckets; vega not fungible across $T$.  
- **Smile:** Skew vega (dV/d skew) and curvature vega (vomma) matter for surface moves.  
- **Hedging:** Use options near ATM and close $T$ to neutralize efficiently.

## 11) Gamma

**Short Answer**  
Curvature w.r.t. $S$: $\Gamma=e^{-qT}\phi(d_1)/(S_0\sigma\sqrt{T})$.

**Example**  
Near-ATM, short-dated options have large $\Gamma$ (sensitive delta).

**Detailed Explanation**  

- **Risk/Reward:** Long gamma benefits from realized volatility; short gamma earns theta but is exposed to large moves.  
- **Inventory:** Market makers run gamma targets and rebalance based on liquidity/vol.

## 12) Theta

**Short Answer**  
Time decay: typically negative for long options, positive for short.

**Example**  
Short-dated ATM options can lose value rapidly into expiry (theta acceleration).

**Detailed Explanation**  

- **Components:** “Carry” from discounting and from expected drift under $\mathbb{Q}$; discrete dividends can flip signs around ex-dates.  
- **Trade Design:** Structures like calendars exploit theta/vega interplay.

## 13) Cost-of-Carry Forward Pricing

**Short Answer**  
$F_0=S_0 e^{(r-q+c-\delta)T}$ with storage cost $c$ and convenience yield $\delta$.

**Example**  
Gold with $r=4\%$, storage $c=1\%$, $\delta=0$ ⇒ $F_0=S_0 e^{0.05T}$.

**Detailed Explanation**  

- **FX:** $F_0=S_0 e^{(r_d-r_f)T}$.  
- **Commodities:** Scarcity $\Rightarrow \delta>0$ (backwardation).  
- **Curve:** Forward curve encodes expectations + risk premia + inventory/flow constraints.

## 14) Futures Convexity Adjustment

**Short Answer**  
With stochastic rates, futures ≠ forwards due to daily settlement.

**Example**  
Eurodollar futures convexity vs FRA often approximated by $\tfrac12\sigma_r^2 T_1 T_2$ (order-of-magnitude guidance).

**Detailed Explanation**  

- **Mechanism:** Covariance of daily gains with discounting shifts fair futures price.  
- **Sign:** If underlying positively co-moves with rates, long futures benefit ⇒ futures > forward.

## 15) Greeks of Digital Options

**Short Answer**  
Extremely sharp near strike: large gamma/vega, unstable delta.

**Example**  
Cash-or-nothing call price $= e^{-rT}N(d_2)$; $\Delta= e^{-rT}\phi(d_2)/(S_0\sigma\sqrt{T})$.

**Detailed Explanation**  

- **Hedging:** Use tight call spreads to approximate a digital and smooth greeks.  
- **Risk:** Jump/announcement risk is acute due to step payoff.

## 16) Asian Options

**Short Answer**  
Payoff depends on average; lower variance ⇒ cheaper than vanilla.

**Example**  
Arithmetic Asian call: $(\bar S - K)^+$ with $\bar S=\frac1n\sum S_{t_i}$.

**Detailed Explanation**  

- **Pricing:** Geometric Asians have closed forms; arithmetic often via MC or analytic approximations (Turnbull–Wakeman).  
- **Greeks:** Pathwise estimators preferred; bridge corrections reduce bias.

## 17) Barrier Options

**Short Answer**  
Activation/extinction based on path crossing; many closed forms via reflection.

**Example**  
Down-and-out call = vanilla call − down-and-in call.

**Detailed Explanation**  

- **Monitoring:** Continuous vs discrete matters (discrete cheaper knock-out); Brownian bridge improves MC accuracy.  
- **Greeks:** Discontinuous near barrier (kinks); hedging requires careful sizing and possibly semi-static portfolios.

## 18) Stochastic Volatility (Heston)

**Short Answer**  
Volatility follows a mean-reverting square-root process; semi-closed forms via characteristic functions.

**Example**  
$dv=\kappa(\theta-v)dt+\eta\sqrt{v}\,dW^v$, $d\langle W^S,W^v\rangle=\rho\,dt$.

**Detailed Explanation**  

- **Calibration:** Fit to smile surface across $K,T$ by minimizing price or IV errors.  
- **Dynamics:** Negative $\rho$ creates equity-type skew; mean-reversion sets term structure.  
- **Greeks:** Additional vanna, volga exposures; hedging needs both underlyings and volatility instruments.

## 19) SABR

**Short Answer**  
Rates/FX model producing analytic IV approximations with parameters controlling level ($\alpha$), skew ($\rho$), and curvature ($\nu$); $\beta$ sets log-normal vs normal.

**Example**  
FX often uses $\beta\approx 1$; rates sometimes $\beta<1$ for low-rate environments.

**Detailed Explanation**  

- **Hagan Formula:** Widely used closed-form IV; care with extreme $K,F$ and very short $T$.  
- **Calibration:** ATM volatility pins $\alpha$; risk-reversal pins $\rho$; butterfly pins $\nu$.

## 20) Local Volatility (Dupire)

**Short Answer**  
Deterministic $\sigma_{loc}(t,S)$ reproducing the entire vanilla surface exactly.

**Example**  
Dupire formula:
$$
\sigma_{loc}^2(t,K)=\frac{\partial_T C + qC - rK\partial_K C}{\tfrac12 K^2 \partial_{KK} C}\Big|_{T=t}.
$$

**Detailed Explanation**  

- **Use:** Good for barrier/exotics when exact vanilla fit is mandated.  
- **Limit:** Unrealistic dynamics (sticky-strike), may mis-hedge under surface moves; numerically sensitive to noisy $\partial_{KK} C$.

## 21) Monte Carlo vs PDE

**Short Answer**  
MC handles high-dimensional/path-dependent payoffs; PDE efficient in low dimensions and for early exercise.

**Example**  
American put via finite-difference (PDE with free boundary) vs Bermudan via LSMC.

**Detailed Explanation**  

- **MC:** Error $\mathcal{O}(1/\sqrt{M})$; QMC lowers effective variance; Greeks via pathwise/LR estimators.  
- **PDE:** Fast & accurate in 1–2D with well-posed boundaries; tricky beyond 2D or with complex path terms.

## 22) Gamma–Theta Tradeoff

**Short Answer**  
Long gamma benefits from movement but pays theta; short gamma earns theta but is hurt by movement.

**Example**  
Long straddle: positive gamma/vega, negative theta; P&L thrives on realized vol exceeding implied.

**Detailed Explanation**  

- **P&L Attribution:** $\Delta \text{P\&L}\approx \Delta\,\Delta S+\tfrac12\Gamma(\Delta S)^2+\nu\,\Delta\sigma+\Theta\,\Delta t$.  
- **Strategy:** Market makers run near-neutral delta and target gamma/theta depending on vol views.

## 23) Forward-Start Options

**Short Answer**  
Strike set at future date; prices depend on time to maturity after start.

**Example**  
At $t_1$, strike $K=S_{t_1}$; payoff at $T$: $(S_T-S_{t_1})^+$.

**Detailed Explanation**  

- **Valuation:** Under BSM, reduces to vanilla with maturity $T-t_1$ and ATM at $t_1$.  
- **Use:** Equity comp, forward vol trades; greeks tied to forward measure over $[t_1,T]$.

## 24) Variance Swaps

**Short Answer**  
Exchange realized variance for fixed variance strike; priced via strip of OTM options.

**Example**  
Payoff $= N\left(\sigma_{\text{real}}^2 - K_{\text{var}}\right)$ with realized variance from high-frequency returns.

**Detailed Explanation**  

- **Replication:** $K_{\text{var}}=\dfrac{2 e^{rT}}{T}\int_0^\infty \frac{P(K)-C(K)}{K^2}\,dK$ (OTM strip).  
- **Risks:** Vol-of-vol, jumps, discretization. Corridors and gamma swaps extend concept.

## 25) Portfolio Greeks

**Short Answer**  
Aggregate by summation across positions (linearity).

**Example**  
$\Delta_{book}=\sum_i \Delta_i Q_i$, $\nu_{book}=\sum_i \nu_i Q_i$.

**Detailed Explanation**  

- **Hierarchy:** Position → strategy → book; limits set per Greek and scenario.  
- **Surface Risk:** Include $\partial\sigma/\partial K$ and $\partial\sigma/\partial T$ (skew/term risk).  
- **Stress:** Nonlinear interactions under jumps/liquidity shocks require scenario P&L beyond first/second order.
