# Chapter 9: Decorators and Context Managers

Decorators and context managers are powerful Python features for modifying behavior and managing resources. This chapter covers these metaprogramming tools.

## 9.1 Understanding Decorators

A decorator is a function that takes a function and returns a modified version of it.

### Functions as First-Class Objects

```python
# Functions can be assigned to variables
def greet(name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Functions can be passed as arguments
def apply_twice(func, value):
    return func(func(value))

def add_one(x):
    return x + 1

print(apply_twice(add_one, 5))  # 7

# Functions can be defined inside other functions
def outer():
    def inner():
        return "I'm inner!"
    return inner

func = outer()
print(func())  # I'm inner!
```

### Creating a Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# @ syntax is equivalent to:
# say_hello = my_decorator(say_hello)
```

### Decorators with Arguments

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet.__name__)  # greet (preserved by @wraps)
print(greet.__doc__)   # Greet someone by name.
```

### Common Decorator Patterns

```python
from functools import wraps
import time

# Timing decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Logging decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

# Retry decorator
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed, retrying...")
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success!"
```

### Decorators with Parameters

```python
def repeat(times):
    """Decorator that repeats function execution."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" 3 times

# Rate limiting decorator
from time import time, sleep
from functools import wraps

def rate_limit(calls_per_second):
    min_interval = 1.0 / calls_per_second
    def decorator(func):
        last_called = [0.0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time() - last_called[0]
            wait = min_interval - elapsed
            if wait > 0:
                sleep(wait)
            last_called[0] = time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def api_call():
    print("Making API call...")
```

### Class Decorators

```python
# Decorator for classes
def singleton(cls):
    instances = {}
    @wraps(cls, updated=[])
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Initializing database connection")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True - same instance

# Classes as decorators
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()  # Call #1, Hi!
say_hi()  # Call #2, Hi!
print(say_hi.count)  # 2
```

### Stacking Decorators

```python
@decorator1
@decorator2
@decorator3
def func():
    pass

# Equivalent to:
# func = decorator1(decorator2(decorator3(func)))
# Order: decorator3 is applied first, decorator1 last
```

## 9.2 Built-in Decorators

```python
class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        """Getter for value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter for value."""
        if new_value < 0:
            raise ValueError("Value must be positive")
        self._value = new_value

    @staticmethod
    def utility_function():
        """No access to instance or class."""
        return "I'm static"

    @classmethod
    def create_default(cls):
        """Access to class but not instance."""
        return cls()


# functools decorators
from functools import lru_cache, cache, cached_property

@lru_cache(maxsize=128)
def expensive_function(n):
    """Results are cached."""
    print(f"Computing for {n}")
    return n ** 2

print(expensive_function(5))  # Computing for 5, then 25
print(expensive_function(5))  # 25 (cached)

# Python 3.9+
@cache  # Simpler unlimited cache
def another_expensive(n):
    return n ** 3

class DataProcessor:
    @cached_property  # Python 3.8+
    def processed_data(self):
        """Computed once and cached."""
        print("Processing...")
        return [1, 2, 3, 4, 5]
```

## 9.3 Context Managers

Context managers handle setup and cleanup using `with` statements.

### Using Context Managers

```python
# File handling (most common use)
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed

# Multiple context managers
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())

# Database connections
with database.connection() as conn:
    conn.execute("SELECT * FROM users")
# Connection automatically closed/returned to pool

# Locks
import threading
lock = threading.Lock()
with lock:
    # Critical section
    pass
# Lock automatically released
```

### Creating Context Managers with Classes

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

with Timer() as t:
    # Some slow operation
    sum(range(1000000))
print(f"Total time: {t.elapsed:.4f}s")

# Exception handling in context manager
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        if exc_type is ValueError:
            print("Handling ValueError")
            return True  # Suppress the exception
        return False  # Re-raise other exceptions
```

### Creating Context Managers with contextlib

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.perf_counter()
    yield  # Code in 'with' block runs here
    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed:.4f} seconds")

with timer():
    sum(range(1000000))

# With a value
@contextmanager
def open_file(path, mode='r'):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

with open_file('test.txt', 'w') as f:
    f.write('Hello!')

# Temporary directory
from contextlib import contextmanager
import tempfile
import shutil

@contextmanager
def temp_directory():
    dirpath = tempfile.mkdtemp()
    try:
        yield dirpath
    finally:
        shutil.rmtree(dirpath)

with temp_directory() as tmpdir:
    print(f"Working in {tmpdir}")
# Directory automatically cleaned up
```

### contextlib Utilities

```python
from contextlib import suppress, redirect_stdout, nullcontext
import io

# Suppress specific exceptions
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
# No error raised

# Redirect stdout
buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes to buffer")
print(buffer.getvalue())

# Null context (placeholder)
def process(use_lock=True):
    cm = lock if use_lock else nullcontext()
    with cm:
        do_work()
```

## 9.4 Exercises

### Exercise 9.1: Debug Decorator
```python
# Create a @debug decorator that:
# - Prints function name, args, and kwargs when called
# - Prints the return value
# - Prints execution time
# - Works with any function
```

### Exercise 9.2: Memoization Decorator
```python
# Create a @memoize decorator that:
# - Caches results based on arguments
# - Works with functions that have hashable arguments
# - Includes a cache_clear() method
```

### Exercise 9.3: Database Transaction Manager
```python
# Create a context manager that:
# - Starts a database transaction
# - Commits on success
# - Rolls back on exception
# - Can be used as decorator too
```

---

**Next Chapter:** [Working with Data](10_data.md) - JSON, CSV, APIs, and data processing.
