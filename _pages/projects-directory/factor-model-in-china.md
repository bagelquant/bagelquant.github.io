---
title: "Factor Models Construction Process"
layout: page
permalink: /factor-model-in-china/
nav: "factor-model-in-china"
---

This project aims to build a **stock scoring and backtesting system** based on classical factor investing techniques. The goal is to start simple, generate interpretable results, and gradually expand into more sophisticated methods.

## Project Settings  

- **Universe**: All historical constituents of CSI 300, CSI 500, and CSI 1000.  
  - [Stock Universe Document](stock_universe.md)  
- **Date Range**: 2000-01-01 to 2025-12-31  
- **Frequency**: Monthly  
- **Data Source**: [Tushare](https://tushare.pro/) via [bagel-tushare](https://github.com/bagelquant/bagel-tushare) (local MySQL database)  
- **Strategy Type**: Long-only, holding top 20–50 stocks  

## Factor Library  

The initial factor set will cover standard categories (all oriented so that *higher = better*):  

- **Market**  
- **Size**  
- **Value**  
- **Momentum**  
- **Quality**  
- **Investment**  
- **Volume**  

A detailed factor dictionary (definitions, formulas, and data fields) will be maintained in a separate file.  

## Factor Evaluation  

Each factor will be tested individually using:  

- **Information Coefficient (IC)** > 0.05  
- **Rank IC** > 0.5  
- **Quantile Analysis**: IC across quantile portfolios  
- **Correlation Check**: pairwise correlation < 0.8 (to reduce redundancy)  

## Validation Methodology (Walk-Forward)  

To better mimic real-time investing, I will use **walk-forward validation** rather than a one-off split.  

1. **Timeline & windows**  
   - **Expanding window**: at date $t$, fit preprocessing/weights using all data up to $t$, then **test on $t \to t+1$**.  
   - Optionally compare with a **rolling window** (e.g., last 60 months) to check regime sensitivity.  

2. **At each rebalance date $t$**  
   - **Universe**: only stocks investable at $t$.  
   - **Preprocessing (fit on train only)**:  
     - Winsorize (1%/99%), z-score by date, optional size/industry neutralization.  
   - **IC testing**: compute cross-sectional IC/RankIC between factor at $t$ and **future return** $t \to t+1$.  
   - **Scoring & portfolio**: form factor scores using equal/IC/ICIR weights calibrated on the train window only.  

3. **Aggregation & inference (OOS only)**  
   - Time series of OOS $\{\text{IC}_t\}$. Report mean IC, ICIR, hit rate, and HAC (Newey–West) t-stat.  
   - Portfolio OOS performance: CAGR, vol, Sharpe, maxDD, turnover, and cost-adjusted returns.  

4. **Acceptance bar (OOS, monthly)**  
   - Mean **RankIC > 0** with HAC t-stat ≥ 2  
   - **ICIR ≥ 0.3**  
   - **Hit rate ≥ 55%**  
   - Factor correlation with others < 0.8  

5. **Practical cautions**  
   - Avoid overlapping returns for multi-month horizons (or use larger HAC lags).  
   - Keep preprocessing parameters fixed within each train window.  
   - Always log data availability dates to prevent look-ahead.  

## Stock Scoring Framework  

Scores will be calculated as a **linear combination** of selected factors. Initial methods to test:  

1. Equal weights  
2. IC-weighted  
3. ICIR-weighted  

## Portfolio Construction  

- **Rebalance**: Score at month-end, trade at next month’s open  
- **Holding Sizes**: Test portfolios of 20, 30, 40, and 50 stocks  
- **Weighting**: Equal-weighted portfolios to start  
- **Transaction Costs**: Apply simple cost models (e.g., 10–20 bps per trade side) to adjust returns. Report turnover, cost-adjusted performance, and sensitivity to different cost assumptions.  

Future improvements: test alternative rebalancing frequencies, sector neutrality, and more sophisticated transaction cost modeling (e.g., volume-based slippage or market impact).  

## Roadmap  

1. **Phase 1**: Build factor library and run baseline equal-weight backtests.  
2. **Phase 2**: Add IC/ICIR weighting, factor correlation pruning, and walk-forward validation.  
3. **Phase 3**: Expand portfolio construction with turnover control, transaction costs, and risk adjustments.  

✅ **Deliverable**: For each rebalance date, generate factor scores, stock rankings, and portfolio backtest results — published as a series of blog posts tracking progress.  
