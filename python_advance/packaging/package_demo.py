"""
Packaging Exercises.

Contains solutions for:
37. Create utility module
38. Module vs Package explanation
39. Package with two modules
40. Mathematical operations package
"""

from python_advance.packaging.utility_functions import (
    calculate_square,
    calculate_cube
)

from python_advance.packaging.math_package import (
    add,
    subtract,
    multiply,
    divide
)


def explain_module_vs_package() -> None:
    """
    Explain module vs package.
    """
    print(
        "Module: A single Python file."
    )

    print(
        "Package: A collection of modules "
        "organized using __init__.py."
    )


def main() -> None:
    """
    Execute packaging exercises.
    """

    print(
        "\n--- Question 37 ---"
    )

    print(
        calculate_square(5)
    )

    print(
        calculate_cube(5)
    )

    print(
        "\n--- Question 38 ---"
    )

    explain_module_vs_package()

    print(
        "\n--- Question 39 ---"
    )

    print(
        "math_package created successfully."
    )

    print(
        "\n--- Question 40 ---"
    )

    print(
        f"Add: {add(10, 5)}"
    )

    print(
        f"Subtract: {subtract(10, 5)}"
    )

    print(
        f"Multiply: {multiply(10, 5)}"
    )

    print(
        f"Divide: {divide(10, 5)}"
    )


if __name__ == "__main__":
    main()
