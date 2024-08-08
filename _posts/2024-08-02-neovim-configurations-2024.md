---
title: "My Neovim Configurations 2024"
date: 2024-08-02
categories: 
  - neovim
tags:
  - productivity
---

This article is a follow-up to my previous post, [Neovim Experience: First Week](https://bagelquant.github.io/neoview/neovim-experience-first-week/). In this post, I will share my Neovim configurations after a week of exploration.

## File structure

I have a simple file structure for my Neovim configurations. using `init.lua` as the entry point. only require other lua files in `lua/eric/` directory. 

I Store basic configurations in `lua/eric/` directory, including: vim options, key mappings, and plugin manager packer.  

All plugins configurations are stored in `after/plugin/` directory. I use this directory to separate my configurations from the plugins' default configurations. 

```plaintext
~/.config/nvim
├── init.lua  # entry point: only require other lua files in lua/eric/ directory
├── lua
│   └── eric
│       ├── init.lua
│       ├── remap.lua     # key mappings, plugin specific key mappings not included
│       ├── settings.lua  # vim options
│       └── packer.lua    # plugin manager packer
├── after
│   └── plugin
│       ├── ALL-PLUGINS-CONFIGURATIONS
```

## Key mappings

I already have plenty of key mappings in my `remap.lua` file. Here are four most interesting key mappings:

```lua
vim.keymap('n', 'j', 'gj')
vim.keymap('n', 'k', 'gk')
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")
```

First two key mappings are used to navigate lines in normal mode, the cursor will move to the visual line instead of the actual line.

The last two key mappings are used to move lines in visual mode, and automatically adjust the indentation of the moved lines.

## Plugins

I use the plugin manager [Packer](https://github.com/wbthomason/packer.nvim) to manage my plugins. Here are some of the plugins I use:

```lua
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
    -- Packer can manage itself
    use 'wbthomason/packer.nvim'

    -- Core
    -- teletscope, fuzzy finder
    use {
        'nvim-telescope/telescope.nvim', tag = '0.1.8',
        -- or                            , branch = '0.1.x',
        requires = { {'nvim-lua/plenary.nvim'} }
    }

    -- treesitter
    use ('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})

    -- lsp-zero
    use {
        'VonHeikemen/lsp-zero.nvim',
        branch = 'v3.x',
        requires = {
            --- Uncomment the two plugins below if you want to manage the language servers from neovim
            -- {'williamboman/mason.nvim'},
            -- {'williamboman/mason-lspconfig.nvim'},
            {'neovim/nvim-lspconfig'},
            {'hrsh7th/nvim-cmp'},
            {'hrsh7th/cmp-nvim-lsp'},
            {'L3MON4D3/LuaSnip'},
        }
    }

    -- autocomplete cmp
    use ('hrsh7th/nvim-cmp')

    -- Appearance

    -- Themes
    -- one dark theme
    -- use {
    --     'navarasu/onedark.nvim', 
    --     config = function()
    --         require('onedark').setup(
    --         {
    --             style = 'dark',
    --         }
    --         );
    --         require('onedark').load()
    --     end
    -- }

    use { 
        "catppuccin/nvim", 
        as = "catppuccin",
        config = function()
            require("catppuccin").setup(
            {
                flavour = "auto", -- latte, frappe, macchiato, mocha
                background = { -- :h background
                    light = "latte",
                    dark = "mocha",
                },
            }
            );
        end
    }

    -- nvim-tree
    use 'nvim-tree/nvim-tree.lua'

    -- icons
    use 'nvim-tree/nvim-web-devicons'

    -- lualine
    use {
        'nvim-lualine/lualine.nvim',
        requires = { 'nvim-tree/nvim-web-devicons', opt = true }
    }

    -- noice
    use('MunifTanjim/nui.nvim')
    use('rcarriga/nvim-notify')
    use('folke/noice.nvim')

    -- Utilities
    -- vim-surround
    use('tpope/vim-surround')

    -- markdown preview
    use({
        "iamcco/markdown-preview.nvim",
        run = function() vim.fn["mkdp#util#install"]() end,
    })

    -- markdown compiler
    use 'abeleinin/papyrus'


    -- autopair
    use {
        "windwp/nvim-autopairs",
        event = "InsertEnter",
        config = function()
            require("nvim-autopairs").setup {}
        end
    }

    -- toggle term
    use {"akinsho/toggleterm.nvim", tag = '*', config = function()
        require("toggleterm").setup()
    end}

    -- github copilot
    use {"github/copilot.vim"}

    -- git
    use {"lewis6991/gitsigns.nvim"}
    use {
        "NeogitOrg/neogit",
        requires = {
            "nvim-lua/plenary.nvim",         -- required
            "sindrets/diffview.nvim",        -- optional - Diff integration

            -- Only one of these is needed, not both.
            "nvim-telescope/telescope.nvim", -- optional
            "ibhagwan/fzf-lua",              -- optional
        },
    }

    -- comment
    use {"terrortylor/nvim-comment"}

    -- harpoon
    use {"ThePrimeagen/harpoon"}

    -- autosave
    use({
        "Pocco81/auto-save.nvim",
        config = function()
            require("auto-save").setup {
                -- your config goes here
                -- or just leave it empty :)
            }
        end,
    })

    -- trouble
    use({
        "folke/trouble.nvim",
        requires = "kyazdani42/nvim-web-devicons",
    })

end)
```

## Conclusion

I'm still exploring Neovim and trying to improve my productivity. I'm excited to see how my Neovim configurations will evolve over time. If you have any suggestions or feedback, please let me know in the comments below.

