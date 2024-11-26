---
layout: splash
title: "BagelQuant Projects"
permalink: /projects/
excerpt: "Projects and code samples from BagelQuant."
header:
  overlay_image: /assets/images/quant-skills-header.png
---

## Bagel Series

bagelquant provides a series of projects that aim to provide a comprehensive quant research and trading platform. The projects are written in Python and are open-source. 

The projects are designed to be modular and can be used independently or together. Separate the concerns of data, strategy, and execution, the projects provide a clear separation of concerns, making it easy to develop and extend the platform.

**Base projects:**

Base projects provide the foundation for the rest of the projects. They include data providers, data storage, datatypes, and other basic functionalities.

- [bagel-tushare](bagel-tushare/bagel-tushare.md): A Python wrapper for Tushare, a Chinese financial data provider. The project provides a simple and easy-to-use automation tool for **downloading** financial data from Tushare, and **storing** the data in a local mysql database.
- [bagel-datatype](https://github.com/bagelquant/bagel-datatype): A Python library for defining and manipulating financial datatypes. Contains **dataclasses** for financial data, such as stock, option, and future. The library also provides factory functions for creating financial data objects from raw data or from `bageltushare` style mysql database.
- [bagel-eval](https://github.com/bagelquant/bagel-eval): A Python library for **evaluating** financial data. Contains functions for calculating financial metrics, such as moving average, RSI, and MACD. The library also provides matplotlib-based visualization functions for plotting financial data.

**Strategy projects:**

- [bagel-bt](): A Python library for **backtesting** trading strategies. The library provides a simple and easy-to-use interface for backtesting trading strategies. 
- [bagel-factor](): A Python library for **factor construction, evaluation, and backtesting**. Includes various factor construction methods.
- [bagel-opt-portfolio](): A Python library for **portfolio optimization**. Includes various portfolio optimization methods.

