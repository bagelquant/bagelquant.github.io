---
title: "Stock Universe"
permalink: /factor-model-in-china/stock-universe/
sidebar:
    nav: "factor-model-in-china"
---
Stock universe: CSI 300 + CSI 500 + CSI 1000

## Overview

This document defines the stock universe we use for empirical research and quantitative strategies in China's A-share market, explains the reasoning behind the choice, and provides practical inclusion rules and implementation guidance to reduce common biases and ensure investability.

In short: the universe is the union of CSI 300, CSI 500, and CSI 1000 constituents through time. This captures a broad, liquid, and investable cross-section of A-share equities while keeping the universe focused enough for portfolio construction and backtesting.

## Why this universe

- Representativeness: The three indices together cover large-, mid-, and smaller-cap liquid stocks, giving a balanced cross-section for factor tests and stock selection.
- Investability: Constituents of these indices are typically liquid and tradable for institutional and retail strategies.
- Data availability: Larger and index-listed firms have more complete fundamental and market data (e.g., financials, required disclosures), which simplifies factor construction.
- Practicality: For monthly/quarterly rebalancing and a target portfolio size of ~20–40 names, this universe provides enough candidate stocks while limiting noise from extremely illiquid microcaps.
