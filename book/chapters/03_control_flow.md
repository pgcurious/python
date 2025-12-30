# Chapter 3: Control Flow and Functions

This chapter covers how Python handles decision-making, iteration, and function definitions. As an experienced programmer, you'll find familiar concepts with Python-specific syntax and idioms.

## 3.1 Conditional Statements

### The if Statement

```python
age = 25

# Basic if
if age >= 18:
    print("Adult")

# if-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else (note: elif, not else if)
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

### Truthiness in Python

Python considers these values as **falsy** (evaluate to False):
- `False`
- `None`
- Zero: `0`, `0.0`, `0j`
- Empty sequences: `""`, `[]`, `()`, `{}`
- Empty set: `set()`

Everything else is **truthy**.

```python
# Pythonic way to check for empty/non-empty
items = []
if items:
    print("Has items")
else:
    print("Empty list")  # This executes

name = ""
if not name:
    print("Name is empty or not provided")

# Check for None specifically
value = None
if value is None:          # Preferred for None checks
    print("Value is None")

if value is not None:      # Preferred over: if value != None
    print("Has a value")
```

### Ternary Operator (Conditional Expression)

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Can be chained (but avoid for readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# Useful in expressions
values = [1, 2, 3]
result = sum(values) if values else 0
```

## 3.2 The match Statement (Python 3.10+)

Python's pattern matching is more powerful than a simple switch statement.

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:  # Multiple patterns
            return "Server Error"
        case _:                 # Default (wildcard)
            return "Unknown"

print(http_status(200))  # OK
print(http_status(502))  # Server Error
```

### Pattern Matching with Structure

```python
# Matching with destructuring
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

print(process_point((0, 5)))    # On Y-axis at 5
print(process_point((3, 4)))    # Point at (3, 4)

# Matching dictionaries
def process_command(cmd):
    match cmd:
        case {"action": "move", "direction": d}:
            return f"Moving {d}"
        case {"action": "attack", "target": t}:
            return f"Attacking {t}"
        case {"action": action}:
            return f"Unknown action: {action}"

print(process_command({"action": "move", "direction": "north"}))
```

## 3.3 Loops

### The for Loop

Python's `for` is a "for-each" loop that iterates over any iterable.

```python
# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over string
for char in "Python":
    print(char)

# Iterate over range
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):      # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step of 2)
    print(i)

for i in range(5, 0, -1):  # 5, 4, 3, 2, 1 (countdown)
    print(i)
```

### Useful Loop Patterns

```python
# Get index with enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start from different index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Iterate over dictionary
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Iterate multiple sequences with zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip with unequal lengths stops at shortest
# Use itertools.zip_longest for different behavior

# Reversed iteration
for fruit in reversed(fruits):
    print(fruit)

# Sorted iteration
for fruit in sorted(fruits):
    print(fruit)
```

### The while Loop

```python
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

### Loop Control: break, continue, else

```python
# break - exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4

# else clause - runs if loop completes without break
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")  # This runs

# Practical use of for-else: search
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found: {target}")
            break
    else:
        print(f"Not found: {target}")

find_item([1, 2, 3, 4], 3)  # Found: 3
find_item([1, 2, 3, 4], 5)  # Not found: 5
```

## 3.4 Functions

### Function Definition

```python
# Basic function
def greet():
    print("Hello!")

# With parameters
def greet(name):
    print(f"Hello, {name}!")

# With return value
def add(a, b):
    return a + b

# Multiple return values (returns tuple)
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 / 5 = {q} remainder {r}")
```

### Default Arguments

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!

# CAUTION: Mutable default arguments are shared!
def append_to(item, target=[]):  # BAD!
    target.append(item)
    return target

# This is a common bug - use None instead:
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

### Keyword Arguments

```python
def create_user(name, email, age=None, role="user"):
    return {"name": name, "email": email, "age": age, "role": role}

# Positional arguments
user1 = create_user("Alice", "alice@email.com")

# Keyword arguments (any order)
user2 = create_user(email="bob@email.com", name="Bob", role="admin")

# Mixed (positional must come first)
user3 = create_user("Charlie", "charlie@email.com", role="moderator")
```

### *args and **kwargs

```python
# *args - variable positional arguments (tuple)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - variable keyword arguments (dict)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# Combined
def flexible_function(required, *args, default="value", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

# Unpacking when calling
numbers = [1, 2, 3]
print(sum_all(*numbers))  # Unpack list as positional args

config = {"name": "Alice", "age": 30}
print_info(**config)      # Unpack dict as keyword args
```

### Type Hints (Python 3.5+)

Type hints are optional but improve code readability and enable static analysis.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Optional types
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    # Returns dict or None
    pass

# Union types (Python 3.10+)
def process(value: int | str) -> str:
    return str(value)

# Type hints don't enforce types at runtime
# Use tools like mypy for static type checking
```

### Lambda Functions

Anonymous functions for simple, one-line operations.

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Common use: sorting with key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_by_grade = sorted(students, key=lambda s: s["grade"])

# Sort by name
sorted_by_name = sorted(students, key=lambda s: s["name"])

# With filter and map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x ** 2, numbers))

# Note: List comprehensions are often preferred over map/filter
evens = [x for x in numbers if x % 2 == 0]
squares = [x ** 2 for x in numbers]
```

### Scope and the `global` Keyword

```python
global_var = "I'm global"

def outer():
    outer_var = "I'm in outer"

    def inner():
        inner_var = "I'm in inner"
        print(global_var)   # Can read global
        print(outer_var)    # Can read enclosing scope

    inner()

# Modifying global variables (generally avoid)
counter = 0

def increment():
    global counter
    counter += 1

# nonlocal for enclosing scope
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print(count)  # 1
```

## 3.5 Exercises

### Exercise 3.1: FizzBuzz
```python
# Classic FizzBuzz: Print numbers 1-100
# - If divisible by 3, print "Fizz"
# - If divisible by 5, print "Buzz"
# - If divisible by both, print "FizzBuzz"
# - Otherwise, print the number

# Your code here
```

### Exercise 3.2: Prime Number Functions
```python
# Write these functions:
# 1. is_prime(n) - returns True if n is prime
# 2. primes_up_to(n) - returns list of all primes up to n
# 3. prime_factors(n) - returns list of prime factors of n

# Your code here
```

### Exercise 3.3: Temperature Converter
```python
# Create a function that:
# - Accepts temperature and source unit (C, F, or K)
# - Returns a dict with temperature in all three units
# - Use type hints

# Example: convert_temp(100, "C")
# Returns: {"celsius": 100, "fahrenheit": 212, "kelvin": 373.15}

# Your code here
```

### Exercise 3.4: Pattern Matching (Python 3.10+)
```python
# Create a function that processes different command structures:
# - {"type": "greet", "name": "Alice"} -> "Hello, Alice!"
# - {"type": "math", "op": "add", "a": 5, "b": 3} -> 8
# - {"type": "math", "op": "multiply", "a": 4, "b": 7} -> 28
# - Unknown commands -> "Unknown command"

# Your code here
```

---

**Next Chapter:** [Object-Oriented Python](04_oop.md) - Classes, inheritance, and Python's special methods.
