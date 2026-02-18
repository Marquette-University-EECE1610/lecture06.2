"""
Test cases for the calculator module.
"""

import pytest
from calculator import add, subtract, multiply, divide, is_even

"""Tests for the add function."""


def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(3, 5) == 8


def test_add_negative_numbers():
    """Test adding two negative numbers."""
    assert add(-3, -5) == -8


def test_add_mixed_signs():
    """Test adding numbers with different signs."""
    assert add(-3, 5) == 2


def test_add_zero():
    """Test adding zero."""
    assert add(10, 0) == 10


"""Tests for the subtract function."""


def test_subtract_positive_numbers():
    """Test subtracting two positive numbers."""
    assert subtract(10, 3) == 7


def test_subtract_negative_result():
    """Test subtraction resulting in negative."""
    assert subtract(3, 10) == -7


def test_subtract_zero():
    """Test subtracting zero."""
    assert subtract(5, 0) == 5


"""Tests for the multiply function."""


def test_multiply_positive_numbers():
    """Test multiplying two positive numbers."""
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    """Test multiplying by zero."""
    assert multiply(10, 0) == 0


def test_multiply_negative_numbers():
    """Test multiplying negative numbers."""
    assert multiply(-3, -4) == 12


"""Tests for the divide function."""


def test_divide_positive_numbers():
    """Test dividing two positive numbers."""
    assert divide(10, 2) == 5


def test_divide_with_remainder():
    """Test division with decimal result."""
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)


"""Tests for the is_even function."""


def test_even_positive_number():
    """Test that even positive numbers are identified."""
    assert is_even(4) is True


def test_odd_positive_number():
    """Test that odd positive numbers are identified."""
    assert is_even(5) is False


def test_even_negative_number():
    """Test that even negative numbers are identified."""
    assert is_even(-4) is True


def test_zero_is_even():
    """Test that zero is considered even."""
    assert is_even(0) is True
