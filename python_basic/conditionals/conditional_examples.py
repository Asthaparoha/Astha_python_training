"""
Operators and Conditionals

Contains solutions for:
7. Check whether a number is even or odd.
8. Check whether a number is positive, negative, or zero.
9. Find the largest of three numbers.
10. Calculate grade based on marks.
11. Check whether a year is a leap year.
"""

GRADE_A_MINIMUM: int = 90
GRADE_B_MINIMUM: int = 75
GRADE_C_MINIMUM: int = 50

MINIMUM_MARKS: int = 0
MAXIMUM_MARKS: int = 100


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
    Get float input from the user.

    Args:
        prompt_message: Message displayed to the user.

    Returns:
        float: User-entered float value.
    """
    return float(input(prompt_message))


# Question 7
def check_even_or_odd(number: int) -> str:
    """
    Check whether a number is even or odd.

    Args:
        number: Number to evaluate.

    Returns:
        str: Even or Odd.
    """
    if number % 2 == 0:
        return "Even"

    return "Odd"


# Question 8
def check_positive_negative_zero(number: float) -> str:
    """
    Check whether a number is positive,
    negative, or zero.
    """
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


# Question 9
def find_largest_number(
    first_number: float,
    second_number: float,
    third_number: float
) -> float:
    """
    Find the largest of three numbers.
    """
    return max(
        first_number,
        second_number,
        third_number
    )


# Question 10
def calculate_grade(marks: float) -> str:
    """
    Calculate grade based on marks.
    """
    if (
        marks < MINIMUM_MARKS
        or marks > MAXIMUM_MARKS
    ):
        return "Invalid"

    if marks >= GRADE_A_MINIMUM:
        return "A"

    if marks >= GRADE_B_MINIMUM:
        return "B"

    if marks >= GRADE_C_MINIMUM:
        return "C"

    return "Fail"


# Question 11
def check_leap_year(year: int) -> bool:
    """
    Check whether a year is a leap year.
    """
    return (
        year % 400 == 0
        or (
            year % 4 == 0
            and year % 100 != 0
        )
    )


def main() -> None:
    """
    Execute all conditional exercises.
    """

    print("\n--- Question 7: Even or Odd ---")

    number: int = get_integer_input(
        "Enter a number: "
    )

    print(
        f"{number} is "
        f"{check_even_or_odd(number)}."
    )

    print(
        "\n--- Question 8: "
        "Positive, Negative, or Zero ---"
    )

    number_value: float = get_float_input(
        "Enter a number: "
    )

    print(
        f"{number_value} is "
        f"{check_positive_negative_zero(number_value)}."
    )

    print(
        "\n--- Question 9: "
        "Largest of Three Numbers ---"
    )

    first_number: float = get_float_input(
        "Enter first number: "
    )

    second_number: float = get_float_input(
        "Enter second number: "
    )

    third_number: float = get_float_input(
        "Enter third number: "
    )

    print(
        f"Largest Number: "
        f"{find_largest_number(first_number, second_number, third_number)}"
    )

    print(
        "\n--- Question 10: "
        "Grade Calculation ---"
    )

    marks: float = get_float_input(
        "Enter marks: "
    )

    grade: str = calculate_grade(marks)

    if grade == "Invalid":
        print(
            "Marks should be between "
            "0 and 100."
        )
    else:
        print(f"Grade: {grade}")

    print(
        "\n--- Question 11: "
        "Leap Year Checker ---"
    )

    year: int = get_integer_input(
        "Enter a year: "
    )

    if check_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()