---
title: "Jupynium: Enhancing Jupyter Notebook Workflow in Neovim"
tags: [Neovim, Jupytext, Jupyter, Python, Workflow]
---

In the previous post regard [jupytext](2025-11-08-neovim-jupyternotebook.md), we explored how to use Jupytext to synchronize Jupyter notebooks with `.py` files for better version control and editing in Neovim. 

However jupytext alone has a critical limitation: it does not allow a "live" connection to a Jupyter kernel. It sync between `.py` and `.ipynb` on a file level, every change on `.py` file will cover the `.ipynb` file, including the outputs. This means you cannot run code interactively in Neovim and see the results immediately in the notebook.

`jupynium` is a Neovim plugin that bridges this gap by enabling interactive execution of code cells in `.py` files while maintaining synchronization with the corresponding Jupyter notebook. This allows you to edit and run code in Neovim, and see the outputs reflected in the notebook format.

## Install Jupynium on Neovim

Lazy example:

```lua
    -- jupynium
    {
        "kiyoon/jupynium.nvim",
        build = "pip3 install --user .",
        -- build = "uv pip install . --python=$HOME/.virtualenvs/jupynium/bin/python",
        -- build = "conda run --no-capture-output -n jupynium pip install .",
    },
    "rcarriga/nvim-notify",   -- optional
    "stevearc/dressing.nvim", -- optional, UI for :JupyniumKernelSelect
```

Configuration example:

```lua
require("jupynium").setup({
  --- For Conda environment named "jupynium",
  python_host = { "conda", "run", "--no-capture-output", "-n", "ml", "python" },
  -- python_host = vim.g.python3_host_prog or "python3",

  default_notebook_URL = "localhost:8888/nbclassic",

  -- Write jupyter command but without "notebook"
  -- When you call :JupyniumStartAndAttachToServer and no notebook is open,
  -- then Jupynium will open the server for you using this command. (only when notebook_URL is localhost)
  -- jupyter_command = "jupyter",
  --- For Conda, maybe use base environment
  --- then you can `conda install -n base nb_conda_kernels` to switch environment in Jupyter Notebook
  jupyter_command = { "conda", "run", "--no-capture-output", "-n", "ml", "jupyter" },

  -- Used when notebook is launched by using jupyter_command.
  -- If nil or "", it will open at the git directory of the current buffer,
  -- but still navigate to the directory of the current buffer. (e.g. localhost:8888/nbclassic/tree/path/to/buffer)
  notebook_dir = nil,

  -- Used to remember the last session (password etc.).
  -- e.g. '~/.mozilla/firefox/profiles.ini'
  -- or '~/snap/firefox/common/.mozilla/firefox/profiles.ini'
  firefox_profiles_ini_path = nil,
  -- nil means the profile with Default=1
  -- or set to something like 'default-release'
  firefox_profile_name = nil,

  -- Open the Jupynium server if it is not already running
  -- which means that it will open the Selenium browser when you open this file.
  -- Related command :JupyniumStartAndAttachToServer
  auto_start_server = {
    enable = false,
    file_pattern = { "*.ju.*" },
  },

  -- Attach current nvim to the Jupynium server
  -- Without this step, you can't use :JupyniumStartSync
  -- Related command :JupyniumAttachToServer
  auto_attach_to_server = {
    enable = false,
    file_pattern = { "*.ju.*", "*.md" },
  },

  -- Automatically open an Untitled.ipynb file on Notebook
  -- when you open a .ju.py file on nvim.
  -- Related command :JupyniumStartSync
  auto_start_sync = {
    enable = false,
    file_pattern = { "*.ju.*", "*.md" },
  },

  -- Automatically keep filename.ipynb copy of filename.ju.py
  -- by downloading from the Jupyter Notebook server.
  -- WARNING: this will overwrite the file without asking
  -- Related command :JupyniumDownloadIpynb
  auto_download_ipynb = false,

  -- Automatically close tab that is in sync when you close buffer in vim.
  auto_close_tab = true,

  -- Always scroll to the current cell.
  -- Related command :JupyniumScrollToCell
  autoscroll = {
    enable = true,
    mode = "always", -- "always" or "invisible"
    cell = {
      top_margin_percent = 20,
    },
  },

  scroll = {
    page = { step = 0.5 },
    cell = {
      top_margin_percent = 20,
    },
  },

  -- Files to be detected as a jupynium file.
  -- Add highlighting, keybindings, commands (e.g. :JupyniumStartAndAttachToServer)
  -- Modify this if you already have lots of files in Jupytext format, for example.
  jupynium_file_pattern = { "*.ju.*" },

  use_default_keybindings = true,
  textobjects = {
    use_default_keybindings = true,
  },

  syntax_highlight = {
    enable = true,
  },

  -- Dim all cells except the current one
  -- Related command :JupyniumShortsightedToggle
  shortsighted = false,

  -- Configure floating window options
  -- Related command :JupyniumKernelHover
  kernel_hover = {
    floating_win_opts = {
      max_width = 84,
      border = "none",
    },
  },

  notify = {
    ignore = {
      -- "download_ipynb",
      -- "error_download_ipynb",
      -- "attach_and_init",
      -- "error_close_main_page",
      -- "notebook_closed",
    },
  },
})

-- You can link highlighting groups.
-- This is the default (when colour scheme is unknown)
-- Try with CursorColumn, Pmenu, Folded etc.
vim.cmd [[
hi! link JupyniumCodeCellSeparator CursorLine
hi! link JupyniumMarkdownCellSeparator CursorLine
hi! link JupyniumMarkdownCellContent CursorLine
hi! link JupyniumMagicCommand Keyword
]]

-- Please share your favourite settings on other colour schemes, so I can add defaults.
-- Currently, tokyonight is supported.

-- keymaps
-- JupyniumStartAndAttachToServer
vim.keymap.set("n", "<leader>jsa", ":JupyniumStartAndAttachToServer<CR>", { desc = "Jupynium Start And Attach To Server" })
-- JupyniumStartSync
vim.keymap.set("n", "<leader>jss", ":JupyniumStartSync<CR>", { desc = "Jupynium Start Sync" })
```

## Install conda environment for Jupynium

I use conda environment named "ml" for all my machine learning work

```shell
conda create -n ml python=3.12.7
```

Activate the environment

```shell
conda activate ml
```

Install Jupynium dependencies

```shell
# jupyter-console is optional and used for `:JupyniumKernelOpenInTerminal`
pip install notebook nbclassic jupyter-console
```

## Usage

1. create a `.ju.py` file
2. run `:JupyniumStartAndAttachToServer` to start Jupyter server and attach Neovim to it
3. run `:JupyniumStartSync` to create an Untitled.ipynb file and start syncing
4. edit code cells in Neovim and run `:JupyniumRunCell` to execute the current cell
5. see the outputs reflected in the notebook format

