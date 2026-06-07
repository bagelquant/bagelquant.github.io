---
layout: content-list
title: "概览"
permalink: /zh/docs/data/
lang: zh
ref: "docs-data"
alternate_lang_url: /docs/data/
nav: docs_zh
---

`bagelquant-data` 是 BagelQuant 的提供商中立数据层。

它保证对数据的一致、可靠、可重复访问。它不
自己的研究、组合构建、图形执行、回溯测试或
analytics.

使用它作为后端Python包来注册提供商、管理本地数据湖
快照、运行提供程序更新并检索 pandas 数据集或面板形状
objects:

```python
from bagelquant_data.datasource import DataSourceRegistry, TushareDataSource
from bagelquant_data.lake import DataLakeManager, LocalDataLake

registry = DataSourceRegistry()
registry.register(TushareDataSource(token="your-token"))

lake = LocalDataLake(".bagelquant-data-lake")
manager = DataLakeManager(lake, registry=registry)
```
