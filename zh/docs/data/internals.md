---
layout: page
title: "Internal Documentation"
permalink: /zh/docs/data/internals/
lang: zh
ref: "docs-data-internals"
alternate_lang_url: /docs/data/internals/
nav: docs_zh
---

# 内部文档

本页描述了维护者和扩展的实现边界
authors.

## 依赖方向

`bagelquant-data` 位于生态系统其他部分的下方。一定不能导入
`bagelquant-core`、`bagelquant-bt`、`bagelquant-app` 或网站。

到 `bagelquant-core` 的切换是简单的数据：`RetrievedPanel` 公开了一个
DataFrame、排序日历和 Universe。下游代码构造`Domain`
和 `Panel` 对象本身。

## 存储布局

本地V1存储按源、表、年、月分区：

```text
lake-root/
  tushare/
    daily/
      year=2024/
        month=01/
          snapshots/
```

JSON 目录跟踪源级 ID、表元数据、最新快照指针、
和推断的面板字段。读取使用分区元数据来跳过快照
超出请求的日期范围，然后在加载后应用精确过滤。

## 更新流程

正常提供者刷新：

```text
DataRequest -> DataSource.read -> DataLakeManager.update -> LocalDataLake.write
```

Tushare生产式刷新：

```text
reference refresh -> scan_tushare_updates -> review report -> execute jobs
```

报告是审查边界。执行应该消耗已确认的作业
从该报告中，而不是隐含地重建计划。

## 模块结构

- `datasource`：提供者适配器、请求对象和注册表。
- `lake`：快照存储、目录、直接读取和更新编排。
- `loader`：湖泊优先检索和面板状返回物体。
- `metadata`：模式、契约、身份和血统。
- `transform`：无状态数据帧转换管道。
- `cache`：可选的缓存策略和实现。
- `config`：环境和配置文件设置。

## 失败处理

提供者和湖泊错误应包括来源、数据集、请求的日期
范围，并尽可能进行操作。缺少可选的提供程序依赖项
应该在适配器构造或第一个提供者使用时失败，而不是在打包期间失败
import.
