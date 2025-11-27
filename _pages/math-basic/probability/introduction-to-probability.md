---
title: "Introduction to Probability: Quantifying Uncertainty"
permalink: /probability/introduction-to-probability/
header:
  overlay_image: /assets/images/headers/probability.png
  overlay_opacity: 0.8
nav: "probability"
---

Imagine you are looking at a price chart late at night.

You have tomorrow's positions on the screen. You know your current P&L. What you do **not** know is what the market will decide to do next. Will the index gap up? Will a single name blow through your stop? Will nothing interesting happen at all?

In calculus, you learned to describe how things change *if* you already know the function. In linear algebra, you learned how to organize and manipulate many variables at once. Both are languages for what is already determined. **Probability** is the third pillar: it is the language we use when the future is not fixed, only *possible*.

In finance, almost everything that matters lives in this gray area:

- Future prices and returns
- Interest rates and inflation
- Default events and credit spreads
- Volatility, liquidity, and order-book dynamics

Probability will not tell you exactly what *will* happen tomorrow. Instead, it will teach you how to describe what *could* happen, how likely each scenario is, and how to make decisions that respect that uncertainty. That is the mathematical core of risk, pricing, and portfolio construction.

## What Is Probability?

Before we write down any formulas, it is worth slowing down and asking: what are we actually trying to quantify?

Informally, probability assigns a number between 0 and 1 to how likely an event is:

- 0 means the event is impossible under our model
- 1 means the event is certain
- Values in between represent degrees of belief or long-run frequencies

More formally (which we will build up to in this course), probability is a function defined on a collection of events that satisfies a small set of axioms (rules). From these axioms, we can derive all the familiar rules of probability: addition, multiplication, conditional probability, Bayes' theorem, and more.

For now, think of probability as a consistent way to assign and manipulate "likelihoods" so that our reasoning about uncertainty does not lead to contradictions.

## Why Probability Is Essential for Quantitative Finance

It is hard to find any serious quantitative work that does **not** lean on probability somewhere. A few examples make this clearer.

1.  **Modeling Returns:** Asset returns are random variables. Probability describes their distributions, tails, and dependence structures.
2.  **Risk Measurement:** Quantities like Value-at-Risk (VaR) and Expected Shortfall (ES) are defined in terms of the distribution of portfolio losses.
3.  **Derivative Pricing:** Pricing an option is equivalent to computing an expected discounted payoff under a suitable probability measure.
4.  **Portfolio Construction:** Diversification, covariance, and correlation are probabilistic concepts that quantify how assets move together.
5.  **Statistical Inference and Machine Learning:** Estimation, hypothesis testing, and predictive modeling are built on probabilistic models of data generation.

As you read the rest of this series, keep these questions in the back of your mind. When we introduce a new definition, try to translate it immediately into "What does this mean for returns, risk, or pricing?" That habit will make the theory much easier to remember.

## Two Viewpoints on Probability

There are two broad ways to interpret probability. Both show up in finance desks and research notes, often without being named.

1.  **Frequentist View (Long-Run Frequency):**

    Probability is the long-run relative frequency of an event when an experiment is repeated many times under the same conditions.

    - Example: The probability that a fair coin lands heads is 0.5 because, in a long series of tosses, about half of them will be heads.
    - Finance analogy: If we say the probability of a daily loss worse than −2% is 5%, we mean that, over a long period under similar market conditions, about 5% of days will see a loss worse than −2%.

2.  **Bayesian View (Degree of Belief):**

    Probability quantifies a rational agent's degree of belief about uncertain events, given their information.

    - Example: Before earnings are released, an analyst might assign a 70% probability that a company will "beat" expectations.
    - Finance analogy: Implied probabilities derived from option prices represent *market beliefs* about future price moves under risk-neutral measures.

Most working quants quietly blend both views: they estimate probabilities from data (frequentist), but they also shift and tilt these estimates as new information arrives, new models are tried, or new market regimes are suspected (Bayesian).

## Experiments, Outcomes, and Events

To talk precisely about probability, we need to pin down the objects we are playing with. At first glance this seems pedantic, but once you start building real models, it helps to be very clear about what is random and what is not.

1.  **Experiment:** A process whose outcome is uncertain but well defined.
    - Examples: Tossing a coin; observing tomorrow's stock return; checking whether a bond defaults within a year.

2.  **Outcome:** A single possible result of the experiment.
    - Coin toss: `H` or `T`
    - Daily stock return: a real number, e.g., `0.8%` or `−1.3%`

3.  **Event:** A collection (set) of outcomes that share a property we care about.
    - "The stock has a negative return tomorrow"
    - "Portfolio loss exceeds 5% in a day"
    - "The option expires in the money"

In the next article, we will take these ingredients and package them into a formal object called a **probability space**. This sounds abstract, but it is just a tidy way of saying: here is the universe of outcomes we are willing to consider, here are the events we care about, and here is how we assign likelihoods to them.

## Deterministic vs. Random Models

In calculus and linear algebra, many examples are **deterministic**: given inputs, the output is fixed.

- Example: If a function is `f(x) = 2x + 1`, then `f(3)` is always `7`.

In probability, key quantities are **random variables**: functions from outcomes to numbers. A random variable does not have a single fixed value ahead of time; instead, it has a *distribution*.

- Example: Let `R` be tomorrow's return of a stock. We do not know the actual value of `R` today, but we may have a model for its distribution (mean, variance, tails, etc.).

This shift—from fixed numbers to distributions—is one of the most important conceptual changes when you move into probability. Instead of asking "What is the value?" you start asking "What is the *distribution* of possible values, and what does that imply for my decisions?"

## How This Course Is Structured

This probability course is organized to be parallel and complementary to the calculus and linear algebra series, but the pacing is intentionally slower and more conversational.

- We begin with **foundations**: probability spaces, events, and axioms.
- We then introduce **random variables and distributions**, both discrete and continuous.
- Next we study **core distributions** that appear everywhere in finance: normal, lognormal, Bernoulli, binomial, Poisson, and heavy-tailed models.
- We develop tools for working with **sequences of random variables**: laws of large numbers and central limit theorems.
- We extend everything to **multivariate settings** and dependence, which is crucial for portfolios.
- Finally, we build **probability tools** that you will see again in stochastic calculus, econometrics, and risk modeling.

In each article, you will first see an informal story or picture, then the clean definition, and only after that some finance-flavored examples. When the notation risks becoming heavy, we will step back and ask, "What is the picture in my head here?"

## Prerequisites and How to Use This Series

To get the most from this course, you should be reasonably comfortable with:

- Basic calculus (derivatives, integrals, and limits)
- Basic linear algebra (vectors, matrices, and matrix multiplication)

If these topics feel rusty, you may want to review:

- [Calculus: A Comprehensive Course](/calculus/)
- [Linear Algebra](/linear-algebra/)

You do **not** need prior exposure to probability. If you have ever looked at a backtest and asked "Is this result meaningful, or just noise?", you already have the right motivation.

In the next article, we will slow down and put names on the building blocks we have been hinting at: **sample spaces, events, and axioms**. Once those are in place, all the familiar rules of probability will fall out almost mechanically.

Next Topic: [Probability Spaces, Events, and Axioms](probability-spaces-and-events.md)
