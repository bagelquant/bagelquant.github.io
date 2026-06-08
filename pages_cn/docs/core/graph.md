---
layout: page
title: "Graph"
permalink: /zh/docs/core/graph/
lang: zh
ref: "docs-core-graph"
alternate_lang_url: /docs/core/graph/
nav: docs_zh
---

# Graph

## 概览

`Graph` 代表研究逻辑的惰性链。

```python
price = Panel.from_domain(price_df, domain, name="price")
signal = rank(zscore(price), name="signal")
```

原始输入是 `Panel`。导出的信号是 `Graph`。

＃＃ 责任

图表管理：

- 逻辑链输出
- 依赖收集
- DAG验证
- 拓扑排序
- 图表规格
- 运行时委托
- 物化输出访问

验证拒绝循环、重复的节点名称、无效的父类型和
父节点数量无效的操作节点。

图不存储原始输入帧，也不包含特定于域的内容
操作方法。

## Output

在执行之前，输出访问会引发错误：

```python
signal.output
```

执行后，`Graph.output`是一个面板：

```python
signal.compute()
signal_panel = signal.output
```

计算下游图还会填充评估中间的输出
graphs.

## 多输出图

```python
strategy = Graph(outputs=[signal, prediction])
strategy.compute()
outputs = strategy.output
```

对于多输出图，`output` 是从输出名称到面板的映射。
