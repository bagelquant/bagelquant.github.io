---
title: "How to Correctly Join Multi-Frequency Data (Quarterly → Daily) Without Leakage"
layout: post
---

Joining quarterly fundamentals to daily equity data is one of the most
subtle and important steps in building factor models and
machine-learning pipelines. Getting this join wrong introduces lookahead
bias, artificially boosting IC, Sharpe, and t‑stats. Getting it right
produces realistic, production‑grade signals.

This article provides the full methodology: intuition, Compustat
details, effective intervals, Python implementation, diagnostics, edge
cases, and empirical impacts.

## Why Multi-Frequency Alignment Is Hard in Finance

Daily return data and quarterly fundamental data behave differently:

-   Daily prices update continuously
-   Fundamentals are reported infrequently
-   Firms file at different times
-   Reporting involves long delays
-   Data has multiple timestamps

Unlike typical ML datasets, financial data does not have a single
authoritative timestamp. Using the wrong one creates leakage.

## The Three Time Dimensions of Fundamental Data

Every fundamental item has three dates:

**Fiscal Period End (datadate)**
The period the numbers refer to. Not the date information becomes
public.

**Earnings Announcement / Filing Date (rdq, report_dt)**
When information actually becomes public. This is the economically
meaningful date.

**Point-in-Time Database Insertion Date (pdate)**
When the data entered the WRDS database. Used to eliminate revision and
survivorship bias.

Only the announcement/filing date determines when the market learns the
information.

## Why Merging on Fiscal Period End Causes Leakage

Many beginner pipelines do:

``` python
df_daily.merge(df_quarterly, on=["permno", "datadate"])
```

This assumes the data is known on the fiscal period end, which is false.
Companies typically file:

-   10‑Q: 30--45 days after quarter end\
-   10‑K: 60--90 days after year end

Using fiscal period end makes the signal appear too early by 1--3
months, inflating backtest performance.

## Realistic Reporting Timeline

Example: Q1 fiscal period ends 2024‑03‑31

```plaintext
    2024-03-31  Quarter ends  
    2024-05-12  10-Q filed  
    2024-05-13  Market reacts  
    2024-08-09  Next quarter filed  
```

Fundamental values should appear on 2024‑05‑12 and stay constant until
the next announcement.

## The Effective Interval Method

For each firm and each quarter:

    effective_start = announce_date
    effective_end   = next_announce_date - 1 day

A daily observation can only use a fundamental value if:

    effective_start ≤ date ≤ effective_end

This creates a piecewise-constant series that reflects real information
availability.

## Python Implementation (Full Version)

### Build Announcement Dates

``` python
quarterly["announce"] = quarterly["rdq"].fillna(quarterly["report_dt"])
quarterly = quarterly.dropna(subset=["announce"])
quarterly["announce"] = pd.to_datetime(quarterly["announce"])
```

### Create Validity Windows

``` python
q = quarterly.sort_values(["permno", "announce"]).copy()
q["next_announce"] = q.groupby("permno")["announce"].shift(-1)

q["eff_start"] = q["announce"]
q["eff_end"] = q["next_announce"] - pd.Timedelta(days=1)
q["eff_end"] = q["eff_end"].fillna(pd.Timestamp("today"))
```

### Perform Merge Using merge_asof

``` python
q = q.rename(columns={"eff_start": "key"})
q = q.sort_values(["permno", "key"])

merged = pd.merge_asof(
    daily.sort_values(["permno", "date"]),
    q.sort_values(["permno", "key"]),
    by="permno",
    left_on="date",
    right_on="key",
    direction="backward"
)
```

### Filter Out-of-Interval Rows

``` python
merged = merged[merged["date"] <= merged["eff_end"]]
```

Leakage is now eliminated.

## Diagnostics to Ensure No Leakage

### Verify no daily row precedes announcement

``` python
assert (merged["date"] >= merged["announce"]).all()
```

### Verify interval consistency

``` python
test = merged.groupby(["permno", "announce"])["date"].agg(["min", "max"])
assert (test["min"] <= test["max"]).all()
```

### Visual checks

Plot signal vs. announce dates --- should look like clean step
functions.

## Empirical Impact of Correct Alignment

Real projects typically observe:

-   IC drops from \~0.06 → \~0.02--0.03\
-   Sharpe collapses from \~2.0 → \~0.6\
-   Turnover increases (data stays stale longer)\
-   ML models stop "cheating" on earnings information

Naive joins create artificial predictive power. Correct joins expose the
real signal strength.

## Alternative Alignment Methods

### Point‑in‑Time (PIT)

The gold standard. Uses WRDS `pdate` to track when each item entered the
database. Completely eliminates revision and survivorship bias.

### 90‑Day Lag

Use:

    fiscal_period_end + 90 days

Simple and safe but not precise. Good fallback if announcement dates are
unavailable.

### Quarter‑Lag Rule

Use Q1 data only starting in Q2. Extremely conservative; makes signals
stale. Mostly used to replicate older academic studies.

## Annual, Monthly, and Other Non‑Quarterly Data

The same effective‑interval logic applies:

-   Annual filings → use 10‑K announce date
-   Monthly macro releases → use BLS/FRED release dates
-   IBES analyst estimates → use actual estimate timestamp

Never use the period-end unless that is the true release date.

## Production Considerations

-   Cache effective intervals so they don't need to be recalculated
-   Use Parquet/Feather for large datasets
-   Prefer Polars for 5--10× faster as‑of joins
-   Add tests: `test_no_leakage`, `test_intervals`,
    `test_announce_alignment`
-   Visualize a few firms to detect anomalies
-   Expect your Sharpe to drop --- this means it's becoming realistic

## Example Timeline for One Firm Over a Year

```plaintext
  Quarter   Fiscal End   Filed        Effective Interval
  --------- ------------ ------------ --------------------
  Q4 2023   2023‑12‑31   2024‑02‑02   Feb 02 → May 02
  Q1 2024   2024‑03‑31   2024‑05‑03   May 03 → Aug 01
  Q2 2024   2024‑06‑30   2024‑08‑02   Aug 02 → Nov 01
```

Daily alignment:

-   Jan → Q3
-   Feb 02--May 02 → Q4
-   May 03--Aug 01 → Q1
-   Aug 02--Nov 01 → Q2

This is how real investors see information.

## Summary Checklist

✔ Use announce/filing dates, never fiscal period end\
✔ Construct effective intervals per firm\
✔ Perform backward merge_asof\
✔ Drop rows outside the interval\
✔ Handle missing filings, restatements, and multiple filings\
✔ Validate with assertions and visual checks\
✔ Expect lower IC/Sharpe\
✔ Use PIT when possible

