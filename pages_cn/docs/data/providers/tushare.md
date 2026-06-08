---
layout: page
title: "Tushare Provider"
permalink: /zh/docs/data/providers/tushare/
lang: zh
ref: "docs-data-providers-tushare"
alternate_lang_url: /docs/data/providers/tushare/
nav: docs_zh
---

# Tushare

Tushare 是第一个 V1 提供商适配器。

安装可选依赖项：

```bash
uv sync --extra tushare
```

显式提供令牌：

```python
from bagelquant_data.datasource import TushareDataSource

source = TushareDataSource(token="your-token")
```

或者通过环境：

```bash
export TUSHARE_TOKEN=your-token
```

支持的V1数据集：

- `stock_basic`
- `trade_cal`
- `daily`
- `index_daily`
- `generic` with `options={"api_name": "..."}`

Tushare 日期标准化为 `YYYYMMDD`。令牌永远不会包含在
`describe()` output.

当 Tushare 数据被摄取到 `LocalDataLake` 中时，`daily` 等表
存储在 `tushare` 源命名空间下并按 `trade_date` 分区
年/月/日。

## 参考 Resources

Tushare `All` 宇宙源自 `stock_basic`。刷新阅读列表
状态 `L`、`D` 和 `P`，然后通过 `ts_code` 去重复，因此除名并
暂停的库存仍然可用，避免了幸存者偏差。资产 ID 为
存储为 `tushare_<ts_code>`，例如 `tushare_000300.SH`。

Tushare 表更新还使用 `trade_cal` 的本地交易日历。
默认日历读取 `cal_date` 并使用 `is_open == 1` 作为交易日。
参考资源的刷新与正常的表更新分开，因此
增量价格刷新不会覆盖 `stock_basic` 或 `trade_cal`。

来源可以定义多个宇宙。例如，索引工作流可以添加
`index_basic` Universe 并将面向索引的表绑定到 `index_basic.ts_code`
而不是默认的股票宇宙。

## 更新策略

- `stock_basic` 从列出、除名和暂停中刷新所有宇宙
股票； `trade_cal` 刷新源交易日历。
- 宇宙和交易日历作为参考资源进行更新，单独
来自正常的表扫描和执行。
- 可以首先从紧凑的更新记录系统表中扫描更新，
生成待处理表、有效开始日期和可执行文件的报告
  jobs.
- `daily` 和 `index_daily` 在开放交易日逐日获取
关联的交易日历以避免 Tushare 行限制。
- 通过 `__tushare_price_update_records` 跳过现有价格日期
以日为粒度存储，因此添加新交易日不会重写
  older days.
- 基本表在关联的更新 Universe 表中为每个代码创建一个作业，
从该资产的最新日期开始
`__tushare_fundamental_update_records`；边界行已去重复
  locally.
- VIP基本表如`income_vip`按报告季节获取
使用 `period`，按年/季度存储，并在季度已经存在时跳过
本地存在。
- 默认更新范围是 `2000-01-01` 到今天。
- 提供程序请求可以与 `workers` 设置同时运行。
