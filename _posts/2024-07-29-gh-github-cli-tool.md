---
title: "GitHub CLI Tool"
author: "Eric"
categories:
  - Mac Setup
tags:
  - productivity
  - copilot
---

Github provides a CLI tool for Copilot. This tool can be used to interact with Copilot from the command line. This tool is useful for automating Copilot workflows and integrating Copilot with other tools.

[Official Document](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

## Installation

1. install gh, a command-line tool that makes it easy to work with GitHub from the command line.

```shell
brew install gh
```

2. Authenticate with GitHub

```shell
gh auth login
```

3. Install the Copilot CLI

```shell
gh extension install github/gh-copilot
```

## Usage

1. Explain

```shell
gh copilot explain "<COMMAND>"
```

2. Suggest

```shell
gh copilot suggest "<COMMAND>"
```

