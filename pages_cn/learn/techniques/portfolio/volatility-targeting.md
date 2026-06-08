---
layout: page
permalink: /zh/learn/techniques/portfolio/volatility-targeting/
lang: zh
ref: "learn-techniques-portfolio-volatility-targeting"
alternate_lang_url: /learn/techniques/portfolio/volatility-targeting/
---

# 波动率目标（Volatility Targeting）

## 核心思想

波动率目标通过动态调整组合暴露，使组合维持在预设风险水平附近。

与预测收益不同：

它控制风险。

核心问题：

> 当市场风险发生变化时，应如何调整仓位与杠杆？

波动率目标本质上是一种动态风险管理机制。

## 定义

目标波动率：

$$
\sigma^*
$$

组合当前估计波动率：

$$
\hat\sigma_t
$$

缩放系数：

$$
k_t
=
\frac{\sigma^}{\hat\sigma_t}
$$

调整后权重：

$$
w_t
=
k_tw_0
$$

其中：

- $\sigma^$ = 目标波动率
- $\hat\sigma_t$ = 当前估计波动率
- $k_t$ = 杠杆调整倍数
- $w_0$ = 原始组合权重

解释：

- 波动率升高 → 降低仓位
- 波动率下降 → 提高仓位

## 示例

假设组合：

- 目标波动率：$10%$
- 当前波动率：$20%$

则：

$$
k
=
\frac{10}{20}
=
0.5
$$

调整后暴露：

$$
50%
$$

即：

组合减仓一半。

若当前波动率下降至：

$$
5%
$$

则：

$$
k=2
$$

组合暴露翻倍。

## 波动率估计

常见估计方法：

滚动窗口：

$$
\hat\sigma_t
=
\sqrt{
252
\cdot
\operatorname{Var}(r)
}
$$

其中：

- $r$ = 日收益率
- $252$ = 年化交易日

指数加权移动平均（EWMA）：

$$
\sigma_t^2
=
\lambda\sigma_{t-1}^2
+
(1-\lambda)r_t^2
$$

常见取值：

$$
\lambda=0.94\sim0.99
$$

特点：

- 更关注近期风险变化
- 响应速度更快

## 与凯利准则关系

连续收益凯利公式：

$$
f^*
=
\frac{\mu}{\sigma^2}
$$

波动率目标则保持：

$$
f\sigma
\approx
\text{常数}
$$

区别：

- 凯利决定理论最优杠杆
- 波动率目标控制实际风险暴露

二者常组合使用：

先生成组合，

再进行波动率缩放。

## 优势与局限

优势：

- 平滑风险暴露
- 控制回撤
- 提升杠杆稳定性
- 提高组合可预测性

潜在问题：

- 对突发风险反应滞后
- 容易产生频繁调仓
- 增加交易成本
- 可能削弱上涨行情收益

## 与风险平价关系

二者都关注风险控制。

区别：

| 方法 | 调整对象 |
|---|---|
| 风险平价 | 横截面风险分配 |
| 波动率目标 | 时间序列风险调整 |

风险平价决定：

资产之间如何分配。

波动率目标决定：

整体仓位大小。

二者经常同时使用。

## 在量化股票中的应用

波动率目标广泛应用于：

- 组合杠杆管理
- 因子风险控制
- CTA 策略
- 多资产配置
- 风险预算
- 实盘组合稳定化

典型流程：

$$
\text{信号}
\rightarrow
\text{组合构建}
\rightarrow
\text{波动率目标}
\rightarrow
\text{执行}
$$

在现代量化投资中，

波动率目标是最常见的组合覆盖层（portfolio overlay）之一。