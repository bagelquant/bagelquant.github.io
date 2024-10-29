---
title: "MacBook Setup Fall 2024" 
tags:
  - setup
---

## System Settings

- Keyboard
    - Increase key repeat rates
    - Reduce delay until repeat - Both changes are particularly helpful in VIM mode
    - Remap `Capslock` key to `ESC`
- Trackpad
    - Increase speed
    - Enable touch to tap
    - Enable three-finger dragging
- Desktop and Dock
    - Minimize windows using scale effect for quicker animation
    - Change clicking on wallpaper to reveal desktop, only in stage manager

Set up keyboard repeat rate and delay until repeat

```shell
defaults write -g ApplePressAndHoldEnabled 0
```

## Homebrew and terminal

### Install oh-my-zsh

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Install Homebrew

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Apps

```shell
brew install --cask miniconda iterm2 Raycast zoom itsycal karabiner-elements pdf-expert cmake
```

The window manage app:

```shell
brew install --cask nikitabobko/tap/aerospace
```
## Git configs

- Config gh: [gh - A GitHub CLI tool](https://bagelquant.github.io/mac%20setup/gh-github-cli-tool/)
- config user name and email

```shell
git config --global user.name ""
git config --global user.email ""
```

## Packages

```shell
brew install nvim thefuck gh zsh-syntax-highlighting zsh-autosuggestions font-jetbrains-mono-nerd-font ripgrep fd pandoc basictex texlive fzf npm wget gcc yazi r 
```

yazi dependencies(previews):

```shell
brew install ffmpegthumbnailer poppler 
```

> imagemagick (for yazi img preview) already install

## Dot configs

All dot files configs stored in Github Repo

- iterm2
- Yazi
- Aeropace
- nvim
- .zshrc

