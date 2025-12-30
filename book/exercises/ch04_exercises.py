#!/usr/bin/env python3
"""
Chapter 4 Exercises: Object-Oriented Python
Complete each exercise by filling in the code where indicated.
"""

print("=" * 60)
print("CHAPTER 4 EXERCISES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercise 4.1: Bank Account Class
# -----------------------------------------------------------------------------
print("\n--- Exercise 4.1: Bank Account Class ---")

# TODO: Create a BankAccount class with:
# - account_number, holder_name, _balance (private)
# - deposit(amount) and withdraw(amount) methods
# - Property for balance (read-only)
# - Transaction history tracking
# - Overdraft protection (can't go below 0)


class BankAccount:
    """A bank account with transaction history."""

    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0):
        # Your code here
        pass

    @property
    def balance(self) -> float:
        # Your code here
        pass

    def deposit(self, amount: float) -> bool:
        # Your code here
        pass

    def withdraw(self, amount: float) -> bool:
        # Your code here
        pass

    def get_transaction_history(self) -> list:
        # Your code here
        pass


# Uncomment to test:
# account = BankAccount("12345", "Alice", 100)
# account.deposit(50)
# account.withdraw(30)
# account.withdraw(200)  # Should fail
# print(f"Balance: ${account.balance}")
# print(f"History: {account.get_transaction_history()}")

# -----------------------------------------------------------------------------
# Exercise 4.2: Shape Hierarchy
# -----------------------------------------------------------------------------
print("\n--- Exercise 4.2: Shape Hierarchy ---")

from abc import ABC, abstractmethod
import math

# TODO: Create abstract Shape class and implement:
# - Rectangle, Circle, Triangle (with base and height)
# - Each with area() and perimeter() methods
# - A function that calculates total area of shapes


class Shape(ABC):
    """Abstract base class for shapes."""
    # Your code here
    pass


class Rectangle(Shape):
    # Your code here
    pass


class Circle(Shape):
    # Your code here
    pass


class Triangle(Shape):
    """Right triangle with base and height."""
    # Your code here
    pass


def total_area(shapes: list) -> float:
    """Calculate total area of all shapes."""
    # Your code here
    pass


# Uncomment to test:
# shapes = [Rectangle(5, 3), Circle(2), Triangle(4, 3)]
# for shape in shapes:
#     print(f"{shape.__class__.__name__}: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")
# print(f"Total area: {total_area(shapes):.2f}")

# -----------------------------------------------------------------------------
# Exercise 4.3: Custom Container - SortedList
# -----------------------------------------------------------------------------
print("\n--- Exercise 4.3: SortedList ---")


class SortedList:
    """A list that always maintains sorted order."""

    def __init__(self, items=None):
        # Your code here
        pass

    def add(self, item):
        """Add item while maintaining sorted order."""
        # Your code here
        pass

    def remove(self, item):
        """Remove first occurrence of item."""
        # Your code here
        pass

    def __len__(self):
        # Your code here
        pass

    def __getitem__(self, index):
        # Your code here
        pass

    def __iter__(self):
        # Your code here
        pass

    def __repr__(self):
        # Your code here
        pass


# Uncomment to test:
# sl = SortedList([3, 1, 4, 1, 5, 9])
# print(f"Initial: {sl}")  # SortedList([1, 1, 3, 4, 5, 9])
# sl.add(2)
# print(f"After add(2): {sl}")  # SortedList([1, 1, 2, 3, 4, 5, 9])
# sl.remove(1)
# print(f"After remove(1): {sl}")  # SortedList([1, 2, 3, 4, 5, 9])
# print(f"Length: {len(sl)}, First: {sl[0]}")

# -----------------------------------------------------------------------------
# Exercise 4.4: Playing Cards with Dataclasses
# -----------------------------------------------------------------------------
print("\n--- Exercise 4.4: Playing Cards ---")

from dataclasses import dataclass, field
from typing import List
import random

# TODO: Create Card and Deck classes using dataclasses


@dataclass
class Card:
    """A playing card."""
    # Your code here
    # Should have suit and rank
    # Should support comparison based on rank value
    pass


@dataclass
class Deck:
    """A deck of 52 playing cards."""
    # Your code here
    # Should auto-generate 52 cards
    # Should have shuffle() and deal(n) methods
    pass


# Uncomment to test:
# deck = Deck()
# print(f"Deck has {len(deck.cards)} cards")
# deck.shuffle()
# hand = deck.deal(5)
# print(f"Hand: {hand}")
# print(f"Remaining: {len(deck.cards)} cards")

# -----------------------------------------------------------------------------
# Exercise 4.5: Mixin Classes
# -----------------------------------------------------------------------------
print("\n--- Exercise 4.5: Mixin Classes ---")


# TODO: Create mixin classes for common functionality
# - JsonMixin: adds to_json() method
# - ComparableMixin: adds comparison based on a key attribute

class JsonMixin:
    """Mixin that provides JSON serialization."""
    # Your code here
    pass


class ComparableMixin:
    """Mixin that provides comparison based on compare_key property."""
    # Your code here
    pass


# Example usage class combining mixins
# class Person(JsonMixin, ComparableMixin):
#     compare_key_attr = 'age'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Uncomment to test:
# p1 = Person("Alice", 30)
# p2 = Person("Bob", 25)
# print(p1.to_json())
# print(f"p1 > p2: {p1 > p2}")  # True (30 > 25)


# =============================================================================
# SOLUTIONS
# =============================================================================

def show_solutions():
    print("\n" + "=" * 60)
    print("SOLUTIONS")
    print("=" * 60)

    # Exercise 4.1
    print("\n--- 4.1 BankAccount Solution ---")

    class BankAccount:
        def __init__(self, account_number, holder_name, initial_balance=0):
            self.account_number = account_number
            self.holder_name = holder_name
            self._balance = initial_balance
            self._transactions = []

        @property
        def balance(self):
            return self._balance

        def deposit(self, amount):
            if amount <= 0:
                return False
            self._balance += amount
            self._transactions.append(f"Deposit: +${amount}")
            return True

        def withdraw(self, amount):
            if amount <= 0 or amount > self._balance:
                self._transactions.append(f"Failed withdrawal: ${amount}")
                return False
            self._balance -= amount
            self._transactions.append(f"Withdrawal: -${amount}")
            return True

        def get_transaction_history(self):
            return self._transactions.copy()

    account = BankAccount("12345", "Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)
    print(f"Balance: ${account.balance}")
    print(f"History: {account.get_transaction_history()}")

    # Exercise 4.2
    print("\n--- 4.2 Shape Hierarchy Solution ---")

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2

        def perimeter(self):
            return 2 * math.pi * self.radius

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base = base
            self.height = height

        def area(self):
            return 0.5 * self.base * self.height

        def perimeter(self):
            hypotenuse = math.sqrt(self.base**2 + self.height**2)
            return self.base + self.height + hypotenuse

    def total_area(shapes):
        return sum(s.area() for s in shapes)

    shapes = [Rectangle(5, 3), Circle(2), Triangle(4, 3)]
    for shape in shapes:
        print(f"{shape.__class__.__name__}: area={shape.area():.2f}")
    print(f"Total area: {total_area(shapes):.2f}")

    # Exercise 4.3
    print("\n--- 4.3 SortedList Solution ---")
    import bisect

    class SortedList:
        def __init__(self, items=None):
            self._items = sorted(items) if items else []

        def add(self, item):
            bisect.insort(self._items, item)

        def remove(self, item):
            self._items.remove(item)

        def __len__(self):
            return len(self._items)

        def __getitem__(self, index):
            return self._items[index]

        def __iter__(self):
            return iter(self._items)

        def __repr__(self):
            return f"SortedList({self._items})"

    sl = SortedList([3, 1, 4, 1, 5, 9])
    print(f"Initial: {sl}")
    sl.add(2)
    print(f"After add(2): {sl}")

    # Exercise 4.4
    print("\n--- 4.4 Playing Cards Solution ---")

    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    @dataclass
    class Card:
        suit: str
        rank: str

        def __lt__(self, other):
            return RANKS.index(self.rank) < RANKS.index(other.rank)

    @dataclass
    class Deck:
        cards: List[Card] = field(default_factory=list)

        def __post_init__(self):
            if not self.cards:
                self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

        def shuffle(self):
            random.shuffle(self.cards)

        def deal(self, n):
            dealt = self.cards[:n]
            self.cards = self.cards[n:]
            return dealt

    deck = Deck()
    print(f"Deck has {len(deck.cards)} cards")
    deck.shuffle()
    hand = deck.deal(5)
    print(f"Hand: {[f'{c.rank} of {c.suit}' for c in hand]}")

    # Exercise 4.5
    print("\n--- 4.5 Mixin Solution ---")
    import json

    class JsonMixin:
        def to_json(self):
            return json.dumps(self.__dict__)

    class ComparableMixin:
        compare_key_attr = None

        @property
        def compare_key(self):
            return getattr(self, self.compare_key_attr)

        def __lt__(self, other):
            return self.compare_key < other.compare_key

        def __le__(self, other):
            return self.compare_key <= other.compare_key

        def __gt__(self, other):
            return self.compare_key > other.compare_key

        def __ge__(self, other):
            return self.compare_key >= other.compare_key

    class Person(JsonMixin, ComparableMixin):
        compare_key_attr = 'age'

        def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    print(f"p1.to_json(): {p1.to_json()}")
    print(f"p1 > p2: {p1 > p2}")


# Uncomment to see solutions:
# show_solutions()
