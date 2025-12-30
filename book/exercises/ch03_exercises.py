#!/usr/bin/env python3
"""
Chapter 3 Exercises: Control Flow and Functions
Complete each exercise by filling in the code where indicated.
"""

print("=" * 60)
print("CHAPTER 3 EXERCISES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercise 3.1: FizzBuzz
# -----------------------------------------------------------------------------
print("\n--- Exercise 3.1: FizzBuzz ---")

# Classic FizzBuzz: Print numbers 1-100
# - If divisible by 3, print "Fizz"
# - If divisible by 5, print "Buzz"
# - If divisible by both, print "FizzBuzz"
# - Otherwise, print the number

# Your code here (print first 20 for testing):


# -----------------------------------------------------------------------------
# Exercise 3.2: Prime Number Functions
# -----------------------------------------------------------------------------
print("\n--- Exercise 3.2: Prime Number Functions ---")


# TODO: Write these functions:

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    # Your code here
    pass


def primes_up_to(n: int) -> list[int]:
    """Return list of all primes up to n."""
    # Your code here
    pass


def prime_factors(n: int) -> list[int]:
    """Return list of prime factors of n."""
    # Your code here
    pass


# Uncomment to test:
# print(f"is_prime(17): {is_prime(17)}")  # True
# print(f"is_prime(15): {is_prime(15)}")  # False
# print(f"primes_up_to(30): {primes_up_to(30)}")  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print(f"prime_factors(84): {prime_factors(84)}")  # [2, 2, 3, 7]

# -----------------------------------------------------------------------------
# Exercise 3.3: Temperature Converter
# -----------------------------------------------------------------------------
print("\n--- Exercise 3.3: Temperature Converter ---")


def convert_temp(temp: float, unit: str) -> dict[str, float]:
    """
    Convert temperature to all three units.

    Args:
        temp: Temperature value
        unit: Source unit ('C', 'F', or 'K')

    Returns:
        Dict with celsius, fahrenheit, and kelvin values
    """
    # Your code here
    pass


# Uncomment to test:
# print(convert_temp(100, "C"))  # {'celsius': 100, 'fahrenheit': 212.0, 'kelvin': 373.15}
# print(convert_temp(32, "F"))   # {'celsius': 0.0, 'fahrenheit': 32, 'kelvin': 273.15}
# print(convert_temp(0, "K"))    # {'celsius': -273.15, 'fahrenheit': -459.67, 'kelvin': 0}

# -----------------------------------------------------------------------------
# Exercise 3.4: Calculator with Functions
# -----------------------------------------------------------------------------
print("\n--- Exercise 3.4: Calculator with Functions ---")


def calculate(expression: str) -> float:
    """
    Simple calculator that parses expressions like "5 + 3" or "10 * 2".
    Support: +, -, *, /, ** (power), // (floor div), % (modulo)

    Args:
        expression: String like "5 + 3"

    Returns:
        Result of the calculation
    """
    # Your code here
    pass


# Uncomment to test:
# print(f"'5 + 3' = {calculate('5 + 3')}")      # 8
# print(f"'10 - 4' = {calculate('10 - 4')}")    # 6
# print(f"'6 * 7' = {calculate('6 * 7')}")      # 42
# print(f"'15 / 4' = {calculate('15 / 4')}")    # 3.75
# print(f"'2 ** 8' = {calculate('2 ** 8')}")    # 256
# print(f"'17 // 5' = {calculate('17 // 5')}")  # 3
# print(f"'17 % 5' = {calculate('17 % 5')}")    # 2

# -----------------------------------------------------------------------------
# Exercise 3.5: Function Composition
# -----------------------------------------------------------------------------
print("\n--- Exercise 3.5: Function Composition ---")


def compose(*functions):
    """
    Return a function that composes all input functions.
    compose(f, g, h)(x) should return f(g(h(x)))

    Args:
        *functions: Variable number of functions

    Returns:
        A composed function
    """
    # Your code here
    pass


# Uncomment to test:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# square = lambda x: x ** 2
#
# composed = compose(add_one, double, square)  # add_one(double(square(x)))
# print(f"compose(add_one, double, square)(3) = {composed(3)}")  # add_one(double(9)) = add_one(18) = 19

# -----------------------------------------------------------------------------
# Exercise 3.6: Recursive Functions
# -----------------------------------------------------------------------------
print("\n--- Exercise 3.6: Recursive Functions ---")


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    # Your code here
    pass


def flatten(nested_list: list) -> list:
    """Flatten a nested list of arbitrary depth."""
    # Your code here
    pass


# Uncomment to test:
# print(f"fibonacci(10) = {fibonacci(10)}")  # 55
# print(f"flatten([1, [2, 3], [[4, 5], 6]]) = {flatten([1, [2, 3], [[4, 5], 6]])}")
# # [1, 2, 3, 4, 5, 6]


# =============================================================================
# SOLUTIONS
# =============================================================================

def show_solutions():
    print("\n" + "=" * 60)
    print("SOLUTIONS")
    print("=" * 60)

    # Exercise 3.1
    print("\n--- 3.1 FizzBuzz Solution ---")
    for i in range(1, 21):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

    # Exercise 3.2
    print("\n--- 3.2 Prime Functions Solution ---")

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def primes_up_to(n):
        return [i for i in range(2, n + 1) if is_prime(i)]

    def prime_factors(n):
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

    print(f"is_prime(17): {is_prime(17)}")
    print(f"primes_up_to(30): {primes_up_to(30)}")
    print(f"prime_factors(84): {prime_factors(84)}")

    # Exercise 3.3
    print("\n--- 3.3 Temperature Converter Solution ---")

    def convert_temp(temp, unit):
        if unit.upper() == 'C':
            c = temp
        elif unit.upper() == 'F':
            c = (temp - 32) * 5 / 9
        elif unit.upper() == 'K':
            c = temp - 273.15
        else:
            raise ValueError(f"Unknown unit: {unit}")

        return {
            "celsius": round(c, 2),
            "fahrenheit": round(c * 9 / 5 + 32, 2),
            "kelvin": round(c + 273.15, 2)
        }

    print(f"convert_temp(100, 'C'): {convert_temp(100, 'C')}")
    print(f"convert_temp(32, 'F'): {convert_temp(32, 'F')}")

    # Exercise 3.4
    print("\n--- 3.4 Calculator Solution ---")

    def calculate(expression):
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '**': lambda a, b: a ** b,
            '//': lambda a, b: a // b,
            '%': lambda a, b: a % b,
        }

        parts = expression.split()
        a = float(parts[0])
        op = parts[1]
        if len(parts) == 4:  # Handle ** operator
            op = parts[1] + parts[2]
            b = float(parts[3])
        else:
            b = float(parts[2])

        return ops[op](a, b)

    # Simpler solution using eval (but be careful with untrusted input!)
    def calculate_simple(expression):
        return eval(expression)

    print(f"'5 + 3' = {calculate_simple('5 + 3')}")
    print(f"'2 ** 8' = {calculate_simple('2 ** 8')}")

    # Exercise 3.5
    print("\n--- 3.5 Function Composition Solution ---")
    from functools import reduce

    def compose(*functions):
        def composed(x):
            return reduce(lambda acc, f: f(acc), reversed(functions), x)
        return composed

    add_one = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x ** 2

    composed = compose(add_one, double, square)
    print(f"compose(add_one, double, square)(3) = {composed(3)}")

    # Exercise 3.6
    print("\n--- 3.6 Recursive Functions Solution ---")

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    # More efficient with memoization
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fibonacci_memo(n):
        if n <= 1:
            return n
        return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    def flatten(nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    print(f"fibonacci(10) = {fibonacci_memo(10)}")
    print(f"flatten([1, [2, 3], [[4, 5], 6]]) = {flatten([1, [2, 3], [[4, 5], 6]])}")


# Uncomment to see solutions:
# show_solutions()
