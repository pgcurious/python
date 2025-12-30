#!/usr/bin/env python3
"""
Chapter 4: Object-Oriented Python
Run this file to see all examples in action.
"""

print("=" * 60)
print("CHAPTER 4: OBJECT-ORIENTED PYTHON")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 Classes and Objects
# -----------------------------------------------------------------------------
print("\n--- 4.1 Classes and Objects ---")


class Dog:
    """A simple Dog class."""
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old"


buddy = Dog("Buddy", 3)
print(f"Created: {buddy.describe()}")
print(f"Bark: {buddy.bark()}")
print(f"Species: {Dog.species}")


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self

    def decrement(self):
        self.count -= 1
        return self


counter = Counter()
counter.increment().increment().increment()
print(f"\nMethod chaining: counter.count = {counter.count}")

# -----------------------------------------------------------------------------
# 4.2 Special Methods
# -----------------------------------------------------------------------------
print("\n--- 4.2 Special Methods ---")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(3, 4)
p2 = Point(1, 2)
print(f"repr(p1): {repr(p1)}")
print(f"str(p1): {str(p1)}")
print(f"p1 == Point(3, 4): {p1 == Point(3, 4)}")
print(f"p1 + p2: {p1 + p2}")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
print(f"\nVector operations:")
print(f"v1 = {v1}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v1 = {3 * v1}")
print(f"abs(v1) = {abs(v1)}")


class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __iter__(self):
        return iter(self._songs)


playlist = Playlist("Favorites")
playlist.add("Song A")
playlist.add("Song B")
print(f"\nPlaylist: len={len(playlist)}, first={playlist[0]}")

# Callable
print("\nCallable objects:")


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)
print(f"Multiplier(2)(5) = {double(5)}")

# -----------------------------------------------------------------------------
# 4.3 Properties
# -----------------------------------------------------------------------------
print("\n--- 4.3 Properties ---")


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32


temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.celsius = 100
print(f"Updated: {temp.celsius}°C = {temp.fahrenheit}°F")

# -----------------------------------------------------------------------------
# 4.4 Inheritance
# -----------------------------------------------------------------------------
print("\n--- 4.4 Inheritance ---")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")
print(f"Dog: {dog.speak()}")
print(f"Cat: {cat.speak()}")


# super()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


emp = Employee("Alice", 30, "E123")
print(f"\nEmployee: {emp.name}, Age: {emp.age}, ID: {emp.employee_id}")

# MRO
print("\nMultiple Inheritance MRO:")


class A:
    def method(self):
        return "A"


class B(A):
    def method(self):
        return "B -> " + super().method()


class C(A):
    def method(self):
        return "C -> " + super().method()


class D(B, C):
    def method(self):
        return "D -> " + super().method()


d = D()
print(f"D().method(): {d.method()}")
print(f"MRO: {[c.__name__ for c in D.__mro__]}")

# Abstract Base Classes
print("\nAbstract Base Classes:")
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


rect = Rectangle(5, 3)
print(f"Rectangle(5, 3).area() = {rect.area()}")

# -----------------------------------------------------------------------------
# 4.5 Dataclasses
# -----------------------------------------------------------------------------
print("\n--- 4.5 Dataclasses ---")

from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_value(self):
        return self.price * self.quantity


product1 = Product("Widget", 29.99, 10)
product2 = Product("Widget", 29.99, 10)
print(f"Product: {product1}")
print(f"product1 == product2: {product1 == product2}")


@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float


ip = ImmutablePoint(3, 4)
print(f"Frozen dataclass: {ip}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
CLASSES:
  - __init__ is the constructor/initializer
  - self is explicitly passed to instance methods
  - Class attributes shared, instance attributes per-object

SPECIAL METHODS:
  - __repr__ for developer-friendly representation
  - __str__ for user-friendly representation
  - __eq__, __lt__ etc. for comparisons
  - __add__, __mul__ etc. for operators
  - __len__, __getitem__, __iter__ for containers
  - __call__ to make objects callable

PROPERTIES:
  - @property for getter
  - @name.setter for setter
  - Encapsulation without boilerplate

INHERITANCE:
  - class Child(Parent): ...
  - super() to call parent methods
  - ABC and @abstractmethod for abstract classes
  - MRO determines method resolution

DATACLASSES:
  - @dataclass for data-focused classes
  - Auto-generates __init__, __repr__, __eq__
  - frozen=True for immutable instances
""")

print("Run the exercises in exercises/ch04_exercises.py!")
