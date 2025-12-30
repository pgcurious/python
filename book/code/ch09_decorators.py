#!/usr/bin/env python3
"""
Chapter 9: Decorators and Context Managers
Run this file to see all examples in action.
"""

from functools import wraps, lru_cache
from contextlib import contextmanager
import time

print("=" * 60)
print("CHAPTER 9: DECORATORS AND CONTEXT MANAGERS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 9.1 Functions as First-Class Objects
# -----------------------------------------------------------------------------
print("\n--- 9.1 Functions as First-Class Objects ---")


def greet(name):
    return f"Hello, {name}!"


# Assign to variable
say_hello = greet
print(f"say_hello('Alice'): {say_hello('Alice')}")


# Pass as argument
def apply_twice(func, value):
    return func(func(value))


def add_exclamation(s):
    return s + "!"


result = apply_twice(add_exclamation, "Hello")
print(f"apply_twice(add_exclamation, 'Hello'): {result}")


# Return from function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)
print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")

# -----------------------------------------------------------------------------
# 9.2 Basic Decorator
# -----------------------------------------------------------------------------
print("\n--- 9.2 Basic Decorator ---")


def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Before {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  After {func.__name__}")
        return result
    return wrapper


@simple_decorator
def say_hi(name):
    """Say hi to someone."""
    print(f"  Hi, {name}!")


print("Calling decorated function:")
say_hi("Alice")
print(f"Function name preserved: {say_hi.__name__}")
print(f"Docstring preserved: {say_hi.__doc__}")

# -----------------------------------------------------------------------------
# 9.3 Practical Decorators
# -----------------------------------------------------------------------------
print("\n--- 9.3 Practical Decorators ---")


# Timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(0.1)
    return "Done"


print("Timer decorator:")
slow_function()


# Logging decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"  Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result!r}")
        return result
    return wrapper


@log_calls
def add(a, b):
    return a + b


print("\nLogging decorator:")
add(3, b=5)

# -----------------------------------------------------------------------------
# 9.4 Decorator with Parameters
# -----------------------------------------------------------------------------
print("\n--- 9.4 Decorator with Parameters ---")


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(times=3)
def say_word(word):
    print(f"  {word}")


print("Repeat decorator:")
say_word("Hello!")

# -----------------------------------------------------------------------------
# 9.5 Class as Decorator
# -----------------------------------------------------------------------------
print("\n--- 9.5 Class as Decorator ---")


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  Call #{self.count}")
        return self.func(*args, **kwargs)


@CountCalls
def say_something():
    print("  Something!")


print("Class decorator:")
say_something()
say_something()
print(f"  Total calls: {say_something.count}")

# -----------------------------------------------------------------------------
# 9.6 Built-in Decorators
# -----------------------------------------------------------------------------
print("\n--- 9.6 Built-in Decorators ---")


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @staticmethod
    def is_valid_radius(value):
        return value > 0

    @classmethod
    def unit_circle(cls):
        return cls(1)


circle = Circle(5)
print(f"radius: {circle.radius}")
print(f"area: {circle.area:.2f}")
print(f"is_valid_radius(5): {Circle.is_valid_radius(5)}")
print(f"unit_circle: {Circle.unit_circle().radius}")

# lru_cache
print("\n@lru_cache:")


@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"fibonacci(30): {fibonacci(30)}")
print(f"Cache info: {fibonacci.cache_info()}")

# -----------------------------------------------------------------------------
# 9.7 Context Managers
# -----------------------------------------------------------------------------
print("\n--- 9.7 Context Managers ---")


# Class-based context manager
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"  Elapsed: {self.elapsed:.4f}s")
        return False


print("Class-based context manager:")
with Timer() as t:
    sum(range(100000))


# Generator-based context manager
@contextmanager
def timer_context():
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"  Elapsed: {elapsed:.4f}s")


print("\n@contextmanager:")
with timer_context():
    sum(range(100000))


# Context manager with value
@contextmanager
def managed_file(path, mode='r'):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()


print("\nManaged file context manager demonstrated")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
DECORATORS:
  @decorator         # Apply decorator
  @decorator(args)   # Decorator factory

  def decorator(func):
      @wraps(func)   # Preserve metadata
      def wrapper(*args, **kwargs):
          # Before
          result = func(*args, **kwargs)
          # After
          return result
      return wrapper

BUILT-IN DECORATORS:
  @property, @staticmethod, @classmethod
  @functools.wraps, @functools.lru_cache

CONTEXT MANAGERS:
  with resource as r:
      use(r)

  # Class-based: __enter__, __exit__
  # Generator-based: @contextmanager with yield

USES:
  - Timing, logging, caching
  - Authentication, validation
  - Resource management (files, connections)
  - Transaction handling
""")
