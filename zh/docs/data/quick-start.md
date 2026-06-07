---
layout: page
title: "快速开始"
permalink: /zh/docs/data/quick-start/
lang: zh
ref: "docs-data-quick-start"
alternate_lang_url: /docs/data/quick-start/
nav: docs_zh
---

# 快速开始

`bagelquant-data` 是 BagelQuant 的提供商中立数据层。它管理
提供者适配器、本地湖快照、元数据和面板型检索。

## Install

```bash
uv add bagelquant-data
```

从 Tushare 加载时使用可选的 Tushare 依赖项：

```bash
uv add "bagelquant-data[tushare]"
```

## 注册提供商

```python
from bagelquant_data.datasource import DataSourceRegistry, TushareDataSource

registry = DataSourceRegistry()
registry.register(TushareDataSource(token="your-token"))
```

## 创建一个本地湖

```python
from bagelquant_data.lake import DataLakeManager, LocalDataLake

lake = LocalDataLake(".bagelquant-data-lake")
manager = DataLakeManager(lake, registry=registry)
```

## 写入或刷新数据

对于自定义数据，直接写一个pandas框架：

```python
manager.add("custom", "prices", prices)
```

对于提供者数据，请求数据集并将结果保留为本地快照：

```python
from bagelquant_data.datasource import DataRequest

manager.update(
    "tushare",
    DataRequest(
        dataset="daily",
        fields=("ts_code", "trade_date", "close"),
        start_date="2024-01-01",
        end_date="2024-01-31",
    ),
)
```

## Retrieve 数据

```python
from bagelquant_data.loader import Loader

loaded = Loader(registry=registry, lake=lake).source("tushare").load(
    "daily",
    fields=("open", "close"),
    start_date="2024-01-01",
    end_date="2024-01-31",
)

frame = loaded.data
```

对于研究输入，加载按资产日期字段：

```python
retrieved = Loader(registry=registry, lake=lake).source("tushare").load_panel(
    dataset="daily",
    field="close",
    universe=["000001.SZ", "600000.SH"],
    start_date="2024-01-01",
    end_date="2024-12-31",
)
```

`RetrievedPanel` 公开普通的 pandas 数据以及日历和 Universe 对象，因此
下游包可以决定如何构造自己的域对象。
