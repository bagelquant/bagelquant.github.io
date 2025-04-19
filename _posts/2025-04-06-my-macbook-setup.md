---
title: "My MacBook Setup"
tags:
    - setup
---
Windows has been my preferred desktop operating system since primary school, offering a wide array of apps, particularly games.

However, since graduating from college, I have gradually transitioned all my digital devices to the Apple ecosystem. I switched from Android to iOS, and from Windows to MacOS. The cohesive experience of MacOS, especially when used in conjunction with other Apple devices, has truly impressed me. Here's my productivity setup for MacOS.

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
    - Enable clicking on wallpaper to reveal desktop, only in stage manager
    - Hide dock use `Cmd + Option + D` to toggle

Set up keyboard repeat rate and delay until repeat

Productivity tip: Prefer keyboard over mouse or trackpad. Navigating with a keyboard is quicker than moving the cursor. I use numerous keyboard shortcuts and prefer VIM mode when writing and coding. Wondering how to navigate using a keyboard? An app called Raycast can be extremely useful. Introduction provided below.


## Configs

```shell
defaults write -g ApplePressAndHoldEnabled 0
```

## Apps

Homebrew

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Casks

```shell
brew install --cask miniconda Raycast zoom itsycal pdf-expert r rstudio google-chrome microsoft-teams visual-studio-code
```

Formulas

```shell
brew install gh zsh-syntax-highlighting zsh-autosuggestions pandoc mysql
```

## Conda

```shell
conda config --set auto_activate_base false
```
