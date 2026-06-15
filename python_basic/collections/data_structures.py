"""
Data Structure Exercises.

Contains solutions for:
25. Create a list of 10 numbers and find sum, max, sort it, and remove duplicates.
26. Count even and odd numbers in a list.
27. Reverse a list without using reverse().
28. Create a tuple and access elements.
29. Convert tuple into list and modify it.
30. Perform union, intersection, and difference on two sets.
31. Remove duplicates from list using set.
32. Create a student dictionary and access values.
33. Count frequency of characters in a string using dictionary.
34. Merge two dictionaries.
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
    return {
        "sum": sum(numbers),
        "maximum": max(numbers),
        "sorted": sorted(numbers),
        "unique": list(set(numbers))
    }


def count_even_and_odd_numbers(
    numbers: list[int]
) -> tuple[int, int]:
    """
    Count even and odd numbers.

    Args:
        numbers: List of numbers.

    Returns:
        tuple[int, int]: Even count and odd count.
    """
    even_count: int = 0
    odd_count: int = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


def reverse_list(
    numbers: list[int]
) -> list[int]:
    """
    Reverse a list.

    Args:
        numbers: Input list.

    Returns:
        list[int]: Reversed list.
    """
    return numbers[::-1]


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


def convert_tuple_to_list(
    values: tuple[str, ...]
) -> list[str]:
    """
    Convert tuple to list and modify it.

    Args:
        values: Tuple values.

    Returns:
        list[str]: Modified list.
    """
    converted_list: list[str] = list(values)

    converted_list.append(
        "JavaScript"
    )

    return converted_list


def perform_set_operations(
    first_set: set[int],
    second_set: set[int]
) -> dict[str, set[int]]:
    """
    Perform set operations.

    Args:
        first_set: First set.
        second_set: Second set.

    Returns:
        dict[str, set[int]]: Set operation results.
    """
    return {
        "union": first_set.union(second_set),
        "intersection": (
            first_set.intersection(
                second_set
            )
        ),
        "difference": (
            first_set.difference(
                second_set
            )
        )
    }


def remove_duplicates(
    numbers: list[int]
) -> list[int]:
    """
    Remove duplicates from list.

    Args:
        numbers: Input list.

    Returns:
        list[int]: Unique values.
    """
    return list(set(numbers))


def create_student_dictionary() -> dict[str, object]:
    """
    Create student dictionary.

    Returns:
        dict[str, object]: Student details.
    """
    return {
        "student_id": 101,
        "name": "Astha",
        "course": "Engineering",
        "semester": 7
    }


def count_character_frequency(
    text: str
) -> dict[str, int]:
    """
    Count character frequency.

    Args:
        text: Input string.

    Returns:
        dict[str, int]: Frequency dictionary.
    """
    frequency: dict[str, int] = {}

    for character in text:
        frequency[character] = (
            frequency.get(
                character,
                0
            ) + 1
        )

    return frequency


def merge_dictionaries(
    first_dictionary: dict,
    second_dictionary: dict
) -> dict:
    """
    Merge two dictionaries.

    Args:
        first_dictionary: First dictionary.
        second_dictionary: Second dictionary.

    Returns:
        dict: Merged dictionary.
    """
    return (
        first_dictionary
        | second_dictionary
    )


def main() -> None:
    """
    Execute all data structure exercises.
    """

    print(
        "\n--- Question 25: List Operations ---"
    )

    results = perform_list_operations(
        NUMBER_LIST
    )

    for key, value in results.items():
        print(
            f"{key}: {value}"
        )

    print(
        "\n--- Question 26: Count Even and Odd Numbers ---"
    )

    even_count, odd_count = (
        count_even_and_odd_numbers(
            NUMBER_LIST
        )
    )

    print(
        f"Even Numbers: {even_count}"
    )

    print(
        f"Odd Numbers: {odd_count}"
    )

    print(
        "\n--- Question 27: Reverse List ---"
    )

    print(
        reverse_list(
            NUMBER_LIST
        )
    )

    print(
        "\n--- Question 28: Tuple Elements ---"
    )

    display_tuple_elements(
        SAMPLE_TUPLE
    )

    print(
        "\n--- Question 29: Convert Tuple to List ---"
    )

    print(
        convert_tuple_to_list(
            SAMPLE_TUPLE
        )
    )

    print(
        "\n--- Question 30: Set Operations ---"
    )

    first_set: set[int] = {
        1,
        2,
        3,
        4
    }

    second_set: set[int] = {
        3,
        4,
        5,
        6
    }

    set_results = (
        perform_set_operations(
            first_set,
            second_set
        )
    )

    for key, value in (
        set_results.items()
    ):
        print(
            f"{key}: {value}"
        )

    print(
        "\n--- Question 31: Remove Duplicates Using Set ---"
    )

    duplicate_numbers: list[int] = [
        1,
        2,
        2,
        3,
        4,
        4,
        5
    ]

    print(
        remove_duplicates(
            duplicate_numbers
        )
    )

    print(
        "\n--- Question 32: Student Dictionary ---"
    )

    student_data = (
        create_student_dictionary()
    )

    for key, value in (
        student_data.items()
    ):
        print(
            f"{key}: {value}"
        )

    print(
        "\n--- Question 33: Character Frequency ---"
    )

    text: str = input(
        "Enter a string: "
    )

    print(
        count_character_frequency(
            text
        )
    )

    print(
        "\n--- Question 34: Merge Dictionaries ---"
    )

    first_dictionary: dict[str, str] = {
        "name": "Astha"
    }

    second_dictionary: dict[str, str] = {
        "course": "Engineering"
    }

    print(
        merge_dictionaries(
            first_dictionary,
            second_dictionary
        )
    )


if __name__ == "__main__":
    main()