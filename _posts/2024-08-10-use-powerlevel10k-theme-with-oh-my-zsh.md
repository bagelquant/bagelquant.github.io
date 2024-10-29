---
title: "Use Powerlevel10k Theme with Oh My Zsh"
date: 2024-08-08
tags:
  - setup
---

I used to use the default terminal theme that comes with Oh My Zsh. However, I recently switched to the Powerlevel10k theme, which is highly customizable anIn this post, I will show you how to install and configure the Powerlevel10k theme with Oh My Zsh.

## Installations

### Install oh-my-zsh

If you haven't already installed Oh My Zsh, you can do so by running the following command:

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Install Powerlevel10k

```zsh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```

## Configuration

After installing Powerlevel10k, you can change the theme by edit `~/.zshrc` file:

In the ZSH_THEME section, change the theme to `powerlevel10k/powerlevel10k`:

```zsh
ZSH_THEME="powerlevel10k/powerlevel10k"
```

Quit and restart the terminal, then follow the on-screen instructions to configure the Powerlevel10k theme.

