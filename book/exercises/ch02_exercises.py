#!/usr/bin/env python3
"""
Chapter 2 Exercises: Data Types and Structures
Complete each exercise by filling in the code where indicated.
"""

print("=" * 60)
print("CHAPTER 2 EXERCISES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercise 2.1: List Manipulation
# -----------------------------------------------------------------------------
print("\n--- Exercise 2.1: List Manipulation ---")

numbers = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21]
print(f"numbers: {numbers}")

# TODO:
# 1. Find the sum, average, min, and max
# 2. Get all even numbers (as a new list)
# 3. Get the second largest number
# 4. Remove duplicates and sort descending (for this, use: [64, 34, 25, 12, 22, 11, 90, 45, 33, 21, 64, 11])

# Your code here:


# -----------------------------------------------------------------------------
# Exercise 2.2: Dictionary Operations
# -----------------------------------------------------------------------------
print("\n--- Exercise 2.2: Dictionary Operations ---")

scores = {
    "Alice": [85, 90, 88],
    "Bob": [72, 78, 75],
    "Charlie": [90, 92, 95],
    "Diana": [88, 85, 82]
}
print(f"scores: {scores}")

# TODO:
# 1. Calculate average score for each student (store in new dict: averages)
# 2. Find the student with highest average
# 3. Create a grade dictionary based on average (A: 90+, B: 80+, C: 70+)

# Your code here:


# -----------------------------------------------------------------------------
# Exercise 2.3: Set Operations
# -----------------------------------------------------------------------------
print("\n--- Exercise 2.3: Set Operations ---")

python_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
javascript_students = {"Bob", "Diana", "Frank", "Grace"}
java_students = {"Charlie", "Eve", "Frank", "Henry"}

print(f"Python: {python_students}")
print(f"JavaScript: {javascript_students}")
print(f"Java: {java_students}")

# TODO: Find:
# 1. Students enrolled in ALL three courses
# 2. Students enrolled in Python but not JavaScript
# 3. Students enrolled in exactly one course
# 4. Students enrolled in at least two courses

# Your code here:


# -----------------------------------------------------------------------------
# Exercise 2.4: Nested Data Structures
# -----------------------------------------------------------------------------
print("\n--- Exercise 2.4: Nested Data Structures ---")

orders = [
    {"id": 1, "customer": "Alice", "items": [("Widget", 2), ("Gadget", 1)], "total": 150.00},
    {"id": 2, "customer": "Bob", "items": [("Widget", 1)], "total": 50.00},
    {"id": 3, "customer": "Alice", "items": [("Gizmo", 3), ("Widget", 1)], "total": 200.00},
    {"id": 4, "customer": "Charlie", "items": [("Gadget", 2)], "total": 100.00},
]

print("Orders:")
for order in orders:
    print(f"  {order}")

# TODO: Calculate:
# 1. Total revenue
# 2. Order count per customer
# 3. Most ordered item (by quantity)
# 4. Average order value

# Your code here:


# -----------------------------------------------------------------------------
# Exercise 2.5: Word Frequency Counter
# -----------------------------------------------------------------------------
print("\n--- Exercise 2.5: Word Frequency Counter ---")

text = """
Python is a programming language that lets you work quickly
and integrate systems more effectively. Python is powerful
and Python is fun to learn. Learning Python opens doors.
"""

# TODO:
# 1. Count the frequency of each word (case-insensitive)
# 2. Find the 5 most common words
# 3. Find words that appear exactly once

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================

def show_solutions():
    print("\n" + "=" * 60)
    print("SOLUTIONS")
    print("=" * 60)

    # Exercise 2.1
    print("\n--- 2.1 Solution ---")
    numbers = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21]
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")

    evens = [n for n in numbers if n % 2 == 0]
    print(f"Even numbers: {evens}")

    sorted_nums = sorted(numbers, reverse=True)
    print(f"Second largest: {sorted_nums[1]}")

    with_dupes = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21, 64, 11]
    unique_sorted = sorted(set(with_dupes), reverse=True)
    print(f"Unique descending: {unique_sorted}")

    # Exercise 2.2
    print("\n--- 2.2 Solution ---")
    scores = {
        "Alice": [85, 90, 88],
        "Bob": [72, 78, 75],
        "Charlie": [90, 92, 95],
        "Diana": [88, 85, 82]
    }

    averages = {name: sum(s) / len(s) for name, s in scores.items()}
    print(f"Averages: {averages}")

    top_student = max(averages, key=averages.get)
    print(f"Top student: {top_student} ({averages[top_student]:.2f})")

    def get_grade(avg):
        if avg >= 90: return 'A'
        elif avg >= 80: return 'B'
        elif avg >= 70: return 'C'
        elif avg >= 60: return 'D'
        else: return 'F'

    grades = {name: get_grade(avg) for name, avg in averages.items()}
    print(f"Grades: {grades}")

    # Exercise 2.3
    print("\n--- 2.3 Solution ---")
    python_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
    javascript_students = {"Bob", "Diana", "Frank", "Grace"}
    java_students = {"Charlie", "Eve", "Frank", "Henry"}

    all_three = python_students & javascript_students & java_students
    print(f"In all three: {all_three}")

    python_not_js = python_students - javascript_students
    print(f"Python but not JS: {python_not_js}")

    all_students = python_students | javascript_students | java_students
    in_two_or_more = set()
    for student in all_students:
        count = sum([
            student in python_students,
            student in javascript_students,
            student in java_students
        ])
        if count >= 2:
            in_two_or_more.add(student)
    exactly_one = all_students - in_two_or_more
    print(f"Exactly one course: {exactly_one}")
    print(f"At least two courses: {in_two_or_more}")

    # Exercise 2.4
    print("\n--- 2.4 Solution ---")
    orders = [
        {"id": 1, "customer": "Alice", "items": [("Widget", 2), ("Gadget", 1)], "total": 150.00},
        {"id": 2, "customer": "Bob", "items": [("Widget", 1)], "total": 50.00},
        {"id": 3, "customer": "Alice", "items": [("Gizmo", 3), ("Widget", 1)], "total": 200.00},
        {"id": 4, "customer": "Charlie", "items": [("Gadget", 2)], "total": 100.00},
    ]

    total_revenue = sum(order["total"] for order in orders)
    print(f"Total revenue: ${total_revenue:.2f}")

    from collections import Counter
    customer_orders = Counter(order["customer"] for order in orders)
    print(f"Orders per customer: {dict(customer_orders)}")

    item_counts = Counter()
    for order in orders:
        for item, qty in order["items"]:
            item_counts[item] += qty
    print(f"Most ordered: {item_counts.most_common(1)[0]}")

    avg_order = total_revenue / len(orders)
    print(f"Average order value: ${avg_order:.2f}")

    # Exercise 2.5
    print("\n--- 2.5 Solution ---")
    text = """
    Python is a programming language that lets you work quickly
    and integrate systems more effectively. Python is powerful
    and Python is fun to learn. Learning Python opens doors.
    """

    import re
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    print(f"Word frequencies: {dict(word_counts)}")
    print(f"Top 5 words: {word_counts.most_common(5)}")
    unique_words = [word for word, count in word_counts.items() if count == 1]
    print(f"Words appearing once: {unique_words}")


# Uncomment to see solutions:
# show_solutions()
