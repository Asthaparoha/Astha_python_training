"""
Module Demonstration Exercises.

Contains solutions for:
22. Use math module.
23. Use random module.
24. Create and import custom module.
"""

import math
import random

from python_basic.modules_demo.custom_math import (
    calculate_average,
    calculate_cube,
    calculate_square
)


RANDOM_START: int = 1
RANDOM_END: int = 100


def get_integer_input(
    prompt_message: str
) -> int:
    """
    Get integer input from user.

    Args:
        prompt_message: Input prompt.

    Returns:
        int: User-entered integer.
    """
    return int(input(prompt_message))


# Question 22
def execute_math_module_program() -> None:
    """
    Demonstrate math module functions.
    """
    print(
        "\n--- Question 22: "
        "Math Module ---"
    )

    number: int = get_integer_input(
        "Enter a number: "
    )

    print(
        f"Square Root: "
        f"{math.sqrt(number)}"
    )

    print(
        f"Power (Square): "
        f"{math.pow(number, 2)}"
    )

    print(
        f"Factorial: "
        f"{math.factorial(number)}"
    )


# Question 23
def execute_random_module_program() -> None:
    """
    Demonstrate random module.
    """
    print(
        "\n--- Question 23: "
        "Random Module ---"
    )

    random_number: int = (
        random.randint(
            RANDOM_START,
            RANDOM_END
        )
    )

    print(
        f"Random Number: "
        f"{random_number}"
    )


# Question 24
def execute_custom_module_program() -> None:
    """
    Demonstrate custom module import.
    """
    print(
        "\n--- Question 24: "
        "Custom Module ---"
    )

    number: int = get_integer_input(
        "Enter a number: "
    )

    print(
        f"Square: "
        f"{calculate_square(number)}"
    )

    print(
        f"Cube: "
        f"{calculate_cube(number)}"
    )

    print(
        f"Average of "
        f"{number} and 10: "
        f"{calculate_average(number, 10)}"
    )


def main() -> None:
    """
    Execute module demonstrations.
    """
    execute_math_module_program()

    execute_random_module_program()

    execute_custom_module_program()


if __name__ == "__main__":
    main()