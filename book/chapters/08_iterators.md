# Chapter 8: Iterators, Generators, and Comprehensions

Python's iteration protocol and generators enable memory-efficient, elegant data processing. This chapter covers these powerful features that are central to writing Pythonic code.

## 8.1 The Iteration Protocol

Everything you can iterate over in Python implements the iteration protocol.

```python
# The iteration protocol
# 1. __iter__ returns an iterator
# 2. __next__ returns next value or raises StopIteration

# How a for loop actually works:
my_list = [1, 2, 3]
iterator = iter(my_list)     # Calls __iter__
print(next(iterator))        # 1 - Calls __next__
print(next(iterator))        # 2
print(next(iterator))        # 3
# next(iterator)             # Raises StopIteration
```

### Creating an Iterator Class

```python
class CountUp:
    """Iterator that counts from start to end."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Usage
for num in CountUp(1, 5):
    print(num)  # 1, 2, 3, 4
```

### Iterable vs Iterator

```python
# Iterable: Has __iter__, can be iterated multiple times
my_list = [1, 2, 3]
for x in my_list:
    print(x)
for x in my_list:  # Can iterate again
    print(x)

# Iterator: Has __next__, typically one-pass
iterator = iter(my_list)
for x in iterator:
    print(x)
for x in iterator:  # Empty! Already exhausted
    print(x)
```

## 8.2 Generators

Generators are a simpler way to create iterators using functions and the `yield` keyword.

### Generator Functions

```python
def count_up(start, end):
    """Generator function that yields numbers."""
    current = start
    while current < end:
        yield current
        current += 1

# Usage
for num in count_up(1, 5):
    print(num)  # 1, 2, 3, 4

# Generator creates an iterator
gen = count_up(1, 5)
print(next(gen))  # 1
print(next(gen))  # 2
```

### How yield Works

```python
def simple_generator():
    print("Starting")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3
    print("Ending")

gen = simple_generator()
print(next(gen))  # "Starting", then 1
print(next(gen))  # "After first yield", then 2
print(next(gen))  # "After second yield", then 3
# next(gen)       # "Ending", then StopIteration
```

### Practical Generator Examples

```python
# Read large file line by line (memory efficient)
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Infinite sequence
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first n items from infinite generator
from itertools import islice
fib = fibonacci()
first_10 = list(islice(fib, 10))
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Pipeline of generators
def numbers(n):
    for i in range(n):
        yield i

def squared(nums):
    for n in nums:
        yield n ** 2

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

# Chain them together (lazy evaluation)
pipeline = evens(squared(numbers(10)))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

### Generator Expressions

```python
# Generator expression (like list comprehension but lazy)
gen = (x ** 2 for x in range(10))
print(type(gen))  # <class 'generator'>

# Compare memory usage
import sys

# List comprehension - stores all in memory
list_comp = [x ** 2 for x in range(1000000)]
print(sys.getsizeof(list_comp))  # ~8MB

# Generator expression - lazy, minimal memory
gen_exp = (x ** 2 for x in range(1000000))
print(sys.getsizeof(gen_exp))    # ~120 bytes

# Use generators with functions expecting iterables
sum_of_squares = sum(x ** 2 for x in range(100))
any_even = any(x % 2 == 0 for x in [1, 3, 4, 5])
```

### yield from

```python
# Delegate to another generator
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]

# Flatten nested structure
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

## 8.3 Comprehensions

### List Comprehensions

```python
# Basic syntax: [expression for item in iterable]
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With transformation and condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), ...]

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conditional expression in output
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
```

### Dictionary Comprehensions

```python
# Basic syntax: {key: value for item in iterable}
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
scores = {'Alice': 85, 'Bob': 72, 'Charlie': 90}
passing = {name: score for name, score in scores.items() if score >= 75}
print(passing)  # {'Alice': 85, 'Charlie': 90}

# From lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
```

### Set Comprehensions

```python
# Basic syntax: {expression for item in iterable}
unique_lengths = {len(word) for word in ['hello', 'world', 'python']}
print(unique_lengths)  # {5, 6}

# With condition
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

## 8.4 The itertools Module

The `itertools` module provides memory-efficient tools for working with iterators.

```python
from itertools import (
    count, cycle, repeat,              # Infinite iterators
    chain, islice, takewhile, dropwhile,  # Terminating
    product, permutations, combinations,  # Combinatoric
    groupby, accumulate, starmap       # More tools
)

# Infinite iterators
for i in islice(count(10), 5):    # count from 10
    print(i)  # 10, 11, 12, 13, 14

colors = cycle(['red', 'green', 'blue'])
for _ in range(6):
    print(next(colors))  # red, green, blue, red, green, blue

# Chain multiple iterables
combined = chain([1, 2], [3, 4], [5, 6])
print(list(combined))  # [1, 2, 3, 4, 5, 6]

# Take while condition is true
nums = [1, 3, 5, 2, 4, 6]
result = takewhile(lambda x: x < 4, nums)
print(list(result))  # [1, 3]

# Drop while condition is true
result = dropwhile(lambda x: x < 4, nums)
print(list(result))  # [5, 2, 4, 6]

# Combinations and permutations
print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print(list(product([1, 2], ['a', 'b'])))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Group by
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3), ('b', 4)]

# Accumulate (running totals)
print(list(accumulate([1, 2, 3, 4, 5])))
# [1, 3, 6, 10, 15]
```

## 8.5 Built-in Functions for Iterables

```python
# map - apply function to each element
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# filter - keep elements where function returns True
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4]

# reduce - accumulate values
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# zip - pair elements from multiple iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# enumerate - get index and value
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# sorted, min, max, sum, any, all
print(sorted([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
print(min(numbers))             # 1
print(max(numbers))             # 5
print(sum(numbers))             # 15
print(any(x > 3 for x in numbers))  # True
print(all(x > 0 for x in numbers))  # True
```

## 8.6 Exercises

### Exercise 8.1: Generator Pipeline
```python
# Create a data processing pipeline using generators:
# 1. Read lines from a file
# 2. Parse each line as CSV
# 3. Filter rows by a condition
# 4. Transform selected columns
# 5. Aggregate results

# Make it memory-efficient for large files
```

### Exercise 8.2: Infinite Sequence
```python
# Create a generator for prime numbers
# Implement a Sieve of Eratosthenes using generators
# Make it lazy (compute only as needed)
```

### Exercise 8.3: Custom Range
```python
# Create a custom_range that:
# - Works like range() but for floats
# - Supports start, stop, step
# - Is a generator (memory efficient)
# Example: custom_range(0.0, 1.0, 0.1)
```

---

**Next Chapter:** [Decorators and Context Managers](09_decorators.md) - Metaprogramming and resource management.
