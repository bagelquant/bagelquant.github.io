---
title: "Pandoc Include Code Highlight"
tags:
    - pandoc
---

Covertign a markdown file to a pdf file, the code block is not highlighted. This is because the default pandoc markdown engine does not support code highlighting. The solution is to use a markdown engine that supports code highlighting.

## Default highlight options

Pandoc supports code highlighting with the following options:

- `--highlight-style` or `-H`: specify the style of code highlighting
- `--list-highlight-languages`: list supported languages for code highlighting
- `--list-highlight-styles`: list supported styles for code highlighting

## Use `--highlight-style` option

To specify the style of code highlighting, use the `--highlight-style` option. For example, to use the `tango` style, run the following command:

```shell
pandoc SAMPLE.md -o SAMPLE.pdf --highlight-style tango
```

## Examples

![Pandoc Syntax Highlighting Color Schemes Examples](https://github.com/kaityo256/pandoc_highlight)
