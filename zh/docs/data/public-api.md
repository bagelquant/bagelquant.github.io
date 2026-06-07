---
layout: page
title: "公开 API"
permalink: /zh/docs/data/public-api/
lang: zh
ref: "docs-data-public-api"
alternate_lang_url: /docs/data/public-api/
nav: docs_zh
---

# 公开 API

`bagelquant-data` 通过 Python API 进行操作。包裹是故意的
返回 pandas 对象和纯元数据，而不是导入下游
研究 packages.

## 顶级导出

```python
from bagelquant_data import (
    DataContract,
    DataLakeManager,
    DataRequest,
    DataSource,
    DataSourceRegistry,
    DatasetSchema,
    FieldSchema,
    LoadedDataset,
    Loader,
    LocalDataLake,
    RetrievedPanel,
    Transform,
    TushareTableUpdateSpec,
    default_registry,
)
```

## 提供商注册表

- `DataSource`：基础提供商适配器协议。
- `DataRequest`：数据集、字段、过滤器、日期范围、版本、快照和选项。
- `DataSourceRegistry.register(source)`：注册适配器。
- `DataSourceRegistry.resolve(name)`：检索已注册的适配器。
- `default_registry`：进程级便利注册表。

## 数据 Lake

- `LocalDataLake(root)`：本地文件系统快照后端。
- `DataLakeManager(lake, registry=None)`：高级突变和更新 API。
- `DataLakeManager.add(source, dataset, frame)`: add custom 数据.
- `DataLakeManager.edit(source, dataset, frame)`：替换数据集快照。
- `DataLakeManager.delete(source, dataset)`：删除数据集指针。
- `LocalDataLake.read(...)`：读取预计和日期过滤的数据。
- `LocalDataLake.read_panel_field(...)`：将合格的字段id整形为面板框架。

## Loader

- `Loader(registry=None, lake=None)`：湖优先检索立面。
- `Loader.source(name).load(...)`: return `LoadedDataset`.
- `Loader.source(name).load_panel(...)`: return `RetrievedPanel`.
- `LoadedDataset.data`：pandas 数据集负载。
- `RetrievedPanel.data`：一个字段的按资产日期框架。

## 元数据和合约

- `DataContract`：提供商或数据集合同。
- `DatasetSchema`：数据集级模式元数据。
- `FieldSchema`：字段级元数据。
- `Transform`：无状态数据帧转换管道。

## Tushare 助手

- `TushareDataSource`：从 `bagelquant_data.datasource` 公开的提供者适配器。
- `TushareTableUpdateSpec`：生产式表更新规范。
- `DataLakeManager.scan_tushare_updates(...)`：构建试运行更新报告。
- `DataLakeManager.execute_tushare_update_report(report, workers=4)`：执行已审核的作业。
