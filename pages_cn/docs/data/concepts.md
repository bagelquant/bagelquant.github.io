---
layout: page
title: "概念"
permalink: /zh/docs/data/concepts/
lang: zh
ref: "docs-data-concepts"
alternate_lang_url: /docs/data/concepts/
nav: docs_zh
---

# 概念

## 数据源

`DataSource` 隔离 `read`、`exists` 和 `describe` 后面的提供者访问。
适配器位于 `bagelquant_data.datasource` 中并使用 `DataRequest` 对象
因此调用者不依赖于特定于提供商的客户端 API。

## Loader

`Loader` 协调请求并返回标准化的 `LoadedDataset` 对象。
当配置了一个湖时，它首先读取本地湖快照，并且只命中一个
用于引导或显式刷新的提供程序。

## 数据湖管理器

`DataLakeManager` 拥有添加、编辑、删除、列表和手动提供程序更新功能
当地的湖泊。

每个源的第一个配置表是其类似 Universe 的参考表。为了
Tushare，这里是 `stock_basic`，已从上市刷新、已下架、已暂停
股票以避免生存偏差。

## Transform

转换是无状态的 DataFrame 操作，可以与
`Transform`.

## Metadata

元数据独立于数据而存在。合约描述数据集身份，
架构、新鲜度、所有权、版本和沿袭。

## 数据 Lake

Lake存储按数据源、表、年份和月份分隔。写入创建
不可变快照并更新表和分区级别的最新指针。
每个存储表都有一个 `date` 索引以及 `create_time` 和 `delete_flag`
列。该湖还维护源本地资产和字段 ID 表。
参考非面板式表格，例如 `stock_basic`，保留其
普通行索引，同时仍然接收生命周期列。

使用 `LocalDataLake.read` 进行直接表读取，使用 `read_panel_field` 进行
按资产日期面板，`fields` 用于现场目录，`asset_ids` 用于源
资产目录。

## Cache

缓存接口是可选的，不应更改数据集标识或
再现性保证。
