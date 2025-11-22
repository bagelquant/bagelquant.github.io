---
title: "My MacBook Setup" 
layout: post
---

Updated on Nov 14, 2025

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
brew install --cask miniconda zoom itsycal pdf-expert raycast r-app rstudio google-chrome microsoft-teams chatgpt visual-studio-code blackhole-16ch karabiner-elements pronotes iterm2
```

Formulas

```shell
brew install nvim gh zsh-syntax-highlighting zsh-autosuggestions font-jetbrains-mono-nerd-font ripgrep fd pandoc basictex texlive fzf npm wget gcc yazi lazygit ffmpegthumbnailer poppler deno pkg-config mysql aerospace
```

add border to active window

```shell
brew tap FelixKratz/formulae
brew install borders
```


## Conda

```shell
conda config --set auto_activate false
```
