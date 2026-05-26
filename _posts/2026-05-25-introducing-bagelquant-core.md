---
layout: post
title: "Introducing BagelQuant-Core: A DAG-Based Quant Research Engine"
date: 2026-05-25
series: "BagelQuant-Core"
---

# Introducing BagelQuant-Core

I recently started building **BagelQuant-Core**, a new project focused on structuring quantitative equity research and portfolio construction as a **composable computational system**.

The goal is not just to implement another factor library or backtesting framework, but to define a **clean abstraction layer for how alpha is represented, composed, and executed**.

## Motivation

In most quant research workflows, alpha signals are treated as:

- standalone formulas
- independent scripts
- loosely connected pipelines

But in practice:

- signals interact
- transformations depend on shared data structures
- portfolio construction is a composition problem, not a collection problem

This creates fragmentation between:

- research
- signal engineering
- portfolio construction
- execution

**BagelQuant-Core is designed to unify these layers.**

## Core Idea: Everything is a DAG

At the center of the system is a simple but powerful idea:

> All quant logic can be represented as a Directed Acyclic Graph (DAG)

In this model:

- **Nodes** = data or transformations
- **Edges** = dependency relationships
- **Execution** = graph evaluation

This allows us to formalize:

- factor computation pipelines
- alpha combination
- risk transformations
- portfolio construction rules

## Key Abstractions

BagelQuant-Core introduces three core concepts:

### 3.1 Panel

A **Panel** is a structured data object:

- indexed by time × asset
- represents factor exposures or features
- immutable and composable

Think of it as the atomic unit of quant data.

### Operator

An **Operator** transforms one or more panels into another panel.

Examples:

- z-score normalization
- cross-sectional ranking
- lag / rolling window features
- signal smoothing

Operators are **pure functions over panels**.


### Composer

A **Composer** combines multiple panels or operators into a higher-level structure.

This is where:

- multi-factor alpha construction
- weighting schemes
- signal blending

happens.

It is the bridge between **research logic and portfolio logic**.

## Execution Model

Once expressed as a DAG:

- nodes are evaluated lazily
- dependencies are resolved automatically
- intermediate results can be cached
- recomputation is minimal and localized

This makes research workflows:

- reproducible
- modular
- scalable

## Example Conceptual Flow

A simple alpha pipeline might look like:

- raw fundamentals → Panel
- factor transformations → Operators
- signal combination → Composer
- portfolio weights → execution layer

Everything is explicitly structured rather than implicit in code scripts.

## Why This Matters

This design is trying to solve a structural problem in quant research:

- scripts do not scale
- factor libraries become messy
- portfolio logic is often implicit
- reproducibility is fragile

By enforcing a DAG + compositional abstraction, we get:

- clearer research logic
- better debugging
- easier factor experimentation
- scalable portfolio construction

## Current Status

BagelQuant-Core is currently in early development.

What exists:

- core abstraction design (Panel / Operator / Composer)
- initial DAG execution prototype
- experimental factor pipeline structure

What is next:

- portfolio optimization layer
- caching + performance optimization
- integration with live data pipelines
- backtesting engine alignment

## Roadmap Direction

The long-term direction is:

> Build a full-stack quantitative research OS built on composable DAG primitives.

This includes:

- research layer (signals)
- portfolio layer (allocation)
- execution layer (trading)
- monitoring layer (analytics)

All unified under a single compositional system.

## Closing

BagelQuant-Core is still early, but the goal is clear:

> Turn quantitative research into a structured, composable system rather than scattered scripts.

Feedback and discussion are welcome.
