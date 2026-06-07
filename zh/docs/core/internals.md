---
layout: page
title: "Internal Documentation"
permalink: /zh/docs/core/internals/
lang: zh
ref: "docs-core-internals"
alternate_lang_url: /docs/core/internals/
nav: docs_zh
---

# 内部文档

本页描述了对维护人员有用的内部结构。用户应该
更喜欢公共 API 文档，除非它们正在扩展包。

## 运行时模型

每个操作调用都会创建一个内部节点：

- 父依赖项
- 操作身份
- 可串行化的配置
- 面向用户的名称和元数据
- 执行后缓存输出

公共 `Graph` 对象是这个惰性节点链的包装器。

## Execution

`Graph.compute()` 创建执行运行时并评估依赖关系
递归地。在一次计算调用中，共享上游节点被执行一次。
运行时在多输入组合之前验证域兼容性，
将操作函数应用于 pandas 框架，然后将结果包装回
`Panel` objects.

动态宇宙掩码在派生计算后重新应用，因此不活动
单元格不会泄漏到后续操作中。

## 哈希和缓存

面板和操作规范参与确定性缓存键。目前的
缓存在内存中，用于一次执行运行。持久缓存、增量缓存
失效和并行调度是未来的扩展。

## 操作注册表

内置操作模块使用以下定义变压器和作曲家功能
用户可以使用相同的装饰器。生成的参考文档来自
导出的操作目录：

```bash
uv run python scripts/generate_operator_reference.py
```

添加、删除或更改操作后重新生成引用
metadata.

## 模块边界

- `panel` 拥有域对齐和不可变数据容器。
- `graph` 拥有惰性图句柄和面向用户的计算/输出访问。
- `execution` 拥有依赖性评估。
- `transformer` 拥有一元帧操作。
- `composer` 拥有多输入帧操作。
- `registry`和`_operation`拥有操作元数据和装饰器。
