---
layout: page
title: "bagelquant-core"
permalink: /zh/projects/bagelquant-core/
excerpt: "面板数据、惰性图逻辑和用于定量研究的可重用操作。"
lang: zh
ref: "projects-bagelquant-core"
alternate_lang_url: /projects/bagelquant-core/
---

`bagelquant-core` 是 BagelQuant 生态系统的共享研究内核。
它将对齐的面板数据转换为可以组合的惰性图逻辑，
执行、缓存和重用。

## 它包含什么

- `Domain`、`Panel` 和 `CategoryPanel` 数据容器。
- 用于因子、预测和权重逻辑的惰性 `Graph` 对象。
- 用于一元面板操作的变压器函数。
- 用于多输入操作的作曲家功能。
- 内部执行运行时和操作元数据。

## 文档

- [Quick start](/zh/docs/core/quick-start/)
- [架构 and design](/zh/docs/core/architecture/)
- [公开 API](/zh/docs/core/public-api/)
- [Internal documentation](/zh/docs/core/internals/)
- [Transformer reference](/zh/docs/core/reference/transformers/)
- [Composer reference](/zh/docs/core/reference/composers/)
