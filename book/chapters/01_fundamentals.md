# Chapter 1: Python Fundamentals for Programmers

Welcome to Python! Since you already have programming experience, this book takes a **transfer learning** approach—we'll leverage what you know and focus on Python's unique characteristics, syntax, and idioms.

## 1.1 Why Python is Different

Python's philosophy is captured in "The Zen of Python" (try running `import this` in Python):

- **Readability counts** - Code is read more than written
- **Explicit is better than implicit** - No hidden magic
- **There should be one obvious way to do it** - Consistency matters

### What Makes Python Unique

| Feature | Other Languages | Python |
|---------|-----------------|--------|
| Blocks | `{ }` braces | Indentation |
| Statement end | `;` semicolon | Newline |
| Types | Static (usually) | Dynamic |
| Memory | Manual/GC varies | Automatic GC |

## 1.2 Your First Python Program

Create a file `hello.py`:

```python
# This is a comment
print("Hello, Python!")

# Variables need no type declaration
name = "Developer"
age = 25
pi = 3.14159

# String formatting (f-strings - Python 3.6+)
print(f"Name: {name}, Age: {age}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Swap without temp variable
x, y = y, x
print(f"After swap: x={x}, y={y}")
```

**Run it:**
```bash
python hello.py
```

## 1.3 Indentation is Syntax

This is the biggest adjustment for most programmers. **Indentation defines code blocks.**

```python
# Correct - consistent indentation
if True:
    print("Inside if")
    print("Still inside")
print("Outside if")

# WRONG - will cause IndentationError
# if True:
#     print("Inside")
#   print("Misaligned!")  # Error!
```

**Convention:** Use 4 spaces (not tabs). Most editors can be configured for this.

## 1.4 Variables and Types

Python is **dynamically typed** but **strongly typed**.

```python
# Dynamic typing - no declarations needed
message = "Hello"      # str
count = 42             # int
price = 19.99          # float
is_valid = True        # bool
nothing = None         # NoneType

# Check types with type()
print(type(message))   # <class 'str'>
print(type(count))     # <class 'int'>

# Strong typing - no implicit conversion
# print("Count: " + count)  # TypeError!
print("Count: " + str(count))  # Correct - explicit conversion

# Type checking with isinstance()
print(isinstance(count, int))      # True
print(isinstance(count, (int, float)))  # True - check multiple types
```

## 1.5 Basic Operators

Most operators work as expected, with some Python-specific additions:

```python
# Arithmetic
a, b = 17, 5
print(f"a + b = {a + b}")     # 22
print(f"a - b = {a - b}")     # 12
print(f"a * b = {a * b}")     # 85
print(f"a / b = {a / b}")     # 3.4  (always float!)
print(f"a // b = {a // b}")   # 3    (floor division)
print(f"a % b = {a % b}")     # 2    (modulo)
print(f"a ** b = {a ** b}")   # 1419857 (exponentiation)

# Comparison
x, y = 10, 10
print(f"x == y: {x == y}")    # True (value equality)
print(f"x is y: {x is y}")    # True (identity - same object)

# Be careful with 'is' for larger numbers or objects
a = 1000
b = 1000
print(f"a == b: {a == b}")    # True
print(f"a is b: {a is b}")    # May be False! (different objects)

# Logical operators (not && || !)
print(True and False)         # False
print(True or False)          # True
print(not True)               # False

# Chained comparisons (Pythonic!)
age = 25
print(18 <= age < 65)         # True - readable range check!
```

## 1.6 Strings

Strings in Python are immutable and very powerful:

```python
# String creation
single = 'Hello'
double = "World"
multi = """This is a
multi-line string"""

raw = r"C:\new\folder"  # Raw string - no escape processing
print(raw)  # C:\new\folder

# String operations
s = "Python Programming"
print(len(s))           # 18
print(s.lower())        # python programming
print(s.upper())        # PYTHON PROGRAMMING
print(s.split())        # ['Python', 'Programming']
print(s.replace("Python", "Java"))  # Java Programming

# Indexing and slicing
print(s[0])             # P (first character)
print(s[-1])            # g (last character)
print(s[0:6])           # Python (characters 0-5)
print(s[7:])            # Programming (from index 7 to end)
print(s[:6])            # Python (from start to index 5)
print(s[::2])           # Pto rgamn (every 2nd character)
print(s[::-1])          # gnimmargorP nohtyP (reversed!)

# String formatting methods
name, language, years = "Alice", "Python", 3

# f-strings (recommended, Python 3.6+)
print(f"{name} has used {language} for {years} years")

# format() method
print("{} has used {} for {} years".format(name, language, years))

# Named placeholders
print("{n} has used {l} for {y} years".format(n=name, l=language, y=years))

# Format specifications
pi = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}")      # 3.14
print(f"Pi with padding: {pi:10.2f}")     # '      3.14'
print(f"Large number: {1000000:,}")       # 1,000,000

# Useful string methods
text = "  hello world  "
print(text.strip())          # "hello world" (remove whitespace)
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))    # True
print("hello world".title())     # "Hello World"
print(",".join(["a", "b", "c"])) # "a,b,c"
print("a,b,c".split(","))        # ['a', 'b', 'c']
```

## 1.7 Input and Output

```python
# Basic output
print("Hello")                    # Simple print
print("Hello", "World")           # Multiple items, space-separated
print("Hello", "World", sep="-")  # Custom separator: Hello-World
print("No newline", end=" ")      # Custom ending (default is \n)
print("continues here")

# Formatted output
name = "Python"
version = 3.12
print(f"{name} version {version}")

# Basic input
user_input = input("Enter your name: ")  # Always returns string
print(f"Hello, {user_input}!")

# Converting input
age_str = input("Enter your age: ")
age = int(age_str)  # Convert to integer
# Or in one line:
# age = int(input("Enter your age: "))
```

## 1.8 The Python REPL

Python's interactive interpreter (REPL - Read-Eval-Print-Loop) is invaluable:

```bash
$ python
>>> 2 + 2
4
>>> "hello".upper()
'HELLO'
>>> import math
>>> math.sqrt(16)
4.0
>>> help(str.split)  # Get help on any function
>>> exit()  # Or Ctrl+D
```

**Pro tip:** Use `_` to access the last result:
```python
>>> 5 * 5
25
>>> _ + 10
35
```

## 1.9 Comments and Docstrings

```python
# Single line comment

# Multi-line comments are just
# multiple single-line comments

"""
This is technically a string, not a comment.
But it's often used for multi-line comments.
"""

def greet(name):
    """
    This is a docstring - special documentation string.

    Args:
        name: The name to greet

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"

# Access docstrings programmatically
print(greet.__doc__)
```

## 1.10 Exercises

Create a file `exercises/ch01_exercises.py` and solve these:

### Exercise 1.1: Variable Swap
```python
# Swap these variables without using a temporary variable
a = "first"
b = "second"
# Your code here

print(f"a = {a}, b = {b}")  # Should print: a = second, b = first
```

### Exercise 1.2: String Manipulation
```python
# Given this string:
text = "   Python is AWESOME   "

# 1. Remove leading/trailing whitespace
# 2. Convert to lowercase
# 3. Replace "awesome" with "powerful"
# 4. Capitalize the first letter of each word

# Your code here
# Expected output: "Python Is Powerful"
```

### Exercise 1.3: F-string Formatting
```python
# Format these values:
product = "Widget"
price = 49.99
quantity = 150

# Create an output like:
# "Product: Widget | Price: $49.99 | Qty: 150 | Total: $7,498.50"
# Use f-strings with proper formatting (currency, commas)

# Your code here
```

### Exercise 1.4: Type Investigation
```python
# Predict and verify the type of each:
values = [42, 42.0, "42", True, None, [1, 2], (1, 2), {"a": 1}]

for v in values:
    print(f"Value: {v!r:15} | Type: {type(v).__name__}")

# What's the difference between 42 and 42.0?
# What happens if you do: 42 == 42.0? What about 42 is 42.0?
```

---

**Next Chapter:** [Data Types and Structures](02_data_structures.md) - Lists, tuples, dictionaries, and sets.
