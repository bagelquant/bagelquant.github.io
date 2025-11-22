---
title: "Edit Python in Neovim, Run in Jupyter: A Clean Jupytext Paired Workflow"
layout: post
---

In quantitative research and data science, we often use Jupyter notebooks for the **interactive execution and visualization of code**. However, jupyter notebooks have some limitations:

- they can be clunky to edit, especially for large codebases.
- Version control with notebooks is difficult due to their JSON format.
- IDEs often trade off efficiency for convenience.

But with **Jupytext paired notebooks**, we can bridge this gap — letting you **edit `.py` files in Neovim** and **run the corresponding `.ipynb` notebook** interactively, while keeping all previous outputs and execution counts.

## Concept: Two Representations of the Same Notebook

Jupytext allows a Jupyter notebook to exist in two synchronized formats:

`notebook.ipynb`  ↔  `notebook.py`

They share the same content and structure, synced through metadata.

Whenever you edit one and run:


```shell
jupytext --sync notebook.ipynb
```

the other side updates automatically.

- ✅ `.ipynb` keeps all outputs and execution states
- ✅ `.py` is pure text — perfect for Git version control
- ✅ Both stay perfectly in sync

## Creating the Pair

Let’s say you have an existing Jupyter notebook:

```shell
jupytext --set-formats ipynb,py:percent demo.ipynb
```

This will:

- create a paired demo.py
- embed pairing metadata in demo.ipynb
- tell Jupytext that these two files represent the same notebook

## What Does py:percent Mean?

The py:percent format uses familiar cell markers to split code and markdown cells, like this:

```plaintext
# %% [markdown]
# # Notebook title
# Some explanation text

# %%
import numpy as np

# %%
x = np.arange(10)
x

	•	# %% marks a new code cell
	•	# %% [markdown] marks a markdown cell
```

This syntax is recognized by VS Code, Spyder, PyCharm, and Neovim.
It’s simple, human-readable, and makes jumping between cells in Vim effortless.

## Typical Workflow: Neovim for Code, JupyterLab for Execution

Here’s how to combine them in practice.

Step 1 — Run JupyterLab

`jupyter lab`

Open demo.ipynb and run the first five cells.

Step 2 — Edit in Neovim

nvim `demo.py`

Edit the 6th cell and save the file.

Step 3 — Sync Changes

jupytext --sync demo.ipynb

Jupytext will:

- detect .py is newer than .ipynb
- update the notebook source accordingly
- preserve outputs and execution counts for unchanged cells
- clear outputs for modified cells only

Back in JupyterLab, refresh the notebook — you’ll see updated code, with old results intact for untouched cells.

🎯 Result: you can write in Vim, run in Jupyter, and keep your notebook history.

5. Optional: Global Jupytext Config

To avoid repeating the pairing command every time, create a .jupytext.toml file in your project root:

## `.jupytext.toml`

```toml
formats = "ipynb,py:percent"
sync_markers = true
```

Now, all notebooks will automatically use the same py:percent paired format.

References
	•	Jupytext Official Docs￼
	•	GitHub: mwouts/jupytext￼
	•	Neovim IPython integration: nvim-ipy￼

