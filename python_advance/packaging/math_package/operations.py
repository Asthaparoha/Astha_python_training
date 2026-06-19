"""
Mathematical operations package.
"""


def add(
    first_number: float,
    second_number: float
) -> float:
    """
    Add two numbers.
    """
    return (
        first_number
        + second_number
    )


def subtract(
    first_number: float,
    second_number: float
) -> float:
    """
    Subtract two numbers.
    """
    return (
        first_number
        - second_number
    )


def multiply(
    first_number: float,
    second_number: float
) -> float:
    """
    Multiply two numbers.
    """
    return (
        first_number
        * second_number
    )


def divide(
    first_number: float,
    second_number: float
) -> float:
    """
    Divide two numbers.
    """
    if second_number == 0:
        raise ValueError(
            "Division by zero is not allowed."
        )

    return (
        first_number
        / second_number
    )
