---
title: "Running Jupyter Notebooks from NeoVim on macOS — A Guide to Jupynium"
tags: [neovim, jupyter, jupynium, macos, quant-research]
---

## 🧠 Why Jupynium?

If you’re a quant, you probably live in Jupyter notebooks for quick modeling — but also love the editing experience and keybindings of NeoVim.  
The problem: VS Code handles `.ipynb` files, but it’s heavy and mouse-driven.  

[Jupynium.nvim](https://github.com/kiyoon/jupynium.nvim) fixes this gap.  
It connects NeoVim to a live Jupyter Notebook (classic) session through Firefox automation.  
You can type in NeoVim, run cells, and watch outputs — plots, widgets, DataFrames — appear instantly in your browser.  
Everything stays synced to the real `.ipynb`, so you **never lose cell outputs or run history**.

## ⚙️ Step 1 — System Setup on macOS

```bash
# 1. Browser automation tools
brew install --cask firefox
brew install geckodriver

# 2. Jupyter classic (nbclassic is required)
conda install -n base -c conda-forge notebook nbclassic jupyter-console

# 3. Optional: register your project kernel
conda activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

Why Firefox?  
Jupynium uses Selenium WebDriver to control a browser. Only **Firefox** is fully supported via **geckodriver** — a small executable that listens for automation commands and controls the Firefox UI. Safari and Chrome won’t work (their drivers lack required APIs).

## ⚡ Step 2 — Install Plugins (Lazy.nvim Example)

Create `lua/plugins/jupynium.lua`:

```lua
return {
  {
    "kiyoon/jupynium.nvim",
    build = "pip3 install --user .",
    dependencies = {
      "rcarriga/nvim-notify",
      "stevearc/dressing.nvim",
    },
    config = function()
      local env = vim.env
      local py = (env.CONDA_PREFIX and ("conda run -p " .. env.CONDA_PREFIX .. " python3")) or "python3"

      require("jupynium").setup({
        default_notebook_URL = "localhost:8888/nbclassic",
        python_host = py,
        auto_download_ipynb = true,
        use_default_keybindings = false,
      })

      local map = vim.keymap.set
      map("n", "<leader>js", ":JupyniumStartAndAttachToServer<CR>", { desc = "Start server" })
      map("n", "<leader>jj", ":JupyniumStartSync<CR>", { desc = "Start sync to Notebook" })
      map("n", "<leader>jk", ":JupyniumKernelSelect<CR>", { desc = "Select kernel" })
      map("n", "<leader>jn", ":JupyniumRunSelectedCells<CR>", { desc = "Run selected cell(s)" })
      map("n", "<leader>jr", ":JupyniumKernelRestart<CR>", { desc = "Restart kernel" })
      map("n", "<leader>jo", ":JupyniumScrollToCell<CR>", { desc = "Scroll to cell" })
    end,
  },
}
```

## 🧩 Step 3 — Daily Workflow

1. **Activate your environment**
   ```bash
   conda activate myenv
   nvim analysis.ju.py
   ```
2. **Start Jupynium inside NeoVim**
   ```
   <leader>js   → start Jupyter server
   <leader>jj   → open Firefox + attach notebook
   <leader>jk   → select kernel
   ```
3. **Edit and run cells**
   - Mark code cells with `# %%`.
   - Run the current or selected cell via `<leader>jn`.
   - Outputs and plots appear in the Firefox tab.
4. **Save**
   - Jupynium automatically writes an updated `.ipynb` next to your file.
   - All execution history and widgets are preserved.

## 🧠 Environment Control

- The **controller** (Jupynium + Jupyter Notebook) can live in your base environment.
- The **execution kernel** (your code) runs in whatever conda env you choose via `Kernel → Change Kernel` or `:JupyniumKernelSelect`.
- This separation keeps your system clean: base env handles infrastructure, each project env handles packages.

## 🧩 Under the Hood

```
NeoVim (Jupynium)
   ↓  WebDriver API
geckodriver
   ↓
Firefox (Jupyter Notebook classic)
   ↓
IPython kernel (your conda env)
```

Every edit in NeoVim is sent via Selenium commands to Firefox, which updates the real notebook DOM.  
That’s why outputs, execution counts, and widget states remain intact — you’re literally editing the real notebook.

## 💡 Pro Tips

- Keep `geckodriver` on your `$PATH`:  
  `which geckodriver` → `/usr/local/bin/geckodriver`
- Don’t type simultaneously in the browser and Neovim — it’s one-way sync (NeoVim → browser).
- Use `auto_download_ipynb=true` so every save keeps your `.ipynb` up-to-date.
- Combine with `Jupytext` if you want text-based diffs for code review (`--sync`, not `--to ipynb`).

## 🚀 Why This Rocks for Quants

- **Reproducibility:** `.ipynb` stays the single source of truth (outputs + metadata).
- **Speed:** pure keyboard workflow, no mouse-dragging cells.
- **Flexibility:** run LightGBM, regression models, or backtests interactively while keeping Vim motions.
- **Portability:** notebooks still open normally in Jupyter, VS Code, or nbviewer.

## 🏁 Closing Thoughts

Jupynium brings back the productivity of Vim without giving up notebook interactivity.  
On macOS with conda, it’s now stable enough for daily quant research — from feature engineering to model debugging — all without leaving your terminal.

*Written by Yanzhong (Eric) Huang*  
[BagelQuant.com](https://bagelquant.com) — *Quantitative Research | Code | Coffee*
