---
title: "Create your own Python package"
layout: post
---
In the past, I used `twine` to upload my packages to PyPI, building them with a `setup.py` file. Recently, I switched to using `pyproject.toml` for project management and package building. In my experience, it is more concise and much easier to maintain. With a single file, you can manage your project, build your package, and upload it to PyPI.

For reference, see the [Official Python Packaging Guide](https://packaging.python.org/en/latest/guides/section-build-and-publish/).

## Writing a `pyproject.toml` File

Here is a full example from the official guide:

```toml
[build-system]
requires = ["setuptools >= 61.0"]
build-backend = "setuptools.build_meta"

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

This file contains all the essential information about your project: dependencies, authors, maintainers, description, license, keywords, classifiers, optional dependencies, URLs, scripts, GUI scripts, and entry points. It is easy to read and manage.

## Project Structure Example

A typical project structure might look like this:

```plaintext
spam-eggs/
├── pyproject.toml
├── README.rst
├── LICENSE.txt
├── src/
│   └── spam/
│       ├── __init__.py
│       ├── main.py
│       ├── eggs.py
│       └── tomatoes.py
└── tests/
    └── test_spam.py
```

## Building and Uploading Your Package with `build` and `twine`

- `build` is a tool for building and packaging your project. Install it with `pip install build`.
- `twine` is used to securely upload your package to PyPI. Install it with `pip install twine`.

To build your package, run:

```shell
python3 -m build
```

To upload your package to TestPyPI (for testing):

```shell
python3 -m twine upload --repository testpypi dist/*
```

To upload your package to the official PyPI:

```shell
python3 -m twine upload --repository pypi dist/*
```

With `pyproject.toml`, managing, building, and publishing your Python package is simple and efficient.

### Using `uv` for Uploading

Alternatively, you can use `uv`, a tool that combines building and uploading into a single command. Install it with `pip install uv`.

To upload your package using `uv`, simply run:

```shell
uv add --dev build twine
```

Then, build and upload your package with:

```shell
uv run python -m build
```

```shell
uv run twine upload dist/*
```
