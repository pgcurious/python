# Chapter 11: Testing in Python

Testing is essential for maintaining code quality and confidence in your software. This chapter covers unit testing, pytest, and testing best practices.

## 11.1 Why Test?

- **Catch bugs early** - Find issues before production
- **Enable refactoring** - Change code with confidence
- **Document behavior** - Tests show how code should work
- **Design feedback** - Hard-to-test code often indicates design problems

## 11.2 unittest - The Standard Library

Python's built-in testing framework.

```python
# test_math.py
import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_result_type(self):
        result = divide(10, 3)
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
```

### Common Assertions

```python
# Equality
self.assertEqual(a, b)
self.assertNotEqual(a, b)

# Boolean
self.assertTrue(x)
self.assertFalse(x)

# None
self.assertIsNone(x)
self.assertIsNotNone(x)

# Identity
self.assertIs(a, b)
self.assertIsNot(a, b)

# Containment
self.assertIn(item, container)
self.assertNotIn(item, container)

# Types
self.assertIsInstance(obj, cls)

# Comparisons
self.assertGreater(a, b)
self.assertLess(a, b)
self.assertGreaterEqual(a, b)

# Floating point
self.assertAlmostEqual(a, b, places=7)

# Exceptions
with self.assertRaises(ValueError):
    risky_function()
```

### Setup and Teardown

```python
class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run once before all tests in this class."""
        cls.db = create_test_database()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests in this class."""
        cls.db.destroy()

    def setUp(self):
        """Run before each test method."""
        self.db.clear()
        self.db.insert({"id": 1, "name": "Test"})

    def tearDown(self):
        """Run after each test method."""
        self.db.rollback()

    def test_insert(self):
        self.db.insert({"id": 2, "name": "New"})
        self.assertEqual(len(self.db), 2)
```

## 11.3 pytest - The Modern Choice

pytest is the most popular Python testing framework. Install with `pip install pytest`.

### Basic pytest

```python
# test_example.py

def add(a, b):
    return a + b

# Simple test function (no class needed!)
def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

# Run with: pytest test_example.py
```

### pytest Features

```python
import pytest

# Testing exceptions
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

    # Check exception message
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Approximate comparisons
def test_float_comparison():
    assert 0.1 + 0.2 == pytest.approx(0.3)

# Parametrized tests - run same test with different inputs
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Marking tests
@pytest.mark.slow
def test_slow_operation():
    # Long running test
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Unix only")
def test_unix_feature():
    pass
```

### Fixtures

Fixtures provide reusable test setup.

```python
import pytest

@pytest.fixture
def sample_user():
    """Provides a sample user for tests."""
    return {"name": "Alice", "age": 30}

def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

def test_user_age(sample_user):
    assert sample_user["age"] == 30

# Fixture with cleanup
@pytest.fixture
def temp_file(tmp_path):
    """Creates a temporary file."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    yield file_path
    # Cleanup after test (optional with tmp_path)

# Fixture scopes
@pytest.fixture(scope="session")
def database():
    """Created once per test session."""
    db = create_database()
    yield db
    db.close()

@pytest.fixture(scope="module")
def config():
    """Created once per test module."""
    return load_config()

@pytest.fixture(scope="function")  # Default
def user():
    """Created for each test function."""
    return create_user()
```

### Conftest.py

Share fixtures across multiple test files.

```python
# conftest.py
import pytest

@pytest.fixture
def app():
    """Application fixture available to all tests."""
    app = create_app()
    app.config["TESTING"] = True
    return app

@pytest.fixture
def client(app):
    """Test client fixture."""
    return app.test_client()
```

## 11.4 Mocking

Mock objects replace real objects during testing.

```python
from unittest.mock import Mock, patch, MagicMock

# Basic mock
mock = Mock()
mock.method.return_value = 42
assert mock.method() == 42

# Check calls
mock.method.assert_called_once()
mock.method.assert_called_with()

# Patching
def get_data():
    response = requests.get("https://api.example.com/data")
    return response.json()

@patch("requests.get")
def test_get_data(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}
    result = get_data()
    assert result == {"key": "value"}

# Context manager patching
def test_with_patch():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        # Test code here

# Patching object methods
class Calculator:
    def add(self, a, b):
        return a + b

def test_calculator():
    calc = Calculator()
    with patch.object(calc, "add", return_value=100):
        assert calc.add(2, 3) == 100

# MagicMock for magic methods
mock = MagicMock()
mock.__len__.return_value = 5
assert len(mock) == 5
```

## 11.5 Testing Best Practices

### Test Structure: Arrange-Act-Assert

```python
def test_user_creation():
    # Arrange - set up test data
    user_data = {"name": "Alice", "email": "alice@example.com"}

    # Act - perform the action
    user = create_user(user_data)

    # Assert - verify the result
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
```

### Test Naming

```python
# Good: Descriptive names that explain what's being tested
def test_user_creation_with_valid_data_succeeds():
    pass

def test_user_creation_with_invalid_email_raises_error():
    pass

def test_transfer_between_accounts_updates_both_balances():
    pass

# Bad: Vague names
def test_user():
    pass

def test_1():
    pass
```

### One Assertion Per Test (Generally)

```python
# Good: Focused tests
def test_user_name_is_set():
    user = User("Alice")
    assert user.name == "Alice"

def test_user_email_is_lowercase():
    user = User("Alice", email="ALICE@EMAIL.COM")
    assert user.email == "alice@email.com"

# Exception: Related assertions are fine
def test_user_creation():
    user = User("Alice", age=30)
    assert user.name == "Alice"
    assert user.age == 30
    assert user.is_active
```

### Testing Edge Cases

```python
def test_empty_list():
    assert calculate_average([]) == 0

def test_single_element():
    assert calculate_average([5]) == 5

def test_negative_numbers():
    assert calculate_average([-1, -2, -3]) == -2

def test_large_numbers():
    assert calculate_average([10**9, 10**9]) == 10**9

def test_unicode_strings():
    assert process_name("日本語") == "日本語"
```

## 11.6 Test-Driven Development (TDD)

The TDD cycle: Red → Green → Refactor

```python
# 1. RED: Write a failing test first
def test_calculate_discount():
    assert calculate_discount(100, 10) == 90

# 2. GREEN: Write minimum code to pass
def calculate_discount(price, percent):
    return price - (price * percent / 100)

# 3. REFACTOR: Improve code while keeping tests green
def calculate_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")
    discount_amount = price * (percent / 100)
    return price - discount_amount

# 4. Add more tests and repeat
def test_calculate_discount_zero_percent():
    assert calculate_discount(100, 0) == 100

def test_calculate_discount_invalid_percent():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
```

## 11.7 Code Coverage

Measure how much code your tests exercise.

```bash
# Install pytest-cov
pip install pytest-cov

# Run with coverage
pytest --cov=mypackage tests/

# Generate HTML report
pytest --cov=mypackage --cov-report=html tests/
```

```python
# coverage configuration in pyproject.toml
[tool.coverage.run]
source = ["src"]
omit = ["tests/*"]

[tool.coverage.report]
fail_under = 80
show_missing = true
```

## 11.8 Testing Async Code

```python
import pytest
import asyncio

async def fetch_data():
    await asyncio.sleep(0.1)
    return {"data": "value"}

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == {"data": "value"}

# Install pytest-asyncio
# pip install pytest-asyncio
```

## 11.9 Exercises

### Exercise 11.1: Test a Calculator
```python
# Write comprehensive tests for a Calculator class:
# - Test all operations (add, subtract, multiply, divide)
# - Test edge cases (zero, negative, large numbers)
# - Test error handling (division by zero)
# - Use parametrized tests
```

### Exercise 11.2: Test with Mocking
```python
# Create tests for a weather service that:
# - Fetches weather from an API
# - Mock the API responses
# - Test success and failure scenarios
# - Test caching behavior
```

### Exercise 11.3: TDD Exercise
```python
# Use TDD to implement a password validator:
# - Minimum 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character
# Write tests first, then implementation
```

---

**Next Chapter:** [Practical Projects](12_projects.md) - Apply your knowledge with real-world projects.
