---
title: "Using Pytest for Unit Testing in Python"
layout: post
---

I have see lots of brilliant quant and data science managing their code only in jupyter notebooks. While notebooks are great for exploration and prototyping, they fall short when it comes to maintaining robust codebases. 

One shortcoming of notebooks is the lack of integrated testing frameworks. Without proper unit tests, it's easy for code to break unnoticed as changes are made. This can lead to significant issues down the line, especially in complex projects. Lead to frustration and wasted time when bugs arise that could have been caught early with proper testing.

While Python's built-in `unittest` framework is functional, `pytest` offers a more concise syntax, powerful fixtures, and advanced features like parameterized tests. This makes it easier to write and maintain tests, especially in larger projects.

Pytest becomes much more powerful and convenient when paired with a proper project structure, clean test modules, and a configuration file that defines default behaviors. This post introduces pytest usage with a detailed file tree, example test code, and a recommended pytest configuration setup for real projects.

Here's a comprehensive example of how to set up and use pytest effectively in a Python project.

## Project File Tree

```
your_project/
├── pyproject.toml
├── pytest.ini
├── src/
│   └── your_package/
│       ├── __init__.py
│       ├── math_utils.py
│       └── data_loader.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_math_utils.py
    ├── test_data_loader.py
    └── test_parametrize.py
```

## Example Application Code

```
# src/your_package/math_utils.py

def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

```
# src/your_package/data_loader.py

def load_lines(path):
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]
```

## Example Tests

```
# tests/test_math_utils.py

import pytest
from your_package.math_utils import add, divide

def test_add_basic():
    assert add(2, 3) == 5

def test_divide_valid():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
```

```
# tests/test_data_loader.py

from your_package.data_loader import load_lines

def test_load_lines(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("hello\nworld\n")
    result = load_lines(p)
    assert result == ["hello", "world"]
```

```
# tests/test_parametrize.py

import pytest
from your_package.math_utils import add

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (-1, -1, -2),
        (10, -5, 5),
    ]
)
def test_add_parametrized(x, y, expected):
    assert add(x, y) == expected
```

## Reusable Fixtures via conftest.py

```
# tests/conftest.py

import pandas as pd
import pytest

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "asset": ["A", "B", "C"],
        "value": [1, 2, 3]
    })
```

## Pytest Configuration File

```
# pytest.ini

[pytest]
minversion = 7.0

testpaths =
    tests

pythonpath =
    src

markers =
    slow: marks tests as slow
    integration: integration tests requiring external resources

filterwarnings =
    ignore::DeprecationWarning

addopts =
    -q
    --disable-warnings
    --maxfail=1
```

## Running the Test

```
pytest
```

Pytest reads `pytest.ini` automatically and applies all configured behaviors.

Other options

- `pytest -v` for verbose output
- `pytest -k "expression"` to run tests matching the expression
- `pytest -m "marker"` to run tests with a specific marker
- `pytest --tb=short` for shorter tracebacks
- `pytest --cov=your_package` to measure code coverage (requires pytest-cov plugin)

Run specific test file:

```
pytest tests/test_math_utils.py
```

