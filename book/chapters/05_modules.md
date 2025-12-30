# Chapter 5: Modules, Packages, and Environments

Organizing code into modules and packages is essential for maintainable Python projects. This chapter covers how to structure your code and manage dependencies.

## 5.1 Modules

A module is simply a Python file (`.py`) that can be imported.

### Creating a Module

```python
# mymath.py
"""A simple math utilities module."""

PI = 3.14159

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

class Calculator:
    """A simple calculator class."""
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self
```

### Importing Modules

```python
# Different ways to import
import mymath
print(mymath.add(2, 3))
print(mymath.PI)

# Import specific items
from mymath import add, PI
print(add(2, 3))
print(PI)

# Import with alias
import mymath as mm
print(mm.add(2, 3))

from mymath import Calculator as Calc
calc = Calc()

# Import everything (generally discouraged)
from mymath import *
```

### The `if __name__ == "__main__"` Pattern

```python
# mymath.py
def add(a, b):
    return a + b

def main():
    # This only runs when file is executed directly
    print("Testing add:", add(2, 3))

if __name__ == "__main__":
    main()
```

When imported: `__name__` is `"mymath"`
When run directly: `__name__` is `"__main__"`

### Standard Library Modules

Python comes with a rich standard library:

```python
# OS operations
import os
print(os.getcwd())          # Current directory
print(os.listdir('.'))      # List files
os.makedirs('new_dir', exist_ok=True)

# Path operations (preferred over os.path)
from pathlib import Path
path = Path('.')
for file in path.glob('*.py'):
    print(file)

# System information
import sys
print(sys.version)
print(sys.platform)

# Date and time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(now.strftime('%Y-%m-%d %H:%M'))

# JSON handling
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data, indent=2)
parsed = json.loads(json_str)

# Regular expressions
import re
pattern = r'\b\w+@\w+\.\w+\b'
emails = re.findall(pattern, "Contact: alice@email.com, bob@mail.org")

# Random numbers
import random
print(random.randint(1, 100))
print(random.choice(['a', 'b', 'c']))
random.shuffle(my_list)

# Math operations
import math
print(math.sqrt(16))
print(math.sin(math.pi / 2))

# Collections utilities
from collections import Counter, defaultdict, namedtuple
from itertools import chain, combinations, groupby

# Functional programming
from functools import reduce, partial, lru_cache
```

## 5.2 Packages

A package is a directory containing modules and an `__init__.py` file.

### Package Structure

```
myproject/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   └── utils.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
└── services/
    ├── __init__.py
    ├── auth.py
    └── database.py
```

### The `__init__.py` File

```python
# myproject/__init__.py
"""Main package initialization."""

__version__ = "1.0.0"
__author__ = "Your Name"

# Control what's exported with __all__
__all__ = ['core', 'models', 'services']

# Import commonly used items for convenience
from .core.utils import helper_function
from .models.user import User
```

### Importing from Packages

```python
# Absolute imports (recommended)
from myproject.models.user import User
from myproject.core import utils

# Relative imports (within package)
# In myproject/services/auth.py:
from ..models.user import User      # Go up one level
from ..core.config import settings  # Go up and into core
from . import database              # Same directory
```

### Namespace Packages (Python 3.3+)

No `__init__.py` required for simple namespace packages:

```
company/
├── package1/
│   └── module1.py
└── package2/
    └── module2.py
```

## 5.3 Virtual Environments

Virtual environments isolate project dependencies.

### Creating and Using Virtual Environments

```bash
# Create virtual environment
python -m venv myenv

# Activate (Linux/Mac)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Deactivate
deactivate

# Install packages
pip install requests flask

# Freeze dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### Best Practices

```bash
# Always create venv for new projects
mkdir my_project && cd my_project
python -m venv .venv
source .venv/bin/activate

# Add to .gitignore
echo ".venv/" >> .gitignore

# Structure of requirements
# requirements.txt - production dependencies
# requirements-dev.txt - development dependencies (includes testing, linting)
```

## 5.4 Package Management with pip

```bash
# Install package
pip install package_name
pip install package_name==1.2.3    # Specific version
pip install package_name>=1.2.0    # Minimum version

# Upgrade package
pip install --upgrade package_name

# Uninstall
pip uninstall package_name

# List installed packages
pip list

# Show package info
pip show package_name

# Install from git
pip install git+https://github.com/user/repo.git

# Install in editable mode (for development)
pip install -e .
```

## 5.5 Creating Your Own Package

### Project Structure

```
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── pyproject.toml
├── README.md
└── LICENSE
```

### Modern Setup with pyproject.toml

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A sample Python package"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "you@email.com"}
]
dependencies = [
    "requests>=2.25.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "mypy>=0.990",
]

[project.scripts]
my-cli = "my_package.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
```

### Building and Installing

```bash
# Install in development mode
pip install -e ".[dev]"

# Build distribution
pip install build
python -m build

# Upload to PyPI (optional)
pip install twine
twine upload dist/*
```

## 5.6 Common Third-Party Packages

Essential packages you'll use frequently:

```python
# HTTP requests
import requests
response = requests.get('https://api.example.com/data')
data = response.json()

# Data manipulation
import pandas as pd
df = pd.read_csv('data.csv')

# Scientific computing
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Web frameworks
from flask import Flask
from django.http import HttpResponse
from fastapi import FastAPI

# Testing
import pytest

# Type checking
# pip install mypy
# mypy your_code.py

# Code formatting
# pip install black
# black your_code.py

# Linting
# pip install ruff
# ruff check .
```

## 5.7 Exercises

### Exercise 5.1: Create a Module
```python
# Create a module called `string_utils.py` with these functions:
# - reverse_string(s) - reverse a string
# - is_palindrome(s) - check if string is palindrome
# - count_vowels(s) - count vowels
# - word_frequency(text) - return dict of word counts

# Then create a main.py that imports and uses these functions
```

### Exercise 5.2: Create a Package
```
# Create a package called `shapes` with this structure:
# shapes/
# ├── __init__.py
# ├── two_d/
# │   ├── __init__.py
# │   ├── circle.py
# │   └── rectangle.py
# └── three_d/
#     ├── __init__.py
#     ├── sphere.py
#     └── cube.py

# Each shape should have area/volume and perimeter/surface_area methods
# __init__.py should expose commonly used classes
```

### Exercise 5.3: Virtual Environment
```bash
# 1. Create a new virtual environment
# 2. Install requests and beautifulsoup4
# 3. Write a script that fetches a webpage and counts the links
# 4. Create requirements.txt
# 5. Test recreating the environment from requirements.txt
```

---

**Next Chapter:** [File Handling and I/O](06_file_io.md) - Reading, writing, and manipulating files.
