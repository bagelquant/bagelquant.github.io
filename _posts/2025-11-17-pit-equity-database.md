---
title: "How to Build a Point-In-Time (PIT) Equity Database"
tags: [finance, data-engineering, quantitative-research]
---

A comprehensive, production-grade guide for constructing a fully leakage-free, survivorship-free, revision-aware PIT database for equity research and quantitative trading.

## Why PIT Matters

Every equity dataset suffers from three major biases:

- **Lookahead bias**: future information appears too early.
- **Survivorship bias**: dead/delisted firms vanish.
- **Revision bias**: datasets overwrite historical values with
    corrected ones.

A Point‑In‑Time (PIT) database solves all three by preserving *exactly
what was known on each historical date*.

## The Three Time Dimensions of PIT

Every data point has three timestamps:

### **Event Date**

When economic activity occurred (e.g., fiscal period end).

### **Announcement / Filing Date**

When information became public (`rdq`, `report_dt`).

### **PIT Load Date (`pdate`)**

When the vendor first loaded the data into the database.

> A true PIT signal must satisfy:\
> **pdate ≤ t and announce_date ≤ t**

## Compustat PIT Essentials

Compustat-specific fields for PIT reconstruction:

- `pdate`: first appearance
- `pitem`: version identifier
- `rdq`: earnings announcement date
- `report_dt`: SEC filing date
- `indfmt`, `datafmt`, `popsrc`, `consol`: statement type filters
- `datadate`: fiscal period end (not a PIT date)

Compustat overwrites history by default, so `pdate` is critical.

## CRSP PIT Considerations

CRSP is partially PIT:

- Prices are PIT (never revised)
- Shares outstanding can be revised
- Delisting returns must be included to avoid survivorship bias
- Use the CCM link table properly:
  - `linktype ∈ {LU, LC}`
  - `linkprim ∈ {P, C}`

## Architecture of a PIT Equity Database

Recommended structure:

```plaintext
    RAW LAYER        →     STAGING LAYER        →     PIT LAYER
    (Vendor files)         (Clean + linked)           (Daily valid data)
```

- **Raw layer**: immutable vendor dumps\
- **Staging layer**: cleaning, linking, normalization\
- **PIT layer**: effective intervals with daily validity

## PIT Table Schema

A PIT table must contain:

- permno\
- gvkey\
- item value\
- event_date\
- announce_date\
- pdate\
- start_date = max(announce_date, pdate)\
- end_date = next_start_date - 1

Query rule:

```sql
SELECT *
FROM pit_table
WHERE start_date <= t AND t <= end_date
```

## Constructing Effective Intervals

### Step 1 -- Sort by announce date

``` python
df = df.sort_values(["permno", "announce"])
```

### Step 2 -- Next announce & next pdate

``` python
df["next_announce"] = df.groupby("permno")["announce"].shift(-1)
df["next_pdate"] = df.groupby("permno")["pdate"].shift(-1)
```

### Step 3 -- Compute start_date

``` python
df["start_date"] = df[["announce", "pdate"]].max(axis=1)
```

### Step 4 -- Compute end_date

``` python
df["next_start"] = df.groupby("permno")["start_date"].shift(-1)
df["end_date"] = df["next_start"] - pd.Timedelta(days=1)
df["end_date"] = df["end_date"].fillna(pd.Timestamp.today())
```

## Daily PIT Joins Using `merge_asof`

``` python
daily = daily.sort_values(["permno", "date"])

joined = pd.merge_asof(
    daily,
    df.sort_values(["permno", "start_date"]),
    by="permno",
    left_on="date",
    right_on="start_date",
    direction="backward"
)

joined = joined[joined["date"] <= joined["end_date"]]
```

## Handling Vendor Edge Cases

### Missing announcement dates

Fallback order: 1. `rdq` 2. `report_dt` 3. Estimate from next quarter

### Preliminary vs. final filings

Prefer earliest *complete* filing.

### Restatements

Use earliest `pdate` per `pitem`.

### Multi‑class shares, ADRs

Filter CCM links carefully.

## Performance Optimization for Large PIT Systems

- Use **Parquet** for columnar storage\
- Use **Polars** for 5--10× faster interval joins\
- Partition by permno / year\
- Cache PIT tables\
- Minimize repeated interval computations

## Unit Tests for PIT Validation

### No backward leakage

``` python
assert (joined["date"] >= joined["announce"]).all()
assert (joined["date"] >= joined["pdate"]).all()
```

### Interval integrity

``` python
assert (df["start_date"] <= df["end_date"]).all()
```

### No gaps / overlaps

``` python
df["gap"] = df.groupby("permno")["start_date"].diff() > pd.Timedelta(days=1)
assert not df["gap"].any()
```

## Example Timeline

```plaintext
  Quarter   Fiscal End   Filed        Effective Interval
  --------- ------------ ------------ --------------------
  Q4 2023   2023‑12‑31   2024‑02‑02   Feb 02 → May 02
  Q1 2024   2024‑03‑31   2024‑05‑03   May 03 → Aug 01
  Q2 2024   2024‑06‑30   2024‑08‑02   Aug 02 → Nov 01

```

Daily alignment becomes realistic and leak‑free.

## Summary Checklist

✔ Track three timestamps: event, announce, pdate\
✔ Compute start_date = max(announce, pdate)\
✔ Build effective intervals per permno\
✔ Join via backward `merge_asof`\
✔ Include CRSP delisting returns\
✔ Validate intervals & PIT logic\
✔ Expect IC & Sharpe to drop\
✔ Cache PIT tables for speed
