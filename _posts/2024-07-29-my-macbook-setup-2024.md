---
title: "My MacBook Setup 2024" 
categories:
  - Mac Setup
tags:
  - productivity
  - MacOS
---

Windows has been my preferred desktop operating system since primary school, offering a wide array of apps, particularly games.

However, since graduating from college, I have gradually transitioned all my digital devices to the Apple ecosystem. I switched from Android to iOS, and from Windows to MacOS. The cohesive experience of MacOS, especially when used in conjunction with other Apple devices, has truly impressed me. Here's my eroductivity setup for MacOS.

## System Settings

- Keyboard
    - Increase key repeat rates
    - Reduce delay until repeat - Both changes are particularly helpful in VIM mode
    - Remap Capslock key to ESC
- Trackpad
    - Increase speed
    - Enable touch to tap
    - Enable three-finger dragging
- Desktop and Dock
    - Minimize windows using scale effect for quicker animation
    - Enable clicking on wallpaper to reveal desktop, only in stage manager
    - Hide dock use `Cmd + Option + D` to toggle

Set up keyboard repeat rate and delay until repeat

```shell
defaults write -g ApplePressAndHoldEnabled 0
```

Productivity tip: Prefer keyboard over mouse or trackpad. Navigating with a keyboard is quicker than moving the cursor. I use numerous keyboard shortcuts and prefer VIM mode when writing and coding. Wondering how to navigate using a keyboard? An app called Raycast can be extremely useful. Introduction provided below.

## Homebrew and terminal

Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's macOS operating system and Linux. It is known as the "missing package manager for macOS" and is a convenient way to install and manage different software packages from the command line.

### Install oh-my-zsh

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

We will edit the `.zshrc` file later to customize the terminal.

### Install Homebrew

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


## Apps

Using homebrew install all my apps

- Coding
  - miniconda --> [Miniconda setting MacOS](https://bagelquant.github.io/mac%20setup/miniconda-setting-macos/)
  - iterm2
  - qt-creator
- Productivity
  - raycast
  - zoom
- Utility
  - ityscal
  - karabiner-elements

```shell
brew install --cask miniconda iterm2 Raycast zoom itsycal qt-creator karabiner-elements logitech-options obsidian pdf-expert
```

## Packages

Here is some main package I use:

- nvim --> [My Neovim journey](https://bagelquant.github.io/neovim/neovim-journey/)
- thefuck
- gh --> [gh - A GitHub CLI tool](https://bagelquant.github.io/mac%20setup/gh-github-cli-tool/)
- pandoc

```shell
brew install nvim thefuck gh pyright zsh-syntax-highlighting zsh-autosuggestions mysql font-jetbrains-mono-nerd-font ripgrep fd pandoc basictex texlive fzf
```

Use command below to add zsh-syntax-highlighting and zsh-autosuyggestions to `.zshrc` file

```shell
source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

```shell
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
```

