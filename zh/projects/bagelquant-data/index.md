---
layout: page
title: "bagelquant-data"
permalink: /zh/projects/bagelquant-data/
excerpt: "提供商中立的数据访问、本地湖泊快照和面板检索。"
lang: zh
ref: "projects-bagelquant-data"
alternate_lang_url: /projects/bagelquant-data/
---

`bagelquant-data` 是 BagelQuant 的数据层。它拥有提供者适配器，
本地湖泊快照、元数据合约、转换管道，以及
面板状检索。

## 它包含什么

- 提供商注册和 `DataRequest` 对象。
- 通过 `LocalDataLake` 进行本地 Parquet 快照存储。
- `DataLakeManager` 更新和管理工作流程。
- Lake-first `Loader` 检索。
- `RetrievedPanel` 下游研究包的交接对象。
- Tushare 特定的更新助手。

## 文档

- [Quick start](/zh/docs/data/quick-start/)
- [架构 and design](/zh/docs/data/architecture/)
- [公开 API](/zh/docs/data/public-api/)
- [Internal documentation](/zh/docs/data/internals/)
- [后端 API](/zh/docs/data/backend-api/)
- [Tushare provider](/zh/docs/data/providers/tushare/)
