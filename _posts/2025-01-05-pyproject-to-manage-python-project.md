---
title: "Use pyproject.toml to manage your Python project"
layout: post
---

A Python project can quickly become disorganized without a clear structure. The `pyproject.toml` file is a modern configuration file that helps you manage your Python project efficiently. It centralizes information about your project, such as dependencies, build system, and metadata.

When combined with environment management tools like `poetry`, `pipenv`, or `conda`, `pyproject.toml` makes managing your Python project much easier and more reliable.

## What is pyproject.toml?

`pyproject.toml` is a standardized configuration file for Python projects. It specifies the build system, dependencies, and other project metadata. It is intended to replace the older `setup.py` file and is now recommended by the Python Packaging Authority (PyPA) as the preferred way to manage Python projects.

- [Official documentation](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### Example: pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "spam-eggs"
version = "2020.0.0"
dependencies = [
  "httpx",
  "gidgethub[httpx]>4.0.0",
  "django>2.1; os_name != 'nt'",
  "django>2.0; os_name == 'nt'",
]
requires-python = ">=3.8"
authors = [
  {name = "Pradyun Gedam", email = "pradyun@example.com"},
  {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
  {name = "Another person"},
  {email = "different.person@example.com"},
]
maintainers = [
  {name = "Brett Cannon", email = "brett@example.com"}
]
description = "Lovely Spam! Wonderful Spam!"
readme = "README.rst"
license = {file = "LICENSE.txt"}
keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"
]

[project.optional-dependencies]
gui = ["PyQt5"]
cli = [
  "rich",
  "click",
]

[project.urls]
Homepage = "https://example.com"
Documentation = "https://readthedocs.org"
Repository = "https://github.com/me/spam.git"
"Bug Tracker" = "https://github.com/me/spam/issues"
Changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

[project.scripts]
spam-cli = "spam:main_cli"

[project.gui-scripts]
spam-gui = "spam:main_gui"

[project.entry-points."spam.magical"]
tomatoes = "spam:main_tomatoes"
```

## Minimal Example for a Personal Project

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "bagel-factor"
version = "0.0.1"
authors = [
  { name="<NAME>", email="<EMAIL>" },
]
description = "<DESCRIPTION>"
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "pandas>=2.2.0",
    "matplotlib",
    "sqlalchemy>=2.0.0",
    "pymysql"
]   

[project.urls]
Homepage = "https://your-homepage.com"
Issues = "https://github.com/<your-repo>/issues"
```
