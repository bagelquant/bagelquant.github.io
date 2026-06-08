---
layout: page
title: "Architecture And Design"
permalink: /zh/docs/data/architecture/
lang: zh
ref: "docs-data-architecture"
alternate_lang_url: /docs/data/architecture/
nav: docs_zh
---

# 架构

```text
Provider APIs and files
    |
    v
DataSource
    |
    v
DataLakeManager.update
    |
    v
LocalDataLake
    |
    +--> LoadedDataset
    |
    +--> RetrievedPanel
             |
             v
       downstream adapter
```

正常路径是提供者到当地湖泊再到用户。 `Loader`从本地读取
配置时首先是 Lake。提供者访问用于引导和刷新。
所有操作均作为后端Python API公开；这里没有 GUI 层
package.

该包保留提供者访问、元数据、转换和存储
接口独立。本地V1存储使用源/表/年/月Parquet
带有 JSON 元数据的快照，而接口则为未来留有空间
Iceberg、Delta、对象存储或云后端。

```text
lake-root/
  tushare/
    daily/
      year=2024/
        month=01/
          snapshots/
```

读取可以投影列并过滤湖边界处的日期。 `LocalDataLake`
使用分区元数据跳过请求范围之外的快照，然后
阅读后应用精确的日期过滤。这使 API 保持简单，同时
减少常见面板字段和日期窗口读取的 IO。

Lake 维护资产 ID 和字段 ID 的源级系统目录。
表目录元数据记录推断的日期、资产和面板字段列，以便
`read_panel_field` 只能加载请求的字段加上最小日期和
形成按资产日期面板所需的资产列。

## 依赖方向

`bagelquant-data` 低于下游存储库。一定不能导入
`bagelquant-core`、`bagelquant-bt`、`bagelquant-app` 或文档站点。

与 `bagelquant-core` 的通信边界是普通检索数据。
`RetrievedPanel` 公开 pandas 数据、宇宙和排序的日历对象，
让下游代码负责创建 `Domain`、`Panel` 和
`CategoryPanel` 不耦合封装。

## Tushare 更新规格

提供程序更新通过 `TushareTableUpdateSpec` 进行描述。规范保留一个
表的种类、更新宇宙引用和交易日历引用在一个对象中，
这避免了并行参数图逐渐分开。经理将规格扫描到
空运行 `TushareUpdateReport`，执行仅消耗已确认的作业
从该报告中。

## 模块结构

- `datasource` 拥有提供者适配器、请求和源注册。
- `lake`拥有本地存储、快照目录、直接读取和更新
编排。
- `loader` 拥有湖优先检索和普通面板形状的返回对象。
- `metadata` 拥有模式、契约、身份和沿袭记录。
- `transform` 拥有无状态 DataFrame 转换管道。
- `cache` 拥有可选的缓存策略和实现。
