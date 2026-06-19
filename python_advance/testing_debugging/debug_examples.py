"""
Debugging examples.

Contains solutions for:
35. Logical bug example
36. pdb breakpoint example
"""


import pdb


def buggy_average(
    numbers: list[int]
) -> float:
    """
    Function containing
    a logical bug.
    """
    total = sum(numbers)

    return total / (
        len(numbers) + 1
    )


def inspect_loop_values() -> None:
    """
    Inspect values inside loop.
    """
    for number in range(5):

        pdb.set_trace()

        square = (
            number ** 2
        )

        print(square)


def explain_debugger() -> None:
    """
    Print debugger advantages.
    """
    advantages = [
        "Inspect variables in real time",
        "Pause execution at breakpoints",
        "Step through code line by line",
        "Faster bug identification",
        "Better than excessive print statements"
    ]

    for advantage in advantages:
        print(advantage)


def main() -> None:
    """
    Execute debugging examples.
    """

    print(
        "\n--- Question 35 ---"
    )

    numbers = [
        10,
        20,
        30
    ]

    print(
        buggy_average(
            numbers
        )
    )

    print(
        "\n--- Question 36 ---"
    )

    explain_debugger()


if __name__ == "__main__":
    main()
