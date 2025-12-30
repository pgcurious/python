#!/usr/bin/env python3
"""
Chapter 8: Iterators, Generators, and Comprehensions
Run this file to see all examples in action.
"""

from itertools import islice, count, cycle, chain, takewhile, dropwhile
from itertools import combinations, permutations, product, groupby, accumulate
import sys

print("=" * 60)
print("CHAPTER 8: ITERATORS, GENERATORS, AND COMPREHENSIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 8.1 The Iteration Protocol
# -----------------------------------------------------------------------------
print("\n--- 8.1 The Iteration Protocol ---")

# How for loops actually work
my_list = [1, 2, 3]
iterator = iter(my_list)
print(f"iter([1, 2, 3]) -> iterator")
print(f"next(iterator) -> {next(iterator)}")
print(f"next(iterator) -> {next(iterator)}")
print(f"next(iterator) -> {next(iterator)}")


# Custom iterator
class CountUp:
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


print(f"\nCustom CountUp(1, 5):", list(CountUp(1, 5)))

# -----------------------------------------------------------------------------
# 8.2 Generators
# -----------------------------------------------------------------------------
print("\n--- 8.2 Generators ---")


def count_up(start, end):
    """Generator function."""
    current = start
    while current < end:
        yield current
        current += 1


print("Generator count_up(1, 5):", list(count_up(1, 5)))


# How yield works
def demo_yield():
    print("  Before first yield")
    yield 1
    print("  Between yields")
    yield 2
    print("  After last yield")


print("\nYield execution order:")
gen = demo_yield()
print(f"next() -> {next(gen)}")
print(f"next() -> {next(gen)}")


# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(f"\nFirst 10 Fibonacci: {list(islice(fibonacci(), 10))}")


# Generator expression
gen_exp = (x ** 2 for x in range(5))
print(f"\nGenerator expression: {list(gen_exp)}")

# Memory comparison
list_size = sys.getsizeof([x for x in range(1000)])
gen_size = sys.getsizeof(x for x in range(1000))
print(f"\nList comp size: {list_size} bytes")
print(f"Generator exp size: {gen_size} bytes")


# yield from
def chain_generators(*iterables):
    for it in iterables:
        yield from it


print(f"\nyield from chain: {list(chain_generators([1, 2], [3, 4], [5, 6]))}")

# -----------------------------------------------------------------------------
# 8.3 Comprehensions
# -----------------------------------------------------------------------------
print("\n--- 8.3 Comprehensions ---")

# List comprehension
squares = [x ** 2 for x in range(6)]
print(f"List comp [x**2]: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"List comp with filter: {evens}")

# Nested
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"Nested: {pairs}")

# Flatten
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(f"Flattened matrix: {flat}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(f"\nDict comp: {word_lengths}")

# Set comprehension
unique_lengths = {len(word) for word in ["cat", "dog", "mouse", "rat"]}
print(f"Set comp: {unique_lengths}")

# -----------------------------------------------------------------------------
# 8.4 itertools
# -----------------------------------------------------------------------------
print("\n--- 8.4 itertools ---")

# Infinite iterators
print("count(10):", list(islice(count(10), 5)))

# cycle
colors = cycle(["red", "green", "blue"])
print("cycle colors:", [next(colors) for _ in range(6)])

# chain
print("chain:", list(chain([1, 2], [3, 4], [5, 6])))

# takewhile / dropwhile
nums = [1, 3, 5, 2, 4, 6]
print(f"takewhile(x < 4, {nums}):", list(takewhile(lambda x: x < 4, nums)))
print(f"dropwhile(x < 4, {nums}):", list(dropwhile(lambda x: x < 4, nums)))

# Combinatorics
print("\ncombinations([1,2,3], 2):", list(combinations([1, 2, 3], 2)))
print("permutations([1,2,3], 2):", list(permutations([1, 2, 3], 2)))
print("product([1,2], ['a','b']):", list(product([1, 2], ['a', 'b'])))

# accumulate
print("\naccumulate([1,2,3,4,5]):", list(accumulate([1, 2, 3, 4, 5])))

# groupby
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
print("groupby:")
for key, group in groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# -----------------------------------------------------------------------------
# 8.5 Built-in Functions
# -----------------------------------------------------------------------------
print("\n--- 8.5 Built-in Functions ---")

numbers = [1, 2, 3, 4, 5]

# map
print(f"map(x**2): {list(map(lambda x: x ** 2, numbers))}")

# filter
print(f"filter(even): {list(filter(lambda x: x % 2 == 0, numbers))}")

# zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(f"zip: {list(zip(names, ages))}")

# enumerate
print("enumerate:")
for i, name in enumerate(names, start=1):
    print(f"  {i}. {name}")

# sorted, min, max, sum
print(f"\nsorted([3,1,4,1,5]): {sorted([3, 1, 4, 1, 5])}")
print(f"min/max: {min(numbers)}/{max(numbers)}")
print(f"sum: {sum(numbers)}")

# any, all
print(f"any(x > 3): {any(x > 3 for x in numbers)}")
print(f"all(x > 0): {all(x > 0 for x in numbers)}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
GENERATORS:
  - Use yield instead of return
  - Memory efficient (lazy evaluation)
  - Can be infinite
  - Generator expressions: (x for x in iterable)

COMPREHENSIONS:
  - List: [expr for x in iter if cond]
  - Dict: {k: v for x in iter}
  - Set: {expr for x in iter}

ITERTOOLS:
  - Infinite: count, cycle, repeat
  - Combining: chain, zip_longest
  - Filtering: takewhile, dropwhile, islice
  - Combinatorics: product, permutations, combinations
  - Grouping: groupby

BUILT-INS:
  - map, filter, reduce
  - zip, enumerate
  - sorted, min, max, sum
  - any, all
""")
