"""
Seaborn Visualization Assignment.

Contains solutions for:
1. Department vs Salary Barplot
2. Salary Distribution Boxplot
3. Correlation Heatmap
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


EMPLOYEE_DATA: dict[str, list] = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Anuj"
    ],
    "Age": [
        25,
        30,
        28,
        35
    ],
    "Department": [
        "HR",
        "IT",
        "Finance",
        "IT"
    ],
    "Salary": [
        30000,
        50000,
        45000,
        60000
    ]
}


def create_employee_dataframe() -> pd.DataFrame:
    """
    Create employee DataFrame.

    Returns:
        pd.DataFrame:
            Employee DataFrame.
    """
    return pd.DataFrame(
        EMPLOYEE_DATA
    )


def create_barplot(
    dataframe: pd.DataFrame
) -> None:
    """
    Create Department vs Salary barplot.
    """
    plt.figure(
        figsize=(8, 5)
    )

    sns.barplot(
        data=dataframe,
        x="Department",
        y="Salary"
    )

    plt.title(
        "Department vs Salary"
    )

    plt.show()


def create_boxplot(
    dataframe: pd.DataFrame
) -> None:
    """
    Create salary distribution boxplot.
    """
    plt.figure(
        figsize=(8, 5)
    )

    sns.boxplot(
        y=dataframe["Salary"]
    )

    plt.title(
        "Salary Distribution"
    )

    plt.show()


def create_heatmap(
    dataframe: pd.DataFrame
) -> None:
    """
    Create correlation heatmap.
    """
    correlation_matrix = (
        dataframe[
            ["Age", "Salary"]
        ].corr()
    )

    plt.figure(
        figsize=(6, 4)
    )

    sns.heatmap(
        correlation_matrix,
        annot=True
    )

    plt.title(
        "Age and Salary Correlation"
    )

    plt.show()


def main() -> None:
    """
    Execute seaborn exercises.
    """

    employee_dataframe = (
        create_employee_dataframe()
    )

    create_barplot(
        employee_dataframe
    )

    create_boxplot(
        employee_dataframe
    )

    create_heatmap(
        employee_dataframe
    )


if __name__ == "__main__":
    main()
