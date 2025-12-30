#!/usr/bin/env python3
"""
Chapter 2: Data Types and Structures
Run this file to see all examples in action.
"""

print("=" * 60)
print("CHAPTER 2: DATA TYPES AND STRUCTURES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 Lists
# -----------------------------------------------------------------------------
print("\n--- 2.1 Lists ---")

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"nested: {nested}")

# List operations
fruits = ["apple", "banana", "cherry"]
print(f"\nfruits: {fruits}")
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[0:2]: {fruits[0:2]}")
print(f"len(fruits): {len(fruits)}")
print(f"'banana' in fruits: {'banana' in fruits}")

# Modifying lists
nums = [1, 2, 3, 4, 5]
print(f"\nOriginal nums: {nums}")
nums.append(6)
print(f"After append(6): {nums}")
nums.insert(0, 0)
print(f"After insert(0, 0): {nums}")
nums.extend([7, 8])
print(f"After extend([7, 8]): {nums}")
popped = nums.pop()
print(f"After pop() [{popped}]: {nums}")

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nUnsorted: {numbers}")
sorted_nums = sorted(numbers)
print(f"sorted(): {sorted_nums}")
numbers.sort(reverse=True)
print(f"sort(reverse=True): {numbers}")

# Copying (important!)
print("\nCopying lists:")
original = [1, 2, [3, 4]]
reference = original
shallow = original.copy()
import copy
deep = copy.deepcopy(original)

original[0] = 'X'
original[2][0] = 'Y'
print(f"After modifying original:")
print(f"  original: {original}")
print(f"  reference: {reference}")  # Same as original
print(f"  shallow: {shallow}")      # First element unchanged, nested changed
print(f"  deep: {deep}")            # Completely unchanged

# -----------------------------------------------------------------------------
# 2.2 Tuples
# -----------------------------------------------------------------------------
print("\n--- 2.2 Tuples ---")

# Creating tuples
single = (1,)  # Note the comma!
coords = (10, 20)
print(f"single tuple: {single}")
print(f"coords: {coords}")

# Tuple unpacking
x, y = coords
print(f"Unpacked: x={x}, y={y}")

# Extended unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"first={first}, middle={middle}, last={last}")

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"\nNamedtuple Point: {p}")
print(f"p.x={p.x}, p.y={p.y}")

# -----------------------------------------------------------------------------
# 2.3 Dictionaries
# -----------------------------------------------------------------------------
print("\n--- 2.3 Dictionaries ---")

person = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"person: {person}")

# Accessing
print(f"\nperson['name']: {person['name']}")
print(f"person.get('job', 'N/A'): {person.get('job', 'N/A')}")

# Modifying
person["age"] = 31
person["email"] = "alice@email.com"
print(f"After modifications: {person}")

# Dictionary methods
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Iterating
print("\nIterating:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"\nSquares dict: {squares}")

# Counter
from collections import Counter
text = "hello world"
counts = Counter(text)
print(f"\nCounter('{text}'): {dict(counts)}")
print(f"Most common 3: {counts.most_common(3)}")

# defaultdict
from collections import defaultdict
words = ["apple", "banana", "apricot", "blueberry"]
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(f"\nGrouped by first letter: {dict(by_letter)}")

# -----------------------------------------------------------------------------
# 2.4 Sets
# -----------------------------------------------------------------------------
print("\n--- 2.4 Sets ---")

# Creating sets
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])
print(f"numbers: {numbers}")
print(f"from_list (with duplicates removed): {from_list}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"\na = {a}")
print(f"b = {b}")
print(f"Union (a | b): {a | b}")
print(f"Intersection (a & b): {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric difference (a ^ b): {a ^ b}")

# Subset/superset
small = {1, 2}
big = {1, 2, 3, 4}
print(f"\n{small} <= {big}: {small <= big}")

# Modifying sets
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
print(f"\nAfter add and update: {s}")
s.discard(6)
print(f"After discard(6): {s}")

# Practical use: remove duplicates
items = [1, 2, 2, 3, 1, 4, 3, 5]
unique = list(dict.fromkeys(items))  # Preserves order
print(f"\nOriginal: {items}")
print(f"Unique (order preserved): {unique}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("QUICK REFERENCE:")
print("=" * 60)
print("""
LIST     []   - Ordered, mutable, allows duplicates
TUPLE    ()   - Ordered, immutable, allows duplicates
DICT     {}   - Key-value pairs, fast lookup, unique keys
SET      {}   - Unordered, unique elements only

Common operations:
  len(x)      - Length of any collection
  in          - Membership testing
  for...in    - Iteration

List methods:  append, extend, insert, pop, remove, sort, reverse
Dict methods:  get, keys, values, items, update, pop, setdefault
Set methods:   add, update, discard, remove, union, intersection
""")

print("\nRun the exercises in exercises/ch02_exercises.py!")
