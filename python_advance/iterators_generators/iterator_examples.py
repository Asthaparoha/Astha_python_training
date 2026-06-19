"""
Iterator and Generator Exercises.

Contains solutions for:
9. Iterator using next()
10. Custom iterator class
11. Generator for squares
12. Fibonacci generator
13. Generator expression for even numbers
14. Iterator vs Generator example
15. Process large dataset using generator
16. Built-in generator example
"""


MAX_EVEN_NUMBER: int = 50
DATASET_SIZE: int = 100000


def demonstrate_list_iterator() -> None:
    """
    Demonstrate iterator using next().
    """
    numbers = [10, 20, 30, 40]

    iterator = iter(numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


class NumberIterator:
    """
    Custom iterator that returns
    numbers from 1 to N.
    """

    def __init__(
        self,
        maximum_number: int
    ) -> None:
        self.maximum_number = (
            maximum_number
        )
        self.current_number = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if (
            self.current_number
            > self.maximum_number
        ):
            raise StopIteration

        number = self.current_number

        self.current_number += 1

        return number


def square_generator(
    maximum_number: int
):
    """
    Yield square numbers.
    """
    for number in range(
        1,
        maximum_number + 1
    ):
        yield number ** 2


def fibonacci_generator(
    maximum_terms: int
):
    """
    Yield Fibonacci numbers.
    """
    first_number = 0
    second_number = 1

    for _ in range(
        maximum_terms
    ):
        yield first_number

        first_number, second_number = (
            second_number,
            first_number + second_number
        )


def process_large_dataset():
    """
    Process large dataset
    using generator.
    """
    for number in range(
        DATASET_SIZE
    ):
        yield number * 2


def demonstrate_iterator_vs_generator(
) -> None:
    """
    Demonstrate difference
    between iterator and generator.
    """
    iterator = iter(
        [1, 2, 3]
    )

    generator = (
        number
        for number in range(3)
    )

    print(
        f"Iterator: "
        f"{next(iterator)}"
    )

    print(
        f"Generator: "
        f"{next(generator)}"
    )


def main() -> None:
    """
    Execute iterator and
    generator exercises.
    """

    print(
        "\n--- Question 9 ---"
    )

    demonstrate_list_iterator()

    print(
        "\n--- Question 10 ---"
    )

    iterator = NumberIterator(
        5
    )

    for number in iterator:
        print(number)

    print(
        "\n--- Question 11 ---"
    )

    for square in square_generator(
        5
    ):
        print(square)

    print(
        "\n--- Question 12 ---"
    )

    for fibonacci in (
        fibonacci_generator(10)
    ):
        print(fibonacci)

    print(
        "\n--- Question 13 ---"
    )

    even_numbers = (
        number
        for number in range(
            1,
            MAX_EVEN_NUMBER + 1
        )
        if number % 2 == 0
    )

    print(
        list(even_numbers)
    )

    print(
        "\n--- Question 14 ---"
    )

    demonstrate_iterator_vs_generator()

    print(
        "\n--- Question 15 ---"
    )

    dataset = (
        process_large_dataset()
    )

    for _ in range(5):
        print(
            next(dataset)
        )

    print(
        "\n--- Question 16 ---"
    )

    range_object = range(5)

    for number in range_object:
        print(number)


if __name__ == "__main__":
    main()
