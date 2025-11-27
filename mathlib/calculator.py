"""
Calculator module providing basic and advanced mathematical operations.
"""
import math
from typing import Union


class Calculator:
    """A calculator class for performing mathematical operations."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent.

        Args:
            base: The base number
            exponent: The exponent

        Returns:
            base raised to the power of exponent
        """
        return base ** exponent

    @staticmethod
    def square_root(n: Union[int, float]) -> float:
        """Calculate the square root of a number.

        Args:
            n: The number to find the square root of

        Returns:
            Square root of n

        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)

    @staticmethod
    def factorial(n: int) -> int:
        """Calculate the factorial of a number.

        Args:
            n: A non-negative integer

        Returns:
            Factorial of n

        Raises:
            ValueError: If n is negative or not an integer
        """
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return math.factorial(n)

    @staticmethod
    def modulo(a: int, b: int) -> int:
        """Calculate a modulo b.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Remainder of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero divisor")
        return a % b
