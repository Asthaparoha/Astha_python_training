"""
Prime checker module.
"""


def is_prime(
    number: int
) -> bool:
    """
    Check whether number
    is prime.
    """
    if number <= 1:
        return False

    for divisor in range(
        2,
        int(number ** 0.5) + 1
    ):
        if (
            number % divisor
            == 0
        ):
            return False

    return True
