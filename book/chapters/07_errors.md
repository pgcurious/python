# Chapter 7: Error Handling and Debugging

Robust error handling is crucial for production code. This chapter covers Python's exception system, debugging techniques, and logging.

## 7.1 Understanding Exceptions

Exceptions are Python's mechanism for handling errors. When an error occurs, Python raises an exception.

```python
# Common exceptions
x = 1 / 0           # ZeroDivisionError
lst = [1, 2, 3]
lst[10]             # IndexError
d = {}
d['missing']        # KeyError
int('abc')          # ValueError
undefined_var       # NameError
"text" + 5          # TypeError
open('nonexistent') # FileNotFoundError
```

### Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── OSError
    │   └── FileNotFoundError
    └── ...
```

## 7.2 Try-Except Blocks

### Basic Exception Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input - not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch multiple in one handler
try:
    # some code
    pass
except (ValueError, TypeError) as e:
    print(f"Value or Type error: {e}")

# Access exception details
try:
    int('abc')
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
```

### The else and finally Clauses

```python
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    # Runs only if no exception occurred
    print(f"File content: {content}")
finally:
    # Always runs (cleanup code)
    print("Cleanup: closing resources")

# Practical example
def read_file_safely(filename):
    file = None
    try:
        file = open(filename, 'r')
        return file.read()
    except FileNotFoundError:
        return None
    finally:
        if file:
            file.close()
```

### Catching All Exceptions

```python
# Catch all exceptions (use sparingly!)
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
    # Log the error, don't just ignore it!

# Never do this (catches even KeyboardInterrupt):
# except:
#     pass

# Better pattern for logging unknown errors
import traceback

try:
    risky_operation()
except Exception:
    traceback.print_exc()  # Print full traceback
```

## 7.3 Raising Exceptions

```python
# Raise built-in exception
def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

# Re-raise current exception
try:
    process_data()
except ValueError:
    print("Logging the error...")
    raise  # Re-raises the caught exception

# Chain exceptions (show cause)
try:
    int('abc')
except ValueError as e:
    raise RuntimeError("Failed to parse config") from e
```

## 7.4 Custom Exceptions

```python
# Simple custom exception
class ValidationError(Exception):
    """Raised when validation fails."""
    pass

# Custom exception with attributes
class APIError(Exception):
    """Raised when API request fails."""

    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

    def __str__(self):
        return f"[{self.status_code}] {super().__str__()}"

# Usage
def fetch_data(url):
    response = make_request(url)
    if response.status_code != 200:
        raise APIError(
            "Request failed",
            status_code=response.status_code,
            response=response
        )
    return response.json()

try:
    data = fetch_data('https://api.example.com')
except APIError as e:
    print(f"API Error: {e}")
    print(f"Status: {e.status_code}")
```

### Exception Hierarchy for Your Application

```python
class AppError(Exception):
    """Base exception for application."""
    pass

class ConfigError(AppError):
    """Configuration-related errors."""
    pass

class DatabaseError(AppError):
    """Database-related errors."""
    pass

class AuthenticationError(AppError):
    """Authentication failures."""
    pass

# Can catch all app errors
try:
    run_application()
except AppError as e:
    handle_app_error(e)
```

## 7.5 Assertions

Assertions are for debugging and catching programming errors, not user input validation.

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

# Assertions can be disabled with python -O
# Don't use for:
# - Input validation
# - Security checks
# - Production error handling

# Good use cases:
assert isinstance(data, dict), "Expected dictionary"
assert 0 <= probability <= 1, "Probability must be 0-1"
```

## 7.6 Logging

Logging is essential for debugging and monitoring production applications.

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create logger
logger = logging.getLogger(__name__)

# Log levels (in order of severity)
logger.debug("Detailed debugging info")
logger.info("General information")
logger.warning("Something unexpected happened")
logger.error("Error occurred but app continues")
logger.critical("Serious error, app may stop")

# Log exceptions with traceback
try:
    risky_operation()
except Exception:
    logger.exception("Operation failed")  # Includes traceback
```

### Advanced Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

# File handler with rotation
file_handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_format)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

## 7.7 Debugging Techniques

### Using print() (Quick and Dirty)

```python
def calculate(x, y):
    print(f"DEBUG: x={x}, y={y}")  # Temporary
    result = x * y + 10
    print(f"DEBUG: result={result}")
    return result
```

### Using the pdb Debugger

```python
import pdb

def buggy_function(data):
    for i, item in enumerate(data):
        pdb.set_trace()  # Breakpoint
        process(item)

# Or use breakpoint() in Python 3.7+
def buggy_function(data):
    for i, item in enumerate(data):
        breakpoint()  # Same as pdb.set_trace()
        process(item)
```

**PDB Commands:**
- `n` (next) - Execute next line
- `s` (step) - Step into function
- `c` (continue) - Continue to next breakpoint
- `p expr` - Print expression
- `l` (list) - Show source code
- `q` (quit) - Quit debugger
- `h` (help) - Show help

### Using IDE Debuggers

Modern IDEs (VS Code, PyCharm) provide graphical debuggers with:
- Breakpoints
- Variable inspection
- Call stack viewing
- Conditional breakpoints
- Watch expressions

## 7.8 Best Practices

```python
# 1. Be specific about exceptions
# Bad
try:
    process_data()
except:  # Catches everything!
    pass

# Good
try:
    process_data()
except ValueError as e:
    logger.error(f"Invalid data: {e}")
except ConnectionError as e:
    logger.error(f"Connection failed: {e}")

# 2. Don't silence exceptions without logging
# Bad
try:
    risky_operation()
except Exception:
    pass  # Silent failure!

# Good
try:
    risky_operation()
except Exception:
    logger.exception("Operation failed, continuing...")

# 3. Use context managers for cleanup
# Instead of try/finally for resources
with open('file.txt') as f:
    process(f)

# 4. Fail fast and explicitly
def process_user(user_id):
    if not isinstance(user_id, int):
        raise TypeError(f"user_id must be int, got {type(user_id)}")
    if user_id <= 0:
        raise ValueError(f"user_id must be positive, got {user_id}")
    # Process...

# 5. Provide helpful error messages
raise ValueError(
    f"Invalid date format: '{date_str}'. "
    f"Expected format: YYYY-MM-DD"
)
```

## 7.9 Exercises

### Exercise 7.1: Robust File Processor
```python
# Create a function that:
# - Reads a file and processes each line
# - Handles FileNotFoundError, PermissionError
# - Logs all errors with appropriate levels
# - Returns partial results on error
# - Includes line numbers in error messages
```

### Exercise 7.2: Custom Exception Hierarchy
```python
# Create a custom exception hierarchy for a banking app:
# - BankingError (base)
#   - AccountError
#     - InsufficientFundsError
#     - AccountNotFoundError
#   - TransactionError
#     - InvalidAmountError
#     - TransactionLimitExceeded
# Include helpful error messages and attributes
```

### Exercise 7.3: Retry Decorator
```python
# Create a decorator that:
# - Retries a function n times on exception
# - Supports configurable exceptions to catch
# - Implements exponential backoff
# - Logs each retry attempt
```

---

**Next Chapter:** [Iterators, Generators, and Comprehensions](08_iterators.md) - Lazy evaluation and elegant data processing.
