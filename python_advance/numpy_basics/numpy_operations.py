"""
NumPy Basics Assignment.

Contains solutions for:
1. Create NumPy array
2. Mean
3. Max
4. Min
5. Sum
6. Array addition
7. Array multiplication
8. Create 3x3 matrix
"""

import numpy as np


BASE_ARRAY: list[int] = [
    10,
    20,
    30,
    40,
    50
]

FIRST_ARRAY: list[int] = [
    1,
    2,
    3
]

SECOND_ARRAY: list[int] = [
    4,
    5,
    6
]


def create_numpy_array() -> np.ndarray:
    """
    Create NumPy array.

    Returns:
        np.ndarray: NumPy array.
    """
    return np.array(
        BASE_ARRAY
    )


def calculate_mean(
    array: np.ndarray
) -> float:
    """
    Calculate mean value.
    """
    return float(
        np.mean(array)
    )


def calculate_maximum(
    array: np.ndarray
) -> int:
    """
    Calculate maximum value.
    """
    return int(
        np.max(array)
    )


def calculate_minimum(
    array: np.ndarray
) -> int:
    """
    Calculate minimum value.
    """
    return int(
        np.min(array)
    )


def calculate_sum(
    array: np.ndarray
) -> int:
    """
    Calculate sum.
    """
    return int(
        np.sum(array)
    )


def add_arrays() -> np.ndarray:
    """
    Add two arrays.
    """
    first_array = np.array(
        FIRST_ARRAY
    )

    second_array = np.array(
        SECOND_ARRAY
    )

    return (
        first_array
        + second_array
    )


def multiply_arrays() -> np.ndarray:
    """
    Multiply two arrays.
    """
    first_array = np.array(
        FIRST_ARRAY
    )

    second_array = np.array(
        SECOND_ARRAY
    )

    return (
        first_array
        * second_array
    )


def create_matrix() -> np.ndarray:
    """
    Create 3x3 matrix.
    """
    return np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )


def main() -> None:
    """
    Execute NumPy exercises.
    """

    numpy_array = (
        create_numpy_array()
    )

    print(
        "\n--- NumPy Array ---"
    )

    print(
        numpy_array
    )

    print(
        "\nMean:",
        calculate_mean(
            numpy_array
        )
    )

    print(
        "Maximum:",
        calculate_maximum(
            numpy_array
        )
    )

    print(
        "Minimum:",
        calculate_minimum(
            numpy_array
        )
    )

    print(
        "Sum:",
        calculate_sum(
            numpy_array
        )
    )

    print(
        "\nArray Addition:"
    )

    print(
        add_arrays()
    )

    print(
        "\nArray Multiplication:"
    )

    print(
        multiply_arrays()
    )

    print(
        "\n3x3 Matrix:"
    )

    print(
        create_matrix()
    )


if __name__ == "__main__":
    main()
