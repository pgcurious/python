#!/usr/bin/env python3
"""
Chapter 1: Python Fundamentals for Programmers
Run this file to see all examples in action.
"""

print("=" * 60)
print("CHAPTER 1: PYTHON FUNDAMENTALS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.2 Your First Python Program
# -----------------------------------------------------------------------------
print("\n--- 1.2 Variables and Basic Output ---")

name = "Developer"
age = 25
pi = 3.14159

print(f"Name: {name}, Age: {age}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Swap without temp variable
x, y = y, x
print(f"After swap: x={x}, y={y}")

# -----------------------------------------------------------------------------
# 1.4 Variables and Types
# -----------------------------------------------------------------------------
print("\n--- 1.4 Variables and Types ---")

message = "Hello"
count = 42
price = 19.99
is_valid = True
nothing = None

print(f"message: {message!r} -> {type(message)}")
print(f"count: {count!r} -> {type(count)}")
print(f"price: {price!r} -> {type(price)}")
print(f"is_valid: {is_valid!r} -> {type(is_valid)}")
print(f"nothing: {nothing!r} -> {type(nothing)}")

# Type checking
print(f"\nisinstance(count, int): {isinstance(count, int)}")
print(f"isinstance(count, (int, float)): {isinstance(count, (int, float))}")

# -----------------------------------------------------------------------------
# 1.5 Basic Operators
# -----------------------------------------------------------------------------
print("\n--- 1.5 Basic Operators ---")

a, b = 17, 5
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")      # Always float
print(f"a // b = {a // b}")    # Floor division
print(f"a % b = {a % b}")      # Modulo
print(f"a ** b = {a ** b}")    # Exponentiation

# Comparison
print(f"\nComparison operators:")
x, y = 10, 10
print(f"x == y: {x == y}")
print(f"x is y: {x is y}")

# Chained comparisons
age = 25
print(f"\nChained comparison: 18 <= {age} < 65 is {18 <= age < 65}")

# Logical operators
print(f"\nLogical operators:")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# -----------------------------------------------------------------------------
# 1.6 Strings
# -----------------------------------------------------------------------------
print("\n--- 1.6 Strings ---")

s = "Python Programming"
print(f"String: '{s}'")
print(f"Length: {len(s)}")
print(f"Lower: {s.lower()}")
print(f"Upper: {s.upper()}")
print(f"Split: {s.split()}")

print(f"\nIndexing and Slicing:")
print(f"s[0] = '{s[0]}'")
print(f"s[-1] = '{s[-1]}'")
print(f"s[0:6] = '{s[0:6]}'")
print(f"s[7:] = '{s[7:]}'")
print(f"s[::-1] = '{s[::-1]}'")

print(f"\nString Formatting:")
name, language, years = "Alice", "Python", 3
print(f"{name} has used {language} for {years} years")

pi = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Large number: {1000000:,}")

print(f"\nUseful String Methods:")
text = "  hello world  "
print(f"'  hello world  '.strip() = '{text.strip()}'")
print(f"'hello'.startswith('he') = {'hello'.startswith('he')}")
print(f"','.join(['a', 'b', 'c']) = {','.join(['a', 'b', 'c'])}")

# -----------------------------------------------------------------------------
# 1.7 Input and Output
# -----------------------------------------------------------------------------
print("\n--- 1.7 Output Examples ---")

print("Hello", "World", sep="-")
print("No newline", end=" -> ")
print("continues here")

# -----------------------------------------------------------------------------
# 1.9 Docstrings
# -----------------------------------------------------------------------------
print("\n--- 1.9 Docstrings ---")


def greet(name):
    """
    Generate a greeting message.

    Args:
        name: The name to greet

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


print(f"Function call: {greet('Python')}")
print(f"Docstring: {greet.__doc__}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
1. Indentation defines code blocks (use 4 spaces)
2. No type declarations needed (dynamic typing)
3. Use f-strings for formatting: f"Hello {name}"
4. // for floor division, ** for exponentiation
5. Use 'and', 'or', 'not' instead of &&, ||, !
6. Chained comparisons: 0 < x < 10
7. Strings are immutable and feature-rich
""")

print("Run the exercises in exercises/ch01_exercises.py!")
