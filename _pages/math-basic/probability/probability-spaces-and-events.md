---
title: "Probability Spaces, Events, and Axioms"
permalink: /probability/probability-spaces-and-events/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

If the previous section was about getting a feel for what probability is trying to do, this one is about agreeing on the rules of the game. Traders can argue all day about whether a particular stock is "cheap" or "expensive", but if you ask them what it means to say "there is a 30% chance of a rate cut", they are all implicitly using the same mathematical machinery.

That machinery is wrapped up in the idea of a **probability space**.

## Sample Space, Events, and Sigma-Algebras (Intuition First)

Every probabilistic model, whether it is a simple coin-toss story or a multi-factor term structure model, starts with three ingredients:

1.  **Sample Space (Ω):** The set of all possible outcomes of an experiment.
2.  **Events (subsets of Ω):** Collections of outcomes we care about.
3.  **Probability Measure (P):** A function that assigns probabilities to events.

In more advanced probability texts, events are organized into a special collection called a **σ-algebra**. For this course, we will stay close to concrete events you can describe explicitly (intervals, finite sets, inequalities), and we will not dive into measure-theoretic details. But it is worth knowing, at least at a high level, what is going on behind the scenes.

### Sample Space Ω

The **sample space** Ω is simply the set of all outcomes that could possibly occur, according to your model.

- Coin toss: Ω = {H, T}
- Roll of a fair die: Ω = {1, 2, 3, 4, 5, 6}
- Tomorrow's stock return for a single stock: Ω = ℝ (all real numbers)
- Next year's return vector for a 3-asset portfolio: Ω = ℝ³

When we build a model, one of the first choices we make—often without saying it out loud—is: *What is Ω?* The richer the sample space, the more detail we can represent, but the more complex the analysis becomes. In practice you are always trading off realism against tractability.

### Events

An **event** is any collection (subset) of outcomes in Ω that we want to be able to talk about.

- "Stock has a positive return tomorrow": {ω ∈ Ω : return(ω) > 0}
- "Portfolio loss exceeds 5%": {ω ∈ Ω : loss(ω) > 0.05}
- "Option expires in the money": {ω ∈ Ω : S_T(ω) > K}

Events can be combined using set operations:

- **Complement:** "Not A" corresponds to Ω \ A
- **Union:** "A or B" corresponds to A ∪ B
- **Intersection:** "A and B" corresponds to A ∩ B

This set-based language will appear throughout probability, statistics, and measure-theoretic finance.

### Sigma-Algebras (High-Level Only)

A **σ-algebra** 𝓕 is a collection of subsets of Ω (possible events) that is closed under complements and countable unions, and contains Ω itself. The triple (Ω, 𝓕, P) is called a **probability space**.

For our purposes, you can think of 𝓕 as "the menu of events we are allowed to assign probabilities to." We will not construct σ-algebras by hand; we use them implicitly whenever we talk about events like intervals (−∞, x] for continuous variables.

## The Axioms of Probability

Probability is a function $P$ that takes in an event $A$ and spits out a number $P(A)$. To avoid paradoxes and Dutch-book situations, we insist that $P$ obey three basic axioms (Kolmogorov's axioms):

1.  **Non-negativity:** For any event A, P(A) ≥ 0.
2.  **Normalization:** P(Ω) = 1.
3.  **Countable Additivity:** If A₁, A₂, A₃, … are disjoint events (no overlap), then

    $$
    P\Big(\bigcup_{i=1}^{\infty} A_i\Big) = \sum_{i=1}^{\infty} P(A_i).
    $$

From these three rules alone, you can derive all the familiar probability identities you see in textbooks and risk reports:

- P(∅) = 0
- P(Aᶜ) = 1 − P(A)
- If A ⊆ B, then P(A) ≤ P(B)
- P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

These properties are not additional assumptions—they are consequences of the axioms.

## Finite and Countable Sample Spaces

For many introductory and discrete models, Ω is **finite** or **countable** (like the integers). This is the setting you implicitly use when you think in terms of "scenarios" with associated probabilities.

- Suppose Ω = {ω₁, …, ωₙ}.
- Assign probabilities pᵢ = P({ωᵢ}) ≥ 0 such that ∑ pᵢ = 1.
- For any event A ⊆ Ω, we have:

  $$
  P(A) = \sum_{\omega_i \in A} p_i.
  $$

**Example (Fair Die):** Ω = {1, 2, 3, 4, 5, 6}, pᵢ = 1/6 for all i.

- P({1, 2, 3}) = 3/6 = 1/2.
- P({even numbers}) = 3/6 = 1/2.

In finance, countable models appear naturally in:

- **Binomial trees** for stock prices
- **Discrete-time models** of states of the world
- **Scenario-based risk analysis** with a finite set of stress scenarios

## Continuous Sample Spaces and Densities (Preview)

When Ω is continuous (e.g., ℝ for returns), the picture changes. Individual points carry zero probability mass, and we cannot just list out outcomes with associated weights. Instead, we describe probability via a **probability density function (pdf)** or a **cumulative distribution function (cdf)**.

- For now, think of P((a, b]) as the probability that a random variable falls between a and b.
- We will return to continuous distributions in detail later in the course.

## Modeling Events in Finance

Let us connect these ideas directly to familiar quant problems so the notation starts to feel less abstract.

### Example 1: Daily Loss Exceeding a Threshold

Let Ω be all possible paths of market prices tomorrow. Define the event

- A = {ω ∈ Ω : portfolio loss L(ω) > 0.02}.

Then P(A) is the probability that your portfolio loses more than 2% in a day. Risk measures like **Value-at-Risk (VaR)** and **Expected Shortfall (ES)** are defined in terms of events like A and their probabilities.

### Example 2: Default Event of a Bond

Let Ω describe all possible states of the world over the life of a corporate bond. Define events:

- D = {bond defaults before maturity}
- N = {bond does not default}

We have D ∩ N = ∅ and D ∪ N = Ω, so P(D) + P(N) = 1. Credit models specify or estimate P(D), sometimes conditional on covariates like macro variables or firm leverage.

## Common Modeling Pitfalls

When you first start translating stories into probability spaces and events, a few mistakes show up often:

- **Forgetting that events are sets:** statements like "the event 0.03" do not make sense on their own. For a return variable $R$, you should write events like $\{R > 0.03\}$ or $\{R \in (0.02,0.05] \}$.

- **Double-counting in unions:** when combining events (e.g., "loss exceeds 2%" OR "volatility spikes"), you must subtract the intersection to avoid counting overlapping outcomes twice. The identity

  $$
  P(A \cup B) = P(A) + P(B) - P(A \cap B)
  $$

  is just the set picture written in probability language.

- **Inconsistent sample spaces:** if you change the story (for example, from one-day returns to full paths over a year), the sample space Ω changes too. Events must always be subsets of whatever Ω you have chosen for the model.

Keeping these in mind early makes it much easier to debug probabilistic arguments later, especially in complex multi-asset or multi-period settings.

## Set Identities and Probability Rules

Because events are sets, we can use set identities to derive probability formulas.

For any two events A and B:

- **Union:**
  $$
  P(A \cup B) = P(A) + P(B) - P(A \cap B).
  $$

- **Inclusion–Exclusion for Three Events:**
  $$
  P(A \cup B \cup C) = P(A) + P(B) + P(C)
  - P(A \cap B) - P(A \cap C) - P(B \cap C)
  + P(A \cap B \cap C).
  $$

These formulas are especially useful when modeling overlapping events (e.g., multiple types of risk triggers or simultaneous defaults).

## Summary

In this article, we:

- Introduced **sample spaces**, **events**, and (informally) **σ-algebras**
- Stated the **axioms of probability** and some key derived properties
- Distinguished between **finite/countable** and **continuous** sample spaces
- Connected events and probabilities to finance through risk and default examples

These foundations will support everything that comes next: conditional probability, random variables, distributions, and eventually stochastic processes.

In the next article, we will turn to **conditional probability and Bayes' theorem**—the formal way to say "given what I know now, how should I update the probabilities I assigned yesterday?"

Next Topic: [Conditional Probability and Bayes' Theorem](conditional-probability-and-bayes-theorem.md)
