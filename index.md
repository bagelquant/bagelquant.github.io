---
layout: home_page
aliases: BagelQuant
author: "Eric Huang"
excerpt: "Your go-to spot for all things quirky and quant!"
header:
  overlay_image: /assets/images/header.png
  actions:
    - label: "About me"
      url: "https://bagelquant.github.io/about-me/"
--- 

BagelQuant is a personal research blog focused on systematic equity investing.

The name comes from Bagel — my Shiba Inu — combined with quantitative research.

This blog is a long-term research notebook for studying how modern quantitative investment systems are designed, researched, and implemented in practice: from alpha generation to portfolio construction, execution, and research infrastructure.

Systematic equity portfolio management can generally be viewed as five core components:

- An **alpha model** that forecasts expected returns
- A **portfolio construction process** that converts forecasts into portfolio weights and positions
- A **risk model** that estimates covariance structure and portfolio exposures
- An **execution and implementation layer** that accounts for transaction costs, liquidity, market impact, and operational constraints
- A **research and production platform** that supports data, infrastructure, backtesting, deployment, and monitoring

Together, the first four components form the core investment process of a quantitative hedge fund.

A simplified but representative workflow may look like this:

![Systematic equity portfolio management workflow](/assets/images/systematic-equity-portfolio-management-workflow.png)

For example, a simple market-neutral strategy may:

- Long the top 100 stocks with the highest predicted returns
- Short the bottom 100 stocks with the lowest predicted returns
- Apply risk constraints to maintain neutrality and diversification
- Rebalance periodically based on updated forecasts

BagelQuant explores these topics in depth — including the mathematics, statistics, machine learning, optimization, and engineering required to build real-world quantitative equity investment systems.

The goal is to serve as a practical and research-oriented hub for learning quantitative equity investing.

See all coverage in the [Topics page](_pages/topics.md). 
