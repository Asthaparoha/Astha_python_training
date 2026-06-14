"""
Variable and Data Type Exercises.

Contains solutions for:
4. Create variables of different data types and print their types.
5. Swap two numbers.
6. Perform arithmetic operations on two numbers.
"""

from typing import Dict


INTEGER_SAMPLE: int = 10
FLOAT_SAMPLE: float = 10.5
STRING_SAMPLE: str = "Python"
BOOLEAN_SAMPLE: bool = True


def display_data_types() -> None:
    """
    Display different data types and their corresponding types.
    """
    print("\nQuestion 4: Data Types")

    print(f"Value: {INTEGER_SAMPLE}, Type: {type(INTEGER_SAMPLE)}")
    print(f"Value: {FLOAT_SAMPLE}, Type: {type(FLOAT_SAMPLE)}")
    print(f"Value: {STRING_SAMPLE}, Type: {type(STRING_SAMPLE)}")
    print(f"Value: {BOOLEAN_SAMPLE}, Type: {type(BOOLEAN_SAMPLE)}")


def get_integer_input(prompt_message: str) -> int:
    """
    Get integer input from the user.

    Args:
        prompt_message: Message displayed to the user.

    Returns:
        int: User-entered integer value.
    """
    return int(input(prompt_message))


def get_float_input(prompt_message: str) -> float:
    """
    Get numeric input from the user.

    Args:
        prompt_message: Message displayed to the user.

    Returns:
        float: User-entered numeric value.
    """
    return float(input(prompt_message))


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
) -> Dict[str, float | str]:
    """
    Perform basic arithmetic operations.

    Args:
        first_number: First number.
        second_number: Second number.

    Returns:
        Dict[str, float | str]: Arithmetic operation results.
    """
    division_result: float | str

    if second_number == 0:
        division_result = "Division by zero is not allowed"
    else:
        division_result = first_number / second_number

    return {
        "sum": first_number + second_number,
        "difference": first_number - second_number,
        "multiplication": first_number * second_number,
        "division": division_result
    }


def execute_swap_program() -> None:
    """
    Execute number swapping program.
    """
    print("\nQuestion 5: Swap Two Numbers")

    first_number: int = get_integer_input(
        "Enter first number: "
    )

    second_number: int = get_integer_input(
        "Enter second number: "
    )

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


def execute_arithmetic_program() -> None:
    """
    Execute arithmetic operations program.
    """
    print("\nQuestion 6: Arithmetic Operations")

    first_number: float = get_float_input(
        "Enter first number: "
    )

    second_number: float = get_float_input(
        "Enter second number: "
    )

    results = calculate_arithmetic_operations(
        first_number,
        second_number
    )

    print("\nResults:")

    for operation_name, result in results.items():
        print(f"{operation_name.capitalize()}: {result}")


def main() -> None:
    """
    Execute all variable and data type exercises.
    """
    display_data_types()
    execute_swap_program()
    execute_arithmetic_program()


if __name__ == "__main__":
    main()