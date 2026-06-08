---
layout: page
permalink: /zh/learn/techniques/portfolio/kelly-criterion/
lang: zh
ref: "learn-techniques-portfolio-kelly-criterion"
alternate_lang_url: /learn/techniques/portfolio/kelly-criterion/
---

# 凯利准则（Kelly Criterion）

## 核心思想

凯利准则是一种仓位配置（position sizing）框架，用于确定应投入多少资本，以最大化长期复利财富增长。

与均值–方差优化不同：

凯利直接优化复合收益增长。

核心问题：

> 在存在优势（edge）且结果存在不确定性的情况下，应该投入多少资本？

其结果是在重复独立机会下理论上的最优杠杆水平。

## 定义

对于二元下注问题：

- 获胜概率：$p$
- 失败概率：$q=1-p$
- 单位风险收益比：$b$

最优资金比例：

$$
f^=\frac{bp-q}{b}
$$

其中：

- $f^$ = 总财富中投入比例
- $b$ = 每单位风险对应收益
- $p$ = 胜率
- $q$ = 失败概率

特殊情况：赔率相等（$b=1$）

$$
f^=2p-1
$$

示例：

- $p=0.60\rightarrow f=0.2$
- $p=0.55\rightarrow f=0.1$
- $p=0.50\rightarrow f=0$

没有优势 → 不下注。

## 推导

假设进行重复投资。

财富演化：

$$
W_T
=
W_0
\prod_t(1+fR_t)
$$

凯利目标：

$$
\max_fE[\log(1+fR)]
$$

对数刻画复利增长。

等价形式：

$$
\max_f
\lim_{T\to\infty}
\frac1T
\log\left(\frac{W_T}{W_0}\right)
$$

## 连续收益版本

假设：

$$
R\sim(\mu,\sigma^2)
$$

近似凯利杠杆：

$$
f^
=
\frac{\mu}{\sigma^2}
$$

其中：

- $\mu$ = 超额收益
- $\sigma^2$ = 方差

解释：

- Alpha 越高 → 仓位越大
- 不确定性越高 → 杠杆越低

这是量化金融中常见公式。

## 分数凯利（Fractional Kelly）

完整凯利通常过于激进。

常见形式：

$$
f=\lambda f^*
$$

其中：

$$
\lambda\in[0.25,0.50]
$$

典型选择：

- 四分之一凯利
- 半凯利

原因：

- 参数估计误差
- 非平稳性
- 回撤控制
- 交易成本

## 与组合理论关系

高斯假设下：

$$
w^*
\propto
\Sigma^{-1}\mu
$$

类似：

- 最大夏普组合
- 无约束均值–方差优化

区别：

| 方法 | 目标 |
|---|---|
| 均值–方差 | 最大化效用 |
| 夏普比率 | 最大收益风险比 |
| 凯利 | 最大化几何增长 |

## 在量化股票中的应用

凯利思想常见于：

- 组合杠杆
- alpha 权重
- 资金配置
- 策略放大
- 风险预算

实际生产环境通常不会直接部署纯凯利。