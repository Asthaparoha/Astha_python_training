"""
Pandas DataFrame Assignment.

Contains solutions for:
1. Create employee DataFrame
2. Show first two rows
3. Show summary statistics
4. Display IT employees
5. Add bonus column
"""

import pandas as pd


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

BONUS_PERCENTAGE: float = 0.10


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


def get_first_two_rows(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Return first two rows.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.DataFrame:
            First two rows.
    """
    return dataframe.head(2)


def get_summary_statistics(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Return summary statistics.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.DataFrame:
            Summary statistics.
    """
    return dataframe.describe()


def get_it_employees(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Filter IT employees.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.DataFrame:
            IT employees.
    """
    return dataframe[
        dataframe[
            "Department"
        ] == "IT"
    ]


def add_bonus_column(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Add bonus column.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.DataFrame:
            Updated DataFrame.
    """
    updated_dataframe = (
        dataframe.copy()
    )

    updated_dataframe[
        "Bonus"
    ] = (
        updated_dataframe[
            "Salary"
        ]
        * BONUS_PERCENTAGE
    )

    return updated_dataframe


def main() -> None:
    """
    Execute Pandas exercises.
    """

    employee_dataframe = (
        create_employee_dataframe()
    )

    print(
        "\n--- Employee DataFrame ---"
    )

    print(
        employee_dataframe
    )

    print(
        "\n--- First Two Rows ---"
    )

    print(
        get_first_two_rows(
            employee_dataframe
        )
    )

    print(
        "\n--- Summary Statistics ---"
    )

    print(
        get_summary_statistics(
            employee_dataframe
        )
    )

    print(
        "\n--- IT Employees ---"
    )

    print(
        get_it_employees(
            employee_dataframe
        )
    )

    print(
        "\n--- DataFrame With Bonus ---"
    )

    print(
        add_bonus_column(
            employee_dataframe
        )
    )


if __name__ == "__main__":
    main()
