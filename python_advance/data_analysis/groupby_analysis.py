"""
Data Analysis Assignment.

Contains solutions for:
1. Average salary by department
2. Maximum salary by department
3. Employee count by department
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


def calculate_average_salary(
    dataframe: pd.DataFrame
) -> pd.Series:
    """
    Calculate average salary
    by department.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.Series:
            Average salary by department.
    """
    return dataframe.groupby(
        "Department"
    )["Salary"].mean()


def calculate_maximum_salary(
    dataframe: pd.DataFrame
) -> pd.Series:
    """
    Calculate maximum salary
    by department.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.Series:
            Maximum salary by department.
    """
    return dataframe.groupby(
        "Department"
    )["Salary"].max()


def count_employees(
    dataframe: pd.DataFrame
) -> pd.Series:
    """
    Count employees
    by department.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.Series:
            Employee count by department.
    """
    return dataframe.groupby(
        "Department"
    )["Name"].count()


def main() -> None:
    """
    Execute data analysis exercises.
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
        "\n--- Average Salary By Department ---"
    )

    print(
        calculate_average_salary(
            employee_dataframe
        )
    )

    print(
        "\n--- Maximum Salary By Department ---"
    )

    print(
        calculate_maximum_salary(
            employee_dataframe
        )
    )

    print(
        "\n--- Employee Count By Department ---"
    )

    print(
        count_employees(
            employee_dataframe
        )
    )


if __name__ == "__main__":
    main()
