---
layout: page
title: "执行"
permalink: /zh/docs/core/execution/
lang: zh
ref: "docs-core-execution"
alternate_lang_url: /docs/core/execution/
nav: docs_zh
---

# 执行模型

## 概览

图表定义了应该计算的内容。调用 `Graph.compute()` 实现
输出面板并缓存执行期间的中间结果。

```python
signal.compute()
panel = signal.output
```

## Pipeline

```text
Graph construction
    -> validation
    -> dependency resolution
    -> panel alignment
    -> node evaluation
    -> Panel output creation
    -> cache storage or reuse
    -> Graph.output population
```

## 中间输出

执行下游图会评估其依赖性。每一个评价的
派生节点接收面板输出：

```python
signal.compute()
prediction_panel = prediction.output
signal_panel = signal.output
```

## 当前语义

- 执行是确定性的。
- 面板对于公共 API 是不可变的。
- 默认情况下，多输入框架在相交的索引和列上对齐。
- 中间缓存值是面板。
- 共享 DAG 节点每次运行时调用都会评估一次。
- 当对齐不改变输入帧时，将重复使用存储的面板散列。
- 日程安排是连续的。

并行调度、持久缓存和显式失效仍将在未来出现
扩展。
