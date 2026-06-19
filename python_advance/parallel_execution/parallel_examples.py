"""
Parallel Execution Exercises.

Contains solutions for:
41. Two threads printing numbers
42. Thread sum from 1 to 100
43. join() demonstration
44. Simulated file downloads
45. Two processes with process IDs
46. Multiprocessing square calculation
47. ThreadPoolExecutor
48. ProcessPoolExecutor
"""

import os
import time
import threading
import multiprocessing

from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor
)


START_NUMBER: int = 1
END_NUMBER: int = 5
SUM_LIMIT: int = 100


def print_numbers(
    thread_name: str
) -> None:
    """
    Print numbers from 1 to 5.
    """
    for number in range(
        START_NUMBER,
        END_NUMBER + 1
    ):
        print(
            f"{thread_name}: "
            f"{number}"
        )


def calculate_sum() -> None:
    """
    Calculate sum from 1 to 100.
    """
    total: int = sum(
        range(
            1,
            SUM_LIMIT + 1
        )
    )

    print(
        f"Sum: {total}"
    )


def simulate_download(
    file_name: str
) -> None:
    """
    Simulate file download.
    """
    print(
        f"Downloading "
        f"{file_name}"
    )

    time.sleep(2)

    print(
        f"Completed "
        f"{file_name}"
    )


def print_process_id() -> None:
    """
    Print current process ID.
    """
    print(
        f"Process ID: "
        f"{os.getpid()}"
    )


def calculate_square(
    number: int
) -> None:
    """
    Calculate square.
    """
    print(
        f"{number} -> "
        f"{number ** 2}"
    )


def square_task(
    number: int
) -> int:
    """
    Square task for executors.
    """
    return (
        number ** 2
    )


def main() -> None:
    """
    Execute parallel
    execution exercises.
    """

    print(
        "\n--- Question 41 ---"
    )

    first_thread = (
        threading.Thread(
            target=print_numbers,
            args=("Thread-1",)
        )
    )

    second_thread = (
        threading.Thread(
            target=print_numbers,
            args=("Thread-2",)
        )
    )

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    print(
        "\n--- Question 42 ---"
    )

    sum_thread = (
        threading.Thread(
            target=calculate_sum
        )
    )

    sum_thread.start()
    sum_thread.join()

    print(
        "\n--- Question 43 ---"
    )

    thread = threading.Thread(
        target=print_numbers,
        args=("JoinDemo",)
    )

    thread.start()

    thread.join()

    print(
        "Thread execution completed."
    )

    print(
        "\n--- Question 44 ---"
    )

    downloads = []

    for file_name in [
        "file1.txt",
        "file2.txt",
        "file3.txt"
    ]:
        thread = (
            threading.Thread(
                target=simulate_download,
                args=(file_name,)
            )
        )

        downloads.append(
            thread
        )

        thread.start()

    for thread in downloads:
        thread.join()

    print(
        "\n--- Question 45 ---"
    )

    process_one = (
        multiprocessing.Process(
            target=print_process_id
        )
    )

    process_two = (
        multiprocessing.Process(
            target=print_process_id
        )
    )

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

    print(
        "\n--- Question 46 ---"
    )

    processes = []

    for number in [
        1,
        2,
        3,
        4,
        5
    ]:
        process = (
            multiprocessing.Process(
                target=calculate_square,
                args=(number,)
            )
        )

        processes.append(
            process
        )

        process.start()

    for process in processes:
        process.join()

    print(
        "\n--- Question 47 ---"
    )

    with ThreadPoolExecutor(
        max_workers=3
    ) as executor:

        results = list(
            executor.map(
                square_task,
                [1, 2, 3, 4, 5]
            )
        )

    print(results)

    print(
        "\n--- Question 48 ---"
    )

    with ProcessPoolExecutor(
        max_workers=3
    ) as executor:

        results = list(
            executor.map(
                square_task,
                [1, 2, 3, 4, 5]
            )
        )

    print(results)


if __name__ == "__main__":
    main()
