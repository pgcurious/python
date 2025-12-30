#!/usr/bin/env python3
"""
Chapter 1 Exercises: Python Fundamentals
Complete each exercise by filling in the code where indicated.
Run this file to check your solutions.
"""

print("=" * 60)
print("CHAPTER 1 EXERCISES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercise 1.1: Variable Swap
# -----------------------------------------------------------------------------
print("\n--- Exercise 1.1: Variable Swap ---")

a = "first"
b = "second"

# TODO: Swap a and b without using a temporary variable
# Your code here:


# Uncomment to check:
# print(f"a = {a}, b = {b}")  # Should print: a = second, b = first

# -----------------------------------------------------------------------------
# Exercise 1.2: String Manipulation
# -----------------------------------------------------------------------------
print("\n--- Exercise 1.2: String Manipulation ---")

text = "   Python is AWESOME   "

# TODO: Transform text in these steps:
# 1. Remove leading/trailing whitespace
# 2. Convert to lowercase
# 3. Replace "awesome" with "powerful"
# 4. Capitalize the first letter of each word
# Store final result in 'result'

# Your code here:
result = text  # Replace this line

# Uncomment to check:
# print(f"Result: '{result}'")  # Should print: "Python Is Powerful"

# -----------------------------------------------------------------------------
# Exercise 1.3: F-string Formatting
# -----------------------------------------------------------------------------
print("\n--- Exercise 1.3: F-string Formatting ---")

product = "Widget"
price = 49.99
quantity = 150

# TODO: Create a formatted string that shows:
# "Product: Widget | Price: $49.99 | Qty: 150 | Total: $7,498.50"
# Use f-strings with proper formatting (currency, commas for thousands)

# Your code here:
output = ""  # Replace this line

# Uncomment to check:
# print(output)

# -----------------------------------------------------------------------------
# Exercise 1.4: Type Investigation
# -----------------------------------------------------------------------------
print("\n--- Exercise 1.4: Type Investigation ---")

values = [42, 42.0, "42", True, None, [1, 2], (1, 2), {"a": 1}]

print("Investigate these values:")
for v in values:
    print(f"  Value: {v!r:15} | Type: {type(v).__name__}")

# TODO: Answer these questions by experimenting:
# 1. What does 42 == 42.0 return?
# 2. What does 42 is 42.0 return?
# 3. What does True == 1 return? Why?
# 4. What does True + True return?

print("\nYour experiments:")
# Your code here - print the results of the above comparisons


# -----------------------------------------------------------------------------
# Exercise 1.5: Chained Comparisons
# -----------------------------------------------------------------------------
print("\n--- Exercise 1.5: Chained Comparisons ---")

# TODO: Using chained comparisons, write expressions to check:
# 1. If a number is between 1 and 100 (inclusive)
# 2. If a character is a lowercase letter (between 'a' and 'z')
# 3. If three numbers are in ascending order

number = 50
char = 'm'
x, y, z = 5, 10, 15

# Your code here:
# is_in_range = ...
# is_lowercase = ...
# is_ascending = ...

# Uncomment to check:
# print(f"{number} is between 1 and 100: {is_in_range}")
# print(f"'{char}' is lowercase letter: {is_lowercase}")
# print(f"{x}, {y}, {z} are ascending: {is_ascending}")

# -----------------------------------------------------------------------------
# Exercise 1.6: String Slicing Challenge
# -----------------------------------------------------------------------------
print("\n--- Exercise 1.6: String Slicing Challenge ---")

text = "Python Programming Language"

# TODO: Using only slicing (no string methods), extract:
# 1. The word "Python"
# 2. The word "Language"
# 3. Every third character
# 4. The string reversed
# 5. "Programming" reversed

# Your code here:
# word1 = text[...]
# word2 = text[...]
# every_third = text[...]
# reversed_text = text[...]
# prog_reversed = text[...]

# Uncomment to check:
# print(f"First word: {word1}")
# print(f"Last word: {word2}")
# print(f"Every third: {every_third}")
# print(f"Reversed: {reversed_text}")
# print(f"Programming reversed: {prog_reversed}")


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

def show_solutions():
    print("\n" + "=" * 60)
    print("SOLUTIONS")
    print("=" * 60)

    print("\n--- 1.1 Solution ---")
    a, b = "first", "second"
    a, b = b, a
    print(f"a = {a}, b = {b}")

    print("\n--- 1.2 Solution ---")
    text = "   Python is AWESOME   "
    result = text.strip().lower().replace("awesome", "powerful").title()
    print(f"Result: '{result}'")

    print("\n--- 1.3 Solution ---")
    product, price, quantity = "Widget", 49.99, 150
    total = price * quantity
    output = f"Product: {product} | Price: ${price:.2f} | Qty: {quantity} | Total: ${total:,.2f}"
    print(output)

    print("\n--- 1.4 Solution ---")
    print(f"42 == 42.0: {42 == 42.0}")      # True - same value
    print(f"42 is 42.0: {42 is 42.0}")      # False - different types
    print(f"True == 1: {True == 1}")        # True - bool is subclass of int
    print(f"True + True: {True + True}")    # 2 - True is 1

    print("\n--- 1.5 Solution ---")
    number, char = 50, 'm'
    x, y, z = 5, 10, 15
    print(f"{number} is between 1 and 100: {1 <= number <= 100}")
    print(f"'{char}' is lowercase letter: {'a' <= char <= 'z'}")
    print(f"{x}, {y}, {z} are ascending: {x < y < z}")

    print("\n--- 1.6 Solution ---")
    text = "Python Programming Language"
    print(f"First word: {text[0:6]}")
    print(f"Last word: {text[19:]}")
    print(f"Every third: {text[::3]}")
    print(f"Reversed: {text[::-1]}")
    print(f"Programming reversed: {text[7:18][::-1]}")


# Uncomment to see solutions:
# show_solutions()
