"""
Pytest cases for prime checker.
"""

from python_advance.testing_debugging.prime_checker import (
    is_prime
)


def test_prime_number() -> None:
    """
    Test prime number.
    """
    assert is_prime(11)


def test_non_prime_number() -> None:
    """
    Test non-prime number.
    """
    assert (
        is_prime(12)
        is False
    )


def test_zero() -> None:
    """
    Test zero.
    """
    assert (
        is_prime(0)
        is False
    )


def test_negative_number() -> None:
    """
    Test negative number.
    """
    assert (
        is_prime(-5)
        is False
    )
