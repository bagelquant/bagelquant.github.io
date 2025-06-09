---
title: "GitHub CLI Tool"
tags:
  - setup
---

Github provides a CLI tool for Copilot. This tool can be used to interact with Copilot from the command line. This tool is useful for automating Copilot workflows and integrating Copilot with other tools.

[Official Document](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

## Installation

Install gh, a command-line tool that makes it easy to work with GitHub from the command line.

```shell
brew install gh
```

Authenticate with GitHub

```shell
gh auth login
```

Install the Copilot CLI

```shell
gh extension install github/gh-copilot
```

## Usage

Explain

```shell
gh copilot explain "<COMMAND>"
```

Suggest

```shell
gh copilot suggest "<COMMAND>"
```
