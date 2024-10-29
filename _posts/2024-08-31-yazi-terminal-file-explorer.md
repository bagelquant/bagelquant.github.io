---
tags:
  - setup
---

## Introduction

Yazi is a terminal file explorer written in Rust. I give it a quick try and found it's a good alternative to `ls` and `tree` command. It provides a more intuitive way to navigate files and directories in the terminal.

Also, yazi is built with Rust, which means it's fast and efficient. It's a good tool for those who prefer using the terminal for file management.

I am using MacOS, the content below is based on my experience with yazi on MacOS.

## Quick use

- [Document link](https://yazi-rs.github.io/docs/installation)

Install yazi with Homebrew:

```shell
brew install yazi
```

### Configs

You need to create a config files in your .config directory:

```shell
mkdir -p ~/.config/yazi
touch ~/.config/yazi/yazi.toml
touch ~/.config/yazi/theme.toml
touch ~/.config/yazi/keymap.toml
```

`yazi.toml`: The main configuration file.

```toml
[manager]
show_hidden = false
ratio = [1, 2, 5]

[opener]
edit = [
	{ run = 'nvim "$@"', block = true, for = "unix" },
	{ run = "nvim %*",   block = true, for = "windows" },
]

[plugin]
prepend_previewers = [
  { name = "*.md", run = "glow" },
]
```

### Using theme

`theme.toml`: The theme configuration file.

You need to install the theme first:

```shell
ya pack -a yazi-rs/flavors:catppuccin-macchiato
```

Then add the theme to the `theme.toml` file:

```toml
[flavor]
use = "catppuccin-macchiato"
```

## Demo

![yazi-demo](/assets/post_img/yazi-demo.png)

