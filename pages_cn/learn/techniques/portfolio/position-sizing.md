---
layout: page
permalink: /zh/learn/techniques/portfolio/position-sizing/
lang: zh
ref: "learn-techniques-portfolio-position-sizing"
alternate_lang_url: /learn/techniques/portfolio/position-sizing/
---

# 仓位管理（Position Sizing）

## 核心思想

仓位管理决定：

每个投资机会应分配多少资本。

好的信号并不足够。

组合表现同时取决于：

- 信号质量
- 资金配置
- 分散化
- 风险控制

核心问题：

> 给定多个机会，每个头寸应该承担多少权重？

仓位管理负责把预测转化为可执行组合。

## 定义

给定：

- 信号向量：$\alpha$
- 权重：$w$

定义：

$$
w=f(\alpha)
$$

约束：

$$
\sum_i|w_i|\le L
$$

其中：

- $w_i$ = 资产权重
- $\alpha_i$ = 预期收益
- $L$ = 杠杆上限

## 等权配置

最简单方法：

$$
w_i=\frac1N
$$

特点：

- 简单
- 高分散
- 不考虑信号强弱

## 信号加权

按信号强度配置：

$$
w_i
=
\frac{\alpha_i}
{\sum_j|\alpha_j|}
$$

解释：

- alpha 越强 → 仓位越高
- alpha 越弱 → 仓位越低

## 波动率调整

按风险缩放：

$$
w_i
\propto
\frac{\alpha_i}{\sigma_i}
$$

其中：

- $\sigma_i$ = 波动率

## 凯利仓位

凯利形式：

$$
w_i
\propto
\frac{\alpha_i}{\sigma_i^2}
$$

解释：

收益驱动配置，

风险控制杠杆。

## 仓位约束

生产环境通常加入：

$$
w_i\in[w_{\min},w_{\max}]
$$

包括：

- 杠杆限制
- 行业约束
- 换手约束
- 流动性约束
- 回撤约束

## 在量化股票中的应用

仓位管理广泛出现于：

- 因子组合
- alpha 融合
- 投资组合优化
- 执行调度
- 杠杆控制

很多时候：

仓位设计的重要性不低于信号本身。