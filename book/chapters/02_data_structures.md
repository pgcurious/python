# Chapter 2: Data Types and Structures

Python's built-in data structures are one of its greatest strengths. This chapter covers the four main collection types: **lists**, **tuples**, **dictionaries**, and **sets**.

## 2.1 Lists - The Versatile Array

Lists are Python's workhorse—mutable, ordered sequences that can hold any type.

```python
# Creating lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

# From other iterables
from_string = list("hello")     # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))     # [0, 1, 2, 3, 4]
```

### List Operations

```python
fruits = ["apple", "banana", "cherry"]

# Indexing (0-based, negative from end)
print(fruits[0])      # apple
print(fruits[-1])     # cherry

# Slicing (same as strings)
print(fruits[0:2])    # ['apple', 'banana']
print(fruits[::-1])   # ['cherry', 'banana', 'apple']

# Length
print(len(fruits))    # 3

# Membership testing
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# Concatenation and repetition
more = fruits + ["date", "elderberry"]
repeated = [0] * 5    # [0, 0, 0, 0, 0]
```

### Modifying Lists

```python
nums = [1, 2, 3, 4, 5]

# Change elements
nums[0] = 10              # [10, 2, 3, 4, 5]
nums[1:3] = [20, 30]      # [10, 20, 30, 4, 5]

# Add elements
nums.append(6)            # Add to end
nums.insert(0, 0)         # Insert at index
nums.extend([7, 8])       # Add multiple items

# Remove elements
nums.pop()                # Remove and return last item
nums.pop(0)               # Remove and return item at index
nums.remove(30)           # Remove first occurrence of value
del nums[0]               # Delete by index
nums.clear()              # Remove all items
```

### Useful List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sorting
numbers.sort()                    # In-place sort
numbers.sort(reverse=True)        # Descending
sorted_copy = sorted(numbers)     # Returns new list, original unchanged

# Reversing
numbers.reverse()                 # In-place
reversed_copy = list(reversed(numbers))  # Returns new list

# Finding elements
print(numbers.index(5))           # Index of first occurrence
print(numbers.count(1))           # Count occurrences

# Copying (important!)
original = [1, 2, 3]
reference = original              # Same list!
shallow_copy = original.copy()    # New list, same elements
shallow_copy2 = original[:]       # Another way to copy
shallow_copy3 = list(original)    # Yet another way

import copy
deep_copy = copy.deepcopy(original)  # Recursive copy for nested lists
```

### List as Stack and Queue

```python
# Stack (LIFO) - use append/pop
stack = []
stack.append(1)    # push
stack.append(2)
stack.append(3)
print(stack.pop()) # 3 - pop from end

# Queue (FIFO) - use collections.deque for efficiency
from collections import deque
queue = deque()
queue.append(1)      # enqueue
queue.append(2)
print(queue.popleft())  # 1 - dequeue from front
```

## 2.2 Tuples - Immutable Sequences

Tuples are like lists but immutable. Use them for fixed collections.

```python
# Creating tuples
empty = ()
single = (1,)              # Note the comma! (1) is just the number 1
coords = (10, 20)
mixed = (1, "hello", 3.14)
nested = ((1, 2), (3, 4))

# From other iterables
from_list = tuple([1, 2, 3])

# Tuple packing and unpacking
point = 10, 20, 30         # Packing (parentheses optional)
x, y, z = point            # Unpacking

# Extended unpacking
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5
```

### When to Use Tuples vs Lists

```python
# Tuples: fixed structure, heterogeneous data
person = ("Alice", 30, "Engineer")    # name, age, job
rgb = (255, 128, 0)                   # color values

# Lists: variable length, homogeneous data
scores = [95, 87, 91, 78]             # collection of similar items
names = ["Alice", "Bob", "Charlie"]

# Tuples as dictionary keys (lists can't be keys!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

# Named tuples for clarity
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)    # 10 20
```

## 2.3 Dictionaries - Key-Value Mapping

Dictionaries are Python's hash maps—fast key-based lookup.

```python
# Creating dictionaries
empty = {}
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Alternative creation methods
from_pairs = dict([("a", 1), ("b", 2)])
from_keys = dict.fromkeys(["a", "b", "c"], 0)  # All values = 0
using_kwargs = dict(name="Alice", age=30)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

### Accessing and Modifying

```python
person = {"name": "Alice", "age": 30}

# Access
print(person["name"])           # Alice
print(person.get("name"))       # Alice
print(person.get("job", "N/A")) # N/A (default if key missing)

# Check key existence
if "name" in person:
    print("Has name")

# Modify
person["age"] = 31              # Update existing
person["city"] = "NYC"          # Add new key

# Remove
del person["city"]              # Remove key
age = person.pop("age")         # Remove and return value
last = person.popitem()         # Remove and return last item (3.7+)
```

### Dictionary Methods

```python
d = {"a": 1, "b": 2, "c": 3}

# Get all keys, values, items
print(list(d.keys()))       # ['a', 'b', 'c']
print(list(d.values()))     # [1, 2, 3]
print(list(d.items()))      # [('a', 1), ('b', 2), ('c', 3)]

# Iterating
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key}: {value}")

# Update (merge dictionaries)
d.update({"c": 30, "d": 4})  # Update c, add d

# Python 3.9+ merge operators
merged = {"a": 1} | {"b": 2}        # {'a': 1, 'b': 2}
d |= {"e": 5}                        # In-place merge

# setdefault - get or set if missing
d.setdefault("f", 6)  # Returns 6, adds {"f": 6}
```

### Common Dictionary Patterns

```python
# Counting occurrences
text = "hello world"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1

# Or use Counter
from collections import Counter
counts = Counter(text)
print(counts.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

# Grouping items
from collections import defaultdict
words = ["apple", "banana", "apricot", "blueberry", "avocado"]
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
# {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry']}

# Ordered dictionary (Python 3.7+ dicts maintain order by default)
from collections import OrderedDict  # Still useful for some operations
```

## 2.4 Sets - Unique Collections

Sets are unordered collections of unique elements. Great for membership testing and eliminating duplicates.

```python
# Creating sets
empty = set()           # NOT {} - that's an empty dict!
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}
```

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all elements from both)
print(a | b)            # {1, 2, 3, 4, 5, 6}
print(a.union(b))       # Same

# Intersection (common elements)
print(a & b)            # {3, 4}
print(a.intersection(b))

# Difference (in a but not in b)
print(a - b)            # {1, 2}
print(a.difference(b))

# Symmetric difference (in either but not both)
print(a ^ b)            # {1, 2, 5, 6}
print(a.symmetric_difference(b))

# Subset and superset
small = {1, 2}
big = {1, 2, 3, 4}
print(small <= big)     # True - small is subset
print(big >= small)     # True - big is superset
print(small < big)      # True - proper subset
```

### Modifying Sets

```python
s = {1, 2, 3}

# Add elements
s.add(4)                # Add single element
s.update([5, 6, 7])     # Add multiple elements

# Remove elements
s.remove(7)             # Remove (raises KeyError if missing)
s.discard(10)           # Remove (no error if missing)
popped = s.pop()        # Remove and return arbitrary element
s.clear()               # Remove all
```

### Practical Set Uses

```python
# Remove duplicates from list while preserving order (Python 3.7+)
items = [1, 2, 2, 3, 1, 4, 3, 5]
unique = list(dict.fromkeys(items))  # [1, 2, 3, 4, 5]

# Fast membership testing
valid_users = {"alice", "bob", "charlie"}
if username in valid_users:  # O(1) lookup
    print("Valid!")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)  # {4, 5}

# Frozen sets (immutable, can be dict keys or set elements)
fs = frozenset([1, 2, 3])
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
```

## 2.5 Choosing the Right Data Structure

| Need | Use | Why |
|------|-----|-----|
| Ordered, mutable sequence | `list` | General purpose |
| Ordered, immutable sequence | `tuple` | Fixed data, dict keys |
| Key-value mapping | `dict` | Fast lookup by key |
| Unique elements, set math | `set` | Membership, deduplication |
| FIFO queue | `collections.deque` | O(1) operations both ends |
| Sorted collection | `sorted()` or `bisect` | Maintained order |
| Count occurrences | `collections.Counter` | Built for counting |
| Group by key | `collections.defaultdict` | Auto-creates missing keys |

## 2.6 Exercises

### Exercise 2.1: List Manipulation
```python
# Given this list of numbers:
numbers = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21]

# 1. Find the sum, average, min, and max
# 2. Get all even numbers
# 3. Get the second largest number
# 4. Remove duplicates and sort descending

# Your code here
```

### Exercise 2.2: Dictionary Operations
```python
# Given student scores:
scores = {
    "Alice": [85, 90, 88],
    "Bob": [72, 78, 75],
    "Charlie": [90, 92, 95],
    "Diana": [88, 85, 82]
}

# 1. Calculate average score for each student
# 2. Find the student with highest average
# 3. Create a grade dictionary (A: 90+, B: 80+, C: 70+, D: 60+, F: <60)

# Your code here
```

### Exercise 2.3: Set Operations
```python
# Course enrollments:
python_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
javascript_students = {"Bob", "Diana", "Frank", "Grace"}
java_students = {"Charlie", "Eve", "Frank", "Henry"}

# Find:
# 1. Students enrolled in ALL three courses
# 2. Students enrolled in Python but not JavaScript
# 3. Students enrolled in exactly one course
# 4. Students enrolled in at least two courses

# Your code here
```

### Exercise 2.4: Nested Data Structures
```python
# E-commerce order data:
orders = [
    {"id": 1, "customer": "Alice", "items": [("Widget", 2), ("Gadget", 1)], "total": 150.00},
    {"id": 2, "customer": "Bob", "items": [("Widget", 1)], "total": 50.00},
    {"id": 3, "customer": "Alice", "items": [("Gizmo", 3), ("Widget", 1)], "total": 200.00},
]

# Calculate:
# 1. Total revenue
# 2. Order count per customer
# 3. Most ordered item
# 4. Average order value

# Your code here
```

---

**Next Chapter:** [Control Flow and Functions](03_control_flow.md) - Conditionals, loops, and function definitions.
