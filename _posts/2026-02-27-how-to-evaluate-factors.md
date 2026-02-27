# How to Evaluate a Trading Factor with bagel-factor

So you've built a signal — a P/E ratio, a moving average crossover, a sentiment score from earnings call transcripts — and you want to know one thing: *does it actually predict future returns?*

That's exactly what [`bagel-factor`](https://github.com/bagelquant/bagel-factor) is for. It's a focused, pandas-first Python toolkit for single-factor evaluation in quantitative finance. No backtesting framework. No portfolio optimizer. Just the rigorous statistical machinery you need to determine whether your signal is worth trading.

This guide walks you through the full workflow, from raw data to a publishable factor tearsheet.

---

## What Is Factor Evaluation?

A **factor** (or alpha signal) is a numeric score assigned to each asset at each point in time. The central question is: does a higher score today predict higher returns tomorrow (or over the next week, month, etc.)?

Factor evaluation answers three questions:

1. **Does the signal contain information?** — Is it statistically correlated with future returns?
2. **Is it economically tradable?** — After transaction costs, can you actually make money?
3. **Is it stable?** — Does it work consistently across time and market regimes?

`bagel-factor` gives you the tools to answer all three rigorously.

---

## Installation

```bash
pip install bagel-factor
```

Requires Python ≥ 3.12.

---

## Step 1: Prepare Your Data

Before anything else, your data needs to be in the right shape. `bagel-factor` expects a **canonical panel** — a `pd.DataFrame` indexed by a two-level `MultiIndex` with levels named `("date", "asset")`.

```python
import pandas as pd
from bagelfactor.data import ensure_panel_index

# Your raw data: one row per (date, asset) pair
df = pd.read_csv("my_data.csv")

# Convert to panel format
panel = ensure_panel_index(df, date="date", asset="ticker")

# CRITICAL: Always sort after creating the panel
panel = panel.sort_index()
```

> ⚠️ **Always sort.** Forward return calculations use `.shift()` internally. Unsorted data produces silently wrong results.

### Avoiding Lookahead Bias

This is the most important data integrity rule: the factor value on date `t` must be computable using *only* information available at date `t`. If you're using fundamental data (earnings, balance sheet metrics), it's usually published after the reporting date. Lag it explicitly:

```python
from bagelfactor.data import lag_by_asset

# If the factor is "as-of" date t, it shouldn't be used until t+1
panel = lag_by_asset(panel, columns=["pe_ratio"], periods=1)
```

Skipping this step is the most common cause of suspiciously good backtest results.

### Validating Your Panel

The package includes a diagnostic utility to catch common issues before they cause silent bugs:

```python
from bagelfactor import diagnose_panel

diag = diagnose_panel(panel)
print(diag)
```

```
Panel Diagnostics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Valid MultiIndex with names ['date', 'asset']
✓ Index is sorted
✓ No duplicate entries
⚠ Missing data: 5.2% of values are NaN
  Date range: 2020-01-01 to 2023-12-31 (1000 dates)
  Assets: 500 unique
```

---

## Step 2: Preprocess the Factor (Optional but Recommended)

Raw factor values often have heavy tails, different scales across time, or other properties that make cross-sectional comparison noisy. A preprocessing pipeline conditions the factor before evaluation.

```python
from bagelfactor.preprocess import Clip, ZScore, Rank, Pipeline

preprocess = Pipeline([
    Clip("alpha", lower=-3.0, upper=3.0),   # Winsorize outliers
    ZScore("alpha"),                          # Standardize cross-sectionally
    Rank("alpha"),                            # Rank for robustness
])
```

All transforms operate cross-sectionally (per date), not over time. The three most useful are:

- **`Clip`** — caps extreme values at a specified range, reducing the influence of data errors or structural outliers
- **`ZScore`** — standardizes to zero mean and unit variance per date, making the factor comparable across time
- **`Rank`** — converts raw values to their ordinal rank, which is the most robust to outliers and non-linearity

You don't have to use all three. A common starting point is `Clip` + `Rank`.

---

## Step 3: Run the Evaluation

With data prepared and preprocessing configured, a single call does everything:

```python
from bagelfactor import SingleFactorJob

res = SingleFactorJob.run(
    panel,
    factor="alpha",        # Name of the factor column in your panel
    price="close",         # Price column used to compute forward returns
    horizons=(1, 5, 20),   # Evaluate 1-day, 5-day, and 20-day forward returns
    n_quantiles=5,         # Split into quintiles (Q1 = worst, Q5 = best)
    preprocess=preprocess, # Optional: your preprocessing pipeline
)
```

The `horizons` parameter lets you evaluate the factor at multiple holding periods simultaneously. A good signal often shows IC decay — stronger at short horizons, weaker as the holding period lengthens. Seeing that decay pattern is itself informative.

---

## Step 4: Interpret the Results

`SingleFactorJob.run()` returns a `SingleFactorResult` object. Here's what's inside and how to read it.

### Information Coefficient (IC)

IC is the cross-sectional Spearman correlation between your factor and forward returns on each date. It's the single most important metric:

```python
h = 5  # 5-day horizon

# IC time series
print(res.ic[h].head())

# Mean IC and ICIR
mean_ic = res.ic[h].mean()
icir = res.icir[h]  # = mean(IC) / std(IC)

print(f"Mean IC:  {mean_ic:.4f}")
print(f"ICIR:     {icir:.2f}")
```

**How to read IC values:**

| Mean IC | Signal Strength |
|---------|-----------------|
| < 0.01  | Likely noise |
| 0.01–0.03 | Weak but possibly real |
| 0.03–0.06 | Solid |
| > 0.10  | Strong — or check for data leakage |

The **sign** matters too. Negative IC just means higher factor → lower returns. You can invert the factor by multiplying by -1.

**ICIR** (IC Information Ratio) measures stability — it's the Sharpe ratio of the IC series. A factor with mean IC of 0.05 but wildly inconsistent IC is harder to trade than one with IC 0.03 that's rock-solid across every period.

| ICIR | Quality |
|------|---------|
| < 0.2 | Unreliable |
| 0.2–0.5 | Modest |
| 0.5–1.0 | Good |
| > 1.0 | Excellent |

### Quantile Returns

Assets are ranked by factor value each date and split into buckets. With `n_quantiles=5`, Q1 contains the bottom 20% (lowest factor values) and Q5 the top 20%. The key pattern to look for is **monotonicity**:

```python
# Mean return per quantile over the full sample
mean_qret = res.quantile_returns[h].mean()
print(mean_qret)
```

A good factor produces an ascending staircase — Q1 earns the least, Q5 earns the most, with smooth steps in between. Non-monotonic returns (Q3 > Q5, for example) suggest the factor doesn't cleanly rank assets and may just be noise.

### Long-Short Returns

The long-short spread (Q5 minus Q1) is your **factor payoff** — what you'd earn by going long the top quintile and short the bottom quintile:

```python
ls = res.long_short[h]

mean_ls = ls.mean()
sharpe = mean_ls / ls.std()

print(f"L/S mean:   {mean_ls*100:.3f}% per period")
print(f"L/S Sharpe: {sharpe:.2f}")

# Cumulative equity curve
cumulative = (1 + ls).cumprod() - 1
print(f"Total return: {cumulative.iloc[-1]*100:.1f}%")
```

A Sharpe above 0.5 (annualized) is typically considered promising for a single factor. Above 1.0 is very good. Above 2.0 — verify you haven't introduced lookahead bias.

### Turnover

IC tells you whether the signal has information. Turnover tells you whether you can act on it profitably:

```python
avg_turnover = res.turnover.mean()
print(f"Average turnover: {avg_turnover:.1%}")
```

Turnover is computed using Jaccard set overlap — it measures what fraction of quantile membership changes each period. 0% means the portfolio never changes. 100% means it completely turns over every rebalance.

| Turnover | Tradability |
|----------|-------------|
| < 20% | Very tradable |
| 20–40% | Manageable |
| 40–60% | High costs, model carefully |
| > 60% | Likely unprofitable unless spreads are enormous |

A factor with IC = 0.05 but 70% daily turnover will likely lose money in practice. A factor with IC = 0.03 and 15% turnover may be a genuine edge.

### Coverage

Coverage is the fraction of your universe with a valid (non-NaN) factor value on each date:

```python
avg_coverage = res.coverage.mean()
print(f"Average coverage: {avg_coverage:.1%}")
```

Low coverage (below 80%) is a red flag — your results may be driven by a small, potentially biased subset of the universe. Sudden drops in coverage on specific dates often indicate data quality problems.

---

## Step 5: Statistical Testing

Visual inspection is necessary but not sufficient. Use statistical tests to quantify how confident you should be.

### Is the Mean IC Significantly Non-Zero?

```python
from bagelfactor import ttest_1samp

ic_test = ttest_1samp(res.ic[h], popmean=0.0)
print(f"t-statistic: {ic_test.statistic:.2f}")
print(f"p-value:     {ic_test.pvalue:.4f}")
```

A |t-stat| > 2 is typically treated as significant at the ~5% level. In finance, with the risk of data mining and multiple testing, you generally want stronger evidence — aim for |t-stat| > 3.

### Does the Long-Short Have Real Alpha?

```python
from bagelfactor import ols_alpha_tstat

ls_alpha = ols_alpha_tstat(res.long_short[h])
print(f"Alpha t-stat: {ls_alpha.tstat:.2f}")
```

This runs an OLS regression and tests whether the intercept is significantly different from zero — i.e., whether the long-short returns are non-trivial after accounting for the baseline.

> ⚠️ **A word of caution**: Financial time series violate classical t-test assumptions (autocorrelation, heteroskedasticity). These tests give you a first-pass answer, not the final word. For serious research, supplement with Newey-West standard errors and out-of-sample validation.

---

## Step 6: Visualize Everything

Numbers are essential, but plots often reveal patterns that summary statistics hide.

### The All-In-One Summary

```python
from bagelfactor import plot_result_summary

fig = plot_result_summary(res, horizon=5)
fig.savefig("factor_summary.png", dpi=150, bbox_inches="tight")
```

This generates a 4×2 grid covering:
- IC time series and histogram
- Quantile cumulative returns and return heatmap
- Long-short period returns and cumulative equity curve
- Turnover and coverage over time

It's the fastest way to get a complete picture of your factor.

### Individual Plots

For presentations or deeper investigation, use targeted plots:

```python
from bagelfactor import (
    plot_ic_time_series,
    plot_ic_hist,
    plot_quantile_returns_time_series,
    plot_quantile_returns_heatmap,
    plot_long_short_time_series,
)

# IC with 20-period rolling average overlay
plot_ic_time_series(res.ic[5], rolling=20)

# IC distribution — should cluster away from zero
plot_ic_hist(res.ic[5])

# Quantile returns through time
plot_quantile_returns_time_series(res.quantile_returns[5])

# Heatmap of quantile returns (great for spotting regime changes)
plot_quantile_returns_heatmap(res.quantile_returns[5])

# Long-short equity curve (cumulative=True shows compounded growth)
plot_long_short_time_series(res.long_short[5], cumulative=True)
```

---

## Putting It All Together: A Complete Workflow

Here's a production-ready evaluation script:

```python
import pandas as pd
from bagelfactor import (
    SingleFactorJob,
    diagnose_panel,
    plot_result_summary,
    ttest_1samp,
    ols_alpha_tstat,
)
from bagelfactor.data import ensure_panel_index, lag_by_asset
from bagelfactor.preprocess import Clip, Pipeline, Rank, ZScore

# --- 1. Load and prepare data ---
df = pd.read_csv("my_data.csv")
panel = ensure_panel_index(df, date="date", asset="ticker")
panel = panel.sort_index()

# Lag fundamental factors to prevent lookahead bias
panel = lag_by_asset(panel, columns=["my_factor"], periods=1)

# Sanity check
print(diagnose_panel(panel))

# --- 2. Preprocessing pipeline ---
preprocess = Pipeline([
    Clip("my_factor", lower=-3.0, upper=3.0),
    ZScore("my_factor"),
    Rank("my_factor"),
])

# --- 3. Run factor evaluation ---
res = SingleFactorJob.run(
    panel,
    factor="my_factor",
    price="close",
    horizons=(1, 5, 20),
    n_quantiles=5,
    preprocess=preprocess,
)

# --- 4. Summarize results ---
h = 5
ic_test = ttest_1samp(res.ic[h], popmean=0.0)
ls_alpha = ols_alpha_tstat(res.long_short[h])

print(f"=== Factor Scorecard (h={h}) ===")
print(f"Mean IC:      {res.ic[h].mean():.4f}")
print(f"ICIR:         {res.icir[h]:.2f}")
print(f"IC t-stat:    {ic_test.statistic:.2f}  (p={ic_test.pvalue:.4f})")
print(f"L/S Sharpe:   {res.long_short[h].mean() / res.long_short[h].std():.2f}")
print(f"L/S α t-stat: {ls_alpha.tstat:.2f}")
print(f"Avg turnover: {res.turnover.mean():.1%}")
print(f"Avg coverage: {res.coverage.mean():.1%}")

# --- 5. Visualize ---
fig = plot_result_summary(res, horizon=h)
fig.savefig("factor_summary.png", dpi=150, bbox_inches="tight")

# --- 6. Decision ---
is_promising = (
    res.icir[h] > 0.5
    and abs(ic_test.statistic) > 2
    and res.turnover.mean() < 0.40
)
print("\n✅ Factor looks promising!" if is_promising else "\n⚠️ Needs more investigation.")
```

---

## Red Flags to Watch For

Even with solid headline metrics, watch out for these patterns:

**Lookahead bias**
- IC consistently above 0.15
- Perfect quantile separation
- Unrealistically high Sharpe (>3 annualized for daily data)

**Data quality issues**
- Coverage drops suddenly on specific dates
- IC correlates with coverage (signal only "works" when data is complete)

**Overfitting**
- Works brilliantly in-sample, fails out-of-sample
- Only works in specific subperiods
- Sensitive to small changes in preprocessing parameters

**Trading reality**
- Turnover > 60% daily
- Factor concentrated in illiquid microcap names
- Gross spread smaller than estimated transaction costs

---

## What bagel-factor Doesn't Do

By design, `bagel-factor` is a *single-factor evaluation engine* — not a full research platform. It deliberately excludes:

- Multi-factor portfolio optimization
- Transaction cost modeling
- Risk model construction (sector/beta neutralization)
- Walk-forward / out-of-sample validation frameworks
- Position sizing and execution

If your factor passes evaluation here, the next step is to integrate it into a full backtesting environment and validate it out-of-sample before trading real capital.

---

## Summary

Factor evaluation with `bagel-factor` follows a clean, repeatable workflow:

1. **Prepare** a sorted `(date, asset)` panel with proper point-in-time alignment
2. **Preprocess** the factor with clip, z-score, and/or rank transforms
3. **Run** `SingleFactorJob.run()` across multiple horizons
4. **Interpret** IC, ICIR, quantile returns, long-short Sharpe, turnover, and coverage
5. **Test** statistical significance with t-tests and OLS alpha
6. **Visualize** with the summary plot and individual charts

A good factor will show consistent IC (with ICIR > 0.5), monotonic quantile returns, a positive long-short equity curve, and turnover low enough that trading costs don't consume the spread. A promising factor that fails on any one of these dimensions isn't necessarily dead — it's a clue about what to improve.

The goal isn't to find a factor that looks perfect in a backtest. It's to find a factor that has a principled, testable reason to predict returns — and that survives rigorous scrutiny before you risk real money on it.

---

*Built with [bagel-factor](https://github.com/bagelquant/bagel-factor) — a pandas-first toolkit for single-factor evaluation.*
