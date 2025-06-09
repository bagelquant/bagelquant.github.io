---
title: "Integrating Mermaid with Pandoc"
tags: 
    - pandoc
---

When converting a markdown file to a pdf file, the mermaid diagram is not rendered. This is because the default pandoc markdown engine does not support mermaid diagrams. The solution is to use a markdown engine that supports mermaid diagrams.

## Install `mermaid-filter`

To render mermaid diagrams, use the `mermaid-filter` filter. To install the `mermaid-filter` filter, run the following command:

```shell
npm i -g mermaid-filter
```

> Assuming you have installed Node.js and npm.

Also, install texlive to render the pdf file:

```shell
brew install texlive
```

## Usage

```shell
pandoc SAMPLE.md -o SAMPLE.pdf --pdf-engine=xelatex -F mermaid-filter
```
