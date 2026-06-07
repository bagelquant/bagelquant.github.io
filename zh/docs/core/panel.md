---
layout: page
title: "Panel"
permalink: /zh/docs/core/panel/
lang: zh
ref: "docs-core-panel"
alternate_lang_url: /docs/core/panel/
nav: docs_zh
---

# Panel

## 概览

`Panel` 是 BagelQuant 中的显式数据对象。每个输入面板都是
通过 `Domain` 创建，定义交易会话和资产
会员资格。面板存储一个数字二维框架：

```text
Time x Assets
```

```python
import pandas as pd

from bagelquant_core import Domain, Panel

domain = Domain(
    calendar=pd.bdate_range("2024-01-01", "2024-12-31"),
    universe=["AAPL", "MSFT"],
)
price = Panel.from_domain(price_df, domain, name="price")
```

## Role

Panels are:

- Raw input 数据
- DAG叶节点
- 物化图输出
- 内部执行运行时存储的缓存值

因子、预测和组合权重通常表示为惰性
图表，直到需要其输出面板为止。

## 不变量

Panels:

- 拥有一维唯一索引
- 具有一维独特的列
- 仅包含数值
- 在构建时复制输入数据
- 通过 `Panel.data` 访问数据时返回防御副本
- 对于公共 API 是不可变的
- 匹配其域的交易会话索引和宇宙列
- 为动态宇宙屏蔽不活跃的细胞

## Alignment

多输入编辑器函数需要等效的域。运行时
在每次导出计算后重新应用动态宇宙成员资格，因此
不活跃的单元格不会影响后续操作。

## 动态宇宙

动态 Universe 是按日期和资产列索引的布尔框架。
缺少的行和单元格处于非活动状态；成员资格不会被转发：

```python
membership = pd.DataFrame(
    {"AAPL": [True], "MSFT": [False]},
    index=pd.to_datetime(["2024-01-03"]),
)
domain = Domain(
    calendar=pd.bdate_range("2024-01-01", "2024-01-31"),
    universe=membership,
)
```

## Calendar

`Domain` 从不检索日历。提供一个非空、唯一、已排序的
来自数据层的日历。第一个和最后一个会话定义域的
开始和结束日期。

## 类别面板

`CategoryPanel` 是一个不可变的叶子节点，用于标签，例如行业、部门、
或国家。它遵循与 `Panel` 相同的时间资产形状，但接受
字符串标签：

```python
import pandas as pd

from bagelquant_core import CategoryPanel

industry = CategoryPanel.from_domain(
    pd.DataFrame(...),
    domain,
    name="industry",
)
```

使用类别面板以及从以下位置导出的类别操作
`bagelquant_core.transformer`.
