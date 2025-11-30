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

```zsh
defaults write -g ApplePressAndHoldEnabled 0
```

## Apps

Homebrew

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Casks

```zsh
brew install --cask miniconda zoom pdf-expert raycast r-app rstudio google-chrome microsoft-teams chatgpt visual-studio-code blackhole-16ch iterm2 zed zen
```

Formulas

```zsh
brew install nvim gh zsh-syntax-highlighting zsh-autosuggestions font-jetbrains-mono-nerd-font ripgrep fd pandoc basictex texlive fzf npm wget gcc yazi lazygit ffmpegthumbnailer poppler deno pkg-config mysql
```

aerospace

```zsh
brew install --cask nikitabobko/tap/aerospace
```

add border to active window

```zsh
brew tap FelixKratz/formulae
brew install borders
```

add sketchybar

```zsh
brew tap FelixKratz/formulae
brew install sketchybar
brew install --cask font-hack-nerd-font
```

[install ruby and run jekyll](https://bagelquant.com/install-ruby-run-jekyll-local/)

## Conda

```zsh
conda config --set auto_activate false
```

