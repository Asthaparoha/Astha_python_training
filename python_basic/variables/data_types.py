"""
Variable and data type examples.

Contains solutions for:
4. Data types
5. Swap two numbers
6. Arithmetic operations
"""

from typing import Dict


INTEGER_VALUE: int = 10
FLOAT_VALUE: float = 10.5
STRING_VALUE: str = "Python"
BOOLEAN_VALUE: bool = True


def display_data_types() -> None:
    """
    Display variables and their data types.
    """
    print(f"{INTEGER_VALUE} -> {type(INTEGER_VALUE)}")
    print(f"{FLOAT_VALUE} -> {type(FLOAT_VALUE)}")
    print(f"{STRING_VALUE} -> {type(STRING_VALUE)}")
    print(f"{BOOLEAN_VALUE} -> {type(BOOLEAN_VALUE)}")


def swap_numbers(
    first_number: int,
    second_number: int
) -> tuple[int, int]:
    """
    Swap two numbers.

    Args:
        first_number: First number.
        second_number: Second number.

    Returns:
        tuple[int, int]: Swapped values.
    """
    return second_number, first_number


def calculate_arithmetic_operations(
    first_number: float,
    second_number: float
) -> Dict[str, float]:
    """
    Perform arithmetic operations.

    Args:
        first_number: First number.
        second_number: Second number.

    Returns:
        Dictionary containing results.
    """
    return {
        "sum": first_number + second_number,
        "difference": first_number - second_number,
        "multiplication": first_number * second_number,
        "division": (
            first_number / second_number
            if second_number != 0
            else 0
        )
    }


def main() -> None:
    """
    Execute examples.
    """
    print("Question 4")
    display_data_types()

    print("\nQuestion 5")
    first_number: int = 10
    second_number: int = 20

    swapped_first, swapped_second = swap_numbers(
        first_number,
        second_number
    )

    print(
        f"Before Swap: "
        f"{first_number}, {second_number}"
    )

    print(
        f"After Swap: "
        f"{swapped_first}, {swapped_second}"
    )

    print("\nQuestion 6")

    results = calculate_arithmetic_operations(
        20,
        10
    )

    for operation, value in results.items():
        print(f"{operation}: {value}")


if __name__ == "__main__":
    main()