"""
Matplotlib Visualization Assignment.

Contains solutions for:
1. Bar Chart
2. Line Chart
3. Histogram
4. Scatter Plot
"""

import matplotlib.pyplot as plt


DEPARTMENTS: list[str] = [
    "HR",
    "IT",
    "Finance"
]

EMPLOYEE_COUNTS: list[int] = [
    5,
    12,
    7
]

SALARIES: list[int] = [
    30000,
    40000,
    50000,
    60000,
    45000
]

AGES: list[int] = [
    25,
    30,
    28,
    35,
    29
]


def create_bar_chart() -> None:
    """
    Create employee count bar chart.
    """
    plt.figure(figsize=(8, 5))

    plt.bar(
        DEPARTMENTS,
        EMPLOYEE_COUNTS
    )

    plt.title(
        "Employees by Department"
    )

    plt.xlabel(
        "Department"
    )

    plt.ylabel(
        "Employees"
    )

    plt.show()


def create_line_chart() -> None:
    """
    Create employee count line chart.
    """
    plt.figure(figsize=(8, 5))

    plt.plot(
        DEPARTMENTS,
        EMPLOYEE_COUNTS,
        marker="o"
    )

    plt.title(
        "Department Employee Trend"
    )

    plt.xlabel(
        "Department"
    )

    plt.ylabel(
        "Employees"
    )

    plt.show()


def create_histogram() -> None:
    """
    Create salary histogram.
    """
    plt.figure(figsize=(8, 5))

    plt.hist(
        SALARIES,
        bins=5
    )

    plt.title(
        "Salary Distribution"
    )

    plt.xlabel(
        "Salary"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.show()


def create_scatter_plot() -> None:
    """
    Create age versus salary scatter plot.
    """
    plt.figure(figsize=(8, 5))

    plt.scatter(
        AGES,
        SALARIES
    )

    plt.title(
        "Age vs Salary"
    )

    plt.xlabel(
        "Age"
    )

    plt.ylabel(
        "Salary"
    )

    plt.show()


def main() -> None:
    """
    Execute visualization exercises.
    """

    create_bar_chart()

    create_line_chart()

    create_histogram()

    create_scatter_plot()


if __name__ == "__main__":
    main()
