#!/usr/bin/env python3
"""
Chapter 11: Testing in Python
Run this file to see testing examples.
Note: Run actual tests with: pytest tests/
"""

print("=" * 60)
print("CHAPTER 11: TESTING IN PYTHON")
print("=" * 60)

# -----------------------------------------------------------------------------
# Sample Code to Test
# -----------------------------------------------------------------------------
print("\n--- Sample Code to Test ---")


def add(a, b):
    """Add two numbers."""
    return a + b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """Simple calculator class."""

    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self

    def subtract(self, value):
        self.result -= value
        return self

    def clear(self):
        self.result = 0
        return self


print("Sample functions: add(), divide()")
print("Sample class: Calculator")

# -----------------------------------------------------------------------------
# unittest Examples
# -----------------------------------------------------------------------------
print("\n--- unittest Example Structure ---")
print("""
import unittest

class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def setUp(self):
        # Runs before each test
        pass

    def tearDown(self):
        # Runs after each test
        pass

if __name__ == '__main__':
    unittest.main()
""")

# Run a simple test inline
import unittest


class InlineTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


suite = unittest.TestLoader().loadTestsFromTestCase(InlineTest)
runner = unittest.TextTestRunner(verbosity=2)
print("Running inline test:")
runner.run(suite)

# -----------------------------------------------------------------------------
# pytest Examples
# -----------------------------------------------------------------------------
print("\n--- pytest Example Structure ---")
print("""
# test_math.py
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Fixtures
@pytest.fixture
def calculator():
    return Calculator()

def test_calculator_add(calculator):
    calculator.add(5).add(3)
    assert calculator.result == 8
""")

# -----------------------------------------------------------------------------
# Mocking Examples
# -----------------------------------------------------------------------------
print("\n--- Mocking Example ---")
from unittest.mock import Mock, patch

# Basic mock
print("Basic mock:")
mock = Mock()
mock.method.return_value = 42
print(f"  mock.method() = {mock.method()}")

# Mock with side effect
print("\nMock with side effect:")
mock.risky.side_effect = ValueError("Boom!")
try:
    mock.risky()
except ValueError as e:
    print(f"  Caught: {e}")


# Patching example
def get_greeting():
    """Get greeting from external service (simulated)."""
    # In real code, this might call an API
    return "Hello from API"


print("\nPatching demo:")
print(f"  Original: {get_greeting()}")

with patch(__name__ + '.get_greeting', return_value="Mocked greeting"):
    # Note: in a real test file, you'd patch the module path
    pass

print("""
# Patching in tests:
@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {'key': 'value'}
    result = fetch_data()
    assert result == {'key': 'value'}
""")

# -----------------------------------------------------------------------------
# Test Best Practices
# -----------------------------------------------------------------------------
print("\n--- Test Best Practices ---")
print("""
1. ARRANGE-ACT-ASSERT Pattern:
   def test_user_creation():
       # Arrange - set up test data
       user_data = {"name": "Alice"}

       # Act - perform action
       user = create_user(user_data)

       # Assert - verify result
       assert user.name == "Alice"

2. TEST NAMING:
   - test_function_does_something_when_condition()
   - test_add_returns_sum_of_positive_numbers()
   - test_divide_raises_error_when_dividing_by_zero()

3. ONE ASSERTION PER TEST (generally):
   def test_name_is_set():
       user = User("Alice")
       assert user.name == "Alice"

   def test_default_age_is_none():
       user = User("Alice")
       assert user.age is None

4. TEST EDGE CASES:
   - Empty inputs
   - Boundary values
   - Large inputs
   - None/null values
   - Unicode strings
""")

# -----------------------------------------------------------------------------
# Running Tests
# -----------------------------------------------------------------------------
print("\n--- Running Tests ---")
print("""
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific file
pytest test_math.py

# Run specific test
pytest test_math.py::test_add

# Run with coverage
pytest --cov=mypackage

# Run with coverage report
pytest --cov=mypackage --cov-report=html

# Run marked tests
pytest -m slow
pytest -m "not slow"

# Stop on first failure
pytest -x

# Show print output
pytest -s
""")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
UNITTEST:
  class TestX(unittest.TestCase):
      def test_something(self):
          self.assertEqual(a, b)
          self.assertTrue(x)
          self.assertRaises(Error, func)

PYTEST (preferred):
  def test_something():
      assert expression
      with pytest.raises(Error):
          risky_code()

  @pytest.fixture
  @pytest.mark.parametrize
  @pytest.mark.skip

MOCKING:
  from unittest.mock import Mock, patch
  mock = Mock()
  mock.method.return_value = value
  @patch('module.function')

BEST PRACTICES:
  - Arrange-Act-Assert pattern
  - Descriptive test names
  - Test edge cases
  - Use fixtures for setup
  - Keep tests focused and fast
""")
