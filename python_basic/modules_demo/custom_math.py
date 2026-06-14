"""
Custom Math Module.

Contains reusable mathematical utility functions.
"""


def calculate_square(number: float) -> float:
    """
    Calculate square of a number.

    Args:
        number: Input number.

    Returns:
        float: Square of the number.
    """
    return number * number


def calculate_cube(number: float) -> float:
    """
    Calculate cube of a number.

    Args:
        number: Input number.

    Returns:
        float: Cube of the number.
    """
    return number * number * number


def calculate_average(
    first_number: float,
    second_number: float
) -> float:
    """
    Calculate average of two numbers.

    Args:
        first_number: First number.
        second_number: Second number.

    Returns:
        float: Average value.
    """
    return (
        first_number + second_number
    ) / 2