---
layout: page
permalink: /zh/learn/techniques/portfolio/risk-parity/
lang: zh
ref: "learn-techniques-portfolio-risk-parity"
alternate_lang_url: /learn/techniques/portfolio/risk-parity/
---

# 风险平价（Risk Parity）

## 核心思想

风险平价配置的是：

风险，而不是资金。

传统组合分配资本。

风险平价分配波动率。

核心问题：

> 如何分配资本，使任何资产都不会主导整体风险？

## 定义

组合波动率：

$$
\sigma_p
=
\sqrt{w^\top\Sigma w}
$$

资产风险贡献：

$$
RC_i
=
w_i
\frac{(\Sigma w)_i}
{\sigma_p}
$$

风险平价要求：

$$
RC_1
=
RC_2
=
\cdots
=
RC_N
$$

即所有资产承担相同风险。

## 等波动近似

忽略相关性：

$$
w_i
\propto
\frac1{\sigma_i}
$$

解释：

- 波动低 → 权重大
- 波动高 → 权重小

## 杠杆

风险平价常需要杠杆。

原因：

- 低风险资产占比提高
- 组合收益下降

通过杠杆恢复目标收益。

## 与均值–方差关系

均值–方差：

$$
\max
w^\top\mu
-
\lambda w^\top\Sigma w
$$

区别：

| 方法 | 目标 |
|---|---|
| 等权 | 等资本 |
| 均值–方差 | 最大效用 |
| 风险平价 | 等风险 |

## 在量化投资中的应用

风险平价常见于：

- 多资产组合
- 因子配置
- 风险预算
- 策略融合
- 波动管理

生产环境通常加入：

- 协方差收缩
- 换手控制
- 暴露限制
- 杠杆约束