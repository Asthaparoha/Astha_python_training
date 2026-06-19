"""
Functional Programming Exercises.

Contains solutions for:
17. Lambda function
18. map()
19. filter()
20. reduce()
21. Recursive factorial
22. Recursive Fibonacci
23. Loop-based program converted to functional style
"""

from functools import reduce


NUMBER_LIST: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]


def calculate_square_using_lambda(
    number: int
) -> int:
    """
    Calculate square using lambda.
    """
    square_function = (
        lambda value: value ** 2
    )

    return square_function(
        number
    )


def convert_numbers_to_squares(
    numbers: list[int]
) -> list[int]:
    """
    Convert numbers to squares
    using map().
    """
    return list(
        map(
            lambda value:
            value ** 2,
            numbers
        )
    )


def extract_even_numbers(
    numbers: list[int]
) -> list[int]:
    """
    Extract even numbers
    using filter().
    """
    return list(
        filter(
            lambda value:
            value % 2 == 0,
            numbers
        )
    )


def calculate_product(
    numbers: list[int]
) -> int:
    """
    Calculate product using reduce().
    """
    return reduce(
        lambda first,
        second:
        first * second,
        numbers
    )


def calculate_factorial(
    number: int
) -> int:
    """
    Calculate factorial
    recursively.
    """
    if number <= 1:
        return 1

    return (
        number
        * calculate_factorial(
            number - 1
        )
    )


def calculate_fibonacci(
    number: int
) -> int:
    """
    Calculate Fibonacci
    recursively.
    """
    if number <= 1:
        return number

    return (
        calculate_fibonacci(
            number - 1
        )
        +
        calculate_fibonacci(
            number - 2
        )
    )


def convert_loop_to_functional_style(
    numbers: list[int]
) -> list[int]:
    """
    Convert loop-based logic
    to functional style.
    """
    return list(
        map(
            lambda value:
            value * 2,
            numbers
        )
    )


def main() -> None:
    """
    Execute functional
    programming exercises.
    """

    print(
        "\n--- Question 17 ---"
    )

    print(
        calculate_square_using_lambda(
            5
        )
    )

    print(
        "\n--- Question 18 ---"
    )

    print(
        convert_numbers_to_squares(
            NUMBER_LIST
        )
    )

    print(
        "\n--- Question 19 ---"
    )

    print(
        extract_even_numbers(
            NUMBER_LIST
        )
    )

    print(
        "\n--- Question 20 ---"
    )

    print(
        calculate_product(
            NUMBER_LIST
        )
    )

    print(
        "\n--- Question 21 ---"
    )

    print(
        calculate_factorial(
            5
        )
    )

    print(
        "\n--- Question 22 ---"
    )

    for index in range(10):
        print(
            calculate_fibonacci(
                index
            )
        )

    print(
        "\n--- Question 23 ---"
    )

    print(
        convert_loop_to_functional_style(
            NUMBER_LIST
        )
    )


if __name__ == "__main__":
    main()
