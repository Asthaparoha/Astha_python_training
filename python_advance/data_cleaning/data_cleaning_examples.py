"""
Data Cleaning Assignment.

Contains solutions for:
1. Detect missing values
2. Replace missing age with mean
3. Replace missing salary with 0
"""

import pandas as pd
import numpy as np


EMPLOYEE_DATA: dict[str, list] = {
    "Name": [
        "Rahul",
        "Priya",
        "Anuj"
    ],
    "Age": [
        25,
        np.nan,
        29
    ],
    "Salary": [
        30000,
        40000,
        np.nan
    ]
}

DEFAULT_SALARY: int = 0


def create_dataframe() -> pd.DataFrame:
    """
    Create employee DataFrame.

    Returns:
        pd.DataFrame:
            Employee DataFrame.
    """
    return pd.DataFrame(
        EMPLOYEE_DATA
    )


def detect_missing_values(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Detect missing values.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.DataFrame:
            Missing value report.
    """
    return dataframe.isnull()


def replace_missing_age(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Replace missing age
    with mean age.

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

    mean_age: float = (
        updated_dataframe[
            "Age"
        ].mean()
    )

    updated_dataframe[
        "Age"
    ] = updated_dataframe[
        "Age"
    ].fillna(
        mean_age
    )

    return updated_dataframe


def replace_missing_salary(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Replace missing salary
    with zero.

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
        "Salary"
    ] = updated_dataframe[
        "Salary"
    ].fillna(
        DEFAULT_SALARY
    )

    return updated_dataframe


def perform_data_cleaning(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Perform complete
    data cleaning.

    Args:
        dataframe:
            Employee DataFrame.

    Returns:
        pd.DataFrame:
            Cleaned DataFrame.
    """
    cleaned_dataframe = (
        replace_missing_age(
            dataframe
        )
    )

    cleaned_dataframe = (
        replace_missing_salary(
            cleaned_dataframe
        )
    )

    return cleaned_dataframe


def main() -> None:
    """
    Execute data cleaning exercises.
    """

    employee_dataframe = (
        create_dataframe()
    )

    print(
        "\n--- Original DataFrame ---"
    )

    print(
        employee_dataframe
    )

    print(
        "\n--- Missing Values ---"
    )

    print(
        detect_missing_values(
            employee_dataframe
        )
    )

    print(
        "\n--- Cleaned DataFrame ---"
    )

    print(
        perform_data_cleaning(
            employee_dataframe
        )
    )


if __name__ == "__main__":
    main()
