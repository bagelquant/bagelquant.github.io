---
titlle: "Create your own python package"
tags:
    - python
---

I used use `twine` to upload my package to PyPI with a `setup.py` file to build the package. Recently, I swap to `pyproject.toml` to manage my project and build the package. It is more consice and easier to manage in my opinion. With one file, you can manage your project, build the package, and upload it to PyPI. 

Here is the [Official Python Packaging Guide](https://packaging.python.org/en/latest/guides/section-build-and-publish/).

## Write a `pyproject.toml` file

Here is the full example from the official guide:

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

You can see in this file, it contains all the information about the project, dependencies, authors, maintainers, description, license, keywords, classifiers, optional dependencies, urls, scripts, gui-scripts, and entry-points. And really easy to read and manage.

## Project structure

Sample project structure:

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

## Using `build` and `twine` to build and upload the package

`build` is a package that provides a simple interface to build and package your project. You can install it with `pip install build`.

`twine` is a package that provides a simple interface to upload your package to PyPI. You can install it with `pip install twine`.

To build the package, you can run `python -m build` in the root of your project. It will create a `dist` folder with the package in it.

To upload the package to PyPI, you can run `twine upload dist/*` in the root of your project. It will upload the package to PyPI.

That's it. It is really easy to manage your project and build the package with `pyproject.toml` file. 

**build command:**

```shell
python3 -m build
```

**upload command to test:**

```shell
python3 -m twine upload --repository testpypi dist/*
```

**upload command to production:**

```shell
python3 -m twine upload --repository pypi dist/*
```


