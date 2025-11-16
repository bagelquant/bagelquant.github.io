---
title: "How to Correctly Join Multi-Frequency Data (Quarterly → Daily) Without Leakage"
tags: [factor-research]
---

Joining quarterly fundamentals (10-Q/10-K) to daily stock returns is one
of the most common tasks in factor research --- and one of the easiest
places to introduce **massive look-ahead bias** if done incorrectly.

This post summarizes the actual production-safe method used by quant
researchers to align multi-frequency datasets without leakage.

## 1. Why Multi-Frequency Joins Are Hard

Quarterly fundamentals have two timestamps:

1.  **Fiscal period end** --- the quarter *covered* by the report\
2.  **Report/filing date** --- when the data becomes *public*

Only the filing date matters for avoiding leakage.

## 2. The Wrong Approach

``` python
df_daily.merge(df_quarterly, on=["permno", "date"], how="left")
```

or

``` python
merge_asof(direction="backward")
```

These incorrectly assume data is known at quarter end.

## 3. The Correct Method --- Effective Date Framework

Each value must have:

    effective_start = announce_date
    effective_end   = next_announce_date - 1 day

Only use a quarter's fundamentals **after** it became public.

## 4. Example

Quarter ending **2024-03-31**\
Filed **2024-05-12**

Valid interval:

    2024-05-12 → (next filing date - 1)

Daily dates before filing use the *previous* quarter.

## 5. Python Implementation

### Step 1: Prepare quarterly data

``` python
quarterly = quarterly.sort_values(["permno", "announce_date"])
quarterly["next_announce"] = quarterly.groupby("permno")["announce_date"].shift(-1)
quarterly["effective_start"] = quarterly["announce_date"]
quarterly["effective_end"] = quarterly["next_announce"] - pd.Timedelta(days=1)
```

### Step 2: Sort daily data

``` python
daily = daily.sort_values(["permno", "date"])
```

### Step 3: Interval join using merge_asof

``` python
quarterly_interval = quarterly.rename(columns={"effective_start": "key_date"})

daily = pd.merge_asof(
    daily,
    quarterly_interval.sort_values("key_date"),
    by="permno",
    left_on="date",
    right_on="key_date",
    direction="backward"
)
```

### Step 4: Filter invalid dates

``` python
daily = daily[daily["date"] <= daily["effective_end"]]
```

## 6. Common Edge Cases

-   Missing announce dates → use SEC or WRDS filing dates\
-   Revisions → use PIT data (`pitem`, `pdate`)\
-   Multiple filings → choose earliest complete 10-Q/K

## 7. Rule of Thumb

When unsure: \> Shift fundamentals forward **90 days**\
This is conservative but standard in academia.

## 8. Summary

✔ Use filing dates, not fiscal period ends\
✔ Build effective intervals\
✔ Join with backward `merge_asof`\
✔ Filter out dates past effective_end\
✔ Avoid lookahead bias and inflated backtests

This method is essential for realistic factor research.

