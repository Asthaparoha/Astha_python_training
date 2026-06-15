"""
Data Structure Exercises.

Contains solutions for:
25. List operations
26. Count even and odd numbers
27. Reverse a list
28. Tuple operations
29. Convert tuple to list and modify
"""


NUMBER_LIST: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]

SAMPLE_TUPLE: tuple[str, ...] = (
    "Python",
    "Java",
    "C++"
)


# Question 25
def perform_list_operations(
    numbers: list[int]
) -> dict[str, object]:
    """
    Perform list operations.

    Args:
        numbers: List of numbers.

    Returns:
        dict[str, object]: Results.
    """
    unique_numbers: list[int] = list(
        set(numbers)
    )

    return {
        "sum": sum(numbers),
        "maximum": max(numbers),
        "sorted": sorted(numbers),
        "unique": unique_numbers
    }


# Question 26
def count_even_and_odd_numbers(
    numbers: list[int]
) -> tuple[int, int]:
    """
    Count even and odd numbers.

    Args:
        numbers: List of numbers.

    Returns:
        tuple[int, int]: Even count, odd count.
    """
    even_count: int = 0
    odd_count: int = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


# Question 27
def reverse_list(
    numbers: list[int]
) -> list[int]:
    """
    Reverse a list without reverse().

    Args:
        numbers: List of numbers.

    Returns:
        list[int]: Reversed list.
    """
    return numbers[::-1]


# Question 28
def display_tuple_elements(
    values: tuple[str, ...]
) -> None:
    """
    Display tuple elements.

    Args:
        values: Tuple values.
    """
    for value in values:
        print(value)


# Question 29
def convert_tuple_to_list(
    values: tuple[str, ...]
) -> list[str]:
    """
    Convert tuple to list.

    Args:
        values: Tuple values.

    Returns:
        list[str]: Converted list.
    """
    converted_list: list[str] = list(
        values
    )

    converted_list.append(
        "JavaScript"
    )

    return converted_list


def main() -> None:
    """
    Execute data structure exercises.
    """

    print(
        "\n--- Question 25: "
        "List Operations ---"
    )

    results = perform_list_operations(
        NUMBER_LIST
    )

    for key, value in results.items():
        print(f"{key}: {value}")

    print(
        "\n--- Question 26: "
        "Even and Odd Count ---"
    )

    even_count, odd_count = (
        count_even_and_odd_numbers(
            NUMBER_LIST
        )
    )

    print(
        f"Even Numbers: "
        f"{even_count}"
    )

    print(
        f"Odd Numbers: "
        f"{odd_count}"
    )

    print(
        "\n--- Question 27: "
        "Reverse List ---"
    )

    print(
        reverse_list(
            NUMBER_LIST
        )
    )

    print(
        "\n--- Question 28: "
        "Tuple Elements ---"
    )

    display_tuple_elements(
        SAMPLE_TUPLE
    )

    print(
        "\n--- Question 29: "
        "Tuple to List ---"
    )

    print(
        convert_tuple_to_list(
            SAMPLE_TUPLE
        )
    )


if __name__ == "__main__":
    main()