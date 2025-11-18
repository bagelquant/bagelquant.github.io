---
title: Miniconda Setting on macOS
tags:
  - setup
---

Use Homebrew to install Miniconda.

```shell
brew install --cask miniconda
```

## Initialized miniconda

```shell
conda init
```

Init in zsh

```shell
conda init zsh
```

## Do not enter base environment when launching terminal

```shell
conda config --set auto_activate_base false
```

