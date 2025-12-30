# Chapter 4: Object-Oriented Python

Python supports object-oriented programming with classes, inheritance, and special "magic" methods. This chapter covers Python's approach to OOP, which differs in some key ways from languages like Java or C++.

## 4.1 Classes and Objects

### Basic Class Definition

```python
class Dog:
    """A simple Dog class."""

    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old"


# Creating instances
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print(buddy.name)           # Buddy
print(buddy.bark())         # Buddy says woof!
print(Dog.species)          # Canis familiaris (access via class)
print(buddy.species)        # Same (access via instance)
```

### The `self` Parameter

Unlike many languages, Python explicitly passes the instance as the first parameter to all instance methods. By convention, this is named `self`.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self  # Return self for method chaining

    def decrement(self):
        self.count -= 1
        return self

# Method chaining
counter = Counter()
counter.increment().increment().increment()
print(counter.count)  # 3
```

### Class vs Instance Attributes

```python
class Employee:
    # Class attribute
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        # Instance attributes
        self.name = name
        self.salary = salary
        Employee.employee_count += 1  # Modify class attribute

    @classmethod
    def get_company(cls):
        return cls.company

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(Employee.employee_count)  # 2
print(Employee.get_company())   # TechCorp
print(Employee.is_valid_salary(50000))  # True
```

## 4.2 Special Methods (Magic Methods / Dunder Methods)

Python uses special methods (surrounded by double underscores) to define how objects behave with operators and built-in functions.

### String Representation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Official string representation (for developers)."""
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """Informal string representation (for users)."""
        return f"({self.x}, {self.y})"


p = Point(3, 4)
print(repr(p))  # Point(3, 4) - uses __repr__
print(str(p))   # (3, 4) - uses __str__
print(p)        # (3, 4) - print uses __str__
```

### Comparison Methods

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    # Python can derive __gt__, __ge__ from __lt__, __le__
    # Or use functools.total_ordering decorator


r1 = Rectangle(3, 4)   # area = 12
r2 = Rectangle(2, 6)   # area = 12
r3 = Rectangle(5, 5)   # area = 25

print(r1 == r2)  # True
print(r1 < r3)   # True
```

### Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)       # Vector(4, 6)
print(v1 - v2)       # Vector(2, 2)
print(v1 * 2)        # Vector(6, 8)
print(3 * v1)        # Vector(9, 12) - uses __rmul__
print(-v1)           # Vector(-3, -4)
print(abs(v1))       # 5.0
```

### Container Methods

```python
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

    def __setitem__(self, index, value):
        self._songs[index] = value

    def __delitem__(self, index):
        del self._songs[index]

    def __contains__(self, song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)


playlist = Playlist("My Favorites")
playlist.add("Song A")
playlist.add("Song B")
playlist.add("Song C")

print(len(playlist))         # 3
print(playlist[0])           # Song A
print("Song B" in playlist)  # True

for song in playlist:
    print(song)
```

### Callable Objects

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Useful for creating function-like objects with state
```

## 4.3 Properties and Encapsulation

Python doesn't have strict access modifiers like `private` or `protected`. Instead, it uses naming conventions:
- `_name`: "Protected" - internal use suggested
- `__name`: "Private" - name mangling applied

### Using Properties

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature via Fahrenheit."""
        self.celsius = (value - 32) * 5/9


temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.fahrenheit = 100
print(temp.celsius)     # 37.77...

# temp.celsius = -300  # Raises ValueError
```

## 4.4 Inheritance

### Single Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

    def describe(self):
        return f"I am {self.name}"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

    def fetch(self):
        return f"{self.name} fetches the ball"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())      # Buddy says woof!
print(dog.describe())   # I am Buddy (inherited)
print(dog.fetch())      # Buddy fetches the ball

print(cat.speak())      # Whiskers says meow!
```

### Using super()

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)  # Call parent constructor
        self.employee_id = employee_id
        self.department = department

    def describe(self):
        return f"{self.name} (ID: {self.employee_id}) - {self.department}"


emp = Employee("Alice", 30, "E123", "Engineering")
print(emp.name)        # Alice (inherited)
print(emp.describe())  # Alice (ID: E123) - Engineering
```

### Multiple Inheritance and MRO

```python
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
print(d.method())  # D -> B -> C -> A

# Method Resolution Order (MRO)
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### Abstract Base Classes

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
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
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


# shape = Shape()  # TypeError: Can't instantiate abstract class
rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")  # 15
```

## 4.5 Dataclasses (Python 3.7+)

For classes that are mainly containers for data, use dataclasses.

```python
from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_value(self):
        return self.price * self.quantity


# Automatic __init__, __repr__, __eq__
product = Product("Widget", 29.99, 10)
print(product)  # Product(name='Widget', price=29.99, quantity=10)

product2 = Product("Widget", 29.99, 10)
print(product == product2)  # True


@dataclass
class ShoppingCart:
    items: List[Product] = field(default_factory=list)

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.total_value() for item in self.items)


@dataclass(frozen=True)  # Immutable dataclass
class Point:
    x: float
    y: float


p = Point(3, 4)
# p.x = 5  # FrozenInstanceError
```

## 4.6 Exercises

### Exercise 4.1: Bank Account Class
```python
# Create a BankAccount class with:
# - account_number, holder_name, balance (private)
# - deposit(amount) and withdraw(amount) methods
# - Property for balance (read-only)
# - Transaction history tracking
# - Overdraft protection

# Your code here
```

### Exercise 4.2: Shape Hierarchy
```python
# Create an abstract Shape class and implement:
# - Rectangle, Circle, Triangle subclasses
# - Each with area() and perimeter() methods
# - A function that calculates total area of a list of shapes

# Your code here
```

### Exercise 4.3: Custom Container
```python
# Create a SortedList class that:
# - Always keeps elements in sorted order
# - Supports len(), indexing, iteration
# - Has add() method to insert while maintaining order
# - Has remove() method

# Your code here
```

### Exercise 4.4: Playing Card
```python
# Using dataclasses, create:
# - Card class with suit and rank
# - Deck class with 52 cards
# - shuffle() and deal(n) methods
# - Comparison based on card values

# Your code here
```

---

**Next Chapter:** [Modules, Packages, and Environments](05_modules.md) - Organizing code and managing dependencies.
