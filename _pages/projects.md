---
layout: topic
title: "Projects"
permalink: /projects/
excerpt: "Quant projects from BagelQuant."
header: 
    overlay_image: /assets/images/headers/topic-header.png
---

## bagel-tushare

Github link: [bagel-tushare](https://github.com/bagelquant/bagel-tushare)

A Python wrapper for Tushare, a Chinese financial data provider. The project provides a simple and easy-to-use automation tool for downloading financial data from Tushare, and storing the data in a local mysql database.

## bagel-mean-variance

Github link: [bagel-mean-variance](https://github.com/bagelquant/bagel-mean-variance)

`bagel-mean-variance` is a Python package designed to calculate optimal portfolio weights using the mean-variance optimization method. The package is implemented using pure matrix operations, avoiding the use of optimization libraries. It is simple, efficient, and flexible, making it ideal for financial analysis and portfolio management tasks. calculation method please refer to [Mean-Variance analysis](https://bagelquant.com/mean-variance/)

## bagel-factor

Github link: [bagel-factor](https://github.com/bagelquant/bagel-factor/blob/main/README.md)

A small, pandas-first toolkit for **single-factor evaluation/testing**.

### Scope (by design)

This package focuses on:
- canonical point-in-time data helpers (`(date, asset)` panel)
- preprocessing transforms (clip / z-score / rank)
- single-factor evaluation (IC/ICIR, quantile returns, long-short, coverage, turnover)

It intentionally does **not** implement multi-factor modeling or portfolio backtesting.

### Key documents

- [Factor evaluation guide](https://github.com/bagelquant/bagel-factor/blob/main/docs/factor_evaluation.md)
- [End-to-end example](https://github.com/bagelquant/bagel-factor/blob/main/docs/example.md)

