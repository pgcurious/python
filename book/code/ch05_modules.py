#!/usr/bin/env python3
"""
Chapter 5: Modules, Packages, and Environments
Run this file to see all examples in action.
"""

print("=" * 60)
print("CHAPTER 5: MODULES, PACKAGES, AND ENVIRONMENTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 5.1 Importing Standard Library Modules
# -----------------------------------------------------------------------------
print("\n--- 5.1 Standard Library Examples ---")

# OS operations
import os
print(f"Current directory: {os.getcwd()}")
print(f"Files here: {os.listdir('.')[:5]}...")  # First 5 files

# Path operations with pathlib (modern approach)
from pathlib import Path
current = Path('.')
print(f"\nPathlib examples:")
print(f"  Current path: {current.absolute()}")
print(f"  Parent: {current.absolute().parent}")
python_files = list(current.glob('*.py'))
print(f"  Python files: {python_files[:3]}")

# System information
import sys
print(f"\nSystem info:")
print(f"  Python version: {sys.version_info.major}.{sys.version_info.minor}")
print(f"  Platform: {sys.platform}")

# Date and time
from datetime import datetime, timedelta
now = datetime.now()
print(f"\nDate/Time:")
print(f"  Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Tomorrow: {(now + timedelta(days=1)).strftime('%Y-%m-%d')}")

# JSON handling
import json
data = {"name": "Alice", "scores": [85, 90, 88]}
json_str = json.dumps(data, indent=2)
print(f"\nJSON example:")
print(f"  Serialized: {json_str}")
parsed = json.loads(json_str)
print(f"  Parsed name: {parsed['name']}")

# Regular expressions
import re
text = "Contact: alice@email.com and bob@mail.org for info"
pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
emails = re.findall(pattern, text)
print(f"\nRegex example:")
print(f"  Found emails: {emails}")

# Random
import random
print(f"\nRandom examples:")
print(f"  Random int (1-100): {random.randint(1, 100)}")
print(f"  Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

# Math
import math
print(f"\nMath examples:")
print(f"  sqrt(16) = {math.sqrt(16)}")
print(f"  pi = {math.pi:.6f}")
print(f"  ceil(4.2) = {math.ceil(4.2)}")

# Collections
from collections import Counter, defaultdict
print(f"\nCollections examples:")
word_counts = Counter("mississippi")
print(f"  Counter('mississippi'): {dict(word_counts)}")

grouped = defaultdict(list)
for word in ["apple", "banana", "apricot", "blueberry"]:
    grouped[word[0]].append(word)
print(f"  Grouped by first letter: {dict(grouped)}")

# Functools
from functools import reduce, lru_cache
print(f"\nFunctools examples:")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"  reduce (product of {numbers}): {product}")


@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"  fibonacci(30) with cache: {fibonacci(30)}")

# -----------------------------------------------------------------------------
# 5.2 Module Pattern Demo
# -----------------------------------------------------------------------------
print("\n--- 5.2 Module Pattern Demo ---")

# Simulating a module's if __name__ == "__main__" pattern
print(f"Current __name__: {__name__}")
print("When run directly, __name__ is '__main__'")
print("When imported, __name__ is the module name")

# -----------------------------------------------------------------------------
# 5.3 Virtual Environments
# -----------------------------------------------------------------------------
print("\n--- 5.3 Virtual Environments (Commands) ---")
print("""
# Create virtual environment
python -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
.venv\\Scripts\\activate

# Install packages
pip install requests flask

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
""")

# -----------------------------------------------------------------------------
# 5.4 pip Commands
# -----------------------------------------------------------------------------
print("--- 5.4 pip Commands ---")
print("""
pip install package_name           # Install latest
pip install package_name==1.2.3    # Specific version
pip install package_name>=1.2.0    # Minimum version
pip install --upgrade package_name # Upgrade
pip uninstall package_name         # Remove
pip list                           # List installed
pip show package_name              # Package info
pip freeze > requirements.txt      # Export deps
pip install -e .                   # Editable install
""")

# -----------------------------------------------------------------------------
# 5.5 Package Structure
# -----------------------------------------------------------------------------
print("--- 5.5 Package Structure ---")
print("""
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py     # Package init, exports
│       ├── core.py         # Core functionality
│       └── utils.py        # Utilities
├── tests/
│   └── test_core.py
├── pyproject.toml          # Modern config (replaces setup.py)
├── README.md
└── LICENSE

# In __init__.py:
from .core import main_function
from .utils import helper
__all__ = ['main_function', 'helper']
__version__ = '1.0.0'
""")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
MODULES:
  - Any .py file is a module
  - import module, from module import item
  - if __name__ == "__main__": for script vs import

PACKAGES:
  - Directory with __init__.py
  - Use absolute imports: from package.module import item
  - Use relative imports within package: from . import module

VIRTUAL ENVIRONMENTS:
  - python -m venv .venv
  - Always use for projects
  - pip freeze > requirements.txt

COMMON STANDARD LIBRARY:
  - os, sys, pathlib - system/files
  - datetime, time - dates
  - json, re - data processing
  - collections, itertools, functools - utilities
  - random, math - numbers

PYPROJECT.TOML:
  - Modern replacement for setup.py
  - Defines build system, dependencies, metadata
""")

print("\nSee exercises/ch05_exercises.py for practice!")
