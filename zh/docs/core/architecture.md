---
layout: page
title: "Architecture And Design"
permalink: /zh/docs/core/architecture/
lang: zh
ref: "docs-core-architecture"
alternate_lang_url: /docs/core/architecture/
nav: docs_zh
---

# BagelQuant 核心架构

## 概览

BagelQuant 将具体面板数据与惰性图逻辑分开。

```text
Panel inputs
    |
    v
Transformer and Composer functions
    |
    v
Graph logic chains
    |
    v
Internal execution runtime
    |
    v
Cached Panel outputs
```

## Panel

`Panel` 是按时间和资产索引的不可变数字框架。每个输入
通过 `Domain` 进行标准化，`Domain` 拥有其交易会话和资产
会员资格。面板通过 `Panel.data` 返回防御副本。

```python
price = Panel.from_domain(price_df, domain, name="price")
```

面板是 DAG 叶子和执行输出。

## Graph

`Graph` 表示惰性派生逻辑：

```python
bm_ratio = div(book, price, name="bm_ratio")
bm_factor = rank(zscore(bm_ratio), name="bm_factor")
```

图职责：

- 收集依赖项
- 验证DAG结构
- 公开可重复的规格
- 委托执行
- 执行后暴露物化的`output`面板

图不拥有域操作或原始输入数据。

## 变压器函数

变压器是一元的：

```text
Panel | Graph -> Graph
```

```python
signal = rank(raw_factor, name="signal")
```

定制变压器使用 `@transformer`。

## 作曲家功能

作曲家接受一个或多个输入：

```text
(Panel | Graph, ...) -> Graph
```

```python
bm_ratio = div(book, price, name="bm_ratio")
```

自定义作曲家使用 `@composer`。

## 内部节点

调用操作会创建一个内部节点，该节点存储：

- 父节点
- 合格的操作名称
- 可串行化的配置
- 节点名称和元数据
- 执行后缓存输出面板

用户不直接构造内部节点。

## Execution

调用 `Graph.compute()` 会递归地调用内部运行时
评估依赖关系，检查多输入域兼容性，计算
确定性缓存键，在执行期间缓存输出面板，并更新
节点输出。动态成员资格掩码被重新应用于导出的输出。
在一次运行时调用内，共享 DAG 节点将被评估一次。什么时候
作曲家输入已经对齐，运行时重用现有框架
以及它们存储的哈希值。

```python
signal.compute()
panel = signal.output
```

在当前的实现中，调度是顺序的。并行调度，
持久化缓存和增量失效仍然是未来的工作。
