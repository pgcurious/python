#!/usr/bin/env python3
"""
Chapter 7: Error Handling and Debugging
Run this file to see all examples in action.
"""

import logging
import traceback

print("=" * 60)
print("CHAPTER 7: ERROR HANDLING AND DEBUGGING")
print("=" * 60)

# -----------------------------------------------------------------------------
# 7.1 Understanding Exceptions
# -----------------------------------------------------------------------------
print("\n--- 7.1 Understanding Exceptions ---")


def demonstrate_exceptions():
    """Show common exception types."""
    exceptions = [
        ("ZeroDivisionError", lambda: 1 / 0),
        ("IndexError", lambda: [1, 2, 3][10]),
        ("KeyError", lambda: {}["missing"]),
        ("ValueError", lambda: int("abc")),
        ("TypeError", lambda: "text" + 5),
    ]

    for name, func in exceptions:
        try:
            func()
        except Exception as e:
            print(f"  {name}: {e}")


demonstrate_exceptions()

# -----------------------------------------------------------------------------
# 7.2 Try-Except Blocks
# -----------------------------------------------------------------------------
print("\n--- 7.2 Try-Except Blocks ---")


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"  Type error: {e}")
        return None
    else:
        print(f"  Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("  Cleanup complete")


print("divide(10, 2):")
divide(10, 2)
print("\ndivide(10, 0):")
divide(10, 0)

# -----------------------------------------------------------------------------
# 7.3 Raising Exceptions
# -----------------------------------------------------------------------------
print("\n--- 7.3 Raising Exceptions ---")


def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    return True


for test_age in [25, -5, "thirty"]:
    try:
        validate_age(test_age)
        print(f"  Age {test_age} is valid")
    except (TypeError, ValueError) as e:
        print(f"  Invalid age {test_age!r}: {e}")

# -----------------------------------------------------------------------------
# 7.4 Custom Exceptions
# -----------------------------------------------------------------------------
print("\n--- 7.4 Custom Exceptions ---")


class ValidationError(Exception):
    """Custom validation exception."""
    pass


class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. Balance: ${balance:.2f}"
        )


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return amount


account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"  Error: {e}")
    print(f"  Balance: ${e.balance}, Attempted: ${e.amount}")

# -----------------------------------------------------------------------------
# 7.5 Logging
# -----------------------------------------------------------------------------
print("\n--- 7.5 Logging ---")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s %(message)s"
)
logger = logging.getLogger(__name__)

print("Log levels demonstration:")
logger.debug("Debug: Detailed debugging information")
logger.info("Info: General information")
logger.warning("Warning: Something unexpected")
logger.error("Error: Error occurred")
logger.critical("Critical: Serious error")

# Log with exception
print("\nLogging an exception:")
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Division failed")

# -----------------------------------------------------------------------------
# 7.6 Traceback
# -----------------------------------------------------------------------------
print("\n--- 7.6 Traceback ---")


def function_a():
    function_b()


def function_b():
    function_c()


def function_c():
    raise RuntimeError("Something went wrong!")


try:
    function_a()
except RuntimeError:
    print("Captured traceback:")
    traceback.print_exc()

# -----------------------------------------------------------------------------
# 7.7 Assertions
# -----------------------------------------------------------------------------
print("\n--- 7.7 Assertions ---")


def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    return sum(numbers) / len(numbers)


print(f"  Average of [1, 2, 3]: {calculate_average([1, 2, 3])}")

try:
    calculate_average([])
except AssertionError as e:
    print(f"  AssertionError: {e}")

# -----------------------------------------------------------------------------
# 7.8 Best Practices Demo
# -----------------------------------------------------------------------------
print("\n--- 7.8 Best Practices ---")


def process_data_safely(data):
    """Demonstrate proper error handling."""
    if data is None:
        raise ValueError("Data cannot be None")

    try:
        # Attempt processing
        result = {"processed": True, "count": len(data)}
        return result
    except TypeError as e:
        # Handle specific error
        logger.error(f"Invalid data type: {e}")
        raise
    except Exception as e:
        # Log unexpected errors but re-raise
        logger.exception("Unexpected error during processing")
        raise


# Test with valid and invalid data
for test_data in [{"items": [1, 2, 3]}, None]:
    try:
        result = process_data_safely(test_data)
        print(f"  Success: {result}")
    except ValueError as e:
        print(f"  ValueError: {e}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
EXCEPTION HANDLING:
  try:
      risky_code()
  except SpecificError as e:
      handle_error()
  else:
      no_error_occurred()
  finally:
      cleanup()

BEST PRACTICES:
  - Catch specific exceptions, not bare except:
  - Don't silence exceptions without logging
  - Use context managers for cleanup
  - Provide helpful error messages
  - Create custom exceptions for your domain

LOGGING LEVELS:
  DEBUG < INFO < WARNING < ERROR < CRITICAL

DEBUGGING:
  - pdb.set_trace() or breakpoint()
  - traceback.print_exc() for stack traces
  - logging.exception() includes traceback
""")
