---
layout: page
title: "后端 API"
permalink: /zh/docs/data/backend-api/
lang: zh
ref: "docs-data-backend-api"
alternate_lang_url: /docs/data/backend-api/
nav: docs_zh
---

# 后端 API

`bagelquant-data` 通过 Python API 进行操作。主要工作流程为：

```text
DataSourceRegistry
  -> DataSource
  -> DataLakeManager
  -> LocalDataLake
  -> Loader / lake.read / lake.read_panel_field
```

## Setup

```python
from bagelquant_data.datasource import DataSourceRegistry, TushareDataSource
from bagelquant_data.lake import DataLakeManager, LocalDataLake

registry = DataSourceRegistry()
registry.register(TushareDataSource(token="your-token"))

lake = LocalDataLake(".bagelquant-data-lake")
manager = DataLakeManager(lake, registry=registry)
```

## 数据湖管理

`LocalDataLake` 拥有文件系统存储。它写入不可变的 Parquet 快照
在源/表分区下并维护 JSON 目录指针。

```python
manager.add("custom", "prices", frame)
manager.edit("custom", "prices", corrected_frame)
manager.delete("custom", "prices")

sources = manager.list_sources()
tables = manager.list_tables("custom")
snapshots = manager.snapshots("custom", "prices")
```

使用 `LocalDataLake.read` 进行直接后端读取：

```python
data = lake.read(
    "tushare",
    "daily",
    columns=("close",),
    start_date="2024-01-01",
    end_date="2024-01-31",
)
```

## 提供商更新

`DataLakeManager.update` 执行简单的提供程序读取和写入一个本地
snapshot.

```python
from bagelquant_data.datasource import DataRequest

manager.update(
    "tushare",
    DataRequest(
        dataset="daily",
        filters={"ts_code": "000001.SZ"},
        start_date="2024-01-01",
        end_date="2024-01-31",
    ),
)
```

对于 Tushare 生产式更新，刷新引用、扫描，然后执行
确认报告：

```python
from bagelquant_data.lake import TushareTableUpdateSpec, TushareTradingCalendarRef

manager.update_tushare_stock_basic()
manager.update_tushare_trading_calendar(start_date="2000-01-01")

report = manager.scan_tushare_updates(
    specs=(
        TushareTableUpdateSpec(
            table="daily",
            kind="price",
            trading_calendar=TushareTradingCalendarRef(
                name="trade_cal",
                table="trade_cal",
                date_column="cal_date",
                open_column="is_open",
            ),
        ),
    ),
    start_date="2024-01-01",
    end_date="2024-12-31",
)

manager.execute_tushare_update_report(report, workers=4)
```

报告是审查边界。它包含计划和可执行作业，因此
调用者可以在运行提供程序读取之前检查待处理的工作。

## Retrieval

`Loader` 返回带有数据、身份、谱系和信息的 `LoadedDataset` 对象
元数据。配置湖后，它首先读取本地快照并使用
提供程序仅用于引导或显式刷新。

```python
from bagelquant_data.loader import Loader

loaded = Loader(registry=registry, lake=lake).source("tushare").load(
    "daily",
    fields=("open", "close"),
    start_date="2024-01-01",
    end_date="2024-01-31",
)
```

对于面板形状的研究输入，请使用 `load_panel` 或 `load_panel_field`。
这些 API 返回普通的 pandas 对象，并且不导入下游包。

```python
retrieved = Loader(registry=registry, lake=lake).source("tushare").load_panel(
    dataset="daily",
    field="close",
    universe=["000001.SZ", "600000.SH"],
    start_date="2024-01-01",
    end_date="2024-12-31",
)

panel = lake.read_panel_field(
    "tushare_daily_close",
    start_date="2024-01-01",
    end_date="2024-12-31",
)
```

## Function 参考

-`DataRequest（数据集，字段=（），过滤器= {}，开始日期=无，结束日期=无，
version=None, snapshot=None, options={})`：提供程序读取请求。
- `DataSourceRegistry.register(source)`：注册提供者适配器。
- `DataSourceRegistry.resolve(name)`：检索已注册的提供者。
- `DataLakeManager.update(source, request, mode="overwrite")`：获取提供者
数据并编写湖快照。
- `DataLakeManager.scan_tushare_updates(...)`：构建试运行 Tushare 更新
  report.
- `DataLakeManager.execute_tushare_update_report(report, workers=4)`: execute
报告作业并写入快照。
- `LocalDataLake.read（源，数据集，列=无，开始日期=无，
end_date=None,year=None,month=None,snapshot=None)`：读取本地数据。
- `LocalDataLake.read_panel_field(qualified_id, start_date, end_date)`: shape a
将合格的字段 ID 放入按资产日期面板中。
- `Loader.source(name).load(...)`：加载数据集为 `LoadedDataset`。
- `Loader.source(name).load_panel(...)`：加载并塑造 `RetrievedPanel`。
