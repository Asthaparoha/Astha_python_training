"""
Loop Exercises.

Contains solutions for:
12. Print numbers from 1 to 100.
13. Print multiplication table of a number.
14. Find factorial of a number.
15. Reverse a number.
16. Check whether a number is prime.
"""


START_NUMBER: int = 1
END_NUMBER: int = 100
MULTIPLICATION_LIMIT: int = 10


def get_integer_input(prompt_message: str) -> int:
    """
    Get integer input from the user.

    Args:
        prompt_message: Message displayed to the user.

    Returns:
        int: User-entered integer value.
    """
    return int(input(prompt_message))


# Question 12
def print_numbers_one_to_hundred() -> None:
    """
    Print numbers from 1 to 100.
    """
    for number in range(
        START_NUMBER,
        END_NUMBER + 1
    ):
        print(number, end=" ")

    print()


# Question 13
def print_multiplication_table(number: int) -> None:
    """
    Print multiplication table of a number.

    Args:
        number: Number for multiplication table.
    """
    for multiplier in range(
        1,
        MULTIPLICATION_LIMIT + 1
    ):
        print(
            f"{number} x {multiplier} "
            f"= {number * multiplier}"
        )


# Question 14
def calculate_factorial(number: int) -> int:
    """
    Calculate factorial of a number.

    Args:
        number: Number whose factorial is calculated.

    Returns:
        int: Factorial value.
    """
    factorial: int = 1

    for current_number in range(
        1,
        number + 1
    ):
        factorial *= current_number

    return factorial


# Question 15
def reverse_number(number: int) -> int:
    """
    Reverse a number using a loop.

    Args:
        number: Number to reverse.

    Returns:
        int: Reversed number.
    """
    reversed_number: int = 0

    while number > 0:
        digit: int = number % 10
        reversed_number = (
            reversed_number * 10
            + digit
        )
        number //= 10

    return reversed_number


# Question 16
def check_prime_number(number: int) -> bool:
    """
    Check whether a number is prime.

    Args:
        number: Number to evaluate.

    Returns:
        bool: True if prime, otherwise False.
    """
    if number <= 1:
        return False

    for divisor in range(
        2,
        int(number ** 0.5) + 1
    ):
        if number % divisor == 0:
            return False

    return True


def main() -> None:
    """
    Execute all loop exercises.
    """

    print(
        "\n--- Question 12: "
        "Numbers from 1 to 100 ---"
    )

    print_numbers_one_to_hundred()

    print(
        "\n--- Question 13: "
        "Multiplication Table ---"
    )

    multiplication_number: int = (
        get_integer_input(
            "Enter a number: "
        )
    )

    print_multiplication_table(
        multiplication_number
    )

    print(
        "\n--- Question 14: "
        "Factorial ---"
    )

    factorial_number: int = (
        get_integer_input(
            "Enter a number: "
        )
    )

    print(
        f"Factorial: "
        f"{calculate_factorial(factorial_number)}"
    )

    print(
        "\n--- Question 15: "
        "Reverse Number ---"
    )

    number_to_reverse: int = (
        get_integer_input(
            "Enter a number: "
        )
    )

    print(
        f"Reversed Number: "
        f"{reverse_number(number_to_reverse)}"
    )

    print(
        "\n--- Question 16: "
        "Prime Number Check ---"
    )

    prime_number: int = (
        get_integer_input(
            "Enter a number: "
        )
    )

    if check_prime_number(
        prime_number
    ):
        print(
            f"{prime_number} "
            f"is a prime number."
        )
    else:
        print(
            f"{prime_number} "
            f"is not a prime number."
        )


if __name__ == "__main__":
    main()