---
title: "Quant Interview FAQ — Stochastic Calculus"
permalink: /quant-interview-faq-stochastic-calculus/
excerpt: "A cheat sheet of common stochastic calculus concepts and formulas for quant interviews."
layout: post
header:
  overlay_image: /assets/images/headers/stochastic-calculus-faq-header.png
  overlay_filter: 0.8
---

This page follows the same structure as the [derivatives FAQ](https://bagelquant.com/quant-interview-faq-derivatives/): each question has a **Short Answer**, a concrete **Example**, and a **Detailed Explanation** with formulas, edge cases, and practical caveats.

## 1) Brownian Motion / Wiener Process

Short Answer

A continuous-time stochastic process with stationary independent Gaussian increments, continuous paths, zero mean and variance proportional to time: for $W_t, W_0 = 0$, $W_t - W_s \sim \mathcal{N}(0, t-s)$.

Example

If $W_t$ is a Brownian motion, then over 1 day ($t=1/252$), the increment $W_{t+1/252}-W_t$ is approximately $\mathcal{N}(0, 1/252)$.

Detailed Explanation

- Definitions: almost surely continuous paths, independent increments, Gaussian increments, and $W_0=0$. Scaling: $W_{ct}$ has law $\sqrt{c} W_t$.
- Construction: limit of random walk (Donsker’s theorem) or via Karhunen–Loève expansion.
- Caveats: Brownian paths are nowhere differentiable and have infinite variation on any interval; quadratic variation over $[0,T]$ equals $T$.

## 2) Quadratic Variation

Short Answer

Quadratic variation $[W]_T$ of Brownian motion over $[0,T]$ equals $T$; for a continuous semimartingale $X$, pathwise limit of sum of squared increments.

Example

Partition $[0,T]$ into $n$ equal subintervals; sum $(W_{t_{i+1}}-W_{t_i})^2 \to T$ as $n\to\infty$.

Detailed Explanation

- Importance: justifies Itô calculus; Itô integral uses quadratic variation term.
- For finite-variation processes the quadratic variation is 0; for diffusions it's positive.
- In practice, realized variance estimators estimate quadratic variation from high-frequency returns, with microstructure noise caveats.

## 3) Itô’s Lemma

Short Answer

Stochastic chain rule: for $X_t$ an Itô process and $f(t,x)$ twice differentiable,
$$
df(t,X_t)=\left(f_t+\mu f_x+\tfrac12\sigma^2 f_{xx}\right)dt+\sigma f_x dW_t.
$$

Example

If $X_t = S_t$ follows $dS = \mu S dt + \sigma S dW$, and $f(S)=\ln S$, then

$$
 d\ln S=(\mu-\tfrac12\sigma^2)dt+\sigma dW.
$$

Detailed Explanation

- Derivation via Taylor expansion keeping up to second-order $dW^2=dt$ term and dropping higher-order terms.
- Contrasts with Stratonovich calculus where the chain rule looks like ordinary calculus; conversion: $dX\circ dW = dX dW + \tfrac12 d\langle X,W\rangle$.
- Use cases: derive Black–Scholes dynamics for log-price, change variables, compute SDEs of functions of processes.

## 4) Itô vs Stratonovich

Short Answer

Itô integral uses nonanticipative integrands (martingale-friendly) and has extra drift (1/2) term in chain rule; Stratonovich obeys ordinary calculus and is convenient for change of variables in physics.

Example

For SDE $dX=a(X)dt+b(X)dW$, the Stratonovich form $dX = A dt + b(X) \circ dW$ relates via $A=a+\tfrac12 b b'$.

Detailed Explanation

- The conversion formula: $a_{Itô}=a_{Strat}+\tfrac12 b b'$ (where derivative is wrt state variable).
- When modeling from physical considerations (limits of smooth noise), Stratonovich is natural; for probabilistic pricing and martingale measures, Itô is standard.
- Numerics: Euler–Maruyama approximates Itô; the midpoint (Stratonovich) scheme converges to Stratonovich.

## 5) Stochastic Integrals (Itô integral)

Short Answer

Integral $\int_0^T H_s dW_s$ defined as mean-square limit of nonanticipative Riemann sums; martingale with variance $\mathbb{E}[\int_0^T H_s^2 ds]$.
Example

If $H_s = 1_{s\le\tau}$ (stopping time), $\int_0^T H_s dW_s = W_{T\wedge\tau}$.

Detailed Explanation

- Construction: approximate by simple predictable processes; isometry: $\mathbb{E}[(\int_0^T H dW)^2]=\mathbb{E}[\int_0^T H^2 ds]$.
- Conditions: H must be predictable and square-integrable. Pathwise interpretations exist (Föllmer) but require different frameworks.
- Use in finance: martingale representation theorem says local martingales can be written as stochastic integrals under completeness assumptions.

## 6) SDE Existence & Uniqueness

Short Answer

 Lipschitz drift and diffusion in the state variable guarantee strong existence and uniqueness for SDE solutions; weaker conditions yield weak solutions.

$$
df(t,X_t)=\left(f_t+\mu f_x+\tfrac12\sigma^2 f_{xx}\right)dt+\sigma f_x\,dW_t.
$$

Example

For $dX = \mu(X) dt + \sigma(X) dW$ with Lipschitz $\mu,\sigma$, there exists a unique strong solution. For geometric Brownian motion $dS = \mu S dt + \sigma S dW$, solution is $S_t = S_0 \exp((\mu - \tfrac12 \sigma^2)t + \sigma W_t)$. For $f(S)=\ln S$,

$$
d\ln S=(\mu-\tfrac12\sigma^2)\,dt+\sigma\,dW.
$$
Detailed Explanation

- Picard iterations give existence/uniqueness under global Lipschitz and linear growth. For CIR (square-root) process, Feller conditions ensure positivity and uniqueness despite non-Lipschitz at 0.
- Strong vs weak solutions: strong = adapted to given Brownian motion, weak = existence of probability space and Brownian motion; Girsanov change-of-measure can convert between laws.

## 7) Girsanov’s Theorem

Short Answer

Change of measure that shifts Brownian drift: under Radon–Nikodym density $Z_T = \exp(\int_0^T \theta_s dW_s - \frac12\int_0^T \theta_s^2 ds)$, process $W^Q_t = W_t - \int_0^t \theta_s ds$ is a Brownian motion under Q.

Example

Risk-neutral pricing: change from real-world measure P with drift $\mu$ to $Q$ with drift $r-q$ by choosing $\theta=(\mu-(r-q))/\sigma$ for geometric Brownian motion.

Detailed Explanation

- Novikov/Kazamaki conditions ensure Z is a martingale. If they fail, the candidate density may be a strict local martingale, causing measure-change problems.
- Applications: pricing, risk premia identification, and filtering/measure transforms in stochastic control.

## 8) Martingales & Local Martingales

Short Answer

Martingale: $E[X_t|F_s]=X_s$ for $t\ge s$; local martingale: martingale property holds up to stopping times. Not every local martingale is a martingale.

Example

Exponential local martingale $M_t=\exp(\sigma W_t - 0.5\sigma^2 t)$ is a martingale; but some strict local martingales (e.g., certain Bessel processes) have $E[M_t]<M_0$.

Detailed Explanation

- Distinctions matter: pricing via a candidate density that is only a local martingale can produce bubbles and asset price anomalies.
- Uniform integrability is a common sufficient condition to promote local martingales to martingales.

## 9) Risk-Neutral Measure & Martingale Representation

Short Answer

Under the risk-neutral measure $Q$, discounted asset prices are martingales; martingale representation says every square-integrable martingale is an Ito integral w.r.t. the driving Brownian motion (in a complete Brownian filtration).

Example

In Black–Scholes, discounted stock price $S_t e^{-rt}$ is a martingale under $Q$ and any derivative price process is a conditional expectation of its payoff.

Detailed Explanation

- Martingale representation underpins replication: the integrand gives the hedging strategy (delta is the integrand for option replication).
- In incomplete markets (extra sources of risk), the representation may require multiple Brownian motions or incomplete spanning.

## 10) Fokker–Planck / Kolmogorov Forward Equation

Short Answer

Describes time evolution of transition density $p(t,x)$ of an SDE: $\partial_t p = -\partial_x(\mu p) + \tfrac12 \partial_{xx}(\sigma^2 p).

Example

For GBM in log-space, the log-price density evolves as a normal distribution with drift $(\mu-\tfrac12\sigma^2)$ and variance $\sigma^2 t$.

$$
Z_T=\exp\Bigl(\int_0^T\theta_s\,dW_s-\tfrac12\int_0^T\theta_s^2\,ds\Bigr).
$$

Detailed Explanation

- It’s the PDE dual to the backward Kolmogorov (pricing) PDE. Useful for density forecasting, likelihood-based calibration, and filtering.
- Numerical challenges: boundary conditions and absorbing/reflecting barriers must be specified carefully.

## 11) Backward Kolmogorov / Feynman–Kac

Short Answer

Feynman–Kac links linear parabolic PDEs to expectations of SDEs: solution $u(x,t)=\mathbb{E}^{x,t}[e^{-\int_t^T r(s,X_s) ds} g(X_T)]$.

Example

Black–Scholes PDE solution for option price is expectation of discounted payoff under risk-neutral GBM.

Detailed Explanation

- Use: derive pricing PDEs and represent solutions as risk-neutral expectations; forms the theoretical basis for Monte Carlo pricing.
- Requires sufficient regularity of coefficients; for payoffs with low regularity, weak solutions or viscosity solutions may be used.

## 12) Numerical Schemes: Euler–Maruyama & Milstein

Short Answer

Euler–Maruyama: basic time-discretization for SDEs (strong order 0.5); Milstein adds derivative term to achieve strong order 1 when diffusion is state-dependent.

Example

Euler step for $dX=\mu(X)dt+\sigma(X)dW$: $X_{n+1}=X_n+\mu(X_n)\Delta t+\sigma(X_n)\Delta W$.

Detailed Explanation

- Order: strong vs weak convergence. For option pricing (expectations) weak order is relevant; for path-dependent Greeks, strong order matters.
- For SDEs with non-Lipschitz coefficients (e.g., CIR), implicit schemes or specialized positivity-preserving methods are preferred.

## 13) Stopping Times & Optional Sampling

Short Answer

A stopping time is a random time $T$ where $\{T\le t\}$ is $\mathcal{F}_t$-measurable; optional sampling theorem gives conditions under which $\mathbb{E}[M_T]=\mathbb{E}[M_0]$ for a martingale $M$.

Example

Hitting time of a barrier for Brownian motion is a stopping time; optional sampling applied to bounded stopped martingales preserves expectation.

Detailed Explanation

- OST conditions: integrability and boundedness or uniformly integrable martingales; naive application can fail leading to paradoxes.

$$
\partial_t p=-\partial_x(\mu p)+\tfrac12\partial_{xx}(\sigma^2 p).
$$

- Use in finance: pricing barrier options and proving optional decomposition for American claims.

## 14) Local Time

Short Answer

Local time $L_t^a$ measures how much time a semimartingale spends at level $a$; appears in Tanaka’s formula.

Example

For Brownian motion, $L_t^0$ is the density of occupation near 0 and appears when decomposing $|W_t|$.

Detailed Explanation

- Tanaka: $|X_t-a| = |X_0-a| + \int_0^t \text{sgn}(X_s-a) dX_s + L_t^a$.
- Local time is nondecreasing in $t$ and increases only when $X_t=a$. Numerically, occupation densities approximate local time.

$$
u(x,t)=\mathbb{E}^{x,t}\bigl[e^{-\int_t^T r(s,X_s)\,ds}\,g(X_T)\bigr].
$$

## 15) Tanaka’s Formula

Short Answer

A generalisation of Ito’s lemma for convex (nonsmooth) functions like absolute value, including local time term.

Example

For $f(x)=|x|$, Tanaka gives decomposition with local time at 0.

Detailed Explanation

- A continuous-time stochastic process with stationary independent Gaussian increments, continuous paths, zero mean and variance proportional to time: for $W_t$, $W_0=0$, and $W_t-W_s\sim\mathcal{N}(0,t-s)$.
- Useful for reflecting boundaries and deriving properties of hitting times. Shows how non-differentiable payoffs introduce local-time terms in SDE transforms.

## 16) Martingale Problems (Stroock–Varadhan)

Short Answer

$$X_{n+1}=X_n+\mu(X_n)\Delta t+\sigma(X_n)\Delta W.$$

Characterise diffusion processes by their generator: existence/uniqueness of solutions to martingale problem equivalent to weak uniqueness of SDE.

Example

Given generator $L=(1/2)\sigma^2(x)\partial_{xx}+\mu(x)\partial_x$, solving martingale problem constructs process with those local characteristics.

Detailed Explanation

Quadratic variation $[W]_T$ of Brownian motion over $[0,T]$ equals $T$; for a continuous semimartingale $X$ it's the pathwise limit of sums of squared increments.

## 17) Jump Processes & Lévy Itô Decomposition

Short Answer

General semimartingales include jump terms; Lévy–Itô decomposition represents a Lévy process as drift + Brownian part + compensated Poisson integral for jumps.

Example

Poisson-driven jump-diffusion: $dX = \mu dt + \sigma dW + J dN_t$ with jump sizes $J$ and intensity of $N_t$.

Detailed Explanation

- Pricing: jumps break completeness; risk-neutral measure selection and option pricing need jump compensator adjustments.
- Numerics: simulate jumps with thinning or exact jump-time simulation; small-jump approximations (diffusion limits) sometimes used.

## 18) Change of Numeraire

Short Answer

> Change measure using a positive tradable as numeraire; asset prices expressed in units of numeraire become martingales under new measure.

Example

Forward measure: use a T-bond as numeraire to price forward-start or bond options; simplifies caplet pricing.

Detailed Explanation

- Radon–Nikodym derivative involves the ratio of numeraires discounted; martingale property shifts accordingly and drift terms adjust.

## 19) Malliavin Calculus (brief)

Short Answer

A probabilistic calculus of variations on Wiener space; provides integration-by-parts to compute Greeks with lower variance estimators.

Example

Use Malliavin weights to produce unbiased delta estimators for path-dependent payoffs in Monte Carlo.
Itô integral uses nonanticipative integrands (martingale-friendly) and has an extra drift $$\tfrac12$$ term in the chain rule; Stratonovich obeys ordinary calculus and is convenient for physical limits.
Detailed Explanation

- Advanced topic: requires smoothness on Wiener space; practical use in Monte Carlo Greeks (likelihood ratio vs pathwise vs Malliavin). Introduces Skorokhod integral (anticipating integrand).

## 20) Practical Caveats for Quant Work

Short Answer

Continuous-time theory is an idealisation; market data is discrete, has microstructure noise, jumps, and model risk. Be careful with calibration and hedging assumptions.

Example

Discrete hedging yields P&L different from continuous-time replication; realized volatility estimation is biased by microstructure noise unless corrected.

Detailed Explanation
The integral $$\int_0^T H_s\,dW_s$$ is defined as a mean-square limit of nonanticipative Riemann sums; it's a martingale with variance $$\mathbb{E}[\int_0^T H_s^2\,ds]$$.

- Robust hedging: model misspecification (stochastic vol, jumps) makes perfect replication impossible; consider robust bounds, super-hedging, or calibration-consistent hedges.
- Numerics and data: choose discretization, account for bid–ask, incorporate jump-robust estimators, and stress-test hedges under scenario moves.

## References & Further Reading

- Karatzas & Shreve — Brownian Motion and Stochastic Calculus
- ksendal — Stochastic Differential Equations
- Shreve — Stochastic Calculus for Finance I & II
- Revuz & Yor — Continuous Martingales and Brownian Motion
