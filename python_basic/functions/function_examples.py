"""
Function Exercises.

Contains solutions for:
17. Calculate square of a number.
18. Check palindrome (number and string).
19. Return maximum number from a list.
20. Demonstrate default parameters.
"""


def get_integer_input(prompt_message: str) -> int:
    """
    Get integer input from the user.

    Args:
        prompt_message: Message displayed to the user.

    Returns:
        int: User-entered integer value.
    """
    return int(input(prompt_message))


# Question 17
def calculate_square(number: float) -> float:
    """
    Calculate the square of a number.

    Args:
        number: Number whose square is calculated.

    Returns:
        float: Square of the number.
    """
    return number * number


# Question 18
def is_palindrome(value: str) -> bool:
    """
    Check whether a string or number is a palindrome.

    Args:
        value: Value to evaluate.

    Returns:
        bool: True if palindrome, otherwise False.
    """
    normalized_value: str = str(value)

    return (
        normalized_value
        == normalized_value[::-1]
    )


# Question 19
def find_maximum_number(
    numbers: list[float]
) -> float:
    """
    Return the maximum number from a list.

    Args:
        numbers: List of numbers.

    Returns:
        float: Largest number.
    """
    return max(numbers)


# Question 20
def greet_user(
    user_name: str = "Guest"
) -> str:
    """
    Demonstrate default parameters.

    Args:
        user_name: Name of the user.

    Returns:
        str: Greeting message.
    """
    return (
        f"Welcome, {user_name}!"
    )


def execute_square_program() -> None:
    """
    Execute square calculation program.
    """
    print(
        "\n--- Question 17: "
        "Square of a Number ---"
    )

    number: int = get_integer_input(
        "Enter a number: "
    )

    print(
        f"Square: "
        f"{calculate_square(number)}"
    )


def execute_palindrome_program() -> None:
    """
    Execute palindrome checker.
    """
    print(
        "\n--- Question 18: "
        "Palindrome Check ---"
    )

    user_input: str = input(
        "Enter a number or string: "
    )

    if is_palindrome(user_input):
        print(
            f"{user_input} is a palindrome."
        )
    else:
        print(
            f"{user_input} is not a palindrome."
        )


def execute_maximum_number_program() -> None:
    """
    Execute maximum number finder.
    """
    print(
        "\n--- Question 19: "
        "Maximum Number in List ---"
    )

    number_list: list[float] = []

    total_numbers: int = get_integer_input(
        "How many numbers do you want to enter? "
    )

    for index in range(total_numbers):
        number: float = float(
            input(
                f"Enter number "
                f"{index + 1}: "
            )
        )

        number_list.append(number)

    print(
        f"Maximum Number: "
        f"{find_maximum_number(number_list)}"
    )


def execute_default_parameter_program() -> None:
    """
    Execute default parameter example.
    """
    print(
        "\n--- Question 20: "
        "Default Parameters ---"
    )

    print(greet_user())

    custom_name: str = input(
        "Enter your name: "
    )

    print(
        greet_user(custom_name)
    )


def main() -> None:
    """
    Execute all function exercises.
    """
    execute_square_program()

    execute_palindrome_program()

    execute_maximum_number_program()

    execute_default_parameter_program()


if __name__ == "__main__":
    main()