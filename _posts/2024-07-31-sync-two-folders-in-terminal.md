---
title: "Sync Two Folders in Terminal"
date: 2024-07-31
tags:
  - terminal
---

If you want to sync two folders in the terminal, you can use the `rsync` command. `rsync` is a fast and versatile file-copying tool that can be used to sync files and directories between two locations.

## Basic Usage

To sync two folders, use the following command:

```shell
rsync -av /path/to/source /path/to/destination
```

- `-a` flag: archive mode; equals `-rlptgoD` (no `-H,-A,-X`)
- `-v` flag: verbose mode

## Options

Here are some common options you can use with `rsync`:

- `-r`: recursive
- `-l`: copy symlinks as symlinks
- `-p`: preserve permissions
- `-t`: preserve modification times
- `-g`: preserve group
- `--delete`: delete files that don't exist in the source directory

## Use Case

For example, if you have a folder stored as notes, you want to sync to a github page folder to publish your notes. You can sync your notes folder to the github page folder using `rsync`.
