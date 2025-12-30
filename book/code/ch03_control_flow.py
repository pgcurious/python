#!/usr/bin/env python3
"""
Chapter 3: Control Flow and Functions
Run this file to see all examples in action.
"""
import sys

print("=" * 60)
print("CHAPTER 3: CONTROL FLOW AND FUNCTIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 3.1 Conditional Statements
# -----------------------------------------------------------------------------
print("\n--- 3.1 Conditional Statements ---")

age = 25
print(f"age = {age}")

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Truthiness
print("\nTruthiness examples:")
for value in [[], [1, 2], "", "hello", 0, 42, None]:
    status = "truthy" if value else "falsy"
    print(f"  {value!r:12} is {status}")

# Ternary operator
status = "adult" if age >= 18 else "minor"
print(f"\nTernary: age {age} -> {status}")

# -----------------------------------------------------------------------------
# 3.2 Pattern Matching (Python 3.10+)
# -----------------------------------------------------------------------------
print("\n--- 3.2 Pattern Matching ---")

if sys.version_info >= (3, 10):
    def http_status(status):
        match status:
            case 200:
                return "OK"
            case 404:
                return "Not Found"
            case 500 | 502 | 503:
                return "Server Error"
            case _:
                return "Unknown"

    for code in [200, 404, 503, 999]:
        print(f"  Status {code}: {http_status(code)}")

    def process_point(point):
        match point:
            case (0, 0):
                return "Origin"
            case (0, y):
                return f"On Y-axis at {y}"
            case (x, 0):
                return f"On X-axis at {x}"
            case (x, y):
                return f"Point at ({x}, {y})"

    print("\nPattern matching with tuples:")
    for pt in [(0, 0), (0, 5), (3, 0), (3, 4)]:
        print(f"  {pt} -> {process_point(pt)}")
else:
    print("Pattern matching requires Python 3.10+")
    print(f"Current version: {sys.version}")

# -----------------------------------------------------------------------------
# 3.3 Loops
# -----------------------------------------------------------------------------
print("\n--- 3.3 Loops ---")

# For loop with range
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 8):", end=" ")
for i in range(2, 8):
    print(i, end=" ")
print()

print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Enumerate
fruits = ["apple", "banana", "cherry"]
print("\nenumerate example:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# Zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("\nzip example:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# For-else
print("\nfor-else example:")


def find_item(items, target):
    for item in items:
        if item == target:
            print(f"  Found: {target}")
            break
    else:
        print(f"  Not found: {target}")


find_item([1, 2, 3, 4], 3)
find_item([1, 2, 3, 4], 5)

# -----------------------------------------------------------------------------
# 3.4 Functions
# -----------------------------------------------------------------------------
print("\n--- 3.4 Functions ---")


# Basic function
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Alice"))
print(greet("Bob", "Hi"))


# Multiple return values
def divide_with_remainder(a, b):
    return a // b, a % b


q, r = divide_with_remainder(17, 5)
print(f"\n17 / 5 = {q} remainder {r}")


# *args and **kwargs
def demo_args(*args, **kwargs):
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")


print("\n*args and **kwargs:")
demo_args(1, 2, 3, name="Alice", age=30)

# Unpacking
numbers = [1, 2, 3]
config = {"greeting": "Hi", "name": "World"}


def greet2(name, greeting):
    return f"{greeting}, {name}!"


print(f"\nUnpacking: {greet2(**config)}")


# Type hints
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


print(f"\nType-hinted function: add_numbers(5, 3) = {add_numbers(5, 3)}")

# Lambda
print("\nLambda examples:")
square = lambda x: x ** 2
print(f"  square(5) = {square(5)}")

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print("  Students sorted by grade (descending):")
for s in sorted_students:
    print(f"    {s['name']}: {s['grade']}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
CONDITIONALS:
  - Use elif, not else if
  - Ternary: value_if_true if condition else value_if_false
  - Check None with 'is None' not '== None'
  - Empty collections are falsy

LOOPS:
  - for...in iterates over any iterable
  - Use enumerate() for index + value
  - Use zip() to iterate multiple sequences
  - for-else runs if no break occurred

FUNCTIONS:
  - def name(params): body
  - Default args: def f(x, y=10)
  - *args for variable positional args
  - **kwargs for variable keyword args
  - Lambda: lambda x: expression
  - Type hints: def f(x: int) -> str
""")

print("Run the exercises in exercises/ch03_exercises.py!")
