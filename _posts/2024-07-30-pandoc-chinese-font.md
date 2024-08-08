---
title: "Pandoc 中文字符无法显示"
date: 2024-07-30
categories:
  - terminal
tags:
  - writing
  - productivity
---

将 markdown 文件转换为 pdf 文件时，中文字符无法显示，这是因为 pandoc 默认使用的字体不支持中文字符。解决方法是使用支持中文字符的字体。

## 解决方法

使用`xelatex`引擎，指定字体为`PingFang SC`。

### Homebrew 安装xelatex

```shell
brew install texlive
```

### 使用xelatex引擎

```shell
pandoc SAMPLE.md -o SAMPLE.pdf --pdf-engine=xelatex
```

这样就可以将 markdown 文件转换为 pdf 文件，但由于缺少字体，中文字符还是无法显示

### 指定字体

```shell
pandoc SAMPLE.md -o SAMPLE.pdf --pdf-engine=xelatex -V mainfont="PingFang SC"
```

