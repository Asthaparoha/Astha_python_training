"""
Exception Handling Exercises.

Contains solutions for:
1. Handle ValueError
2. Handle ZeroDivisionError
3. try-except-else-finally
4. Handle multiple exceptions
5. Catch all exceptions
6. Raise ValueError for negative numbers
7. Custom AgeException
8. Handle FileNotFoundError
"""


FILE_NAME: str = "number.txt"
MINIMUM_AGE: int = 18


class AgeException(Exception):
    """
    Custom exception raised when
    age is below the minimum age.
    """


def get_integer_input(
    prompt_message: str
) -> int:
    """
    Read an integer from user input.

    Args:
        prompt_message: Input prompt.

    Returns:
        int: User-entered integer.
    """
    try:
        return int(
            input(prompt_message)
        )

    except ValueError:
        raise ValueError(
            "Input must be a valid integer."
        )


def divide_numbers(
    numerator: float,
    denominator: float
) -> float:
    """
    Divide two numbers.

    Args:
        numerator: Dividend.
        denominator: Divisor.

    Returns:
        float: Division result.
    """
    return numerator / denominator


def read_number_and_print_square(
    file_name: str
) -> None:
    """
    Read a number from file
    and print its square.

    Args:
        file_name: File name.
    """
    try:
        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:
            number: int = int(
                file.read().strip()
            )

    except (
        FileNotFoundError,
        ValueError
    ) as error:
        print(
            f"Error: {error}"
        )

    else:
        print(
            f"Square: "
            f"{number ** 2}"
        )

    finally:
        print(
            "File operation completed."
        )


def handle_multiple_exceptions() -> None:
    """
    Demonstrate multiple exception handling.
    """
    try:
        number: int = int(
            input(
                "Enter a number: "
            )
        )

        result: float = (
            100 / number
        )

        print(
            f"Result: {result}"
        )

    except ValueError:
        print(
            "Invalid integer entered."
        )

    except ZeroDivisionError:
        print(
            "Division by zero is not allowed."
        )


def catch_all_exceptions() -> None:
    """
    Demonstrate generic exception handling.
    """
    try:
        values = [10, 20]

        print(values[5])

    except Exception as error:
        print(
            f"Error: {error}"
        )


def validate_positive_number(
    number: int
) -> None:
    """
    Raise ValueError for
    negative numbers.

    Args:
        number: Number to validate.
    """
    if number < 0:
        raise ValueError(
            "Number cannot be negative."
        )


def validate_age(
    age: int
) -> None:
    """
    Validate minimum age.

    Args:
        age: User age.
    """
    if age < MINIMUM_AGE:
        raise AgeException(
            "Age must be at least 18."
        )


def handle_file_not_found(
    file_name: str
) -> None:
    """
    Handle FileNotFoundError.

    Args:
        file_name: File name.
    """
    try:
        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:
            print(
                file.read()
            )

    except FileNotFoundError:
        print(
            "File not found."
        )


def main() -> None:
    """
    Execute exception handling exercises.
    """

    print(
        "\n--- Question 1 ---"
    )

    try:
        number = get_integer_input(
            "Enter an integer: "
        )

        print(
            f"Number: {number}"
        )

    except ValueError as error:
        print(error)

    print(
        "\n--- Question 2 ---"
    )

    try:
        numerator: float = float(
            input(
                "Enter numerator: "
            )
        )

        denominator: float = float(
            input(
                "Enter denominator: "
            )
        )

        result = divide_numbers(
            numerator,
            denominator
        )

        print(
            f"Result: {result}"
        )

    except ZeroDivisionError:
        print(
            "Division by zero is not allowed."
        )

    print(
        "\n--- Question 3 ---"
    )

    read_number_and_print_square(
        FILE_NAME
    )

    print(
        "\n--- Question 4 ---"
    )

    handle_multiple_exceptions()

    print(
        "\n--- Question 5 ---"
    )

    catch_all_exceptions()

    print(
        "\n--- Question 6 ---"
    )

    try:
        validate_positive_number(
            -5
        )

    except ValueError as error:
        print(error)

    print(
        "\n--- Question 7 ---"
    )

    try:
        validate_age(
            16
        )

    except AgeException as error:
        print(error)

    print(
        "\n--- Question 8 ---"
    )

    handle_file_not_found(
        "missing_file.txt"
    )


if __name__ == "__main__":
    main()
