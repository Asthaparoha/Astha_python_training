"""
Pytest cases for calculator.
"""

from python_advance.testing_debugging.calculator import (
    add_numbers
)


def test_add_positive_numbers() -> None:
    """
    Test positive numbers.
    """
    assert (
        add_numbers(10, 20)
        == 30
    )


def test_add_negative_numbers() -> None:
    """
    Test negative numbers.
    """
    assert (
        add_numbers(-5, -5)
        == -10
    )


def test_add_zero() -> None:
    """
    Test zero values.
    """
    assert (
        add_numbers(0, 0)
        == 0
    )
