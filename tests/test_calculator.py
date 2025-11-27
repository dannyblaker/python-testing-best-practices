"""Unit tests for the Calculator module."""
import pytest
import math
from mathlib.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    @pytest.fixture
    def calc(self):
        """Fixture to provide a Calculator instance."""
        return Calculator()

    # Test addition
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
        (-5, -3, -8),
        (1000000, 2000000, 3000000),
    ])
    def test_add(self, calc, a, b, expected):
        """Test addition with various inputs."""
        assert calc.add(a, b) == expected

    # Test subtraction
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 2),
        (0, 0, 0),
        (-1, -1, 0),
        (10.5, 5.5, 5.0),
        (3, 5, -2),
    ])
    def test_subtract(self, calc, a, b, expected):
        """Test subtraction with various inputs."""
        assert calc.subtract(a, b) == expected

    # Test multiplication
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (1.5, 2, 3.0),
        (0.1, 0.2, pytest.approx(0.02)),
    ])
    def test_multiply(self, calc, a, b, expected):
        """Test multiplication with various inputs."""
        assert calc.multiply(a, b) == expected

    # Test division
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (6, 2, 3.0),
        (5, 2, 2.5),
        (-6, 2, -3.0),
        (-6, -2, 3.0),
        (0, 5, 0.0),
    ])
    def test_divide(self, calc, a, b, expected):
        """Test division with various inputs."""
        assert calc.divide(a, b) == expected

    @pytest.mark.unit
    def test_divide_by_zero(self, calc):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(5, 0)

    # Test power
    @pytest.mark.unit
    @pytest.mark.parametrize("base,exp,expected", [
        (2, 3, 8),
        (5, 0, 1),
        (2, -1, 0.5),
        (9, 0.5, 3.0),
        (0, 5, 0),
        (10, 2, 100),
    ])
    def test_power(self, calc, base, exp, expected):
        """Test power operation with various inputs."""
        assert calc.power(base, exp) == pytest.approx(expected)

    # Test square root
    @pytest.mark.unit
    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (4, 2),
        (9, 3),
        (16, 4),
        (2, math.sqrt(2)),
        (0.25, 0.5),
    ])
    def test_square_root(self, calc, n, expected):
        """Test square root with various inputs."""
        assert calc.square_root(n) == pytest.approx(expected)

    @pytest.mark.unit
    def test_square_root_negative(self, calc):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            calc.square_root(-1)

    # Test factorial
    @pytest.mark.unit
    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (10, 3628800),
    ])
    def test_factorial(self, calc, n, expected):
        """Test factorial with various inputs."""
        assert calc.factorial(n) == expected

    @pytest.mark.unit
    def test_factorial_negative(self, calc):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            calc.factorial(-1)

    @pytest.mark.unit
    def test_factorial_non_integer(self, calc):
        """Test that factorial of non-integer raises ValueError."""
        with pytest.raises(ValueError, match="Factorial requires an integer"):
            calc.factorial(3.5)

    # Test modulo
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (10, 3, 1),
        (20, 5, 0),
        (7, 4, 3),
        (15, 7, 1),
        (-10, 3, 2),
    ])
    def test_modulo(self, calc, a, b, expected):
        """Test modulo operation with various inputs."""
        assert calc.modulo(a, b) == expected

    @pytest.mark.unit
    def test_modulo_by_zero(self, calc):
        """Test that modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate modulo with zero divisor"):
            calc.modulo(5, 0)

    # Edge cases
    @pytest.mark.unit
    def test_operations_with_large_numbers(self, calc):
        """Test operations with large numbers."""
        large = 10**15
        assert calc.add(large, large) == 2 * large
        assert calc.multiply(large, 2) == 2 * large

    @pytest.mark.unit
    def test_operations_with_small_numbers(self, calc):
        """Test operations with very small numbers."""
        small = 1e-10
        assert calc.add(small, small) == pytest.approx(2 * small)
        assert calc.multiply(small, 2) == pytest.approx(2 * small)
