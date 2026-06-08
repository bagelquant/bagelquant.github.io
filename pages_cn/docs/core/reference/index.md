---
layout: page
title: "概览"
permalink: /zh/docs/core/reference/
lang: zh
ref: "docs-core-reference"
alternate_lang_url: /docs/core/reference/
nav: docs_zh
---

# API 参考

BagelQuant 操作从 `Panel` 输入构建惰性图。

- [Transformer reference](./transformers/index.md)：85 个公共操作
- [Composer reference](./composers/index.md)：49 个公共操作

参考页面是从导出的 API 生成并精心策划的
文档元数据。更改操作目录后重新生成它们：

```bash
uv run python scripts/generate_operator_reference.py
```
